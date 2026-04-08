import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ── PAGE CONFIG ─────────────────────────────
st.set_page_config(page_title="Supply Chain Analytics", layout="wide")

# ── LOAD DATA ──────────────────────────────
@st.cache_data
def load_data():
    df = pd.read_csv("supply_chain_clean.csv")

    # Fix column issues safely
    df.columns = df.columns.str.strip()

    # Feature Engineering
    df["Margin"] = (df["Order Profit Per Order"] / df["Sales"]) * 100

    if "Order Date" in df.columns:
        df["Order Date"] = pd.to_datetime(df["Order Date"], errors='coerce')

    return df

df = load_data()

# ── SIDEBAR FILTERS ────────────────────────
st.sidebar.title("🔍 Filters")

segment = st.sidebar.multiselect(
    "Customer Segment",
    df["Customer Segment"].dropna().unique(),
    default=df["Customer Segment"].dropna().unique()
)

category = st.sidebar.multiselect(
    "Category",
    df["Category Name"].dropna().unique(),
    default=df["Category Name"].dropna().unique()
)

market = st.sidebar.multiselect(
    "Market",
    df["Market"].dropna().unique(),
    default=df["Market"].dropna().unique()
)

region = st.sidebar.multiselect(
    "Region",
    df["Order Region"].dropna().unique(),
    default=df["Order Region"].dropna().unique()
)

discount_range = st.sidebar.slider(
    "Discount Rate",
    float(df["Order Item Discount Rate"].min()),
    float(df["Order Item Discount Rate"].max()),
    (0.0, float(df["Order Item Discount Rate"].max()))
)

# ── APPLY FILTERS ──────────────────────────
df = df[
    (df["Customer Segment"].isin(segment)) &
    (df["Category Name"].isin(category)) &
    (df["Market"].isin(market)) &
    (df["Order Region"].isin(region)) &
    (df["Order Item Discount Rate"].between(discount_range[0], discount_range[1]))
]

if df.empty:
    st.warning("No data available for selected filters")
    st.stop()

# ── HEADER ─────────────────────────────────
st.title("📦 Supply Chain Analytics Dashboard")

# ── KPIs ───────────────────────────────────
total_sales = df["Sales"].sum()
total_profit = df["Order Profit Per Order"].sum()
margin = (total_profit / total_sales * 100) if total_sales else 0

col1, col2, col3, col4 = st.columns(4)
col1.metric("💰 Revenue", f"${total_sales:,.0f}")
col2.metric("📈 Profit", f"${total_profit:,.0f}")
col3.metric("📊 Margin", f"{margin:.2f}%")
col4.metric("⚠️ Loss Orders", len(df[df["Order Profit Per Order"] < 0]))

# 🚨 Alerts
if margin < 3:
    st.error("🚨 Critical: Very low profit margin!")
elif margin < 8:
    st.warning("⚠️ Profit margin is below optimal level")

st.markdown("---")

# ── TABS ──────────────────────────────────
tab1, tab2, tab3, tab4 = st.tabs([
    "📈 Overview",
    "👥 Customers",
    "🛒 Products",
    "💸 Discounts"
])

# ═══════════ OVERVIEW ═══════════
with tab1:
    st.subheader("Revenue vs Profit by Market")

    market_data = df.groupby("Market").agg(
        Revenue=("Sales", "sum"),
        Profit=("Order Profit Per Order", "sum")
    ).reset_index()

    fig = px.bar(market_data, x="Market", y=["Revenue", "Profit"], barmode="group")
    st.plotly_chart(fig, use_container_width=True)

    # Forecast
    if "Order Date" in df.columns:
        st.subheader("Revenue Forecast")

        trend = df.groupby(df["Order Date"].dt.to_period("M")).agg(
            Sales=("Sales", "sum")
        ).reset_index()

        trend["Order Date"] = trend["Order Date"].astype(str)
        trend["Forecast"] = trend["Sales"].rolling(3).mean()

        fig = px.line(trend, x="Order Date", y=["Sales", "Forecast"])
        st.plotly_chart(fig, use_container_width=True)

# ═══════════ CUSTOMERS ═══════════
with tab2:
    st.subheader("Customer Analysis")

    customer = df.groupby("Customer Id").agg(
        Name=("Customer Fname", "first"),
        Revenue=("Sales", "sum"),
        Profit=("Order Profit Per Order", "sum")
    ).reset_index()

    # Tiering
    def tier(p):
        if p > 500: return "Platinum"
        elif p > 200: return "Gold"
        elif p > 0: return "Silver"
        else: return "Loss"

    customer["Tier"] = customer["Profit"].apply(tier)
    customer["CLV"] = customer["Revenue"] * 0.3

    col1, col2 = st.columns(2)

    with col1:
        st.write("Top Customers")
        st.dataframe(customer.sort_values("Profit", ascending=False).head(10))

    with col2:
        st.write("Loss Customers")
        st.dataframe(customer.sort_values("Profit").head(10))

# ═══════════ PRODUCTS ═══════════
with tab3:
    st.subheader("Product Performance")

    product = df.groupby("Product Name").agg(
        Revenue=("Sales", "sum"),
        Profit=("Order Profit Per Order", "sum")
    ).reset_index()

    product["Margin"] = (product["Profit"] / product["Revenue"]) * 100

    fig = px.scatter(product, x="Revenue", y="Margin",
                     size="Revenue", hover_name="Product Name")
    st.plotly_chart(fig, use_container_width=True)

# ═══════════ DISCOUNTS ═══════════
with tab4:
    st.subheader("Discount Impact")

    fig = px.scatter(df,
                     x="Order Item Discount Rate",
                     y="Order Item Profit Ratio",
                     opacity=0.5)
    st.plotly_chart(fig, use_container_width=True)

    # What-if
    st.subheader("What-if Scenario")
    sim = st.slider("Change Discount", 0.0, 0.5, 0.1)

    simulated_profit = (df["Sales"] * (1 - sim)).sum()
    st.metric("Simulated Profit", f"${simulated_profit:,.0f}")

# ── SHIPPING ANALYSIS ──────────────────────
st.subheader("🚚 Shipping Performance")

ship = df.groupby("Shipping Mode").agg(
    Orders=("Sales", "count"),
    Late=("Late_delivery_risk", "mean")
).reset_index()

ship["Late %"] = ship["Late"] * 100

fig = px.bar(ship, x="Shipping Mode", y="Late %", color="Late %")
st.plotly_chart(fig, use_container_width=True)

# ── MAP ────────────────────────────────────
st.subheader("🌍 Profit by Country")

country = df.groupby("Order Country")["Order Profit Per Order"].sum().reset_index()

fig = px.choropleth(
    country,
    locations="Order Country",
    locationmode="country names",
    color="Order Profit Per Order"
)

st.plotly_chart(fig, use_container_width=True)

# ── AI INSIGHTS ────────────────────────────
st.subheader("🤖 AI Insights")

insights = []

if margin < 5:
    insights.append("Reduce discounts to improve margin")

if df["Order Item Discount Rate"].mean() > 0.2:
    insights.append("High discount usage detected")

top_market = df.groupby("Market")["Sales"].sum().idxmax()
insights.append(f"Top market: {top_market}")

for i in insights:
    st.info(i)

# ── DOWNLOAD ───────────────────────────────
st.download_button(
    "📥 Download Report",
    df.to_csv(index=False),
    "report.csv"
)
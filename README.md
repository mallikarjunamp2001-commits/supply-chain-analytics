# 📦 Supply Chain Analytics Dashboard

An interactive **Streamlit web application** designed to analyze customer, product, and profitability performance in supply chain operations. This dashboard enables organizations to shift from **revenue-focused decisions to profit-driven strategies**.

---

## 🚀 Project Overview

In modern supply chain systems, **high sales do not always guarantee high profit**. Factors like discounts, shipping costs, and customer behavior can significantly impact margins.

This project provides **end-to-end analytical insights** to answer critical business questions:

* Which customers generate the most profit?
* Which products or categories are loss-making?
* How do discounts affect profitability?
* Which markets and regions perform best?

---

## 🎯 Problem Statement

Organizations often lack:

* Visibility into **customer and product-level profitability**
* Understanding of **discount-driven margin erosion**
* Identification of **high-value vs low-value customers**
* Market-level **profit diagnostics**

This dashboard solves these challenges by delivering **financial clarity and actionable insights**.

---

## 📊 Key Features

### 💰 Revenue & Profit Overview

* Total Revenue, Profit, and Profit Margin KPIs
* Revenue vs Profit comparison
* Loss-making order identification

### 👥 Customer Value Dashboard

* Customer segmentation (Platinum, Gold, Silver, Loss)
* Top and bottom customers by profit
* Customer contribution analysis
* Pareto (80/20) profit distribution

### 🛒 Product & Category Performance

* Product-level margin analysis
* Category profitability comparison
* High-revenue but low-margin detection
* Loss-making product identification

### 💸 Discount Impact Analyzer

* Discount vs Profit Margin visualization
* Discount band performance analysis
* Profit erosion detection
* What-if discount scenario exploration

### 🌍 Market & Regional Insights

* Market-wise revenue and profit analysis
* Region-level performance tracking
* Country-wise profit visualization (Choropleth map)

### 🚚 Shipping & Delivery Insights

* Shipping mode performance comparison
* Late delivery risk analysis
* Delivery status breakdown

### 🤖 Intelligent Insights (Advanced)

* Automated identification of:

  * High-risk discount zones
  * Loss-making customers/products
  * High-value opportunities

---

## 📂 Dataset Description

The dataset contains **supply chain transactional data** including:

* Customer details (ID, segment, location)
* Product and category information
* Sales, profit, and discount metrics
* Shipping and delivery data
* Market and regional attributes

Key fields include:

* `Sales`
* `Order Profit Per Order`
* `Order Item Discount Rate`
* `Customer Segment`
* `Market`, `Order Region`
* `Product Name`, `Category Name`

---

## 🧠 Analytical Methodology

1. **Data Cleaning & Validation**

   * Removed inconsistencies and null values
   * Standardized financial metrics

2. **Feature Engineering**

   * Profit Margin calculation
   * Discount bands creation
   * Customer value segmentation

3. **Exploratory Data Analysis (EDA)**

   * Revenue vs Profit comparisons
   * Customer and product contribution analysis

4. **Profitability Analysis**

   * Customer-level profit aggregation
   * Product/category margin analysis

5. **Discount Impact Analysis**

   * Correlation between discount rate and profit ratio
   * Threshold detection for margin loss

6. **Geographical Analysis**

   * Market and region performance comparison

---

## 📁 Project Structure

```
supply-chain-analytics/
│── app.py                     # Streamlit dashboard application
│── supply_chain_clean.csv     # Cleaned dataset
│── requirements.txt          # Python dependencies
│── README.md                 # Project documentation
```

---

## 🧰 Tech Stack

* **Python**
* **Streamlit**
* **Pandas**
* **NumPy**
* **Plotly**

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/supply-chain-analytics.git
cd supply-chain-analytics
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run Application

```bash
python -m streamlit run app.py
```

---


## 🌐 Live Demo

https://supply-chain-analytics-f7h8uasph7b2zkikh8b9mp.streamlit.app/

---

## 📈 Key KPIs

* Total Revenue
* Total Profit
* Profit Margin (%)
* Customer Value Index
* Category Margin
* Discount Impact Ratio

---

## 🎯 Business Impact

This dashboard enables organizations to:

* Identify **high-value customers**
* Detect **loss-making products and categories**
* Optimize **discount strategies**
* Improve **profitability-focused decision making**

---

## 🔮 Future Enhancements

* Machine Learning-based profit prediction
* Demand forecasting models
* Real-time data integration
* AI chatbot for business queries

---

## 👨‍💻 Author

**Mallikarjuna M P**

---

## 📜 License

This project is licensed under the MIT License.

---

## ⭐ Support

If you found this project useful, please ⭐ star the repository!



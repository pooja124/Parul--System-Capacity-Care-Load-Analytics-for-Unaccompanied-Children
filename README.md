# 📊 System Capacity & Care Load Analytics for Unaccompanied Children

## 📌 Overview

This project presents a **data-driven healthcare analytics framework** for monitoring system capacity and care load within the **Unaccompanied Alien Children (UAC) Program** administered by the U.S. Department of Health and Human Services (HHS).

The system analyzes daily operational data to provide insights into:

* Total system load
* Inflow vs outflow balance
* Capacity stress periods
* Backlog accumulation

An interactive **Streamlit dashboard** is also developed for real-time monitoring and decision support.

---

## 🎯 Objectives

### Primary Objectives

* Quantify daily and cumulative care load across CBP and HHS
* Identify periods of system stress and relief
* Analyze balance between intake, transfers, and discharges

### Secondary Objectives

* Support healthcare staffing and shelter planning
* Improve situational awareness for policymakers
* Enable data-driven humanitarian decision-making

---

## 📂 Dataset Description

The dataset contains daily records (2023–2025) of the UAC care pipeline:

| Column                  | Description           |
| ----------------------- | --------------------- |
| Date                    | Reporting date        |
| Children apprehended    | Daily intake into CBP |
| Children in CBP custody | Active CBP load       |
| Children transferred    | Flow into HHS         |
| Children in HHS care    | Active HHS load       |
| Children discharged     | Sponsor placements    |

---

## ⚙️ Methodology

### 1. Data Preprocessing

* Date conversion and sorting
* Handling missing values
* Validation of logical constraints:

  * Transfers ≤ CBP custody
  * Discharges ≤ HHS care

### 2. Feature Engineering

Derived key metrics:

* **Total System Load** = CBP + HHS
* **Net Daily Intake** = Transfers − Discharges
* **Growth Rate** (day-over-day)
* **Backlog Indicator**

### 3. Trend Analysis

* Daily, weekly, and monthly trends
* Rolling averages (7-day, 14-day)
* Seasonal pattern analysis

### 4. Pressure Detection

* Identification of prolonged high-load periods
* Variability and volatility analysis

---

## 📈 Key Performance Indicators (KPIs)

* **Total Children Under Care**
* **Net Intake Pressure**
* **Care Load Volatility Index**
* **Backlog Accumulation Rate**
* **Discharge Offset Ratio**

---

## 📊 Streamlit Dashboard

### Features

* System Load Overview
* CBP vs HHS Comparison
* Net Intake Trends
* KPI Summary Cards

### User Controls

* Date range selection
* Metric toggles
* Time granularity filters (daily / weekly / monthly)

---

## 🧠 Key Insights

* System experiences **periodic inflow spikes**
* HHS facilities carry the majority of long-term load
* Backlog forms when **discharges lag behind transfers**
* Sustained positive net intake leads to **capacity stress**

---

## 💡 Recommendations

* Increase temporary capacity during surge periods
* Improve discharge efficiency to reduce backlog
* Use predictive analytics for proactive planning
* Implement real-time monitoring dashboards

---

## 🛠️ Tech Stack

* Python (Pandas, NumPy)
* Data Visualization (Matplotlib / Plotly / Seaborn)
* Streamlit (Dashboard)
* Time-Series Analysis

---

## 🚀 How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/Spacharya005/System-Capacity-Care-Load-Analytics-for-Unaccompanied-Children.git
cd System-Capacity-Care-Load-Analytics-for-Unaccompanied-Children
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit App

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
├── data/
├── assets/
├── app.py
├── forecasting.py
├── metrics.py
├── preprocessing.py
```



## 🤝 Acknowledgment

This project was developed as part of the **Unified Mentor Internship Program** in collaboration with healthcare analytics use cases inspired by HHS UAC operations.

---

## 🌐streamlit web application link


https://github.com/pooja124/Parul--System-Capacity-Care-Load-Analytics-for-Unaccompanied-Children.git
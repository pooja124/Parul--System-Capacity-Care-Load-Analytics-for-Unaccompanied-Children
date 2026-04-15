import streamlit as st
import pandas as pd
import plotly.express as px
import os

from preprocessing import load_and_structure_data, validate_data
from metrics import compute_metrics
from forecasting import forecast_load


# -----------------------------------------------------
# Page Configuration
# -----------------------------------------------------
st.set_page_config(
    page_title="System Capacity & Care Load Analytics for Unaccompanied Children",
    page_icon="📊",
    layout="wide"
)


st.markdown("""
<style>

/* ---------------- Main Background ---------------- */
.stApp {
    background-color: #F4F7FB;
}

/* ---------------- Main Container ---------------- */
.block-container {
    padding-top: 1rem;
    padding-bottom: 2rem;
}

/* ---------------- Headings ---------------- */
h1 {
    color: #0A3D62;
    font-weight: 700;
}

h2, h3 {
    color: #003366;
    font-weight: 600;
}

/* ---------------- Sidebar Styling ---------------- */
section[data-testid="stSidebar"] {
    background-color: #0A3D62;
    color: white;
}

/* Labels */
section[data-testid="stSidebar"] label {
    color: #FFFFFF !important;
}


/* Checkbox label */
section[data-testid="stSidebar"] div[data-testid="stCheckbox"] label {
    color: #EAF4FF !important;
    font-weight: 600;
}

/* Selectbox label */
section[data-testid="stSidebar"] .stSelectbox label {
    color: #FFFFFF !important;
}

/* Date input label */
section[data-testid="stSidebar"] .stDateInput label {
    color: white;
}

/* Headings */
section[data-testid="stSidebar"] h2 {
    color: white;
}

/* ✅ FIX: Selectbox value (Time Aggregation) */
section[data-testid="stSidebar"] div[data-baseweb="select"] span {
    color: black !important;
}

/* ✅ FIX: Selectbox background */
section[data-testid="stSidebar"] div[data-baseweb="select"] > div {
    background-color: white !important;
    color: black !important;
}

/* ✅ FIX: Dropdown options */
div[role="listbox"] div {
    color: black !important;
}

/* ✅ FIX: Date input text */
section[data-testid="stSidebar"] input {
    color: black !important;
    background-color: white !important;
}

/* ✅ FIX: Metric Toggles & Time Granularity headings */
section[data-testid="stSidebar"] h3 {
    color: #FFFFFF !important;
    font-weight: 700;
}
                                 
/* ---------------- KPI Cards ---------------- */
[data-testid="metric-container"] {
    background: white;
    border-radius: 16px;
    padding: 20px;
    box-shadow: 0 6px 18px rgba(0, 0, 0, 0.08);
    border-left: 6px solid #0A3D62;
}
/* Center metric labels */
[data-testid="stMetricLabel"] {
    justify-content: center;
}
            
/* ---------------- Tabs ---------------- */
button[role="tab"] {
    font-weight: 600;
    color: #0A3D62;
}

button[role="tab"][aria-selected="true"] {
    border-bottom: 3px solid #0A3D62;
    color: #003366;
}

/* ---------------- Plot Container ---------------- */
.stPlotlyChart {
    background-color: white;
    padding: 10px;
    border-radius: 16px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.06);
}

/* ---------------- Mobile Responsive ---------------- */
@media (max-width: 768px) {

    h1 {
        font-size: 22px !important;
    }

    h2 {
        font-size: 18px !important;
    }

    .block-container {
        padding: 1rem !important;
    }

    [data-testid="metric-container"] {
        padding: 12px !important;
    }
}            

/* ---------------- Footer ---------------- */
footer {
    visibility: hidden;
}
/* Fix Metric Toggle Checkbox Text Color */
section[data-testid="stSidebar"] div[data-testid="stCheckbox"] p {
    color: #EAF4FF !important;
    font-weight: 600 !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div style="
    background-color:#0A3D62;
    padding:18px;
    border-radius:14px;
    color:white;
    text-align:center;
    font-size:18px;
    font-weight:500;
    margin-top:25px;
    margin-bottom:15px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.08);
">
    Centralized Capacity Intelligence Framework for Humanitarian Care Monitoring
</div>
""", unsafe_allow_html=True)

# -----------------------------------------------------
# Header Section
# -----------------------------------------------------
col_logo, col_title = st.columns([1, 4], gap="small")

with col_logo:
    # Replace with your actual logo file names

    logo1_path = os.path.join("assets", "unified_mentor_logo_2.png")
    logo2_path = os.path.join("assets", "hhs_logo.png")

    if os.path.exists(logo1_path):
        st.image(logo1_path, width=200)

    if os.path.exists(logo2_path):
        st.image(logo2_path, width=160)

with col_title:
    st.title("System Capacity & Care Load Analytics for Unaccompanied Children")
    st.markdown("""
    **Internship Project By:** Unified Mentor  
    **Data Source:** U.S. Department of Health & Human Services (HHS)
    """)

st.markdown("---")

# -----------------------------------------------------
# Load & Process Data
# -----------------------------------------------------
df = load_and_structure_data("data/HHS_Unaccompanied_Alien_Children_Program.csv")
df = validate_data(df)
df = compute_metrics(df)

# -----------------------------------------------------
# Sidebar Filters
# -----------------------------------------------------
st.sidebar.markdown("## 📌 Dashboard Controls")
st.sidebar.markdown("---")

start_date = st.sidebar.date_input("Start Date", df.index.min())
end_date = st.sidebar.date_input("End Date", df.index.max())

st.sidebar.markdown("---")

st.sidebar.markdown("### 📊 Metric Toggles")

show_system_load = st.sidebar.checkbox("Total System Load", True)
show_cbp_hhs = st.sidebar.checkbox("CBP vs HHS Comparison", True)
show_intake_backlog = st.sidebar.checkbox("Net Intake & Backlog", True)

st.sidebar.markdown("---")

st.sidebar.markdown("### ⏱ Time Granularity")

granularity = st.sidebar.selectbox(
    "Select Time Aggregation",
    ["Daily", "Weekly", "Monthly"]
)

filtered_df = df.loc[start_date:end_date]
# Apply time aggregation
if granularity == "Weekly":
    filtered_df = filtered_df.resample("W").mean()

elif granularity == "Monthly":
    filtered_df = filtered_df.resample("M").mean()
    
# -----------------------------------------------------
# Tabs Layout
# -----------------------------------------------------
tab1, tab2, tab3, tab4 = st.tabs([
    "📊 Dashboard",
    "📈 Forecast",
    "✅ Validation",
    "ℹ️ About Project"
])

# =====================================================
# TAB 1 — DASHBOARD
# =====================================================
with tab1:

    st.markdown("## 📌 Key System Metrics Overview")

    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)

    col1.metric(
        "Total Children Under Care",
        f"{int(filtered_df['Total_System_Load'].iloc[-1]):,}"
    )

    col2.metric(
        "Net Intake Pressure",
        f"{int(filtered_df['Net_Intake'].iloc[-1]):,}"
    )

    col3.metric(
        "Backlog Accumulation",
        f"{int(filtered_df['Cumulative_Backlog'].iloc[-1]):,}"
    )

    col4.metric(
        "Discharge Offset Ratio",
        round(filtered_df['Discharge_Offset_Ratio'].mean(), 2)
    )

    st.markdown("---")

    # System Load Trend
    if show_system_load:
        st.subheader("📈 Total System Load Over Time")

        fig = px.line(
            filtered_df,
            y='Total_System_Load',
            color_discrete_sequence=["#0A3D62"]
        )
        fig.update_layout(
            height=500,   # 🔥 controls vertical size
            margin=dict(l=20, r=20, t=40, b=20)
        )
        st.plotly_chart(fig, use_container_width=True)

    # CBP vs HHS
    if show_cbp_hhs:
        st.subheader("📊 CBP vs HHS Load Comparison")

        fig2 = px.line(
            filtered_df,
            y=['CBP_Custody', 'HHS_Care'],
            color_discrete_sequence=["#1B9CFC", "#F39C12"]
        )
        fig2.update_layout(
            height=500,   # 🔥 controls vertical size
            margin=dict(l=20, r=20, t=40, b=20)
        )
        st.plotly_chart(fig2, use_container_width=True)

    # Net Intake & Backlog
    if show_intake_backlog:
        st.subheader("📉 Net Intake & Backlog Trend")

        fig3 = px.line(
            filtered_df,
            y=['Net_Intake', 'Cumulative_Backlog'],
            color_discrete_sequence=["#E74C3C", "#2ECC71"]
        )
        fig3.update_layout(
            height=500,   # 🔥 controls vertical size
            margin=dict(l=20, r=20, t=40, b=20)
        )   
        st.plotly_chart(fig3, use_container_width=True)


# =====================================================
# TAB 2 — FORECAST
# =====================================================
with tab2:

    st.subheader("🔮 60-Day Forecast of Total System Load")

    forecast = forecast_load(df)

    fig4 = px.line(
        forecast,
        x='ds',
        y='yhat',
        title='Forecasted Total System Load',
        color_discrete_sequence=["#8E44AD"]
    )

    st.plotly_chart(fig4, use_container_width=True)


# =====================================================
# TAB 3 — VALIDATION
# =====================================================
with tab3:

    st.subheader("🛡 Data Validation Summary")

    transfer_issues = df['Transfer_Validation'].sum()
    discharge_issues = df['Discharge_Validation'].sum()

    col1, col2 = st.columns(2)

    col1.metric("Transfer Validation Checks Passed", int(transfer_issues))
    col2.metric("Discharge Validation Checks Passed", int(discharge_issues))

    st.markdown("""
    **Validation Logic Applied:**
    - Transfers must not exceed children in CBP custody.
    - Discharges must not exceed children in HHS care.
    """)


# =====================================================
# TAB 4 — ABOUT PROJECT
# =====================================================
with tab4:

    st.subheader("About This Project")

    st.markdown("""
    This dashboard was developed as part of the **Unified Mentor Data Analytics Internship Program**.

    The dataset is sourced from the **U.S. Department of Health & Human Services (HHS)** and provides
    operational insights into:

    - Total system care load
    - Balance between intake, transfers, and discharges
    - Capacity stress and backlog accumulation
    - Forecasted system demand

    The objective of this project is to support data-driven decision-making
    for healthcare capacity planning and sustainability monitoring.
    """)


    # st.markdown("""
    # **Project Mentorship:**
    # AI-Powered Engineer | Head of Data Science | Sports Analytics Engineer [LinkedIn](https://www.linkedin.com/in/saiprasad-kagne)

    # **Developed By:**  
    # Parul Sharma
    # Data Analytics Intern – Unified Mentor
    # [LinkedIn](https://www.linkedin.com/in/shramanth-p-acharya)
    # """)

    st.markdown("""

    ### Developed By

    **Parul Sharma**  
    Data Analyst Intern – Unified Mentor  
    [LinkedIn Profile](https://www.linkedin.com/in/parul-sharma-215800208)
    """)

# -----------------------------------------------------
# Footer
# -----------------------------------------------------
st.markdown("---")
st.markdown(
    """
    <div style='text-align:center; font-size:13px; color:gray;'>
        Developed by <a href='https://www.linkedin.com/in/parul-sharma-215800208' target='_blank'>Parul Sharma</a><br> |
        Unified Mentor Internship Program<br>
        Data Source: U.S. Department of Health & Human Services (HHS)
    </div>
    """,
    unsafe_allow_html=True
)

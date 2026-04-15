import pandas as pd

def compute_metrics(df):

    # Total System Load
    df['Total_System_Load'] = df['CBP_Custody'] + df['HHS_Care']

    # Net Daily Intake
    df['Net_Intake'] = df['Transfers'] - df['Discharges']

    # Growth Rate
    df['Care_Load_Growth_Rate'] = df['Total_System_Load'].pct_change() * 100

    # Backlog Indicator
    df['Cumulative_Backlog'] = df['Net_Intake'].cumsum()

    # Rolling Stress Indicators
    df['7D_Rolling_Load'] = df['Total_System_Load'].rolling(7).mean()
    df['14D_Rolling_Load'] = df['Total_System_Load'].rolling(14).mean()

    # Volatility Index
    df['Volatility_Index'] = df['Total_System_Load'].rolling(7).std()

    # Discharge Offset Ratio
    df['Discharge_Offset_Ratio'] = df['Discharges'] / df['Transfers']

    return df
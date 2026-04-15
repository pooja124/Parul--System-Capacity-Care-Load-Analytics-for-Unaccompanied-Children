import pandas as pd
import numpy as np

def load_and_structure_data(filepath):
    df = pd.read_csv("data/HHS_Unaccompanied_Alien_Children_Program.csv")
    # Convert date column
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.drop_duplicates(subset='Date')

    df.columns = df.columns.str.strip()

    df = df.rename(columns={
        'Children apprehended and placed in CBP custody*': 'Apprehended',
        'Children in CBP custody': 'CBP_Custody',
        'Children transferred out of CBP custody': 'Transfers',
        'Children in HHS Care': 'HHS_Care',
        'Children discharged from HHS Care': 'Discharges'
    })

    numeric_cols = [
        'Apprehended','CBP_Custody',
        'Transfers','HHS_Care', 'Discharges'
    ]

    for col in numeric_cols:
        df[col] = (
            df[col]
            .astype(str)
            .str.replace(',', '', regex=False)  # remove commas
        )
        df[col] = pd.to_numeric(df[col], errors='coerce')
    # Sort chronologically
    df = df.sort_values('Date')

    # Create full daily date index
    full_range = pd.date_range(start=df['Date'].min(),
                               end=df['Date'].max(),
                               freq='D')

    df = df.set_index('Date').reindex(full_range)
    df.index.name = 'Date'

    # Forward fill missing values
    # df = df.fillna(method='ffill')
    df = df.ffill()
    return df

# Data Validation
def validate_data(df):
    df['Transfer_Validation'] = df['Transfers'] <= df['CBP_Custody']
    df['Discharge_Validation'] = df['Discharges'] <= df['HHS_Care']

    df['Anomaly_Flag'] = ~(
        df['Transfer_Validation'] &
        df['Discharge_Validation']
    )

    return df

from prophet import Prophet
import pandas as pd

def forecast_load(df, periods=60):

    forecast_df = df.reset_index()[['Date', 'Total_System_Load']]
    forecast_df.columns = ['ds', 'y']

    model = Prophet()
    model.fit(forecast_df)

    future = model.make_future_dataframe(periods=periods)
    forecast = model.predict(future)

    return forecast
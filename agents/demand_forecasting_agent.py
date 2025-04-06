# agents/demand_forecasting_agent.py

import pandas as pd
from prophet import Prophet
from sklearn.linear_model import LinearRegression
import joblib
import os

class DemandForecastingAgent:
    def __init__(self, data_path='data/demand_forecasting.csv', model_path='models/demand_model.pkl'):
        self.data_path = data_path
        self.model_path = model_path
        self.model = None

    def load_data(self):
        df = pd.read_csv(self.data_path, parse_dates=['Date'])
        df = df.rename(columns={'Date': 'ds', 'Sales Quantity': 'y'})
        return df[['ds', 'y']]

    def train_model(self, save=True):
        df = self.load_data()
        model = Prophet()
        model.fit(df)
        self.model = model
        if save:
            joblib.dump(model, self.model_path)

    def load_model(self):
        if os.path.exists(self.model_path):
            self.model = joblib.load(self.model_path)
        else:
            self.train_model()

    def forecast(self, periods=7):
        if self.model is None:
            self.load_model()
        future = self.model.make_future_dataframe(periods=periods)
        forecast = self.model.predict(future)
        return forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(periods)

if __name__ == '__main__':
    agent = DemandForecastingAgent()
    agent.train_model()
    forecast_df = agent.forecast()
    print(forecast_df)

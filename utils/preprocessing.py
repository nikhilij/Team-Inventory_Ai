# utils/preprocessing.py

import pandas as pd
from sklearn.preprocessing import LabelEncoder

def preprocess_demand_data(df):
    # Convert date
    df['Date'] = pd.to_datetime(df['Date'])
    df['DayOfWeek'] = df['Date'].dt.dayofweek
    df['Month'] = df['Date'].dt.month

    # Encode categorical features
    cat_cols = ['Promotions', 'Seasonality Factors', 'External Factors', 'Demand Trend', 'Customer Segments']
    for col in cat_cols:
        encoder = LabelEncoder()
        df[col] = encoder.fit_transform(df[col])

    return df

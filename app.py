import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from agents.demand_forecasting_agent import DemandForecastingAgent
from agents.inventory_agent import InventoryMonitoringAgent
from agents.pricing_agent import PricingOptimizationAgent
from agents.coordinator import CoordinatorAgent

# Load data
df_demand = pd.read_csv("data/demand_forecasting.csv")
df_inventory = pd.read_csv("data/inventory_monitoring.csv")
df_pricing = pd.read_csv("data/pricing_optimization.csv")

# Initialize Agents
demand_agent = DemandForecastingAgent("data/demand_forecasting.csv")
inventory_agent = InventoryMonitoringAgent("data/inventory_monitoring.csv")
pricing_agent = PricingOptimizationAgent("data/pricing_optimization.csv")
coordinator = CoordinatorAgent(demand_agent, inventory_agent, pricing_agent)

# Streamlit UI
st.title("🛒 Retail Inventory Optimization with Multi-Agent AI")
st.sidebar.header("🧠 Agent Control Panel")

# Select product ID
product_ids = df_demand["Product ID"].unique()
selected_product = st.sidebar.selectbox("Select Product ID", product_ids)

# Run Agent Simulation
if st.sidebar.button("Run Optimization"):
    result = coordinator.run_cycle(selected_product)
    st.success("Optimization Complete!")
    st.json(result)

# Show Product Data
st.subheader("📊 Product Details")
col1, col2 = st.columns(2)
with col1:
    st.write("Demand Forecasting Data")
    st.dataframe(df_demand[df_demand["Product ID"] == selected_product])
with col2:
    st.write("Inventory Monitoring Data")
    st.dataframe(df_inventory[df_inventory["Product ID"] == selected_product])

st.write("Pricing Optimization Data")
st.dataframe(df_pricing[df_pricing["Product ID"] == selected_product])

# Optional: Plot Sales Trends
if st.checkbox("📈 Show Sales Trend Chart"):
    product_data = df_demand[df_demand["Product ID"] == selected_product]
    product_data["Date"] = pd.to_datetime(product_data["Date"])
    fig, ax = plt.subplots()
    ax.plot(product_data["Date"], product_data["Sales Quantity"], marker="o")
    ax.set_title("Sales Trend Over Time")
    ax.set_xlabel("Date")
    ax.set_ylabel("Sales Quantity")
    st.pyplot(fig)

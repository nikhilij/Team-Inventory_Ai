# agents/coordinator.py

from agents.demand_forecasting_agent import DemandForecastingAgent
from agents.inventory_agent import InventoryMonitoringAgent
from agents.pricing_agent import PricingOptimizationAgent
from agents.supplier_agent import SupplierAgent

class CoordinatorAgent:
    def __init__(self):
        self.demand_agent = DemandForecastingAgent()
        self.inventory_agent = InventoryMonitoringAgent()
        self.pricing_agent = PricingOptimizationAgent()
        self.supplier_agent = SupplierAgent()

    def run_all_agents(self):
        print("\n--- Demand Forecasting ---")
        forecast = self.demand_agent.forecast_demand()
        print(forecast.head())

        print("\n--- Inventory Monitoring ---")
        inventory_issues = self.inventory_agent.check_stock_levels()
        print(inventory_issues)

        print("\n--- Reorder Suggestions ---")
        reorder = self.inventory_agent.reorder_suggestions()
        print(reorder)

        print("\n--- Pricing Optimization ---")
        pricing_suggestions = self.pricing_agent.suggest_new_prices()
        print(pricing_suggestions)

        print("\n--- Supplier Evaluation ---")
        supplier_issues = self.supplier_agent.evaluate_lead_times()
        print(supplier_issues)

        print("\n--- Supplier Suggestions ---")
        alt_sourcing = self.supplier_agent.suggest_alternate_sourcing()
        print(alt_sourcing)

if __name__ == '__main__':
    coordinator = CoordinatorAgent()
    coordinator.run_all_agents()

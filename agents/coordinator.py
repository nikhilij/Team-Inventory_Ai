# agents/coordinator.py

from agents.demand_forecasting_agent import DemandForecastingAgent
from agents.inventory_agent import InventoryMonitoringAgent
from agents.pricing_agent import PricingOptimizationAgent
from agents.supplier_agent import SupplierAgent

class CoordinatorAgent:
    def __init__(self, demand_agent, inventory_agent, pricing_agent, supplier_agent=None):
        self.demand_agent = demand_agent
        self.inventory_agent = inventory_agent
        self.pricing_agent = pricing_agent
        self.supplier_agent = supplier_agent or SupplierAgent()

    def run_cycle(self, product_id):
        print(f"Running cycle for product: {product_id}")

        # Step 1: Demand Forecasting
        print("\n--- Demand Forecasting ---")
        forecast = self.demand_agent.forecast(product_id)
        print(f"Forecast for Product {product_id}:")
        print(forecast)

        # Step 2: Inventory Monitoring
        print("\n--- Inventory Monitoring ---")
        inventory_status = self.inventory_agent.check_stock_levels()
        product_inventory = inventory_status[inventory_status['Product ID'] == product_id]
        print(f"Inventory Status for Product {product_id}:")
        print(product_inventory)

        # Step 3: Reorder Suggestions
        print("\n--- Reorder Suggestions ---")
        reorder_suggestions = self.inventory_agent.reorder_suggestions()
        product_reorder = [
            suggestion for suggestion in reorder_suggestions if suggestion['Product ID'] == product_id
        ]
        print(f"Reorder Suggestions for Product {product_id}:")
        print(product_reorder)

        # Step 4: Pricing Optimization
        print("\n--- Pricing Optimization ---")
        pricing_suggestions = self.pricing_agent.suggest_new_prices()
        product_pricing = [
            suggestion for suggestion in pricing_suggestions if suggestion['Product ID'] == product_id
        ]
        print(f"Pricing Suggestions for Product {product_id}:")
        print(product_pricing)

        # Compile results
        result = {
            "forecast": forecast,
            "inventory_status": product_inventory,
            "reorder_suggestions": product_reorder,
            "pricing_suggestions": product_pricing,
        }

        return result

    def run_all_agents(self):
        print("\n--- Demand Forecasting ---")
        forecast = self.demand_agent.forecast()  # Corrected method call
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
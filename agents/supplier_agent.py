# agents/supplier_agent.py

import pandas as pd

class SupplierAgent:
    def __init__(self, inventory_path='data/inventory_monitoring.csv'):
        self.inventory_df = pd.read_csv(inventory_path)

    def evaluate_lead_times(self):
        # Highlight suppliers with high lead times
        slow_suppliers = self.inventory_df[self.inventory_df['Supplier Lead Time (days)'] > 15]
        return slow_suppliers[['Product ID', 'Store ID', 'Supplier Lead Time (days)', 'Order Fulfillment Time (days)']]

    def suggest_alternate_sourcing(self):
        suggestions = []
        for _, row in self.evaluate_lead_times().iterrows():
            if row['Order Fulfillment Time (days)'] > 7:
                suggestions.append({
                    'Product ID': row['Product ID'],
                    'Store ID': row['Store ID'],
                    'Issue': 'High lead time and fulfillment time',
                    'Recommendation': 'Evaluate alternate supplier'
                })
        return suggestions

if __name__ == '__main__':
    agent = SupplierAgent()
    print("Suppliers with High Lead Times:")
    print(agent.evaluate_lead_times())
    print("\nAlternate Sourcing Suggestions:")
    print(agent.suggest_alternate_sourcing())

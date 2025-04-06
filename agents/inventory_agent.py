# agents/inventory_agent.py

import pandas as pd

class InventoryMonitoringAgent:
    def __init__(self, inventory_path='data/inventory_monitoring.csv'):
        self.inventory_path = inventory_path
        self.inventory_df = pd.read_csv(inventory_path)

    def check_stock_levels(self):
        low_stock = self.inventory_df[self.inventory_df['Stock Levels'] < self.inventory_df['Reorder Point']]
        return low_stock[['Product ID', 'Store ID', 'Stock Levels', 'Reorder Point']]

    def reorder_suggestions(self):
        low_stock = self.check_stock_levels()
        suggestions = []
        for _, row in low_stock.iterrows():
            reorder_qty = row['Reorder Point'] * 2 - row['Stock Levels']
            suggestions.append({
                'Product ID': row['Product ID'],
                'Store ID': row['Store ID'],
                'Suggested Order Quantity': reorder_qty
            })
        return suggestions

if __name__ == '__main__':
    agent = InventoryMonitoringAgent()
    print("Low Stock Items:")
    print(agent.check_stock_levels())
    print("\nReorder Suggestions:")
    print(agent.reorder_suggestions())

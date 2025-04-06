# agents/inventory_agent.py

import pandas as pd

import os

class InventoryMonitoringAgent:
    def __init__(self, inventory_data='data/inventory_monitoring.csv'):
        if isinstance(inventory_data, pd.DataFrame):
            self.inventory_df = inventory_data
        elif isinstance(inventory_data, str):
            if not os.path.exists(inventory_data):
                raise FileNotFoundError(f"Inventory file not found: {inventory_data}")
            self.inventory_df = pd.read_csv(inventory_data)
        else:
            raise TypeError("inventory_data should be a DataFrame or a file path (string).")

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

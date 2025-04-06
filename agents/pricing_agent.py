# agents/pricing_agent.py

import pandas as pd

import os

class PricingOptimizationAgent:
    def __init__(self, pricing_path='data/pricing_optimization.csv'):
        self.pricing_path = pricing_path
        if not os.path.exists(pricing_path):
            raise FileNotFoundError(f"Pricing file not found: {pricing_path}")
        self.pricing_df = pd.read_csv(pricing_path)

    def identify_discount_opportunities(self):
        # Identify products with low sales volume but high storage cost and low elasticity
        candidates = self.pricing_df[(self.pricing_df['Sales Volume'] < 100) &
                                     (self.pricing_df['Storage Cost'] > 7) &
                                     (self.pricing_df['Elasticity Index'] > 1.0)]
        return candidates[['Product ID', 'Store ID', 'Price', 'Storage Cost', 'Elasticity Index']]

    def suggest_new_prices(self):
        suggestions = []
        for _, row in self.identify_discount_opportunities().iterrows():
            discount_factor = min(0.2, 0.1 * row['Elasticity Index'])
            new_price = row['Price'] * (1 - discount_factor)
            suggestions.append({
                'Product ID': row['Product ID'],
                'Store ID': row['Store ID'],
                'Current Price': row['Price'],
                'Suggested Price': round(new_price, 2)
            })
        return suggestions

if __name__ == '__main__':
    agent = PricingOptimizationAgent()
    print("Discount Opportunities:")
    print(agent.identify_discount_opportunities())
    print("\nSuggested Price Updates:")
    print(agent.suggest_new_prices())

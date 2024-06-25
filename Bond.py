import numpy as np
import pandas as pd
from scipy.optimize import newton

def ytm(price, cash_flows):
    def calculate_present_value(rate):
        return np.sum([cf / (1 + rate)**((date - cash_flows.index[0]).days / 365) for date, cf in cash_flows.items()]) - price

    return newton(calculate_present_value, 0.05)

# Example usage
bond_price = 950
cash_flows = pd.Series([50, 50, 50, 50, 50], index=pd.to_datetime(['2023-01-01', '2024-01-01', '2025-01-01', '2026-01-01', '2027-01-01']))

yield_to_maturity = ytm(bond_price, cash_flows)
print(f"Yield to Maturity: {yield_to_maturity}")

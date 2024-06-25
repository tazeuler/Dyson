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

import numpy as np
import pandas as pd
from scipy.optimize import newton

class Bond:
    def __init__(self, isin, face_value, issue_date, maturity_date, price=None, yield_to_maturity=None):
        self.isin = isin
        self.face_value = face_value
        self.issue_date = pd.to_datetime(issue_date)
        self.maturity_date = pd.to_datetime(maturity_date)
        self.price = price
        self.yield_to_maturity = yield_to_maturity

    def calculate_cash_flows(self, coupon_rate):
        cash_flows = pd.Series([coupon_rate * self.face_value] * ((self.maturity_date.year - self.issue_date.year) + 1), 
                               index=pd.date_range(start=self.issue_date, end=self.maturity_date, freq=pd.DateOffset(years=1)))
        cash_flows.iloc[-1] += self.face_value  # Add face value to the last payment
        return cash_flows

    def calculate_price(self, yield_to_maturity, coupon_rate):
        cash_flows = self.calculate_cash_flows(coupon_rate)
        return np.sum([cf / (1 + yield_to_maturity)**((date - cash_flows.index[0]).days / 365) for date, cf in cash_flows.items()])

    def calculate_yield_to_maturity(self, coupon_rate):
        def calculate_present_value(rate):
            return np.sum([cf / (1 + rate)**((date - cash_flows.index[0]).days / 365) for date, cf in cash_flows.items()]) - self.price

        cash_flows = self.calculate_cash_flows(coupon_rate)
        return newton(calculate_present_value, 0.05)

# Example usage
bond = Bond(isin='US1234567890', face_value=1000, issue_date='2022-01-01', maturity_date='2027-01-01', price=950)
coupon_rate = 0.05
yield_to_maturity = bond.calculate_yield_to_maturity(coupon_rate)
print(f"Yield to Maturity: {yield_to_maturity}")

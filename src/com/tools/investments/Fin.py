import numpy as np
import numpy_financial as npf

# Constants for calculations
cost_of_property_czk = 9000000
down_payment_percentage = 0.20
current_savings_czk = 1200000
monthly_savings_czk = 65000
monthly_investment_usd = 1000
usd_to_czk_rate = 23  # Estimated current exchange rate
annual_return_rate = 0.06  # 6%
mortgage_rate = 0.065  # 6.5%
mortgage_term_years = 30
monthly_investment_czk = monthly_investment_usd * usd_to_czk_rate

# 1. Down Payment Savings Time
down_payment_required_czk = cost_of_property_czk * down_payment_percentage
remaining_for_down_payment_czk = down_payment_required_czk - current_savings_czk
net_monthly_savings_czk = monthly_savings_czk - monthly_investment_czk
time_to_save_down_payment_months = remaining_for_down_payment_czk / net_monthly_savings_czk

# 2. Mortgage Payment and Payoff Time
mortgage_amount_czk = cost_of_property_czk - down_payment_required_czk
monthly_mortgage_rate = mortgage_rate / 12
number_of_payments = mortgage_term_years * 12
monthly_mortgage_payment_czk = mortgage_amount_czk * monthly_mortgage_rate / (1 - (1 + monthly_mortgage_rate) ** -number_of_payments)
#
# # 3. Investment Value at Mortgage Payoff
# investment_period_months = mortgage_term_years * 12
# investment_value_at_mortgage_payoff_czk = np.fv(annual_return_rate / 12, investment_period_months, -monthly_investment_czk, 0)
#
# # 4. Investment Value in 30 Years
# total_investment_period_months = 30 * 12
# investment_value_in_30_years_czk = np.fv(annual_return_rate / 12, total_investment_period_months, -monthly_investment_czk, 0)

# time_to_save_down_payment_months, monthly_mortgage_payment_czk, investment_value_at_mortgage_payoff_czk, investment_value_in_30_years_czk



# Correcting the variable name for total investment period in months
total_investment_period_months = 30 * 12

# Recalculating the investment value in 30 years using numpy_financial
# investment_value_in_30_years_czk = npf.fv(annual_return_rate / 12, total_investment_period_months, -monthly_investment_czk, 0)

# time_to_save_down_payment_months, monthly_mortgage_payment_czk, investment_value_at_mortgage_payoff_czk, investment_value_in_30_years_czk


# Updated figures for calculations
available_savings_for_down_payment = 360000  # CZK

# Option 1: Getting a Mortgage

# # 1. Down Payment Savings Time (Updated)
# remaining_for_down_payment_czk = down_payment_required_czk - available_savings_for_down_payment
# time_to_save_down_payment_months = remaining_for_down_payment_czk / net_monthly_savings_czk
#
# # The rest of the calculations for Option 1 remain the same
# # Recalculating with the updated figures for Option 1
# time_to_save_down_payment_months, monthly_mortgage_payment_czk, investment_value_at_mortgage_payoff_czk, investment_value_in_30_years_czk
#
#
#
#
#
# # Recalculating the investment value at mortgage payoff and in 30 years using numpy_financial
#
# # 3. Investment Value at Mortgage Payoff (using numpy_financial)
# investment_value_at_mortgage_payoff_czk = npf.fv(annual_return_rate / 12, investment_period_months, -monthly_investment_czk, 0)
#
# # 4. Investment Value in 30 Years (using numpy_financial)
# investment_value_in_30_years_czk = npf.fv(annual_return_rate / 12, total_investment_period_months, -monthly_investment_czk, 0)
#
# time_to_save_down_payment_months, monthly_mortgage_payment_czk, investment_value_at_mortgage_payoff_czk, investment_value_in_30_years_czk



# Constants for Option 2 calculations
inflation_rate = 0.03  # 3% annual inflation rate

# 1. Time to Save Cash for Full Purchase (Considering Inflation)
# Adjusting the target cost of the property for inflation over time
# We'll use a loop to calculate how long it will take to reach the target considering inflation

current_savings = current_savings_czk
target_property_cost = cost_of_property_czk
years_to_save = 0

# while current_savings < target_property_cost:
#     current_savings += net_monthly_savings_czk * 12  # Adding annual savings
#     target_property_cost *= (1 + inflation_rate)  # Adjusting target for inflation
#     years_to_save += 1

# 2. Investment Value When Ready to Buy
# Assuming investments start after reaching the target
# Since the savings goal is reached at the point of buying the house, the investment value will start from that point.

# 3. Investment Value in 30 Years (Considering Investments Start After House Purchase)
investment_start_year = years_to_save
remaining_investment_period_months = (30 - investment_start_year) * 12
investment_value_in_30_years_after_purchase_czk = npf.fv(annual_return_rate / 12, remaining_investment_period_months, -monthly_savings_czk, 0)

print(f"investment value: {investment_value_in_30_years_after_purchase_czk}")



# Efficient calculation for Option 2: Time to Save Cash for Full Purchase
# Option 2: Buying with Cash (Updated Calculations)

# 1. Time to Save Cash for Full Purchase (Considering Inflation) - Updated
current_savings = available_savings_for_down_payment  # Starting with available savings
target_property_cost = cost_of_property_czk
years_to_save_for_cash_purchase = 0

# while current_savings < target_property_cost:
#     current_savings += net_monthly_savings_czk * 12  # Adding annual savings
#     target_property_cost *= (1 + inflation_rate)  # Adjusting target for inflation
#     years_to_save_for_cash_purchase += 1

# 3. Investment Value in 30 Years (Considering Investments Start After House Purchase) - Updated
investment_start_year_for_cash_purchase = years_to_save_for_cash_purchase
remaining_investment_period_months_for_cash_purchase = (30 - investment_start_year_for_cash_purchase) * 12
investment_value_in_30_years_after_cash_purchase_czk = npf.fv(annual_return_rate / 12, remaining_investment_period_months_for_cash_purchase, -monthly_savings_czk, 0)

years_to_save_for_cash_purchase, investment_value_in_30_years_after_cash_purchase_czk



# Function to calculate the years needed to save for the house, considering inflation
def calculate_years_to_save(starting_savings, monthly_savings, target_cost, inflation_rate):
    years = 0
    current_savings = starting_savings

    while current_savings < target_cost:
        current_savings += monthly_savings * 12  # Annual savings
        current_savings *= (1 + inflation_rate)  # Savings growth due to interest
        target_cost *= (1 + inflation_rate)  # Cost increase due to inflation
        years += 1

    return years

# Recalculating years to save for cash purchase
years_to_save_for_cash_purchase = calculate_years_to_save(available_savings_for_down_payment, net_monthly_savings_czk, cost_of_property_czk, inflation_rate)

# Recalculating investment value in 30 years for cash purchase
remaining_investment_period_months_for_cash_purchase = (30 - years_to_save_for_cash_purchase) * 12
investment_value_in_30_years_after_cash_purchase_czk = npf.fv(annual_return_rate / 12, remaining_investment_period_months_for_cash_purchase, -monthly_savings_czk, 0)

years_to_save_for_cash_purchase, investment_value_in_30_years_after_cash_purchase_czk





# Function to calculate the accumulated investment value over time, considering regular contributions
def calculate_investment_value(starting_savings, monthly_savings, annual_return_rate, years):
    current_savings = starting_savings
    for year in range(years):
        # Adding annual savings and interest for the year
        current_savings += monthly_savings * 12
        current_savings *= (1 + annual_return_rate)
    return current_savings


if __name__ == "__main__":

    # 1. Calculating the investment value when ready to buy
    # We need to find the year when the investment value reaches the target property cost considering inflation
    investment_year_to_buy = 0
    investment_value_when_ready_to_buy = 0
    print(investment_year_to_buy)
    while investment_value_when_ready_to_buy < target_property_cost:
        investment_value_when_ready_to_buy = calculate_investment_value(available_savings_for_down_payment,
                                                                        net_monthly_savings_czk, annual_return_rate,
                                                                        investment_year_to_buy)
        target_property_cost *= (1 + inflation_rate)  # Adjusting target for inflation
        investment_year_to_buy += 1
        # print(target_property_cost)

    # 2. Investment Value in 30 Years (Considering Investments Start Now)
    investment_value_in_30_years_with_continuous_investment_czk = calculate_investment_value(
        available_savings_for_down_payment, net_monthly_savings_czk, annual_return_rate, 30)

    investment_year_to_buy, investment_value_when_ready_to_buy, investment_value_in_30_years_with_continuous_investment_czk
    print(investment_year_to_buy)
    print(investment_value_when_ready_to_buy)
    print(investment_value_in_30_years_with_continuous_investment_czk)

import numpy_financial as npf
import pandas as pd
import locale
import matplotlib.pyplot as plt


def calculate_investment_over_time(initial_investment, monthly_investment, annual_interest_rate, years):
    """
    Calculate the future value of an investment over a specified number of years,
    allowing for adjustments at the end of each year.

    Args:
    initial_investment (float): The initial amount invested.
    annual_interest_rate (float): The annual interest rate (as a decimal).
    years (int): The number of years to calculate the investment for.
441380.52
    Returns:
    dict: A dictionary containing the year and the corresponding investment value for each year.
    """
    investment_data = []
    previous_year_value = 0
    starting_year = 2024
    for year in range(1, years + 1):
        future_value = npf.fv(annual_interest_rate / 12, year * 12, monthly_investment, -initial_investment)
        total_contributions = initial_investment + (-monthly_investment * 12 * year)
        if year == 1:
            interest_earned = future_value - total_contributions
        else:
            interest_earned = future_value - previous_year_value - (-monthly_investment * 12)
        investment_return = future_value - total_contributions
        investment_data.append({
            'Year': year + starting_year,
            'Investment Value': locale.currency(round(future_value, 2), grouping=True), # combined of total contributions and interest
            'Investment Return': locale.currency(round(investment_return, 2), grouping=True), # this is an actual value of the investments
            'Total Contributions': locale.currency(round(total_contributions, 2), grouping=True),
            'Interest Earned': locale.currency(round(interest_earned), grouping=True)
        })
        previous_year_value = future_value
    df = pd.DataFrame(investment_data)
    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(df['Year'], df['Investment Value'], marker='o', label='Investment Value')
    # plt.yscale('log')  # Set logarithmic scale
    plt.plot(df['Year'], df['Interest Earned'], marker='x', label='Interest Earned')
    plt.title('Investment Over Time')
    plt.xlabel('Year')
    plt.ylabel('Amount ($)')
    plt.grid(True)
    plt.legend()
    plt.show()
    return df

if __name__ == "__main__":
    locale.setlocale(locale.LC_ALL, 'cs_CZ.UTF-8')
    # Example usage (you can modify the initial values)
    initial_investment = float(input("Enter initial investment amount: "))
    monthly_investment = -float(input("Enter monthly investment amount: "))
    annual_interest_rate = float(input("Enter annual interest rate (as a decimal): "))
    years = int(input("Enter the number of years for the investment: "))

    investment_over_time = calculate_investment_over_time(initial_investment, monthly_investment, annual_interest_rate, years)
    print("Investment Values Over Time:")
    print(investment_over_time)

import numpy_financial as npf
import locale

def calculate_mortgage_payments_np(property_cost, down_payment, mortgage_rate, mortgage_period, desired_payoff_time=None):
    # Convert annual rate to monthly and period to months
    monthly_rate = mortgage_rate / 100 / 12
    mortgage_period_months = mortgage_period * 12

    # Calculate principal
    principal = property_cost - down_payment

    # Monthly payment calculation using numpy_financial
    monthly_payment = npf.pmt(monthly_rate, mortgage_period_months, -principal)

    # Total amount paid over the life of the mortgage
    total_payment = monthly_payment * mortgage_period_months

    results = {
        "Monthly Payment for Original Period": locale.currency(round(monthly_payment, 2), grouping=True),
        "Total Payment for Original Period": locale.currency(round(total_payment, 2), grouping=True)
    }

    # Calculation for desired payoff time
    if desired_payoff_time:
        desired_payoff_months = desired_payoff_time * 12
        monthly_payment_desired = npf.pmt(monthly_rate, desired_payoff_months, -principal)
        total_payment_desired = monthly_payment_desired * desired_payoff_months

        results.update({
            f"Monthly Payment for {desired_payoff_time} Years": locale.currency(round(monthly_payment_desired, 2), grouping=True) ,
            f"Total Payment for {desired_payoff_time} Years": locale.currency(round(total_payment_desired, 2), grouping=True)
        })

    return results


if __name__ == "__main__":
    locale.setlocale(locale.LC_ALL, 'cs_CZ.UTF-8')
    res = calculate_mortgage_payments_np(8_100_000, 800_000, 6.5, 30, 10)
    for key, value in res.items():
        print(f"{key}: {value}")


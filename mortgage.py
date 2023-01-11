import math


def mortgage_payment(principal, rate, terms, compounding_interval):
    """
    Calculates the monthly mortgage payment.
    principal: the total loan amount
    rate: the annual interest rate (decimal)
    terms: the number of terms (months)
    compounding_interval: the number of compounding periods per year
    """
    # Convert interest rate to decimal and adjust for compounding interval
    r = rate / compounding_interval
    # Calculate the fixed monthly payment
    payment = principal * ((r * (1 + r) ** terms) / ((1 + r) ** terms - 1))
    return payment


def time_to_repayment(principal, rate, payment, compounding_interval):
    """
    Calculates the number of years to repayment.
    principal: the total loan amount
    rate: the annual interest rate (decimal)
    payment: the monthly payment amount
    compounding_interval: the number of compounding periods per year
    """
    r = rate / compounding_interval
    terms = math.log(payment / (payment - r * principal)) / math.log(1 + r)
    return terms / compounding_interval


def main():
    principal = 600000  # total loan amount
    rate = 0.04  # annual interest rate (decimal)
    terms = 30 * 12  # number of terms (months)
    compounding_interval = 365  # number of compounding periods per year (12 for monthly, 52 for weekly, 365 for daily)
    monthly_payment = mortgage_payment(principal, rate, terms, compounding_interval)
    years = round(time_to_repayment(principal, rate, monthly_payment, compounding_interval), 2)
    print("Years to repayment: ", years)


if __name__ == '__main__':
    main()

#Dave has decided to take out a 30-year fixed rate mortgage of $500,000
# with Guido's Mortgage, Stock Investment, and Bitcoin trading corporation.
# The interest rate is 5% and the monthly payment is $2684.11.

year = 30
amount = 500000.0
rate = 0.05
monthly_paymant = 2684.11
total_paid = 0.0

while amount > 0:
    amount_with_interest = amount * (1 + rate/12)
    if amount_with_interest < monthly_paymant:
        total_paid += amount_with_interest
        amount = 0
    else:
        amount = amount_with_interest - monthly_paymant
        total_paid += monthly_paymant
print('Total paid', total_paid)
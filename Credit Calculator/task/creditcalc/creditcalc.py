from math import ceil

credit_principal = 'Credit principal: 1000'
final_output = 'The credit has been repaid!'
first_month = 'Month 1: paid out 250'
second_month = 'Month 2: paid out 250'
third_month = 'Month 3: paid out 500'

# write your code here
print(credit_principal, first_month, second_month, third_month, final_output, sep='\n')


def last_payment(p, pay, period):
    return p - (period - 1) * pay


print("Enter the credit principal:")
principal = float(input())

print("What do you want to calculate?")
print('type "m" - for the number of months,')
print('type "p" - for the monthly payment:')
choice = input()
if choice == 'm':
    print("Enter the monthly payment:")
    m_payments = float(input())
    p_p = ceil(principal / m_payments)
    print(f"It takes {p_p} months to repay the credit" if p_p != 1 else "It takes 1 month to repay the credit")

elif choice == 'p':
    print("Enter the count of months:")
    count_months = float(input())
    m_p = ceil(principal / count_months)
    if (m_p * count_months) <= principal:
        print(f"Your monthly payment = {m_p}")

    if (m_p * count_months) > principal:
        print(f"Your monthly payment = {m_p} with last monthly payment = {principal - (count_months - 1) * m_p}.")

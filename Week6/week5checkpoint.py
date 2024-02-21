print("Let's see if you can get a loan!")
print("On a scale of 1-10...")
loan_size = int(input('How large is the loan? '))
credit_history = int(input('How good is your credit history? '))
income_level = int(input('How high is your income? '))
down_payment_largeness = int(input('How large is your downpayment? '))

decision = 'no'

if loan_size >= 5:
    if credit_history >= 7 and income_level >= 7:
        decision = 'yes'
    elif credit_history >= 7 or income_level >= 7:
        if down_payment_largeness >= 5:
            decision = 'yes'
        else:
            decision = 'no'
else: #loan size is less than 5
    if credit_history < 4:
        decision = 'no'
    elif credit_history >= 4:
        if (income_level >= 7 or down_payment_largeness >= 7) or (income_level >= 4 and down_payment_largeness >= 4):
            decision = 'yes'
        else:
            decision = 'no'
if decision == 'yes':
    print('You can get a loan!')
else:
    print("You can't get a loan!")
            
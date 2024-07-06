bank_accounts = []
account_balances =[]
ending_keyword = 'quit'

#for appending to lists
account_list = ''
balances_list = ''

print('Enter the names and balances of bank accounts (type: quit when done)')

while True:
    account_list = input('What is the name of this account? ')
    if account_list.lower() == ending_keyword:
        break
    balances_list = float(input('What is the balance? '))
    bank_accounts.append(account_list)
    account_balances.append(balances_list)  
      
sum = 0

print('Account Information: ')
for i, accountname in enumerate(bank_accounts):
    print(f'{accountname} - ', end = ' ')
    balance = account_balances[i]
    sum += balance
    print(f'${balance:.2f}')

sum_average = sum / (len(account_balances))

highest_account = ''
highest_balance = 0
for i, balance in enumerate(account_balances):
    if balance > highest_balance:
        highest_balance = balance
        highest_account = bank_accounts[i]

print(f'Total: ${sum:.2f}')
print(f'Average: ${sum_average:.2f}')
print(f'Highest balance: {highest_account} - ${highest_balance}')
print('')

answer = ''

if answer != 'no':  
    answer = input('Do you want to update an account? ')
    account_index_change = input('What account index do you want to update? ')
    account_new_amount = input('What is the new amount? ')
    
    account_balances[account_index_change]=account_new_amount
        

#This code is unfinished

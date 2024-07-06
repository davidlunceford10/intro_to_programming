number = int(input('Please type a positive number: '))

while number <= -1:
    print("That's negative. Try again.")
    number = int(input('Please type a positive number: '))

print(f'The number is: {number}.')


candy = input('May I have a piece of candy? ')

while candy.lower() == 'no':
    candy = input('May I have a piece of candy? ')
    
if candy.lower() == 'yes':
    print('Thank you.')


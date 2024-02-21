number = int(input('Please type a positive number: '))

while number <= 0:
    print("That's negative bruh. Try again.")
    number = int(input('Please type a positive number: '))

print(f'The number is: {number}.')


candy = input('May I have a piece of candy? ')

while candy == 'no'.lower():
    candy = input('May I have a piece of candy? ')


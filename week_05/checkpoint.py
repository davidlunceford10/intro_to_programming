number_one = float(input('What is the first number? '))
number_two = float(input('What is the second number? '))

response1 = ''
response2 = ''
response3 = ''

if number_one > number_two:
    response1 = 'The first number is greater.'
else:
    response1 = 'The first number is not greater.'

    
if number_one == number_two:
    response2 = 'The numbers are equal.'
else:
    response2 = 'The numbers are not equal.'


if number_two > number_one:
    response3 = 'The second number is greater.'
else:
    response3 = 'The second number is not greater'

print('')
print(response1)
print(response2)
print(response3)

my_favorite_animal = 'wolverine'
user_favorite_animal = input('What is your favorite animal? ')

if user_favorite_animal.lower() == my_favorite_animal:
    print("That's my favorite animal too!")
else:
    print("That one is not my favorite.")
    
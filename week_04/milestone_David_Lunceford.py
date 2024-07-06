print("Welcome to Bigtop Burger! Let's get your order started!")

child_meal_price = float(input("What's the price of a child's meal? "))
adult_meal_price = float(input("What's the price of an adult's meal? "))
child_count = int(input('How many children are there? '))
adult_count = int(input('How many adults are there? '))
salestax_rate = float(input('What is the sales tax rate? '))

meal_subtotal = (child_count * child_meal_price) + (adult_count * adult_meal_price)
meal_subtotal_rounded = round(meal_subtotal, 2)

print('')

print(f'Subtotal: ${meal_subtotal_rounded:.2f}')

sales_tax = meal_subtotal_rounded * salestax_rate / 100

print(f'Sales Tax: ${sales_tax:.2f}')

total_price = meal_subtotal_rounded + sales_tax

print(f'Total: ${total_price:.2f}')
print('')

payment_amount = float(input('What is the payment amount? '))

change = payment_amount - total_price

print(f'Change: ${change:.2f}')

print('')
customer_rating = int(input('On a scale of 1 to 10 how was your visit? '))
print(f'Your rating was {customer_rating}. Thank you for eating at Bigtop Burger!')




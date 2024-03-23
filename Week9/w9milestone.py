shopping_list_items = []
shopping_list_prices = []
action = ''

while action != '5':
    print('Welcome to the Shopping Cart Program!')
    print('')
    print('Please select one of the following: ')
    print('1. Add item')
    print('2. View cart')
    print('3. Remove item')
    print('4. Compute total')
    print('5. Quit')

    action = input('Please enter an action: ')

    if action == '1':
        item = input('What item would you like to add? ')
        item_price = float(input('What is the price of the item? '))
        shopping_list_items.append(item)
        shopping_list_prices.append(item_price)
        print(f'"{item.title()}" has been added to the cart.')
        print('')

    if action == '2':
        print('The contents of the shopping cart are: ')
        
        for index, (item, price) in enumerate(zip(shopping_list_items,shopping_list_prices), start=1):
            print(f'{index}. {item.title()} - ${price:.2f}')

    if action == '5':
        print('Thank you. Goodbye.')

    print('')
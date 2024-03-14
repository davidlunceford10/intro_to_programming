shopping_list_items = []
shopping_list_price = []
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
        shopping_list_items.append(item)
        print(f'{item.title()} has been added to the cart.')
        print('')

    if action == '2':
        print('The contents of the shopping cart are: ')
        for item in shopping_list_items:
            print(item)
    print('')
import time
shopping_list_items = []
action = None


print('\nWelcome to the Shopping Cart Program!\n')
time.sleep(1.5)

while action != '5':
    print('Please select one of the following: ')
    print('1. Add item') 
    print('2. View cart')
    print('3. Remove item')
    print('4. Compute total')
    print('5. Quit')

    action = float(input('Please enter an action: '))

    if action == 1:
        item = input('What item would you like to add? ')   
        price = float(input('What is the cost of the item? '))
        shopping_list_items.append([item, price])
        print(f"\n'{item}' has been added to the cart.\n")
        time.sleep(1.5)

    if action == 2:
        print('The contents of the shopping cart are:\n')
        for i, item in enumerate(shopping_list_items):
            print(f'{i+1}. {item[0].title()} - ${item[1]:.2f}' )  
        print()
        time.sleep(2)
   
    if action == 3:
        input_v = None
        while input_v != -1:
            rm_item = int(input('Which item would you like to remove? '))
            if rm_item > len(shopping_list_items):
                print('Invalid value')
            else:
                shopping_list_items.pop(rm_item-1)
                print('\nItem removed')
                input_v=-1
                time.sleep(1.5)
                print('')
                
    if action == 4:
        total =0
        for i, items in enumerate(shopping_list_items):
            total += items[1]
        print(f'\nTotal: ${total:.2f}\n')
        time.sleep(3)
        
    if action == 5:
        print('Thank you! Goodbye.')
        break
            
            
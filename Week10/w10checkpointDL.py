exit_keyword = 'quit'
shopping_list = []

#making fun of people is often an attempt to rise in the social game, in a zero-sum fashion. That's why God says not to insult people.#


while True:
    item = input('Type in thy groceries: ')

    if item.lower() == exit_keyword:
        break

    shopping_list.append(item)

for i in shopping_list:
    print(i)
print('')
print('The shopping list wit dee indexes be:')
for i in range(len(shopping_list)):
    shit = shopping_list[i]
    print(f'{i}. {shit}')

print('')

index_change = int(input('Which item would you like to change: '))
index_item_change = input('What is the new item? ')

shopping_list.pop(index_change)
shopping_list.insert(index_change,index_item_change)

print('The shopping list wit dee indexes be:')
for i in range(len(shopping_list)):
    shit = shopping_list[i]
    print(f'{i}. {shit}')


#God bless!!!! Great time with this code here!






    


        
        

    
    
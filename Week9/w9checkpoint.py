friends_list = []

while True:
    friend_name = input("Type the name of a friend: ")
    
  
    if friend_name == 'end':
        break  
    
    
    friends_list.append(friend_name)


print("List of friends:")
for friend in friends_list:
    print(friend)




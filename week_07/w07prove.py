number = 0

while number <= 0:
    number = int(input('Please enter a positive number: '))
    if number <= 0:
        print("That is not a positive number.")
print(f"The number is {number}.")

answer = "no"

while answer != "yes":
    answer = input("Can I have a piece of candy? " )
print("Thank you.")
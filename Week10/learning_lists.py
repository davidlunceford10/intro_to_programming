books = ['First', 'Second', 'Third', 'Obama']

for i in range(len(books)):
    book = books[i]
    i += 1
    print(f'{i}. {book}')

print('')
names = ["Alice", "Bob", "Charlie", "David", "Emma", "Frank", "Grace", "Henry", "Ivy", "Jack"]
numbers = [
    "555-123-4567",
    "555-987-6543",
    "555-456-7890",
    "555-234-5678",
    "555-876-5432",
    "555-345-6789",
    "555-765-4321",
    "555-678-9012",
    "555-543-2109",
    "555-890-1234"
]

# ...
# Code here that populates the two lists
# ...

for i in range(len(names)):
    name = names[i]
    number = numbers[i]

    print(f"{name} - {number}")
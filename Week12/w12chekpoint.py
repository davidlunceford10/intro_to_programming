people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

names = []
ages = []
youngest_person_age = float('inf')
youngest_person_name = ''

for guy in people:
    name, age = guy.split()
    names.append(name)
    ages.append(int(age))

proper_age_dictionary = {name_key: age_value for name_key, age_value in zip(names, ages)}

min_name_key = None
min_age_value = None

for key, value in proper_age_dictionary.items():
    if min_age_value is None or value < min_age_value:
        min_name_key = key
        min_age_value = value

print(f"The youngest person here is {min_name_key}, coming in at {min_age_value} years old. Give him high fives and fist bumps he is legitimately better than you as as person.")


            

  
    


    
    
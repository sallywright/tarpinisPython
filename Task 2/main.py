# Turimas "users" masyvas. 

# Parašykite funkcijas, kurios atlikas nurodytas užduotis:
# 1. funkcija "get_user_average_age" - kaip argumentą priims masyvą ir duoto masyvo
# atveju grąžins visų "users" amžiaus visurkį kaip skaičių.
# 2. funkcija "get_user_names" -  kaip argumentą priims masyvą ir duoto masyvo
# atveju grąžins visų "users" vardus naujame list'e pvz., ['Alex John', 'Ann Smith'...].

# Pastaba: rezultatai turi būti išrikiuoti abėcėlės tvarka

users = [
  { "id": '1', "name": 'John Smith', "age": 20 },
  { "id": '2', "name": 'Ann Smith', "age": 24 },
  { "id": '3', "name": 'Tom Jones', "age": 31 },
  { "id": '4', "name": 'Rose Peterson', "age": 17 },
  { "id": '5', "name": 'Alex John', "age": 25 },
  { "id": '6', "name": 'Ronald Jones', "age": 63 },
  { "id": '7', "name": 'Elton Smith', "age": 16 },
  { "id": '8', "name": 'Simon Peterson', "age": 30 },
  { "id": '9', "name": 'Daniel Cane', "age": 51 },
]

def get_user_average_age(users:list):
  average = 0
  for user in users:
    average+=user["age"]
  
  return (average/len(users))

def get_user_names(users:list):
  names= []
  for user in users:
    names.append(user["name"])
  return names

print(get_user_average_age(users))
print(get_user_names(users))
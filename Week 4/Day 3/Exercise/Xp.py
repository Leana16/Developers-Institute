#Exercise 1
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

my_dict = zip(keys,values)
print(my_dict)
print(dict(my_dict))

#Exercise 2
# age = ''
# if age < 3:
#     print('the ticket is free')
# elif 3 >= age <= 12:
#     print('the ticket is $10')
# elif age > 12:
#     print('the ticket is $15')

# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

#Exercise 3
brand = {
    'name': 'Zara',
    'creation_date': 1975, 
    'creator_name': 'Amancio Ortega Gaona', 
    'type_of_clothes': ['men', 'women', 'children', 'home'],
    'international_competitors': ['Gap', 'H&M', 'Benetton'], 
    'number_stores': 7000, 
    'major_color': {
    'France': 'blue', 
    'Spain': 'red', 
    'US': ['pink', 'green']
    }
}
brand['number_stores'] = 2
print(brand)

txt = 'My clients are {}'.format('types_of_clothes')
print(txt)

brand['country_creation'] = 'Spain'
print(brand)

brand['international_competitors'] += ['Desigual']
print(brand)

del brand['creation_date']
print(brand)

print(brand['international_competitors'][3])

print(brand['major_color']['US'][0])

print(len(brand))

print(brand.keys())

more_on_zara ={
     'creation_date': 1975,
     'number_stores': 7000 
}

brand.update(more_on_zara)
print(brand)

print(brand['number_stores'])

#Exercise 4
users = ["Mickey","Minnie","Donald","Ariel","Pluto"]

for  user in enumerate(users):
    li = list(user)
    print(li)

list = users.index
for user in users:
    list.append(user)
    print(list)
    
#Exercise 1
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

my_dict = zip(keys,values)
print(my_dict)
print(dict(my_dict))

#Exercise 2
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
fam = {}

price = 0
for age in family.values():
 if age < 3:
     price += 0
 elif 3 <= age <= 12:
     price += 15
 elif age > 12:
     price += 15
   # print('You will pay ${}'.format())

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

txt = 'My competitors are {}'.format('international_competitors')
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
disney_users_A = {}

for  user in enumerate(users):
    a, b = user
    disney_users_A[b] = a
print(disney_users_A)

disney_users_B = {}

for  user in enumerate(users):
    c, d = user
    disney_users_B[c] = d
print(disney_users_B)

disney_users_C = {}
sort = sorted(users)

for  user in enumerate(sort):
    e, f = user
    disney_users_C[f] = e
print(disney_users_C)

#Daily challenge
dic = {}
words = input('Enter a word: ')

for i, letter in enumerate(words):
    if letter not in dic:
        dic[letter] = []
        dic[letter].append(i)
print(dic)
    
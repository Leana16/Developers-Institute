dic = {
    'name':'Sone',
    'color':'black',
    'hobby':'coding'
}
print(dic['name'], dic['color'])
print(dic.items())

for name, sone in dic.items():
    print(name, '->', sone)


shirts = [
  {
    'name': 'Awesome T-shirt 3000',
    'size': 'S',
    'price': 20
  },
  {
    'name': 'Awesome T-shirt 3000',
    'size': 'M',
    'price': 25
  },
  {
    'name': 'Awesome T-shirt 3000',
    'size': 'L',
    'price': 30
  },
]
for s in shirts:
  print(s['name'])

for s in shirts:
    for key, value in s.items():
        print(key,value)


# for s in range(len(shirts)):
#     print(shirts[s]['name'])

sample_dict = { 
   "class":{ 
      "student":{ 
         "name":"Mike",
         "marks":{ 
            "physics":70,
            "history":80
         }
      }
   }
}
print(sample_dict['class']['student']['marks']['history'])

sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}
remove_keys = ['name','salary']
for key in remove_keys:
    del sample_dict[key]
    print(sample_dict)  

print(list(range(1, 10, 2)))

#enumerate
for item in enumerate('abcd'):
    print(item)

for (index_count, letter) in enumerate('abcd'):
    print('At index {} the letter is {}'.format(index_count, letter))

#zip(iterate)
list1 = [12, 14, 16, 17, 18]
list2 = ['AB','BD','KA', 'TB', 'EX']
list3 = ['Ar', 'Br', 'Cr', 'Zr', 'Yr']

for item in zip(list1, list2, list3):
    print(item)

#for else
for i in range(1, 10):
    print(i)
else:
    print('The for loop is over')

#while else as long as the condition is true, the program will be excuted stilll
x = 0
while x < 6:
    print(f'x is {x}')
    x += 1 
else:
    print('x is bigger than 6')

#break
# for letter in 'Leonardo':
#     if letter == 'o':
#         break
#     print(letter, end='') #end='' join each letter next together

nom = 'Leonardo'
li =list(nom)
print(''.join(li[0:7]))

for l in li:
    if l == li[7]:
         break
    print(l, end='')

for l in range(len(name)):
    if l == name.find('o', name.find('o')+1):
      break
print(name[l], end='')


while True:
      s = input('Enter something : ')
      if s == 'quit':
         break
      print('Length of the string is', len(s))
print('Done')

#continue
for letter in 'Leonardo':
    if letter == 'o':
        continue
    print(letter, end='')

while True:
    s = input('Enter something : ')
    if 'quit' in s:
        break
    if len(s) < 3:
        print('Too small')
        continue
    print('Input is of sufficient length')

#pass(to avoid the error)
for item in [1,2,3]: 
    pass 
print('Finish the script')

my_number = '1234'
my_list = []

#ppend an element into a list
for num in my_number:
    my_list.append(num)
print(my_list)

#range
my_list = [x for x in range(0,6)]
print(my_list)

my_list = [x**2 for x in range(0,6)] # square
print(my_list)

my_list = [x for x in range(0,11) if x%2 == 0] # only even
print(my_list)

#append an element into a list with nested loop
my_list = []

for i in [2, 3, 4]:
    for j in [100, 200, 300]:
        my_list.append(i*j)

print(my_list)

family_age = {'Lea': 12, 'Mark': 25, 'George': 50}
new_year = 1
family = {name: 'age'+new_year}
for family in family_age.items():
    print(family)

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
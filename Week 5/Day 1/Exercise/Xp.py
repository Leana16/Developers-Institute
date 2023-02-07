#Exercise 1
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

cat1 = Cat('Mimi', 6)
cat2 = Cat('Kitty', 10)
cat3 = Cat('Helly', 2)
#Exercise 2
class Dog():
    def __init__(self, name, height):
     self.name = name
     self.height = height
    def bark(self):
        print(f'{self.name} goes woof!')
    def jump(self):
        x  = self.height * 2
        print(f'{self.name} jumps {x} cm high!')
davids_dog = Dog('Rex', 30)
davids_dog.bark()
davids_dog.jump()

sarahs_dog = Dog('Teacup', 20)
sarahs_dog.bark()
sarahs_dog.jump()

if davids_dog.height > sarahs_dog.height:
    print(davids_dog.name)
else:
    print(sarahs_dog.name)

#Exercise 3
class Song():
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for i in self.lyrics:
          print(i)
stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
stairway.sing_me_a_song()

#Exercise 4
class Zoo():
    def __init__(self, zoo_name):
        animals = []
        self.animals = animals
        self.name = zoo_name
    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
    
    def get_animals(self):
        for animal in self.animals:
            print(animal)

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    def sort_animals(self):
      temp =list(list1.pop())
      list2 = []
      while list1:
        if temp[0][0] == list1[0][0]:
            temp.append(list1.pop())
        else:
            list2.append(temp)
            temp = list(list1.pop())

list1 = ['jklsd', 'acildw', 'whqil','alndalid']        

park = Zoo('Botanic Park')
park.animals = ['Aigle', 'Emu', 'Cat', 'Bear', 'Cougar', 'Lion', 'Tiger']
park.get_animals()


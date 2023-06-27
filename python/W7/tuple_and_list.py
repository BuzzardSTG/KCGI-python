tuple_animal = () # standard brackets => tuple
list_car = []
print(type(tuple_animal))
print(type(list_car))


list_car.append("Ford")
list_car.append("Mustang")
list_car.append(1969)
list_car.append("Blue with white strpes") #mistake in english
list_car.append(True) # petrol
list_car.append("something to delete")
list_car[3] = "blue with striipes" # I am able to edit the idem
print(f"{list_car} size is {len(list_car)}")
list_car.pop(3) # pop with arguments means deleting on specific index (without arguments removing the last item)
list_car.remove("something to delete") # removing if we do not know index, but know the value (only first occurance will be deleted)
print(f"{list_car} size is {len(list_car)}")

for att in list_car:
    print(att, end=", ")
print()



#lets explore the animeal()
#print(tuple_animal.count()
if len(tuple_animal) == 0:
    print("There is nothing in the tuple_animal")
else:
    for att in tuple_animal:
        print(att)
#so we can not add, remove, edit, basically do anything with tuple, why do we have tuple(s)?
# tuples are immutable = unchangeble therefore once we set them up, we can not change them

my_second_tuple = ("one", "two", "three", "two", "three", "two")
print(type(my_second_tuple))
print(f"The value 'two' is: {my_second_tuple.count('two')} - times in our second tuple")
print(f"What is the item on index '2'?: {my_second_tuple[2]}")
print(f"What index does the first value 'three' has?: {my_second_tuple.index('three')}")

#tuple is "constant" list
#workaround
tuple_to_workaround = ("john", "smith", 39, True)
#tuple_to_workaround[3] = False
list_of_tuple = []
print(type(list_of_tuple))
list_of_tuple = list(tuple_to_workaround)
print(type(list_of_tuple))
list_of_tuple[3] = False
print(list_of_tuple)
print(type(list_of_tuple))
new_tuple = tuple(list_of_tuple)
print(type(new_tuple))
print(new_tuple)
print("---")
print(new_tuple[1])
print(new_tuple[-3])
print(new_tuple[-4])

c=0
for item in range(-1,-5,-1):
    print(f"#{c} {new_tuple[item]}")
    c+=1

#slicing
cars = tuple(("toyota", "skoda", "vw", "bmw", "suzuki", "honda", "audi", "peuget", "citroen"))
print(cars)
print(cars[2:4]) #start - stop - step
print(cars[3:])
print(cars[:5])
print(cars[2:-2:2])
print(cars[-2:-9:-2])

if "lamborgini" in cars:
    print("there is lambo")
else:
    print("boring")

our_car = cars[0]
my_father_car = cars[3]
print(f"{our_car},{my_father_car}")

#unpacking
"""
toyota = cars[0]
skoda= cars[1]
vw= cars[2]
bmw= cars[3]
suzuki= cars[4]
honda = cars[5]
audi = cars[6]
peuget = cars[7]
citroen = cars[8]
"""

#unpacking...
toyota, skoda, vw, bmw, suzuki, honda, audi, peuget, citroen = cars
print(bmw)

fruits = (f'"apple", "banana", "cherry" \n')
mytuple = fruits * 200
print(mytuple)
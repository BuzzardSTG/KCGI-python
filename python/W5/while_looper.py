import random

random_number = random.randint(0,50)
print(random_number)

stop = int(input("How many times should this run?:\n"))
i = 1
while i<= stop:
    i +=1
    #break-countinue-else
    if i == random_number:
        break
    if i == 4:
        continue
    print(i)

print("\n Second loop:")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    if fruit == "banana":
        continue
    print(fruit)

money = [1000, 5000, 2000, -1000, 3000, -500]
the_numbers_we_skipped = []

for i in money:
    if(i<0):
        the_numbers_we_skipped.append(i)
        continue
    print(i)

print(f"The numbers we skipped was: {the_numbers_we_skipped}")
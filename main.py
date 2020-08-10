import random

# including 100 and 200, in otherwords including limits
random_number = random.randint(100,200)
print(random_number)
rand = random.random() * 100
print(rand)

mylist = ["Star Plus", "DD1", "Aaj Tak", "JainamShroff"]
choice = random.choice(mylist)
print(choice)
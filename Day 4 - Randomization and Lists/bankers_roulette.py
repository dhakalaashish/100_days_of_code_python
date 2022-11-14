import random

names = input("Input the names of the people who will pay the bill separated by a comma:\n")
names_list = [name.strip() for name in names.split(',')]
num_people = len(names_list)

choice = random.randint(0,num_people-1)

print(f"{names_list[choice]} will pay the bill!")

#print(f"{random.choice(names_list)} will pay the bill!")

#1. Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list.
import random
def shuffle_list (lista):
    random.shuffle(lista)
    return lista
print(shuffle_list([1,2,3,4,5]))

#2. Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
def unique_seven_numbers ():
    return random.sample(range(10),7)
print(unique_seven_numbers())
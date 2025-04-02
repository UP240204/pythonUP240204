#1. Write a function called is_prime, which checks if a number is prime.
def is_prime (number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True
print("¿El numero 5 es primo?",is_prime(6))

#2. Write a functions which checks if all items are unique in the list.
def all_unique_items (lista):
    all_unique = len(lista) == len(set(lista))
    return all_unique
print("¿Todos los elementos son unicos en la lista?",all_unique_items([1,2,3,3,4,5]))

#3. Write a function which checks if all the items of the list are of the same data type.
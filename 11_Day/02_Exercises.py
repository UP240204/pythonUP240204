#1. Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
def even_and_odds (number):
    odds = 0
    even = 0
    for i in range (0,number +1):
        if i % 2 == 0:
            even = even +1
        else :
            odds = odds + 1
    return {"evens":even,"odds":odds}
print(even_and_odds(number = 100))

#2. Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number.
def factorial (number):
    factorial_ = 1
    for i in range (1,number + 1):
        factorial_ = factorial_ * i
    return factorial_
print("El factorial de 5 es:",factorial(5))

#3. Call your function is_empty, it takes a parameter and it checks if it is empty or not.
def is_empty (items):
    if len(items) == 0:
        return True
    else:
        return False
print("¿Esta vacio?",is_empty([1,2,3]))

#4. Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
from statistics import mean, median, mode, variance, stdev
lista = [1, 2, 3, 4, 5, 5, 6, 8, 8, 8]
def calculate_mean (lista):
    return mean(lista)
def calculate_median (lista):
    return median(lista)
def calculate_mode (lista):
    return mode(lista)
def calculate_range (lista):
    return max(lista) - min(lista)
def calculate_variance (lista):
    return variance(lista)
def calculate_std (lista):
    return stdev(lista)
print("Media:",calculate_mean(lista))
print("Median:",calculate_median(lista))
print("Mode:",calculate_mode(lista))
print("Rango:",calculate_range(lista))
print("Varianza:",calculate_variance(lista))
print("Desviacion estandar:",calculate_std(lista))
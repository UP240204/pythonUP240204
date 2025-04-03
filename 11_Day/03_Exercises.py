#1. Write a function called is_prime, which checks if a number is prime.
def is_prime (number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True
print("¿El numero 5 es primo?",is_prime(5))

#2. Write a functions which checks if all items are unique in the list.
def all_unique_items (lista):
    all_unique = len(lista) == len(set(lista))
    return all_unique
print("¿Todos los elementos son unicos en la lista?",all_unique_items([1,2,3,3,4,5]))

#3. Write a function which checks if all the items of the list are of the same data type.
def same_data_type (lista):
    same_type = all(isinstance(lista[0],type(item)) for item in lista)
    return same_type
print("¿Todos los elementos de la lista son del mismo tipo?",same_data_type([1,2,3,4,5]))

#4. Write a function which check if provided variable is a valid python variable.
def is_python_variable (variable):
    if variable.isidentifier():
        return True
    else:
        return False
print("¿La variable proporcionada es una variable de Python válida?",is_python_variable('formula_1'))

#5. Go to the data folder and access the countries-data.py file.
#-Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order.
#-Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order.
import countries_data as p
datos = p.countries
country_language = []
def most_spoken_languages ():
    for pais in datos:
        for lenguaje in pais['languages']:
            country_language.append(lenguaje)
    country_language_set = set(country_language)
    country_language_dict = {}
    for lenguaje in country_language_set:
        country_language_dict[lenguaje] = 0
    for idioma in country_language_dict:
        for pais in datos:
            if idioma in pais['languages']:
                country_language_dict[idioma] = pais['population'] + country_language_dict[idioma]
    sort_keys_languages_population = sorted(country_language_dict,key=country_language_dict.get,reverse=True)
    return sort_keys_languages_population[:20]
print("Los lenguajes mas hablados son:",most_spoken_languages())

def most_populated_countries ():
    country_population_dict = {}
    for pais in datos:
        country_population_dict[pais['name']] = pais['population']
    sort_keys_population = sorted(country_population_dict,key=country_population_dict.get,reverse=True)
    return sort_keys_population[:20]
print("Los paises mas poblados son:",most_populated_countries())
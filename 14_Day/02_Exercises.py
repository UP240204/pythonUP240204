#1. Use map to create a new list by changing each country to uppercase in the countries list.
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
def change_to_uppercase (country):
    return country.upper()
print(list(map(lambda country: country.upper(), countries)))

#2. Use map to create a new list by changing each number to its square in the numbers list.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def square (x):
    return x**2
print(list(map(lambda x: x**2, numbers)))

#3. Use map to change each name to uppercase in the names list.
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
def change_names_to_uppercase (name):
    return  name.upper()
print(list(map(lambda name: name.upper(), names)))

#4. Use filter to filter out countries containing 'land'.
def land_in_countries (country):
    if 'land' in country:
        return True
    return False
print(list(filter(land_in_countries,countries)))

#5. Use filter to filter out countries having exactly six characters.
def characters (country):
    if len(country) == 6:
        return True
    return False
print(list(filter(characters,countries)))

#6. Use filter to filter out countries containing six letters and more in the country list.
def characters_more (country):
    if len(country) >= 6:
        return True
    return False
print(list(filter(characters_more,countries)))

#7. Use filter to filter out countries starting with an 'E'.
def countries_start_e (country):
    if country[0] is 'E':
        return True
    return False
print(list(filter(countries_start_e,countries)))

#8. Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback)).
from functools import reduce
print(reduce(lambda x,y:x + y, map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers))))

#9. Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
lista = [1,'hello',2,'mundo',3,'python']
def get_string_lists (list):
    return [item for item in lista if isinstance(item, str)]
print(get_string_lists(lista))

#10. Use reduce to sum all the numbers in the numbers list.
print("La suma de los numeros:",reduce(lambda x,y: x+y,numbers))

#11. Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries.
def concatenate_countries (a, country):
    return f"{a}, {country}"
sentence = reduce(concatenate_countries,countries[:-1])
final = f"{sentence} y {countries[-1]} son paises del norte de Europa"
print(final)

#12. Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).
from list_of_countries import countries
def categorize_countries (countries,pattern):
    return list(filter(lambda country: pattern in country, countries))
print(categorize_countries(countries,'stan'))

#13. Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.
def starting_letters_countries (countries):
    cont = {}
    for country in countries:
        start = country[0].upper()
        cont[start] = cont.get(start, 0) + 1
    return cont
print(starting_letters_countries(countries))

#14. Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.
def get_first_ten_countries (countries):
    return list(map(lambda x:x, countries[:10]))
print("Los primeros 10 paises de la lista son:",get_first_ten_countries(countries))

#15. Declare a get_last_ten_countries function that returns the last ten countries in the countries list.
def get_last_ten_countries (countries):
    return list(map(lambda x:x, countries[-10:]))
print("Los ultimos 10 paises de la lista son:",get_last_ten_countries(countries))
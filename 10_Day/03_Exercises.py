#1. Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.
import countries as p
paises = p.countries
for pais in paises:
    if 'land' in pais:
        print(pais)

#2. This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
fruits = ['banana', 'orange', 'mango', 'lemon']
for fruit in reversed(fruits):
    print(fruit)

#3. Go to the data folder and use the countries_data.py file.
#-What are the total number of languages in the data.
#-Find the ten most spoken languages from the data.
#-Find the 10 most populated countries in the world.

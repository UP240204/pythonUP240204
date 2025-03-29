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
import countries_data as a
datos = a.caca
country_language = []
for pais in datos:
    for lenguaje in pais['languages']:
        country_language.append(lenguaje)
country_language_set = set(country_language)
print("Hay un total de",len(country_language_set),"lenguajes:",country_language_set)

dictlanguages = {}
for language in country_language_set:
    dictlanguages[language] = 0
print(dictlanguages)
for idioma in dictlanguages:
    for pais in datos:
        if idioma in pais['languages']:
            dictlanguages[idioma] = pais['population'] + dictlanguages[idioma]
sort_keys_languages_population = sorted(dictlanguages.values(),reverse=True)
sort_values_languages_population = sorted(dictlanguages,key=dictlanguages.get,reverse=True)
print(sort_keys_languages_population[1],sort_values_languages_population[1])

for c in range(10):
    print(sort_keys_languages_population[c],sort_values_languages_population[c])
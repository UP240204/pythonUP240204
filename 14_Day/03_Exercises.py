#1. Use the countries_data.py (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) file and follow the tasks below:
#-Sort countries by name, by capital, by population.
#-Sort out the ten most spoken languages by location.
#-Sort out the ten most populated countries.
from countries_data import data
sort_name =  sorted(data, key=lambda x: x["name"])
sort_capital= sorted(data, key=lambda x: x["capital"])
sort_population= sorted(data, key=lambda x:x["population"], reverse=True)
print ("sorted by name: ", sort_name)
print ("sorted by capital: ", sort_capital)
print ("sorted by population: ", sort_population)


from collections import Counter
def most_spoke_languges (datos, cantidad):
    languages = []
    for country in datos:
        languages.extend(country["languages"])
        return Counter (languages).most_common(cantidad)
print(most_spoke_languges(data, 10))


def most_populated_countries(datos, cantidad):
    return sorted(datos,key=lambda x:x['population'], reverse=True)[:cantidad]
print ([i['name']for i in most_populated_countries(data, 10)])

print("Revisado")
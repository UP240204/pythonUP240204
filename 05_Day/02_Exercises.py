#1. The following is a list of 10 students ages:
#-Sort the list and find the min and max age
#-Add the min age and the max age again to the list
#-Find the median age (one middle item or two middle items divided by two)
#-Find the average age (sum of all items divided by their number )
#-Find the range of the ages (max minus min)
#-Compare the value of (min - average) and (max - average), use abs() method
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
ages.insert(0, 19)
ages.insert(11, 26)
edad_media = int((ages[5] + ages[6])/2)
edad_promedio = sum(ages)/len(ages)
rango = ages[11] - ages[0]
comparacion = abs((ages[0]-edad_promedio) and (ages[11]-edad_promedio)) 
print("La edad media son",edad_media,"años.")
print("La edad promedio son",edad_promedio,"años.")
print("El rango de edades es de",rango,"años.")
print("La comparación es:",comparacion)

#1. Find the middle country(ies) in the countries list.
import COUNTRIES as p
paises = p.countries
pais_middle = (len(paises))//2 #96
print("Los paises de en medio de la lista son",paises[95],"y",paises[96])

#2. Divide the countries list into two equal lists if it is even if not one more country for the first half.
first_list = paises[:96]
second_list = paises[96:]
print("Lista 1:",first_list)
print("Lista 2:",second_list)

#3. ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
p.countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
p1, p2, p3, * escandinavos = p.countries
print("Los paises escandinavos son", escandinavos)
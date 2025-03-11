#LEVEL 1
#1. Declare an empty list.
empty_list = []

#2. Declare a list with more than 5 items.
liston = ['Pan','Taza','Balon','Cable','Caca']

#3. Find the length of your list.
print("La longitud de la lista es de",len(liston),"palabras")

#4. Get the first item, the middle item and the last item of the list.
first_word = liston[0]
middle_word = liston[2]
last_word = liston[4]
print("La primera palabra de la lista es",first_word)
print("La palabra de en medio de la lista es",middle_word)
print("La ultima palabra de la lista es",last_word)

#5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address).
mixed_data_types = ['Octavio','18','1.85','soltero','Cacaloapan #129']

#6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']

#7. Print the list using print().
print(mixed_data_types)
print(it_companies)

#8. Print the number of companies in the list.
print("La lista de empresas contiene",len(it_companies),"empresas")

#9. Print the first, middle and last company.
print("La primera empresa es",it_companies[0])
print("La empresa de en medio es",it_companies[3])
print("La ultima empresa es",it_companies[6])

#10. Print the list after modifying one of the companies.
it_companies[3] = 'Bimbo'
print(it_companies)

#11. Add an IT company to it_companies.
it_companies.append('IT')
print(it_companies)

#12. Insert an IT company in the middle of the companies list.
it_companies.insert(4, 'IT')
print(it_companies)

#13. Change one of the it_companies names to uppercase (IBM excluded!).
it_companies [2] = it_companies[2].upper()
print(it_companies)

#14. Join the it_companies with a string '#;  '.
print('#; '.join(it_companies))

#15. Check if a certain company exists in the it_companies list.
print("¿'Amazon' esta en la lista?", 'Amazon' in it_companies)

#16. Sort the list using sort() method.
it_companies.sort()
print(it_companies)

#17. Reverse the list in descending order using reverse() method.
it_companies.reverse()
print(it_companies)

#18. Slice out the first 3 companies from the list.
print(it_companies[3:])

#19. Slice out the last 3 companies from the list.
print(it_companies[:6])

#20. Slice out the middle IT company or companies from the list.
companies = ['IT','Facebook', 'Google', 'MICROSOFT', 'Bimbo', 'IT', 'IBM', 'Oracle', 'Amazon', 'IT']
print(companies[1:5] + companies[6:9])

#21. Remove the first IT company from the list.
companies.remove('IT')
print(companies)

#22. Remove the middle IT company or companies from the list.
del companies[4]
print(companies)

#23. Remove the last IT company from the list.
companies.pop()
print(companies)

#24. Remove all IT companies from the list.
companys = ['IT','Facebook', 'Google', 'MICROSOFT', 'Bimbo', 'IT', 'IBM', 'Oracle', 'Amazon', 'IT']
del companys[0]
del companys[4]
del companys[7]
print(companys)

#25. Destroy the IT companies list.
companys.clear()
print(companys)

#26. Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end + back_end
print(full_stack)

#27. After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
full_stack.insert(5, 'Python')
full_stack.insert(6, 'SQL')
print(full_stack)

#LEVEL 2 
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

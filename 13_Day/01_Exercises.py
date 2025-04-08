#1. Filter only negative and zero in the list using list comprehension.
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
zero_negative = [i for i in numbers if i <= 0]
print(zero_negative)

#2. Flatten the following list of lists of lists to a one dimensional list.
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flatten_list = [number for i in list_of_lists for a in i for number in a]
print(flatten_list)

#3. Using list comprehension create the following list of tuples.
tuples_list = [(i,1,i,i**2,i**3,i**4,i**5) for i in range(11)]
print(tuples_list)

#4. Flatten the following list to a new list.
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
list = [[country.upper(),country[:3].upper(),city.upper()] for sublist in countries for country, city in sublist]
print(list)

#5. Change the following list to a list of dictionaries.
countries_dict = [{'country':country.upper(),'city':city.upper()} for [(country,city)] in countries]
print(countries_dict)

#6. Change the following list of lists to a list of concatenated strings.
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
list_name_complete = [[name + ' ' + last_name] for [(name,last_name)] in names]
print(list_name_complete)

#7. Write a lambda function which can solve a slope or y-intercept of linear functions.
slope = lambda x1,y1,x2,y2: (y2 - y1)/(x2 - x1)
print("La pendiente es de:",slope(1,2,3,6))
y_intercept = lambda x,y,m: y - m * x
print("La intercepcion en Y es en:",y_intercept(1,2,2))

print("Revisado")
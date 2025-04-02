#1. Create an empty dictionary called dog.
dog = {}

#2. Add name, color, breed, legs, age to the dog dictionary.
dog['Nombre'] = 'Dante'
dog['Color'] = 'Café'
dog['Raza'] = 'Pastor Aleman'
dog['Patas'] = '4'
dog['Edad en años'] = '5'
print(dog)

#3. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary.
student = {
    'first_name':'Octavio',
    'last_name':'Hernández',
    'gender':'Masculino',
    'age':'18',
    'is_marred':False,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'country':'México',
    'city':'Aguascalientes',
    'address':{
        'street':'Robinia',
        'zipcode':'20326'
        }
}

#4. Get the length of the student dictionary.
print("La longitud del diccionario es de:",len(student))

#5. Get the value of skills and check the data type, it should be a list.
print("El valor de skills es",student['skills'])
print("El tipo de dato de skills es",type(student['skills']))

#6. Modify the skills values by adding one or two skills.
student['skills'].append('soccer')
student['skills'].append('soy una 🔫 para todo')
print(student)

#7. Get the dictionary keys as a list.
print("Las llaves del diccionario son",student.keys())

#8. Get the dictionary values as a list.
print("Los valores del diccionario son",student.values())

#9. Change the dictionary to a list of tuples using items() method.
print(student.items())

#10. Delete one of the items in the dictionary.
student.popitem()
print(student)

#11. Delete one of the dictionaries.
del student['skills']
print(student)

print("Revisado")
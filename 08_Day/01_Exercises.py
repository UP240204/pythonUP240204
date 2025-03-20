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
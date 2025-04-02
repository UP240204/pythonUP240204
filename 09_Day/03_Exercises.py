#1. Here we have a person dictionary. Feel free to modify it!
#* Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
#* Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
#* If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
#* If the person is married and if he lives in Finland, print the information in the following format: Asabeneh Yetayeh lives in Finland. He is married.
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
if 'skills' in person:
    print("La skill de en medio es",person['skills'][len(person['skills'])//2])
else:
    print("No estan las skills en el diccionario")


if 'Python' in person['skills']:
    print("Python esta en las skills, mira",person['skills'])
else:
    print("No esta Python rey")


if 'JavaScript' in person['skills'] and 'React' in person['skills']:
    print("Es desarrollador front-end")
elif 'Node' in person['skills'] and 'Python' in person['skills'] and 'MongoDB' in person['skills']:
    print("Es desarrollador back-end")
elif 'React' in person['skills'] and 'Node' in person['skills'] and 'MongoDB' in person['skills']:
    print("Es desarrolador full-stack")
else:
    print("Titulo desconocido")


if 'Finland' in person['country'] and person['is_marred'] is True:
    print("Asabeneh Yetayeh reside en Finlandia. Está casado.")


print("Revisado")
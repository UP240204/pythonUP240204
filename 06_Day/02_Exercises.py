brothers = ('Omar', 'Oscar', 'Osvaldo', 'Diego', 'Andre')
sisters = ('Olivia', 'Paula', 'Dariana', 'Camila', 'Isabella')
brothers_all = brothers + sisters
parents = ('Carlos', 'Nelia')
family_members = parents + brothers_all

#1. Unpack siblings and parents from family_members.
print("Mis padres son:",family_members[:2])
print("Mis hermanos son:",family_members[2:])

#2. Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('Mango', 'Manzana', 'Fresa')
vegetables = ('Brocoli', 'Pimiento', 'Zanahoria')
animal_products = ('Queso', 'Leche', 'Huevo')
food_stuff_tp = fruits + vegetables + animal_products
print("Comida:",food_stuff_tp)

#3. Change the about food_stuff_tp tuple to a food_stuff_lt list.
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

#4. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
print(food_stuff_lt[:4] + food_stuff_lt[5:])

#5. Slice out the first three items and the last three items from food_staff_lt list.
print(food_stuff_lt[3:6])

#6. Delete the food_staff_tp tuple completely.
del food_stuff_lt

#7. Check if an item exists in tuple:
#-Check if 'Estonia' is a nordic country
#-Check if 'Iceland' is a nordic country
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print("¿Estonia es un pais nordico?",'Estonia' in nordic_countries)
print("¿Islandia es un pais nordico?",'Iceland' in nordic_countries)

print("Revisado")
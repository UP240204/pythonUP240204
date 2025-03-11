#LEVEL 1
#1. Create an empty tuple.
empty_tuple = ()

#2. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine).
brothers = ('Omar', 'Oscar', 'Osvaldo', 'Diego', 'Andre')
sisters = ('Olivia', 'Paula', 'Dariana', 'Camila', 'Isabella')
print("Mis hermanos son:",brothers)
print("Mis hermanas son:",sisters)

#3. Join brothers and sisters tuples and assign it to siblings.
brothers_all = brothers + sisters
print("Todos mis hermanos son:",brothers_all)

#4. How many siblings do you have?
print("Tengo",len(brothers_all),"hermanos.")

#5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members.
parents = ('Carlos', 'Nelia')
family_members = parents + brothers_all
print("Los miembros de la familia son:",family_members)

#LEVEL 2
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

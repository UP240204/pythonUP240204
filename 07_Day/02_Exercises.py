A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

#1. Join A and B.
C = A.union(B)
print(C)

#2. Find A intersection B.
print("La intersección entre 'A' y 'B' es:",A.intersection(B))

#3. Is A subset of B.
print("¿'A' es un subconjunto de 'B'?",B.issubset(A))

#4. Are A and B disjoint sets.
print("¿Son A y B conjuntos disjuntos?",B.isdisjoint(A))

#5. Join A with B and B with A.
print("'A' con 'B':",A.union(B))
print("'B' con 'A':",B.union(A))

#6. What is the symmetric difference between A and B.
print("¿Cuál es la diferencia simétrica entre A y B?",A.symmetric_difference(B))

#7. Delete the sets completely.
del A
del B
# This file is the first prototype of the project, it was made in Python and then converted to JavaScript and incorporated into a website made with HTML and CSS

import math, json

with open("cores_tailwind.json") as file:
  cores_tailwind = json.load(file)

r = int(input("Enter the first number: "))
g = int(input("Enter the second number: "))
b = int(input("Enter the third number: "))

range = 10
coordenadas = [r, g, b]
lista = []

def acharProximos(range):
  minimo = [r-range, g-range, b-range]
  maximo = [r+range, g+range, b+range]
  for key, value in cores_tailwind.items():
    if all(valor>=minimo[i] and valor<=maximo[i] for i, valor in enumerate(value)) and key not in lista:
      lista.append(key)

while len(lista) < 3:
  acharProximos(range)
  range += 10

distancias = []
for cor in lista:
  distancia_atual = []
  for i, coordenada in enumerate(cores_tailwind[cor]):
    distancia_atual.append((coordenadas[i]-coordenada)**2)
  distancias.append(math.sqrt(sum(distancia_atual)))

lista_ordenada = []
while distancias:
    index_min_distancia = distancias.index(min(distancias))
    lista_ordenada.append(lista[index_min_distancia])

    lista.pop(index_min_distancia)
    distancias.pop(index_min_distancia)

print(f"\n{"-"*23}\nClosest Tailwind Colors\n{"-"*23}")
for cor in lista_ordenada:
  cor_formatada = str(cores_tailwind[cor]).replace("[","").replace("]","")
  print(f"Name: {cor} | ", end="")
  print(f"RGB: {cor_formatada}")
print(f"\n")

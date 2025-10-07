
#EJERCIO 1
temp = [15,15,17,30,25,30,30,30,31,32,30,36,38]
media = sum(temp) / len(temp)

for i in temp:
  if i  > media:
    print(i, "esta arriba")

#EJERCIO 2
alumnos = ["reymundo,iker,giovani,santiago"]
calificaciones = ["50,60,40,28"]
promedio = sum(calificaciones) / lent(calificaciones)

for i in calif:
  if i > 70:
    print(i "esta arriba de 70")

#EJERCIO 3
compras = ["leche,pan,huevos,manzana"]
ya_comprado = [False , False , False, False]

for i in range(len(compras)):
  if not ya_comprado[i]:
  respuesta = input (f" ¿Ya compraste {compras[i]}? (s/n): ").lower()
    if respuesta == "s":
      ya_comprado[i] = True

print("Estados de la lista de compras:")
for i in range(len(compras)):
  estado = "* comprado" if ya_comprado[i] else "+ pendiente"
print(f"{compras[i]} - {estado}")

#Ejercio 4
numeros = [45, 12, 89, 33, 7, 56, 72, 18, 90]

maximo = numeros[0]
minimo = numeros[0]

for n in numeros:
  if n > maximo:
    maximo = n
  if n < minimo:
    minimo = n

ordenados = sorted(numeros)

print("Lista original:", numeros)
print("Número máximo:", maximo)
print("Número mínimo:", minimo)
print("Lista ordenada:", ordenados)




#EJERCIO 5
numeros = [12, 5, 7, 8, 14, 21, 33, 40, 42, 55]
pares = []
impares = []

for n in numeros:
  if n % 2 == 0:
    pares.append(n)
  else:
    impares.append(n)

print("Pares:", pares)
print("Impares:", impares)


#EJERCIO 5

usuarios = ["ana", "luis", "carlos", "maria", "sofia", "ana"]

# Elimina nombres repetidos
usuarios = list(set(usuarios))
print("Lista actual de usuarios:", usuarios)

while True:
  nuevo = input("Ingresa un nombre de usuario: ")

  if nuevo in usuarios:
    print("Ese nombre ya existe, intenta con otro.")
  else:
    usuarios.append(nuevo)
    print("Usuario agregado correctamente.")
    break

print("Lista final de usuarios:", usuarios)
     

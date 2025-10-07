
#EJERCIO 1
temp = [15,15,17,30,25,30,30,30,31,32,30,36,38]
media = sum(temp) / len(temp)

for i in temp:
  if i  > media:
    print(i, "esta arriba")

#EJERCIO 2
alumnos = ["reymundo", "iker", "giovani", "santiago"]
calificaciones = [50, 90, 20, 28]

promedio = sum(calificaciones) / len(calificaciones)
print("El promedio del grupo es:", promedio)

aprobados = 0
reprobados = []

for i in range(len(calificaciones)):
  if calificaciones[i] >= 70:
    aprobados = aprobados + 1
  else:
    reprobados.append(alumnos[i])

porcentaje = (aprobados / len(alumnos)) * 100
print("El porcentaje de alumnos aprobados es:", porcentaje, "%")

print("Los alumnos reprobados son:")
for nombre in reprobados:
  print(nombre)

#EJERCIO 3

compras = ["pan", "leche", "huevos", "arroz", "manzanas"]
ya_comprado = [False, True, False, False, True]

print("Artículos que aún no has comprado:")

for i in range(len(compras)):
  if ya_comprado[i] == False:
    print(compras[i])

for i in range(len(compras)):
  if ya_comprado[i] == False:
    respuesta = input("¿Ya compraste " + compras[i] + "? (si/no): ")
    if respuesta == "si":
      ya_comprado[i] = True

print("Estado final de compras:")
for i in range(len(compras)):
  if ya_comprado[i] == True:
    print(compras[i], "ya está comprado")
  else:
    print(compras[i], "aún pendiente")

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

agregar = "si"

while agregar == "si":
  nuevo = input("Ingresa un nombre de usuario: ")

  if nuevo in usuarios:
    print("Ese nombre ya existe, intenta con otro.")
  else:
    usuarios.append(nuevo)
    print("Usuario agregado correctamente.")

  agregar = input("¿Quieres agregar otro usuario? (si/no): ")

print("Lista final de usuarios:", usuarios)
     

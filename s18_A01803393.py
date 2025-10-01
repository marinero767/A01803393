temp = [15,15,17,30,25,30,30,30,31,32,30,36,38]
media = sum(temp) / len(temp)

for i in temp:
  if i  > media:
    print(i, "esta arriba")


alumnos = ["reymundo,iker,giovani,santiago"]
calificaciones = ["50,60,40,28"]
promedio = sum(calificaciones) / lent(calificaciones)

for i in calif:
  if i > 70:
    print(i "esta arriba de 70")


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
     

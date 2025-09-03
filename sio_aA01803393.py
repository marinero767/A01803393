
#Ejercicio 1
donas = int(input("¿Cuantas donas tienes?))
docenas = donas // 12
print("Con", donas,"donas puedes hacer" docenas, "docenas!")

# Ejercicio 2
num1 = int(input("Escribe el primer numero: "))
num2 = int(input("Escribe el primer numero: "))
residuo = donas // 12
print(num1, "dividido entre", num2, "tiene un residuo de", residuo, "!")

# Ejercicio 3
segundos = int(input("Escribe la cantidad de segundos: "))
horas = segundos // 3600
minutos = (segundos % 3600) // 60
seg_restantes = segundos % 60
print(segundos, "segundos son", horas, "horas,", minutos, "minutos y", seg_restantes, "segundos")

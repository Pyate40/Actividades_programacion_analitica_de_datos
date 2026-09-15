# %%
# 1.Completa una decision simple
edad=20

if edad >=18:
    print("Mayor de edad")


# %%
#2.Agrega la ruta alternativa

temperatura = 32

if temperatura > 30:
    print("Alta")
else:
    print ("Normal") 


# %%
#3.Predice la salida

numero = 7

if numero % 2 == 0:
    print("par")
else:
    print("Impar")

#7 ya que es un numero impar y no cumple la condicion que al dividirlo en 2 su residuo sea cero


# %%
#4. Completa la clasificación
nota = 4.2
if nota >= 4.5:
 print("Excelente")
elif nota >=4:
 print("Muy buen desempeño")
elif nota >=3:
 print("Aprobado")
else:
 print("No aprobado")


# %%
#5. Corrige el orden

nota = 4.8

if nota >= 4.5:
 print("Excelente")
elif nota >= 3.0:
 print("Aprobado")

#Como python evalua de arriba hacia abajo solo evaluaba la primera condicion y como ya se cumplia no
#evaluaba más condiciones del código.


# %%
#6. Traza la ejecución

valor = 12

if valor < 5:
    print("A")
elif valor <10:
    print ("B")
elif valor <15:
    print ("C")
else:
 print("D")
 # La respuesta es C, depues de evaluar las 3 primerasd condiciones, la tercera es la cumpla


# %%
#7 Acceso con dos requisitos

usuario_activo = True
tiene_permiso = True
if usuario_activo and tiene_permiso:
 print("Acceso permitido")
else:
 print("Acceso denegado")


# %%
#8 Dos rutas válidas

correo_valido = False
telefono_valido = True
if correo_valido  or telefono_valido:
 print("Continuar registro")
else:
 print("Faltan datos de contacto")


# %%
#9 Usa negacion
cuenta_bloqueada = False
if not cuenta_bloqueada:
 print("Puede operar")


# %%
#10 Recorre del 1 al 5

for numero in range(1,6):
 print (numero)


# %%
#11 Recorre con paso

for numero in range(2,11,2):
 print (numero)


# %%
#12 Predice el acumulado

suma = 0
for i in range(1, 4):
 suma = suma + i
print(suma)

# Va a sumar los numeros 1, 2 y 3, cada vez que se ejecuta guarta el nuevo valor sumandolo al que 
# ya esta guardado


# %%
#13 Completa el contador

numero = 1
while numero <= 5:
 print(numero)
 numero = numero +1


# %%
#14 Encuentra el ciclo infinito

numero = 1

while numero <= 5:
  print(numero)
  numero = numero +1

#El ciclo era infinito porque la variable numero iniciaba en 1 y no se actualizaba dentro del while, la condición numero <= 5 siempre era verdadera y hacia infinito el ciclo

# %%
#15 Control de intentos

intentos = 0
while intentos <= 2:
 clave = input("Ingrese la clave: ")
 intentos = intentos + 1
print("Proceso finalizado")

#%%
# 16 ¿for o while?

#Situación for / while 
#Procesar exactamente 10 mediciones. -> for
#Pedir una clave hasta que sea correcta. -> while
#Imprimir los números del 1 al 20. -> for
#Repetir un cálculo hasta que el error sea menor que 0.01. -> while

#Se usa for cuando se conoce la cantidad de repeticiones y while cuando la repetición depende de que se cumpla una condición.

#%%
# 17 Combina for + if

for numero in range(1,13):
  if numero % 3 == 0:
    print(numero)
# %%
# 18 Predice antes de ejecutar

for numero in range(1, 8):
    if numero < 3:
      print(numero, "A")
    elif numero < 6:
      print(numero, "B")
    else:
      print(numero, "C")

#Los números menores que 3 se clasifican con la letra “A”, los que van de 3 hasta 5 con la letra “B” y los que estan entre 6 y 7 con la letra “C”.

# %%
# 19 Traduce una decisión

#PSEUDOCÓDIGO

nota = float(input("Nota: "))

if nota >= 3.0:
  print("Aprobado")
else:
  print("No aprobado")

#%%
# 20 Traduce una repetición

for i in range(1, 6):
  print(i)

#%%
# Reto integrador
# Clasificación de temperaturas

# El programa debe solicitar 5 temperaturas.
# Para cada una debe mostrar:
# "Baja" si t < 18
# "Normal" si 18 <= t <= 25
# "Alta" si t > 25
for i in range(5):
  t = float(input("Temperatura: "))
if t < 18:
  print("Baja")
elif t <= 25:
  print("Normal")
else:
  print("Alta")

# %%

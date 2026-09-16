# %%
# 1 Definir una función

def saludar():
    print("Hola")
saludar()

# %%
# 2 Llamar a la función

def bienvenida():
    print("Bienvenido al curso")
bienvenida()
# %%
# 3 Predice el orden de ejecución
def uno():
    print("A")
print("B")
uno()
print("C")
#Primero se imprime B, despues se llama la función uno(), que imprime A y luego se imprime C
# %%
# 4 Corrige el orden
def saludar(nombre):
    print("Hola,", nombre)
saludar("Ana")
# %%
# 5 Función con un parámetro

def saludar(nombre):
    print("Hola,", nombre)
saludar("Ana")

# %%
# 6 Función con dos parámetros
def area(base, altura):
    return base * altura
print(area(3, 4))
# %%
# 7 Completa la llamada

def area(base, altura):
    return base * altura
print(area(5,5)) # 25.0
# %%
# 8 Reutilizar la misma función

def con_iva(precio):
    return precio * 1.19
print(con_iva(500))
print(con_iva(1000))
print(con_iva(2000))
# %%
# 9 Parámetro o argumento
def doble(n):
    return n * 2
resultado = doble(5)
# n es el parametro porque aparece en la definicion de la funcion.
# 5 es el argumento porque es el valor enviado al llamar la funcion.
# %%
#10 Argumentos por posición
def perfil(nombre, edad, ciudad):
    print(nombre, edad, ciudad)
perfil("Ana", "20", "Bogota")
# %%
#11 Argumentos por nombre
def perfil(nombre, edad, ciudad):
    print(nombre, edad, ciudad)
perfil(edad=20, nombre="Ana", ciudad="Bogota")

# %%
# 12 Valor por defecto
def saludar(nombre, saludo="Hola"):
    print(saludo, nombre)
saludar("Ana")
# %%
# 13 Reemplazar el valor por defecto

def saludar(nombre, saludo="Hola"):
    print(saludo, nombre)
saludar("Luis","Buen dia")

# %%
# 14 Orden de los parámetros

def registrar(producto, cantidad=1):
    print(producto, cantidad)

# %%
# 15 Una lista como argumento
def total(precios):
    suma = 0
    for p in precios:
        suma = suma + p
    return suma
print(total([1200, 950, 3400]))
# %%
# 16 Devolver un valor
def doble(n):
    return n * 2
print(doble(5))
# %%
# 17 Usar el valor devuelto
def doble(n):
    return n * 2
resultado = doble(6)
print(resultado + 1)
# %%
# 18 Función sin return
def saludo(nombre):
    print("Hola,", nombre)
x = saludo("Ana")
print(x)
# La función imprime el saludo, pero como no tiene return no devuelve un resultado.
# %%
# 19 print o return
def doble(n):
    return(n * 2)
total = doble(5) + 3
print(total)
# %%
# 20 return dentro de una condición
def signo(n):
    if n < 0:
        return "negativo"
    return"positivo"
print(signo(-4))
print(signo(7))
# %%
# 21 return termina la función
def prueba(n):
    if n > 0:
        return "positivo"
    print("linea intermedia")
    return "otro"
print(prueba(5))

#La linea intermedia no aparece porque 5 es mayor que 0 y cuando se ejecuta el return es "positivo" y termina la funcion.
# %%
# 22 Devolver dos valores
def resumen(valores):
    return min(valores), max(valores)
menor, mayor = resumen([8, 3, 10, 5])
print(menor, mayor)
# %%
# 23 Encadenar funciones
def con_iva(p):
    return p * 1.19
def redondear(valor):
    return round(valor, 2)
print(redondear(con_iva(1200)))
# %%
# 24 Variable local y global
mensaje = "global"
def prueba():
    mensaje = "local"
    print(mensaje)
prueba()
print(mensaje)
# La variable creada dentro de la función es "local".
# La variable que está fuera de la función conserva el valor "global".
# %%
# 25 Evitar las variables globales

iva = 0.19
precio = 100
def con_iva(precio,iva):
    return precio * (1 + iva)
print(con_iva(precio, iva))

# %%
# 26 No modificar el original
def agregar(lista):
    nueva = lista + [3]
    return nueva
datos = [1, 2]
print(agregar(datos))
print(datos)
# %%
# 27 Función que recibe una lista
def promedio(notas):
    total = 0
    for n in notas:
        total = total + n
    return total / len(notas)
print(promedio([3.5, 4.2, 2.8]))
# %%
# 28 Función que recibe un diccionario
def describir(alumno):
    print(alumno["nombre"], alumno["nota"])
describir({"nombre": "Laura", "nota": 4.6})
# %%
# 29 Función que devuelve una lista
def aprobados(estudiantes):
    resultado = []
    for e in estudiantes:
        if e["nota"] >= 3.0:
            resultado.append(e["nombre"])
    return resultado
datos = [{"nombre": "Ana", "nota": 4.2},
{"nombre": "Luis", "nota": 2.8}]
print(aprobados(datos))

# %%
# 30 Reporte de notas con funciones
def promedio(notas):
    total = 0
    for n in notas:
        total = total + n
    return total / len(notas)
    
def aprueba(prom, minimo=3):
    return prom >= minimo

def reporte(nombre, notas):
    prom = promedio(notas)
    print(nombre, round(prom, 2))
    
    if aprueba(prom):
        print("Aprobado")
    else:
        print("No aprobado")

reporte("Laura", [3.5, 4.2, 2.8])
#La funcion promedio recibe las notas y devuelve el promedio, la funcion aprueba recibe el promedio y la nota mínima, la funcion reporte recibe el nombre y las notas del estudiante,saca el promedio y estado de aprobación.
# %%

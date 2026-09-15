# %%
# 1 Crear una lista de notas}
notas = [3.0, 4.3, 2.1, 4.6, 3.2]
print(len(notas))
print(notas)

# %%
# 2 Acceder por índice
temperaturas = [18, 20, 19, 21, 22]
print(temperaturas[0])
print(temperaturas[2])
print(temperaturas[4])
# %%
# 3 Actualizar un elemento

ventas = [120, 80, 200, 50]
ventas[1] = 85
print(ventas)

# %%
# 4 Agregar y extraer datos

notas = [3.5, 4.0, 2.8]
notas.append(4.6)
ultima = notas.pop()
print(ultima)
print(notas)

# %%
#5 Calcular promedio 

notas = [4.2, 3.8, 5.0, 2.9]
total = 0

for nota in notas:
    total = total + nota

promedio = total / len(notas)
print(round(promedio, 2))

# %%
# 6 Contar aprobados 

notas = [4.2, 2.5, 3.0, 1.8, 4.7]
aprobados = 0
for nota in notas:
    if nota >= 3.0:
        aprobados = aprobados + 1
        
print(aprobados)


# %%
# 7 Filtrar valores válidos 

lecturas = [18, 200, 21, -99, 19, 22]
validas = []
for t in lecturas:
 if t >= -10 and t <= 50:
     validas.append(t)

print(validas)

# %%
#8 Ordenar sin perder el original

montos = [120000, 85000, 210000, 50000]
ordenados = sorted(montos)
print(montos)
print(ordenados)

# %%
#9 Comprensión de listas 
numeros = [1, 2, 3, 4, 5, 6]
cuadrados_pares = [n**2 for n in numeros if n % 2 == 0]
print(cuadrados_pares)


# %%
#10 Lista anidada

matriz = [[1, 2, 3], [4, 5, 6]]
total = 0
for fila in matriz:
    for valor in fila:
        total += valor
print(total)

#Una matriz se puede representar como una lista de listas porque cada lista interna corresponde a una fila que contiene varios elementos.
# %%
#11 Crear una tupla fija 
ubicacion = (20, 35)
print(ubicacion)
print(type(ubicacion))

# %%
# 12 Desempaquetar una tupla
registro = ("A01", "Laura", 4.6)
codigo, nombre, nota = registro
print(nombre)
print(nota)

# %%
#13 Tupla de un solo elemento
codigo = ("A01",)
print(codigo)
print(type(codigo))


# %%
#14 Convertir lista a tupla

columnas = ["fecha", "monto", "cliente"]
columnas_fijas = tuple(columnas)
                  
print(columnas_fijas)

# %%
#15 Retorno múltiple

def resumen(valores):
 menor = min(valores)
 mayor = max(valores)
 return menor, mayor
minimo, maximo = resumen([8, 3, 10, 5])
print(minimo, maximo)

#%%
#16 Reconocer inmutabilidad 

punto = (10, 20)
punto[0] = 99
print(punto)
#Esta restricción protege los datos fijos y evita que sean modificados accidentalmente durante la ejecución.

# %%
#17 Tupla como clave

lecturas = {}
coordenada = (4.65, -74.05)
lecturas[coordenada] = 18.5
print(lecturas[(4.65, -74.05)])


# %%
# 18 Combinar listas con zip 

nombres = ["Ana", "Luis", "Marta"]
notas = [4.2, 3.8, 5.0]
pares = list(zip(nombres, notas))
print(pares)


# %%
#19 Crear un diccionario 

estudiante = {
    
    "codigo": "A01",
    "nombre": "Laura",
    "nota": 4.6
}
print(estudiante)

# %%
# 20 Acceso seguro con get()

cliente = {"nombre": "Carlos", "puntaje": 720}
saldo = cliente.get("saldo", 0)
print(saldo)


# %%
#21 Actualizar valores

producto = {"codigo": "P01", "stock": 8}
producto["stock"] = producto["stock"] - 3
print(producto["stock"])


# %%
#22 Recorrer pares clave-valor 

producto = {"codigo": "P01", "precio": 12000, "stock": 8}
for clave, valor in producto.items():
 print(clave, valor)


# %%
#23 Contar por categoría 

tipos = ["Debito", "Credito", "Debito", "Debito", "Credito"]
conteo = {}
for tipo in tipos:
    conteo[tipo] = conteo.get(tipo, 0) + 1
print(conteo)


# %%
#24 Diccionario anidado 

grupo = {
 "A01": {"nombre": "Laura", "nota": 4.6},
 "A02": {"nombre": "Luis", "nota": 3.8}
}
print(grupo["A01"]["nota"])


# %%
#25 Lista de diccionarios 

transacciones = [
 {"id": "T01", "monto": 120000},
 {"id": "T02", "monto": 85000},
 {"id": "T03", "monto": 210000}
]
total = 0
for t in transacciones:
 total += t["monto"]
print(total)

# %%
#26 Buscar por código 

estudiantes = [
 {"codigo": "A01", "nombre": "Laura"},
 {"codigo": "A02", "nombre": "Luis"}
]
buscado = "A02"
resultado = None
for e in estudiantes:
   if e["codigo"] == buscado:
      resultado = e["nombre"]
print(resultado)


# %%
#27 Filtrar diccionarios

estudiantes = [
 {"nombre": "Ana", "nota": 4.2},
 {"nombre": "Luis", "nota": 2.8},
 {"nombre": "Marta", "nota": 3.5}
]
aprobados = []
for e in estudiantes:
 if e["nota"] >= 3.0:
     aprobados.append(e["nombre"])
print(aprobados)

# %%
#28 Agrupar por estado

clientes = [
{"nombre": "Ana", "riesgo": "bajo"},
{"nombre": "Luis", "riesgo": "alto"},
{"nombre": "Marta", "riesgo": "bajo"}
]
grupo = {}

for c in clientes:
   riesgo = c["riesgo"]
   if riesgo not in grupo:
      grupo[riesgo] = []
   grupo[riesgo].append(c["nombre"])
print(grupo)

# %%
# 29 Inventario académico
inventario = [
{"producto": "Marcador", "stock": 4},
{"producto": "Cuaderno", "stock": 20},
{"producto": "Borrador", "stock": 2}
]
bajos = []
for item in inventario:
   if item["stock"] < 5:
      bajos.append(item["producto"])
print(bajos)


# %%
# 30 Mini caso integrador

transacciones = [
    {"cliente": "Ana", "tipo": "Credito", "monto": 120000},
    {"cliente": "Luis", "tipo": "Debito", "monto": 85000},
    {"cliente": "Marta", "tipo": "Credito", "monto": 210000}
]
total_creditos = 0
clientes = []

for t in transacciones:
   if t["tipo"] == "Credito" and t["monto"] >= 100000:
      total_creditos += t["monto"]
      clientes.append(t["cliente"])

print(total_creditos)
print(clientes)

# Se utiliza una lista de diccionarios para almacenar las transacciones, una lista para guardar los clientes seleccionados y un acumulador para sumar los créditos que cumplen la condicion.
# %%

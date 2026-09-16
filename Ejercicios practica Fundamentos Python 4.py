# %%
# 1 Su primera clase

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
p = Persona("Ana", 21)
print(p.nombre, p.edad)

# %%
# 2 Crear varios objetos
a = Persona("Ana", 21)
b = Persona("Juan",22)
c = Persona("Pedro",25)
for x in [a, b, c]:
    print(x.nombre)
# %%
# 3 Leer y modificar un atributo
p = Persona("Luis", 30)
print(p.edad)
p.edad = 31
print(p.edad)
# %%
# 4 Objetos independientes
a = Persona("Ana", 21)
b = Persona("Ana", 21)
a.edad = 40
print(a.edad, b.edad)
# %%
# 5 La clase no guarda datos
#print(Persona.nombre) # AttributeError
# corrección:
p = Persona ("Ana",21)
print(p.nombre)
# nombre es un atributo de instancia, por lo que pertenece a cada objeto creado y no directamente a la clase Persona, para consultarlo se utiliza un objeto (p.nombre)
# %%
# 6 Un método que consulta
class Estudiante:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    def aprobo(self):
        return self.nota >= 3.0
    
print(Estudiante("Ana", 4.2).aprobo())

# %%
# 7 Un método que modifica
class Estudiante:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    def subir(self, puntos):
        self.nota = min(5.0, self.nota + puntos)
        return self.nota

e = Estudiante("Luis", 4.8)
print(e.subir(0.5))
# %%
# 8 Método con parámetros
class Estudiante:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    def promedio_con(self, otra):
        return round((self.nota + otra) / 2, 2)
e = Estudiante("Sara", 3.0)
print(e.promedio_con(4.0))

# %%
# 9 Atributo de clase
class Estudiante:
    total = 0
    def __init__(self, nombre):
        self.nombre = nombre
        Estudiante.total += 1
Estudiante("Ana")
Estudiante("Luis")
print(Estudiante.total)

# %%
# 10 ¿De instancia o de clase?

# codigo_curso = "20000151" -> Atributo de clase
# self.nombre = nombre -> Atributo de instancia
# self.nota = nota -> Atributo de instancia
# nota_minima = 3.0 -> Atributo de clase
#nota_minima es atributos de clase porque representa valores compartidos por todos los estudiantes

#%%
# 11 Encontrar el error
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def con_iva(self):
        return self.precio * 1.19

producto = Producto("prod1", 100)
print(producto.nombre)
print(producto.con_iva())
#Faltaba self en los métodos y en los atributos (self.nombre y self.precio) y Python mostraba un TypeError por recibir una cantidad incorrecta de argumentos.

# %%
# 12 Atributo privado
class Cuenta:
    def __init__(self, saldo):
        self.___saldo = saldo
    def consultar(self):
        return self.___saldo
c = Cuenta(100)
print(c.consultar())
# %%
# 13 Validar antes de modificar
class Cuenta:
    def __init__(self, saldo):
        self.__saldo = saldo
    def consignar(self, valor):
        if valor <= 0:
            return "Valor inválido"
        self.__saldo = self.__saldo + valor
        return self.__saldo
c = Cuenta(100)
print(c.consignar(-20))
print(c.consignar(50))

# %%
# 14 Retirar con control de saldo
class Cuenta:
    def __init__(self, saldo):
        self.__saldo = saldo
    def retirar(self, valor):
        if valor > self.__saldo:
            return "Fondos insuficientes"
        self.__saldo = self.__saldo - valor
        return self.__saldo
c = Cuenta(150)
print(c.retirar(200))

# %%
# 15 __str__: una vista legible
class Estudiante:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    def __str__(self):
        return f"{self.nombre}: {self.nota}"
print(Estudiante("Ana", 4.2))

# %%
# 16 Heredar de una clase base
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
class Estudiante(Persona):
    def __init__(self, nombre, nota):
        super().__init__(nombre)
        self.nota = nota
print(Estudiante("Ana", 4.2).nombre)
# %%
# 17 Sobrescribir un método

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    def saludar(self):
        return f"Hola, soy {self.nombre}"
class Estudiante(Persona):
    def __init__(self, nombre, nota):
        super().__init__(nombre)
        self.nota = nota
    def saludar(self):
        return f"Soy {self.nombre} y mi nota es {self.nota}"
print(Estudiante("Ana", 4.2).saludar())
#Se requiere conservar los constructores de Persona y Estudiante, ya que al redefinir las clases sin __init__, la ejecución genera error.

# %%
# 18 Una llamada, varias respuestas
grupo = [Persona("Sara"), Estudiante("Ana", 4.2)]
for p in grupo:
    print(p.saludar())

# %%
# 19 ¿Herencia o composición?
# Un docente es una persona -> herencia
# Un curso tiene estudiantes -> composicion
# Una cuenta de ahorros es una cuenta -> herencia
# Una biblioteca tiene libros -> composicion

#%%
# 20 La clase Curso
class Curso:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estudiantes = []
    def inscribir(self, estudiante):
        self.estudiantes.append(estudiante)
    def promedio(self):
        if len(self.estudiantes) == 0:
            return 0
        suma = sum(e.nota for e in self.estudiantes)
        return round(suma / len(self.estudiantes), 2)
# Se crea para probar el ejercicio
curso = Curso("Programación")
curso.inscribir(Estudiante("Ana", 4.2))
curso.inscribir(Estudiante("Luis", 3.1))
curso.inscribir(Estudiante("Marta", 2.7))
print(curso.promedio())
# %%
# 21 El reporte del curso
def aprobo(self):
    return self.nota >= 3.0
Estudiante.aprobo = aprobo
def reporte(self):
    aprobados = 0
    mejor = self.estudiantes[0]
    for e in self.estudiantes:
        if e.aprobo():
            aprobados = aprobados + 1
        if e.nota > mejor.nota:
            mejor = e
    return f"{aprobados} aprobados · mejor: {mejor.nombre}"
Curso.reporte = reporte
print(curso.reporte())

# %%
# 22 Diseñe usted la clase
class Vehiculo:
    def __init__(self, placa, tipo, hora_entrada):
        self.placa = placa
        self.tipo = tipo
        self.hora_entrada = hora_entrada
class Parqueadero:
    def __init__(self):
        self.vehiculos = []
    def recibir(self, vehiculo):
        self.vehiculos.append(vehiculo)
    def entregar(self, placa):
        for vehiculo in self.vehiculos:
            if vehiculo.placa == placa:
                self.vehiculos.remove(vehiculo)
                return vehiculo
        return None
    def cantidad(self):
        return len(self.vehiculos)
parqueadero = Parqueadero()
parqueadero.recibir(Vehiculo("AAA111", "Carro", "6:00"))
print(parqueadero.cantidad())
parqueadero.entregar("AAA111")
print(parqueadero.cantidad())

# %%

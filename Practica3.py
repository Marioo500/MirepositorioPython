nombre = str("Mario")
edad = int(19)
ingreso = float(750.6)
numcop = complex(1j)
lista = list(("pluma","lapiz","borrador","sacapuntas"))
tupla = tuple(("carro", "color", "llantas"))
rango = range(6)
maping = dict(name="Luis", age=19)
frpt = frozenset(("apple", "banana", "cherry"))
boolenao = bool(5)
byt = bytes(5)
arreglo = bytearray(5)
membyt = memoryview(bytes(5))

print(nombre)
print(edad)
print(numcop)
print(lista)
print(tupla)
print(rango)
print(maping)
print(frpt)
print(boolenao)
print(byt)
print(arreglo)
print(membyt)

x = int(9)
print(x)
y = int(9.5)
print(y)
z = int("4")
print(z)

x = float(9)
print(x)
y = float(9.50)
print(y)
z = float("4.002")
print(z)

x = str(9)
print(x)
y = str(9.5)
print(y)
z = str("4.002")
print(z)

mensaje = """"Hola muy buenas gente
de UABC me encuentro programando."""
cambio = "\n"
print(cambio)

#conocer la longitud de una cadena
nombre2 = "Lorenzo Lozano"
print(len(nombre2))

#Concacentacion
name = "Ricardo"
lastname = "Torres"
fullname = name + lastname
print(fullname)

fullname2 = name + " " + lastname
print(fullname2)

age = '43'
datos = "Mi nombre es " + name + " " + "tengo " + age
print(datos)

'''
print("inicio")
def saludo():
    print("hola mundo")

saludo()
'''

'''
def suma(a,b):
    c = a + b
    print(c)
num1 = int(input("numero 1: "))
num2 = int(input("numero 2: "))

suma(num1,num2)
'''

# Tuplas

'''
dupla = ("hola",2,4,False,4.4,"texto",("otra dupla",1,2),4)
print(dupla[0])
print(dupla[1]+dupla[2]+dupla[4])
print(dupla[1]+dupla[2]+dupla[4],dupla[0])
print(dupla[0]+" "+dupla[5])
print(f'la suma entre {dupla[1]}, {dupla[2]} y {dupla[4]} es: {dupla[1]+dupla[2]+dupla[4]}')

print(dupla[1:5])
print(dupla[:4])
print(dupla[4:])
print(dupla[:])

print(dupla[6])
print(dupla[6][0])
print(f'la suma entre {dupla[6][1]} y {dupla[6][2]} es: {dupla[6][1]+dupla[6][2]}')
''' 

# Inmutabilidad de las tuplas:

'''
dupla.append(6)
print(dupla)
'''

'''
dupla.pop()
print(dupla)
'''

'''
dupla[0] = 2.3
print(dupla)
'''

# Busquedas en tuplas

'''
print(4 in dupla)
print(("otra dupla",1,2) in dupla)
print("holaa" in dupla, 2 in dupla)

print(dupla.index(4.4))
print(dupla.index(4))
print(dupla.count(4))
print(dupla.count(7))
print(dupla.index(("otra dupla",1,2)))
print(dupla.index("hola"),dupla.index(4))
print(f'longitud de la tupla: {len(dupla)}')

# Convertir tuplas en listas 

dupla_a_lista = list(dupla)
print(dupla_a_lista)

dupla_a_lista[6] = ["otra lista",1,2]
print(dupla_a_lista)

dupla_a_lista.append(("soy una tupla en una lista",1,2.3))
print(dupla_a_lista)
'''

# Listas

'''
lista = ["asd",6,"hola",4,"texto",5.3,[1,2,3,"lista2"],True,False]
print(lista)
print(lista[0])
print(lista[3]+lista[1])
print(lista[0]+lista[4])
print(lista[3]+lista[1],lista[4])
print(lista[0]+" "+lista[4])
print(f'ejemplo de f print: {lista[0]} {lista[4]}')
print(f'otro ejemplo: {lista[3]+lista[1]} {lista[4]}')
print(lista[1]+lista[3]+lista[5])
'''

# Mutabilidad de las listas

'''
lista[1] = 2.5
print(lista[3]+lista[1])
print(lista[3]+lista[1],lista[4])
print(f'ejemplo de f print: {lista[0]} {lista[4]}')
print(f'otro ejemplo: {lista[3]+lista[1]} {lista[4]}')

lista[2] = "nuevo hola"

lista.append("3")
print(lista)

lista.append(3)
print(lista)

print(lista[1:4])
print(lista[:3])
print(lista[3:])
print(lista[:5])
print(lista[0:])
print(lista[:])

print(lista[6])
print(lista[6][0])
print(lista[6][0]+lista[6][1])
print(f'la suma de {lista[6][3]} entre {lista[6][0]} y {lista[6][1]} es: {lista[6][0]+lista[6][1]}')

elemento_removido = lista.pop(4)
print('elemento removido:',elemento_removido)
print("nueva lista:",lista)
'''

# Convertir listas a tuplas

'''
tupla = tuple(lista)
print(tupla)
'''

# Index en strings

'''
palabra = "ejemplo"

print(palabra[0])
print(palabra[2])
print(palabra[1],palabra[4])
print(palabra[2]+palabra[5])
print(f'ejemplo de f print: {palabra[2]} {palabra[5]}')
print(palabra[1:5])
print(palabra[:5])
print(palabra[2:])
print(palabra[:])
'''

# Conjuntos

'''
conjunto = set()
conjunto = {1,2,3.5,"texto",False}
print(conjunto)
'''

# Los conjuntos no permiten ingresar colecciones ni otros conjuntos
# Los conjuntos solo guardan valores unicos

'''
conjunto = set()
conjunto = {1,1,2,2,3,3}
print(conjunto)
'''

# Agregar valores a un conjunto

'''
conjunto.add(9)
conjunto.add("Hola")
conjunto.add(3.2)
print(conjunto)
'''

# Eliminar valores de un conjunto

'''
conjunto.discard(1)
print(conjunto)
'''

# Buscar valores en un conjunto 

'''
print(1 in conjunto)
print(3.2 not in conjunto)
'''

# Vaciar un conjunto 

'''
conjunto.clear()
print(conjunto)
'''

# Diccionarios

'''
diccionario = {"azul":"blue","rojo":"red","verde":"green","uno":1,"dos":2}
print(diccionario["azul"])
print(diccionario["azul"],diccionario["rojo"],diccionario["verde"])
print(f'la suma es: {diccionario["uno"]+diccionario["dos"]}')
print(f'lista de colores: {diccionario["azul"],diccionario["rojo"],diccionario["verde"]}')
print(f'lista de colores: {diccionario["azul"]+", "+diccionario["rojo"]+", "+diccionario["verde"]}')
print(f'lista de colores: {diccionario["azul"]}, {diccionario["rojo"]}, {diccionario["verde"]}')
'''

# Agregar elementos a un diccionario

'''
diccionario["amarillo"] = "yellow"
print(diccionario)
'''

# Modificar elementos de un diccionario

'''
diccionario["azul"] = "BLUE"
print(diccionario["azul"])
'''

# Eliminar elementos de un diccionario

'''
del(diccionario["verde"])
print(diccionario)
'''

# Diccionarios compuestos

'''
Dic_lista = {"Colores":["rojo","verde","azul"],"Animales":("tigre","ballena","gato"),"Numeros":[2,2,3.6,4]}
print(Dic_lista)
print(Dic_lista["Colores"])
print(Dic_lista["Animales"][0])
print(f'Los colores son: {Dic_lista["Colores"][0]}, {Dic_lista["Colores"][1]}, {Dic_lista["Colores"][2]}')
print(f'la suma entre {Dic_lista["Numeros"][0]}, {Dic_lista["Numeros"][1]}, {Dic_lista["Numeros"][2]}, {Dic_lista["Numeros"][3]} es: {Dic_lista["Numeros"][0]+Dic_lista["Numeros"][1]+Dic_lista["Numeros"][2]+Dic_lista["Numeros"][3]}')

print(Dic_lista["Colores"].index("azul"))
print(Dic_lista["Numeros"].count(2))
'''

# Diccionarios dentro de otros

'''
animales = {"lobo":{"color":"gris","clase":"mamifero","esperanza de vida":15},
"venado":{"color":"cafe","clase":"mamifero","esperanza de vida":10},
"tiburon":{"color":"azul","clase":"pez","esperanza de vida":30}}
print(animales)
print(animales["lobo"])
print(animales["tiburon"]["clase"])
print(f'la suma de la esperanza de vida de los animales es {animales["lobo"]["esperanza de vida"]+animales["venado"]["esperanza de vida"]+animales["tiburon"]["esperanza de vida"]} años')

print("venado" in animales)
print("clase" in animales)
print("clase" in animales["lobo"])
print("mamifero" in animales["lobo"]["clase"])
'''

'''
print(animales.index(["lobo"]))
print(animales.count(30))
'''
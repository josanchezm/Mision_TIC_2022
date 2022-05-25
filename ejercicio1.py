# Semana 1

# comentar una linea de codigo

# print("holaaaaa")

'''
print("Algoritmo Adquisicion_libro")
print("Inicio")
print("\t 1. Saber cual libro se quiere adquirir")
print("\t 2. Dirigirse a una libreria")
print("\t 3. Preguntar por el libro")

print("\t Si esta disponible")
print("\t \t Comprarlo y detenerse ahi")

print("\t si no esta disponible")
print("\t \t volver al paso 2")
'''
'''
a = 8
b = a
c = a+b

print(a,b,c)

var = "asdsada"
print(var)

var = 1.7
print(var)

var += 1.7
print(var)
'''
'''
x = 1
x = x*2
x *= 2
print(x)
'''

'''
rem = 5
rem = rem % 10
print(rem)
rem %= 10
print(rem)
'''

'''
j = 50
x = 100
var = 55
rem = 99
i = 65
j =  j - (i+var+rem)
print(j)
j -= (i+var+rem)
x = x**2
print(x)
x **= 2
print(j,x)
'''

# errores en declaracion de variables

'''
var 1 = 120
@var = 120
1var = 120
var-1 = 120
'''

# asignacion multiple en variables

'''
var1,var2,var3 = 1,2,3
print(var1,var2,var3)
'''

# prompts y asignacion de tipo de variables
'''
largo = float(input("ingrese el largo: "))
ancho = float(input("ingrese el ancho: "))
unidad = input("ingrese la unidad de medida: ")
area = largo * ancho
print("El area del rectangulo es: ", area, unidad)
'''

# Condicional simples

'''
edad = int(input("ingrese la edad: "))

if edad >= 18:
    print("es mayor de edad")
else:
    print("es menor de edad")
'''

# Condicional while

'''
numero = 1

while numero <= 5:
    print(numero)
    numero += 1
print("zoi el ciclo ia me mori")
'''

# Errores de sintaxis en Python

'''
Print("uwu")
Traceback (most recent call last):
  File "d:\Jaime\Programming\MisionTIC\Ciclo 1\semana_1\ejercicio1.py", line 112, in <module>
    Print("uwu")
NameError: name 'Print' is not defined. Did you mean: 'print'?

print("uwu"
File "d:\Jaime\Programming\MisionTIC\Ciclo 1\semana_1\ejercicio1.py", line 120
    print("uwu"
         ^
SyntaxError: '(' was never closed

print"uwu")
File "d:\Jaime\Programming\MisionTIC\Ciclo 1\semana_1\ejercicio1.py", line 126
    print"uwu")
              ^
SyntaxError: unmatched ')'

print("uwu)
Usuario@DESKTOP-GGG10EN MINGW64 ~ (main)
$ C:/Users/Usuario/AppData/Local/Programs/Python/Python310/python.exe "d:/Jaime/Programming/MisionTIC/Ciclo 1/semana_1/ejercicio1.py"
  File "d:\Jaime\Programming\MisionTIC\Ciclo 1\semana_1\ejercicio1.py", line 132
    print("uwu)
          ^
SyntaxError: unterminated string literal (detected at line 132)

print(uwu)
Traceback (most recent call last):
  File "d:\Jaime\Programming\MisionTIC\Ciclo 1\semana_1\ejercicio1.py", line 141, in <module>
    print(uwu)
NameError: name 'uwu' is not defined

print("asdasd")
File "d:\Jaime\Programming\MisionTIC\Ciclo 1\semana_1\ejercicio1.py", line 147
    print("asdasd")
IndentationError: unexpected indent
'''

# Comillas simples vs comillas dobles en Python

'''
print('ola')
$ C:/Users/Usuario/AppData/Local/Programs/Python/Python310/python.exe "d:/Jaime/Programming/MisionTIC/Ciclo 1/semana_1/ejercicio1.py"
ola

print("hola")
$ C:/Users/Usuario/AppData/Local/Programs/Python/Python310/python.exe "d:/Jaime/Programming/MisionTIC/Ciclo 1/semana_1/ejercicio1.py"
hola

Comillas simples y doble es la misma monda xd
'''

# Prints multiples y arrays recorridos con whiles

'''
print("Hola", "Hello", "Ola")

saludo = ["Hola", "Hello", "Ola"]

numero = 0

while numero <= 2:
    print(saludo[numero])
    numero += 1
print("c acabo")
'''

# Un robot en Python

'''
print("     _____ ")
print("    / (oo)\ ")
print("   |       | ")
print("  _|_______|_")
print(" | |  ===  | |")
print(" |_|   O   |_|")
print(" | |   O   | |")
print(" | |___ ___| |")
print("|~ \_______/~ |")
print("/=\   /=\   /=\ ")
print("[ ]   [ ]   [ ]")
'''

# Funciones en Python

'''
def gradosCaF():
    Celcius = float(input("ingrese los grados celcius: "))
    Fahrenheit = (Celcius*(9/5))+32
    print(Celcius,"grados Celcius equivalen a",Fahrenheit,"grados Fahrenheit")
gradosCaF()
'''

'''
def gradosFaC():
    Fahrenheit = float(input("ingrese los grados Fahrenheit: "))
    Celcius = (Fahrenheit-32)*(5/9)
    print(Fahrenheit,"grados Fahrenheit equivalen a",Celcius,"grados Celcius")
gradosFaC()
'''

'''
def usdACop():
    usd = float(input("ingrese los dolares: "))
    cop = usd * 3931.74
    print(usd,"dolar(es) equivalen a",cop,"peso(s) colombianos")
usdACop()
'''

'''
def IMC():
    peso = float(input("ingrese el peso: "))
    altura = float(input("ingrese su altura: "))
    imc = peso / (altura**2)
    print("el IMC es de:",imc,"kg/m^2")
IMC()
'''

'''
def censo():
    nombre = input("ingrese su nombre: ")
    cumpleannios = input("ingrese su fecha de nacimiento: ")
    edad = input("ingrese su edad: ")
    ocupacion = input("a que se dedica? ")
    telefono_fijo = input("cual es su numero fijo? ")
    nombre_calle = input("ingrese el nombre de su calle: ")
    ciudad = input("cual es su ciudad? ")
    habitantes_vivienda = input("cuantas personas viven en su casa? ")
    estado_civil = input("cual es su estado civil? ")
    print("los datos que ingreso al formulario son los siguientes: \n",nombre,"\n",cumpleannios,"\n",edad,"\n",ocupacion,"\n",telefono_fijo,"\n",nombre_calle,"\n",ciudad,"\n",habitantes_vivienda,"\n",estado_civil)
censo()
'''

# concatenacion de strings en Python

'''
def concatenacion():
    uno = input("digite el primer numero: ")
    dos = input("digite el otro numero: ")
    suma = uno + dos
    print("la suma entre",uno,"y",dos,"es",suma)
concatenacion()
'''

# Tipo de variables y variables de tipo dinamico

'''
def tipoVariable():
    n1 = input("ingrese el numero: ")
    print(type(n1))
    n1 = float(n1)
    print(type(n1))
tipoVariable()
'''

# Operaciones aritmeticas

'''
def suma():
    uno = float(input("digite el primer numero: "))
    dos = float(input("digite el otro numero: "))
    suma = uno + dos
    print("la suma entre",uno,"y",dos,"es",suma)
suma()
'''

'''
def cuadrado():
    numero = float(input("ingrese un numero para elevar al cuadrado: "))
    cuadrado = numero**2
    print("el cuadrado de",numero,"es",cuadrado)
cuadrado()
'''

'''
def potencia():
    numero = float(input("ingrese el numero: "))
    potencia = float(input("ingrese la potencia: "))
    calculo = numero**potencia
    print("el numero",numero,"elevado a la potencia",potencia,"es igual a",calculo)
potencia()
'''

'''
def operacionesAritmeticas():
    numero_1 = float(input("ingrese el primer numero: "))
    numero_2 = float(input("ingrese el segundo numero: "))

    suma = numero_1 + numero_2
    resta = numero_1 - numero_2
    multiplicacion = numero_1 * numero_2
    division = numero_1 / numero_2
    potencia = numero_1 ** numero_2
    division_entera = numero_1 // numero_2
    modulo = numero_1 % numero_2

    print("el resultado de las operaciones entre",numero_1,"y",numero_2,"es: \n",
    "suma:",suma,"\n","resta:",resta,"\n","mutiplicacion:",multiplicacion,"\n",
    "division:",division,"\n","potencia:",potencia,"\n","division entera:",division_entera,"\n",
    "modulo:",modulo)
operacionesAritmeticas()
'''

# Semana 2

# Mas funciones en Python

# funcion con parametro, evaluada con argumento:

'''
def lbAKg (libras):
    kg = libras*.453592
    print(libras,"libras equivalen a",kg,"kilogramos")
lbAKg(180)
'''

'''
def lbAKg ():
    libras = float(input("ingrese su masa en libras: "))
    kg = libras*.453592
    print(libras,"libras equivalen a",kg,"kilogramos")
lbAKg()
'''

'''
def calculoHipotenusa():
    catetoOpuesto = float(input("ingrese el cateto opuesto: "))
    catetoAdyacente = float(input("ingrese el cateto adyacente: "))
    unidad = input("ingrese la unidad de medida: ")
    hipotenusa = (catetoOpuesto**2+catetoAdyacente**2)**(1/2)
    print("cateto opuesto:",catetoOpuesto,unidad,"\ncateto adyacente:",catetoAdyacente,unidad,"\nhipotenusa:",hipotenusa,unidad)
calculoHipotenusa()
'''

'''
def millasAKm():
    millas = float(input("ingrese las millas: "))
    km = millas * 1.60934
    print(millas,"millas equivalen a",km,"kilometros")
millasAKm()
'''

'''
def kmAmillas():
    km = float(input("ingrese los kilometros: "))
    millas = km * .621371
    print(km,"kilometros equivalen a",millas,"millas")
kmAmillas()
'''

'''
def operacionesBasicas():
    suma1 = float(input("primer numero de la suma: "))
    suma2 = float(input("segundo numero de la suma: "))
    suma = suma1+suma2

    resta1 = float(input("primer numero de la resta: "))
    resta2 = float(input("segundo numero de la resta: "))
    resta = resta1-resta2

    multiplicacion1 = float(input("primer numero de la multiplicacion: "))
    multiplicacion2 = float(input("segundo numero de la multiplicacion: "))
    multiplicacion = multiplicacion1 * multiplicacion2

    division1 = float(input("primer numero de la division: "))
    division2 = float(input("segundo numero de la division: "))
    division = division1 / division2

    print("suma:",suma,"\nresta:",resta,"\nmultiplicacion:",multiplicacion,"\ndivision:",division)
operacionesBasicas()
'''
# invocacion de funciones dentro de un print, haciendo uso de variables externas a esta como argumentos y usando return para devolver el resultado de la ejecucion de las sentencias de la funcion

'''
def ejemploSuma(numeroA,numeroB):
    resultado = numeroA+numeroB
    return resultado

input1 = float(input("ingrese el numero A: "))
input2 = float(input("ingrese el numero B: "))
print("el resultado de la suma es: ",ejemploSuma(input1,input2))
'''

'''
def operacionesBasicas2(a,b):
    suma = a+b
    resta = a-b
    multiplicacion = a*b
    division = a/b
    resultado =  print("suma:",suma,"\nresta:",resta,"\nmultiplicacion:",multiplicacion,"\ndivision:",division)
    return resultado

n1 = float(input("primer numero: "))
n2 = float(input("segundo numero: "))
operacionesBasicas2(n1,n2)
'''

# Condicional if

'''
def edades():
    edad = int(input("ingrese la edad: "))
    if edad >= 18:
        print("usuario mayor de edad")
    else:
        print("usuario menor de edad")
edades()
'''

'''
def edades(edad):
    if edad >= 18:
        print("es mayor de edad")
    else:
        print("eres menor de edad")
edades(15)
'''

# importacion de librerias

# importacion de funciones trigonometricas y de una que pasa grados a radianes (ya que python calcula este tipo de funciones solo en radianes)

from bdb import GENERATOR_AND_COROUTINE_FLAGS
from contextlib import nullcontext
import math as m
from mimetypes import init
from operator import truediv
from re import S
from xmlrpc.client import TRANSPORT_ERROR

'''
def trigonometria():
    grados = float(input("ingrese los grados: "))
    radianes = m.radians(grados)
    seno = m.sin(radianes)
    coseno = m.cos(radianes)
    tangente = m.tan(radianes)
    print("para",grados,"grados, tenemos:","\nseno:",seno,"\ncoseno:",coseno,"\ntangente:",tangente)
    print("para",grados,"grados, el seno es:",m.sin(radianes))
trigonometria()
'''

'''
def seno(x):
    seno = m.sin(x)
    return seno

def coseno(x):
    resultado = m.cos(x)
    return resultado



def tangente(x):
    resultado = m.tan(x)
    return resultado

grados = float(input("ingrese los grados: "))
radianes = m.radians(grados)
respuesta = coseno(radianes)

print("para",radianes,"radianes, tenemos:","\nseno:",seno(radianes),"\ncoseno:",respuesta,"\ntangente:",tangente(radianes))
'''

'''
def raizCuarta(x):
    resultado = m.sqrt(m.sqrt(x))
    return resultado

numero = float(input("ingrese el numero: "))

print("la raiz cuarta de",numero,"es:",raizCuarta(numero))
'''

# generar numeros aleatorios a traves de librerias


import random as r

'''
def juegoDados():
    lanzar_dado_1 = r.randint(1,6)
    lanzar_dado_2 = r.randint(1,6)
    casillas_a_recorrer = lanzar_dado_1+lanzar_dado_2
    print("tiraste los dados, tu primer dado dio",lanzar_dado_1,"y el segundo",lanzar_dado_2,"\ntienes derecho a avanzar",casillas_a_recorrer,"posiciones")
juegoDados()
'''

# Programa para identificar titulos

# istitle() es una funcion de python que evalua si una cadena de caracteres inicia cada una de sus palabras capitalizadas

'''
def esTitulo(titulo):
    if titulo.istitle():
        print("el texto ingresado es un titulo")
        return True
    else:
        print("el texto ingresado no es un titulo")
        return False

texto = input("ingrese el titulo de su libro: ")
esTitulo(texto)
'''

# Programa que verifica numeros enteros a medias, esto es solo un ejemplo para ver como funciona las posiciones index dentro de los strings

'''
def numerosEnteros(numero):
    if numero.isdigit():
        print("el numero es un entero positivo")
    elif numero[0] == "-":
        print("el numero es un entero negativo")
    else:
        print("el valor ingresado no es un entero")

valor_usuario = input("ingrese un numero entero: ")
numerosEnteros(valor_usuario)
'''

# Juego de adivinar numeros entre 1 y 10

'''
def adivinar(numero):
    if 0<=numero<=10:
        al_azar = r.randint(1,10)
        print("el numero generado al azar fue:",al_azar)
        if numero == al_azar:
            return True
        else:
            return False
    else:
        print("el numero ingresado no esta entre 1 y 10")
        return False

valor = int(input("ingrese un numero entre 1 y 10: "))

if adivinar(valor):
    print("ganaste")
else:
    print("perdiste")
'''

# Ejercicio de condicionales

# retornar el resultado de una funcion evaluada por medio de condicionales, para incorporarlo dentro del string de un print

'''
def mundoJugador(edad,experiencia,nivel):
    if 12<=edad<=20 and experiencia == "no" and nivel == 0:
        return 1
    elif 12<=edad<=20 and experiencia == "si" and nivel<50:
        return 2
    elif 12<=edad<=20 and experiencia == "si" and 50<=nivel<=100:
        return 3
    elif edad>20 and experiencia == "no" and nivel == 0:
        return 4
    elif edad>20 and experiencia == "si" and nivel<50:
        return 5
    elif edad>20 and experiencia == "si" and 50<=nivel<=100:
        return 6
    else:
        print("has ingresado datos incorrectos, vuelve a intentarlo")
        return "ninguno"

edad = int(input("ingrese su edad: "))
experiencia = input("tiene experiencia? (si o no): ")
nivel = int(input("en que nivel de 0 a 100 se encuentra? "))

mundoAsignado = mundoJugador(edad,experiencia,nivel)

# en el espacio de memoria mundoAsignado, guardamos el retorno de la funcion mundo jugador

print("mundo asignado:",mundoAsignado)
'''

# Cadenas de caracteres

'''
cadena = "el hijo de rana"
print(cadena[0])
print(cadena[5:])
print(cadena[:5])
print(cadena[5:9])
'''

'''
def edadFormato(fecha):
    fecha_formato = fecha[0]+"/"+fecha[5:8]+"/"+fecha[12:]
    edad = 2022 - int(fecha[12:])
    resultado = print(fecha_formato+",","su edad es",edad,"años")
    return resultado

fecha_nacimiento = input("ingrese su fecha de nacimiento (formato de ejemplo: 8 de nov de 1977): ")

edadFormato(fecha_nacimiento)
'''

'''
saludo = "assdaasd"
print(saludo)

a=5
b=2
c=a+b
print(c)
'''

'''
def CDT(usuario,capital,tiempo):
    porcentaje_interes = .03
    porcentaje_a_perder = .02

    if tiempo > 2:
        valor_intereses = (capital*porcentaje_interes*tiempo)/12
        valor_total = valor_intereses + capital
    else:
        valor_a_perder = capital*porcentaje_a_perder
        valor_total = capital-valor_a_perder
    return print(f'Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {capital} para un tiempo de {tiempo} meses es: {valor_total}')
CDT("ER3366",650000,2)
'''

'''
print("inicio")
def saludo():
    print("hola mundo")

saludo()
'''

# Diccionarios:

# permite relacionar una entidad (llave) con un valor, puede ser de mismo tipo o diferente las llaves y sus valores

'''
diccionario_vacio = {}
sensores = {"living room": 21,"kitchen": 23,"bedroom":20}
'''

# agregar elementos a un diccionario

'''
sensores["bathroom"] = 18
print(sensores)
'''

# ver el tipo de un elemento en python

'''
dic1 = {}
print(type(dic1))
print(dic1)
dic1["numero"] = 23
print(dic1)

dic2 = {"id":1, "nombre":"Carlos", "edad":49, "primerizo":True}
print(dic2)
dic2["color"] = "rojo"
print(dic2)

dic3 = {1:"perro"}
print(dic3)
dic3[2] = "gato"
print(dic3)
'''

# Reescribir el valor asociado a una llave (nombre)

dic1 = {"Id_cliente": 1, "nombre": "Johana Fernandez", "edad": 20, "primer_ingreso": True}

'''
dic1["nombre"] = "Valentina"
'''

# Reto 2

'''
def cliente(informacion):
    respuesta = {}
    respuesta["nombre"] = informacion["nombre"]
    respuesta["edad"] = informacion["edad"]
    if informacion["edad"]>18:
        respuesta["atraccion"] = "X-Treme"
        respuesta["apto"] = True
    respuesta["primer_ingreso"] = informacion["primer_ingreso"]
    return respuesta

print(cliente(dic1))
'''

# Mas ciclos while

'''
amiguis = 3

while amiguis <= 30:
    print(amiguis)
    amiguis += 3
print("se acabo el ciclo")
'''

'''
numero = 0
saludo = ["hola","buenos","dias"]

while numero <= 2:
    print(saludo[numero])
    numero += 1
print("se acabo el otro ciclo")
'''

# Programa que muestra la tabla de multiplicar que se pida\

'''
tabla = int(input("que tabla desea ver? "))

tabla_inicio = tabla
tabla_final = tabla*10
i = 1

while tabla <= tabla_final:
    print(f'{tabla_inicio}x{i} = {tabla}')
    tabla += tabla_inicio
    i += 1
print(f'se termino la tabla del {tabla_inicio}')
'''

#While con sumatorias y conteos

'''
i = 1
sumatoria = 0
while i <= 5:
    print(i)
    sumatoria += i
    i+=1
print("se acabo")
print(f'la sumatoria es: {sumatoria}')
'''

# Programa que imprime los numeros pares y su sumatoria

'''
i = 0
sumatoria = 0

while i <= 100:
    par = 2*i
    i += 1
    sumatoria += par
    print(par)
print(f'la sumatoria de los numeros pares del 0 al {i-1} es: {sumatoria}')
'''

# Programa que imprime los numeros impares y su sumatoria

'''
i = 0
sumatoria = 0

while i < 100:
    impar = (2*i)+1
    i += 1
    sumatoria += impar
    print(impar)
print(f'la sumatoria de los numeros impares entre el 0 y el {i} es: {sumatoria}')
'''

#La sumatoria de los multiplos de 7

'''
def sumatoria_7(numero, multiplos):
    i = 1
    sumatoria = 0

    while i <= multiplos:
        multiplos_numero = i*numero
        sumatoria += multiplos_numero
        i += 1
        print(multiplos_numero)
    print(f'La sumatoria de los primeros {multiplos} multiplos de {numero} es: {sumatoria}')


numero_usuario = int(input("digite el numero al cual desea obtener sus multiplos: "))
multiplos_usuario = int(input("digite la cantidad de multiplos a los que les desea hacer sumatoria: "))
sumatoria_7(numero_usuario,multiplos_usuario)
'''

# La sumatoria de la n cantidad de numeros que indique el usuario

'''
def sumatoria_usuario(inicio,n):
    numero_inicial = inicio
    numero_final = n
    sumatoria = 0
    while inicio <= n:
        sumatoria += inicio
        inicio += 1
        print(sumatoria)
    print(f'la sumatoria de los numeros del {numero_inicial} al {numero_final} es: {sumatoria}')

numero_inicio = int(input("ingrese el numero de inicio: "))
numero_final = int(input("ingrese el numero de cierre: "))
sumatoria_usuario(numero_inicio,numero_final)
'''

# La sumatoria de la n cantidad de numeros que indique el usuario, pero ahora con los int dentro del ciclo:

'''
numero_usuario = int(input("indique cuantos numeros desea sumar: "))


def sumatoria_numeros(numero):
    i = 1
    sum = 0
    while i <= numero:
        sum += int(input("ingrese el numero: "))
        i += 1
    return print(f'la sumatoria es: {sum}')
sumatoria_numeros(numero_usuario)
'''

#Programa que calcula las notas del ciclo 1

'''
def notas(r1,r2,r3,r4,r5,ingles,coach):
    nota_r1 = r1 * .1
    nota_r2 = r2 * .1
    nota_r3 = r3 * .2
    nota_r4 = r4 * .2
    nota_r5 = r5 * .2
    nota_ingles = ingles * .1
    nota_coach = coach * .1
    nota_ciclo = nota_r1+nota_r2+nota_r3+nota_r4+nota_r5+nota_ingles+nota_coach

    return print(f'su nota del ciclo 1 es: {nota_ciclo}')

nota_1 = float(input("ingrese la nota del reto 1: "))
nota_2 = float(input("ingrese la nota del reto 2: "))
nota_3 = float(input("ingrese la nota del reto 3: "))
nota_4 = float(input("ingrese la nota del reto 4: "))
nota_5 = float(input("ingrese la nota del reto 5: "))
nota_ingles = float(input("ingrese la nota de ingles: "))
nota_coach = float(input("ingrese la nota de coach: "))
notas(nota_1,nota_2,nota_3,nota_4,nota_5,nota_ingles,nota_coach)
'''

#Programa que calcula las notas del ciclo 1 pero con while y condicionales

'''
def notas():
    i = 1
    notas = 0

    while i <= 7:
        if i<=2 or i>= 6:
            notas += float(input(f"ingrese la {i} nota: "))*.1
        else:
            notas += float(input(f"ingrese la {i} nota: "))*.2
        i += 1
    return print(f'su nota del ciclo es: {notas}')
notas()
'''

#Reto 2 ahora si:

'''
def cliente(d):
    respuesta = {}
    respuesta["nombre"] = d["nombre"]
    respuesta["edad"] = d["edad"]
    if d["edad"]>18 and d["primer_ingreso"] == True:
        respuesta["atraccion"] = "X-Treme"
        respuesta["apto"] = True
        respuesta["primer_ingreso"] = d["primer_ingreso"]
        respuesta["total_boleta"] = 20000 * .95
    elif d["edad"]> 18 and d["primer_ingreso"] == False:
        respuesta["atraccion"] = "X-Treme"
        respuesta["apto"] = True
        respuesta["primer_ingreso"] = d["primer_ingreso"]
        respuesta["total_boleta"] = 20000
    elif 15<=d["edad"]<=18 and d["primer_ingreso"] == True:
        respuesta["atraccion"] = "Carros chocones"
        respuesta["apto"] = True
        respuesta["primer_ingreso"] = d["primer_ingreso"]
        respuesta["total_boleta"] = 5000 * .93
    elif 15<=d["edad"]<=18 and d["primer_ingreso"] == False:
        respuesta["atraccion"] = "Carros chocones"
        respuesta["apto"] = True
        respuesta["primer_ingreso"] = d["primer_ingreso"]
        respuesta["total_boleta"] = 5000
    elif 7<=d["edad"]<15 and d["primer_ingreso"] == True:
        respuesta["atraccion"] = "Sillas voladoras"
        respuesta["apto"] = True
        respuesta["primer_ingreso"] = d["primer_ingreso"]
        respuesta["total_boleta"] = 10000 * .95
    elif 7<=d["edad"]<15 and d["primer_ingreso"] == False:
        respuesta["atraccion"] = "Sillas voladoras"
        respuesta["apto"] = True
        respuesta["primer_ingreso"] = d["primer_ingreso"]
        respuesta["total_boleta"] = 10000
    elif d["edad"]<7:
        respuesta["atraccion"] = "N/A"
        respuesta["apto"] = False
        respuesta["primer_ingreso"] = d["primer_ingreso"]
        respuesta["total_boleta"] = "N/A"
    return respuesta

dic1={"id_cliente":1,"nombre":"Johana Fernandez","edad":20,"primer_ingreso":True}
dic2={"id_cliente":1,"nombre":"Johana Fernandez","edad":20,"primer_ingreso":False}
dic3={"id_cliente":2,"nombre":"Gloria Suarez","edad":3,"primer_ingreso":True}
dic4={"id_cliente":3,"nombre":"Tatiana Suarez","edad":17,"primer_ingreso":True}
dic5={"id_cliente":3,"nombre":"Tatiana Suarez","edad":17,"primer_ingreso":False}
dic6={"id_cliente":4,"nombre":"Tatiana Ruiz","edad":8,"primer_ingreso":True}
dic7={"id_cliente":4,"nombre":"Tatiana Ruiz","edad":8,"primer_ingreso":False}

cliente(dic1)
cliente(dic2)
'''

#Programa que hace la sumatoria de un contador de numeros

'''
contador = int(input("ingrese cuantos numeros quiere contar: "))

def contador_sumatoria(numero):
    i = 1
    sumatoria = 0
    while i <= contador:
        sumatoria += i
        print(i)
        i += 1
    print(f'la sumatoria es: {sumatoria}')
contador_sumatoria(contador)
'''

#Programa que hace la sumatoria y conteo entre dos numeros:

'''
numero_1 = int(input("ingrese el numero inicial: "))
numero_2 = int(input("ingrese el numero final: "))

def contador_sumatoria(inicio,final):
    sum=0
    while inicio <= final:
        sum += inicio
        print(inicio)
        inicio += 1
    return print(f'la sumatoria de los numeros entre el {numero_1} y el {numero_2} es: {sum}')
contador_sumatoria(numero_1,numero_2)
'''

#Programa que hace la sumatoria de los n multiplos de un numero que indique el usuario

'''
numero_usuario = int(input("ingrese el numero: "))
multiplos_usuario = int(input(f'ingrese la cantidad de mutiplos de {numero_usuario}: '))

def sumatoria_multiplos(numero, multiplos):
    i = 1
    sum = 0
    while i <= multiplos:
        multiplos_numero = numero * i
        sum += multiplos_numero
        i += 1
        print(multiplos_numero)
    return print(f'para los primeros {multiplos} multiplos de {numero}, la sumatoria es: {sum}')
sumatoria_multiplos(numero_usuario,multiplos_usuario)
'''

# Programa que calcula la nota del ciclo 1:

'''
def calculo_Notas():
    i=1
    notas = 0
    while i <= 7:
        if i<=2 or i>= 6:
            notas += float(input(f"ingrese la {i} nota: "))*.1
        else:
            notas += float(input(f"ingrese la {i} nota: "))*.2
        i += 1
    return print(f'su promedio del ciclo 1 es: {notas}')
calculo_Notas()
'''

#Calculo de promedios

'''
def promedios():
    numero = int(input("ingrese la cantidad de numeros a promediar: "))
    i = 1
    sum = 0
    while i <= numero:
        sum += float(input(f'ingrese el numero {i}: '))
        i += 1
    promedio = sum / numero
    return print(f'el promedio es: {promedio}')
promedios()
'''

# Listas
# Son mutables y ordenadas

'''
lista = [1, 2, 3, 3, 8.8, "Hola", ["xd", 1], True, False]
'''

# guardar cada elemento de una tupla en una variable

'''
x,y,r,z = [2,3.4,"y",152]
print(x,y,r,z)
'''

# Acceder a elementos en una lista y operarlos:

'''
print(lista)
print(type(lista))
print(lista[0])
print(f'La suma de {lista[0]} y {lista[3]} es: {lista[0]+lista[3]} ')
print(lista[5])
print(lista[5][1])
print(f"la contatenacion entre {lista[6][0]} y {lista[6][1]} es: {lista[6][0]+str(lista[6][1])}")
'''

# reasignar valores en los elementos de la lista

'''
lista[4] = 99.9
print(lista[4])
'''

# Metodos aplicados a listas

# ver el index de un elemento de la lista

'''
print(lista.index("Hola"))

'''
# ver el conteo de un elemento de la lista

'''
print(f'el conteo de {lista[2]} en la lista es: {lista.count(3)} veces')
'''

# agregar elementos al final de la lista

'''
lista.append("Nuevo elemento")
print(lista)
'''

# eliminar el ultimo elemento de la lista

'''
lista.pop()
print(lista)
'''
# eliminar el valor en el index indicado

'''
lista.pop(0)
print(lista)
'''
# eliminar el valor especificado de la lista, si el valor se encuentra mas de una vez, elimina el primero

'''
lista.remove(3)
print(lista)
'''

# copiar una lista en una variable

'''
l2 = lista.copy()
print(lista)
print(l2)
'''

# limpiar una lista

'''
l2.clear()
print(f'la lista l2 esta vacia: {l2}')
'''

# agregar los elementos de una lista al final de otra lista

'''
l3 = ["texto",1,3.2]
lista.extend(l3)
print(l3)
print(lista)
'''

# agregar un valor en el index indicado, el valor que se encontraba en ese index pasa al siguiente

'''
lista.insert(4,"valor agregado")
print(lista)
'''

# voltear el orden de la lista

'''
print(lista)
lista.reverse()
print(lista)
'''

# ordenar la lista de menor a mayor (solo para listas de un solo tipo)

'''
numeros = [7,6, 10, 11, 1, 0.9, 2]
numeros.sort()
print(numeros)

palabras = ["Sofia","Alejandra","Karen","Jaime","Barbara"]
palabras.sort()
print(palabras)
'''

# ordernar la lista de mayor a menor (solo para listas de un solo tipo)

'''
numeros.sort(reverse = True)
print(numeros)

numeros.sort()
numeros.reverse()
print(numeros)

palabras.sort(reverse = True)
print(palabras)

palabras.sort()
palabras.reverse()
print(palabras)
'''

# los ciclos pueden recorrer listas

'''
nombres = ["Sofia","Alejandra","Karen","Jaime","Barbara","Elizabeth"]

i = 1
for nombre in nombres:
    print(f'{i} nombre: {nombre}')
    i += 1
'''

# cortar listas en pedazos, guarda en la nueva variable la lista seccionada desde la posicion incial indicada hasta el index anterior a la posicion final indicada

'''
l1 = [3,5,7,2,9,8.8,10,"asd"]
p1 = l1[:3]
p2 = l1[3:]
p3 = l1[1:5]
print(l1)
print(p1)
print(p2)
print(p3)
'''

# convertir tuplas en listas

'''
tupla = (1,3.3,"texto",9,"texto")
lista = list(tupla)
print(lista)
'''

# Tuplas
# Son inmutables y ordenadas

'''
tupla = (3,5,"hola",4.7,8,3)
'''

'''
print(tupla)
print(tupla[:3])
print(tupla[0:])
print(tupla[0:2])
print(tupla[:])
'''

# guardar cada elemento de una tupla en una variable

'''
x,y,r,z = (5,8,0,"asd")
print(x,y,r,z)
'''

# Metodos de tuplas

# hacer conteo de un valor en la tupla

'''
print(f'el 3 sale {tupla.count(3)} veces en la tupla')
'''

# saber el index de un valor en la tupla, si el valor se repite, mostrara el index del primer valor que coincida

'''
print(f'el index de texto en la lista es: {tupla.index("texto")}')
'''

# convertir una lista en tupla

'''
lista = [2,4,"texto",99.9]
tupla = tuple(lista)
print(tupla)
'''

# Conjuntos
# son desorganizados (no tienen index, los elementos se agregan en orden aleatorio)

'''
conjunto = {5,2,3.6,"triqui"}
print(type(conjunto))
print(conjunto)
'''

# longitud de un conjunto

'''
print(len(conjunto))
'''

# ciclos en un conjunto

'''
for elemento in conjunto:
    print(elemento)
'''

# verificar con booleanos si un elemento existe en el conjunto

'''
print("triqui" in conjunto)
'''

# agregar elementos a un conjunto

'''
conjunto.add("naranja")
print(conjunto)
'''

# agregar los elementos de un conjunto a otro, los conjuntos no repiten elementos, solo muestran valores unicos

'''
frutas = {"pina","papaya","mango"}
otras_frutas = {"fresa","pera","manzana"}
frutas.update(otras_frutas)
print(frutas)
'''

# es posible agregar los valores de cualquier tipo de coleccion

'''
animales = {"lobo","gallina","pez"}
mas_animales = ("cerdo","puma")
animales.update(mas_animales)
print(animales)
'''

# Eliminar elementos de los conjuntos

'''
animales.remove("cerdo")
print(animales)

animales.discard("gallina")
print(animales)
'''

# la diferencia es que remove saca error si se intenta sacar un elemento que no existe

# sacar un elemento al azar del conjunto

'''
marcas_autos = {"mazda","alfa romeo","toyota","bmw"}
print(marcas_autos)
marcas_autos.pop()
print(marcas_autos)
'''

# es posible guardar el elemento extraido en una variable

'''
carro = marcas_autos.pop()
print(carro)
'''

# vaciar un conjunto

'''
marcas_autos.clear()
print(marcas_autos)
'''

# eliminar un conjunto

'''
print(marcas_autos)
del marcas_autos
print(marcas_autos)
'''

# las operaciones matematicas entre conjuntos funcionan 

# union

'''
conjunto1 = {2,10.3,4}
conjunto2 = {"hola","asd","conjunto",4,2}

conjunto3 = conjunto1.union(conjunto2)
print(conjunto3)
'''

# los valores repetidos en los conjuntos seran unicos en la union de estos

# interseccion

'''
conjunto3 = conjunto1.intersection(conjunto2)
print(conjunto3)
'''

# diferencia (los valores que existen en el conjunto indicado y que no existen en los demas)

'''
print(conjunto1.difference(conjunto2))
'''

# diferencia simetica (guarda los valores unicos entre ambos conjuntos)

'''
conjunto3 = conjunto1.symmetric_difference(conjunto2)
print(conjunto3)
'''

# el .copy tambien funciona en conjuntos

'''
conjunto3 = conjunto1.copy()
print(conjunto3)
'''

# Lambda

# Programacion funcional que nos sirve para realizar calculos de una manera mas rapido

'''
x = lambda a: a+10
print(x(5))

y = lambda a: 100 - a
print(y(9))

z = lambda a: 3**a+a
print(z(2))
'''

# Numpy
# Es una libreria de python para trabajar con arraysfd

'''
import numpy as np

arr = np.array([1,3,"asd",4])
print(arr)
print(type(arr))
'''

# arrays de varias dimensiones

'''
arr2d = np.array([1,6.2,"arr",[1.2,2,"2d"]])
print(type(arr2d))
print(arr2d)
print(arr2d[1])
print(arr2d[3][0]+arr2d[3][1])
'''

# Juego de triqui

# Para el desarrollo de este juego usaremos colecciones

# Pasos para su creacion

# 1. crear una funcion que dibuje el tablero
# 2. realizar una jugada
# 3. verificar si hay ganador 
# 4. jugar

# dibujar el tablero

# 1|2|3
# 4|5|6
# 7|8|9

# El jugador X o O puede ganar haciendo una linea con las casillas junto con sus reversos:

# 1,2,3
# 1,4,7
# 3,6,9
# 2,5,8
# 1,5,9
# 3,5,7

# El tablero se puede representar como una cadena de caracteres

'''
tablero = "|1|2|3|4|5|6|7|8|9|"
'''

# Si un jugador marca una casilla, esta cambia su valor por X o O 

# Como los strings son indexados, esto significa que podemos partir la cadena para asi obtener cada una de las 3 filas por separado 

# index de las casillas:
# de 0 a 2 (123)
# de 3 a 5 (456)
# de 6 a 8 (789)

# una vez tengamos las subcadenas, separaremos estas lineas de codigo independientes haciendo uso de \n

'''
fila1 = tablero[:7]
fila2 = tablero[6:13]
fila3 = tablero[12:]
tablero_lleno = f"{fila1}\n{fila2}\n{fila3}"
print(tablero_lleno)
'''

# Lo que necesitamos para que jueguen es una funcion que reciba como argumento la posicion que el jugador quiere marcar y reemplace el valor de la casilla en cuestion por ese valor recibido en el argumento

# Lo que quiere decir que cuando el programa identifique  que alguna de las lineas para ganar indicadas arriba han cambiado todos los valores de sus casillas por X o O, hay ganador

# El metodo .format es capaz de buscar llaves en strings para en su interior ubicar valores

'''
def renderizar_tablero(tablero):
    plantilla = "| {} | | {} | {} |"
    salto = "\n"
    bar = "---------------"
    a=plantilla.format(*tablero[:3])
    b=plantilla.format(*tablero[3:6])
    c=plantilla.format(*tablero[6:])

    t=salto.join([bar,a,bar,b,bar,c,bar])
    return print(t)
renderizar_tablero("123456789")
'''

# Haremos una funcion que debe validar que el valor recibido por los usuarios esta entre 1 y 9, reasignar el valor a de la casilla indicada con X o O, asi como validar si la casilla ya habia sido marcada

'''
def actualizar_movimiento(juego,jugada,jugador): 
    if not (jugada.isdigit() and int(jugada) in range(1,10)): 
        print(f'Jugada invalida "{jugada}", solo son validos numeros entre 1 y 9')
        return juego
    numero_jugada = int(jugada)
    if juego[numero_jugada - 1] in 'XO':
        print(f'La casilla "{jugada}" ya esta ocupada')
        return juego
    juego = juego[:numero_jugada-1]+jugador+juego[numero_jugada:]
    return print(juego)
actualizar_movimiento("123456789","7","X")

def encontrar_ganador(juego):
    ganadores = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))

    for jugador in ('X', 'O'):
        for i, j, k in  ganadores:
            linea = (juego[i], juego[j], juego[k])
            if linea == (jugador,jugador,jugador):
                return jugador
    return None
'''

# reto 3

l1=[(2001,'rosca', 'PT29872',2,45,'Luis Molero',3456,'12/06/2020'),
 (2010,'bujía', 'MS9512',4,15,'Carlos Rondon',1256,'12/06/2020'),
 (2010,'bujía', 'ER6523',9,36,'Pedro Montes',1243,'12/06/2020'),
 (3578,'tijera', 'QW8523',1,128,'Pedro Faria',1456,'12/06/2020'),
 (9251,'piñón', 'EN5698',2,8,'Juan Peña',565,'12/06/2020')]

l2=[(5489,'tornillo', 'RS8512',2,33,'Julio Perez',3654213,'13/06/2020'),
 (3215,'zocalo', 'UM8587',2,125,'Laura Macias',1256321,'13/06/2020'),
 (3698,'biela', 'PT3218',1,78,'Luis Peña',14565487,'13/06/2020'),
 (8795,'cilindro', 'AZ8794',2,96,'Carlos Casio',5612405,'13/06/2020')]

l3=[(9852,'Culata', 'XC9875',2,165,'Luis Molero',3455846,'14/06/2020'),
 (9852,'Culata', 'XC9875',2,165,'Jose Mejia',1355846,'14/06/2020'),
 (2564,'Cárter', 'PT29872',2,32,'Peter Cerezo',8545436,'14/06/2020'),
 (5412,'válvula', 'AZ8798',2,11,'Juan Peña',568975,'14/06/2020')]

def AutoPartes(ventas):
    dic={"l1": ventas}
    print(dic)
AutoPartes(l1) 

'''
def consultaRegistro(ventas, idProducto):
    respuesta = ""
    encontrado = False
    for t in ventas: 
        if t[0] == idProducto:
            respuesta += f'Producto consultado : {idProducto} Descripción {t[1]} #Parte {t[2]} Cantidad vendida {t[3]} Stock {t[4]} Comprador {t[5]} Documento {t[6]} Fecha Venta {t[7]}\n\n'
            encontrado = True
    if encontrado == True:
        return respuesta
    else: 
        return 'No hay registro de venta de ese producto'

print(consultaRegistro(l1,201054654156)) 
'''
 





 
    


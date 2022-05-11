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

import math as m
from operator import truediv

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


saludo = "assdaasd"
print(saludo)

a=5 
b=2
c=a+b
print(c)


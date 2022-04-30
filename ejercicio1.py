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


def gradosCaF():
    Celcius = float(input("ingrese los grados celcius: "))
    Fahrenheit = (Celcius*(9/5))+32
    print(Celcius,"grados Celcius equivalen a",Fahrenheit,"grados Fahrenheit")
gradosCaF()


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


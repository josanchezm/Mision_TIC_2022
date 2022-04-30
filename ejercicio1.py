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

# Fahrenheit a Celcius

'''
Fahrenheit = 50 

Celcius = (Fahrenheit-32)*(5/9) 

print(Fahrenheit,"grados Fahrenheit equivalen a",Celcius,"grados celcius")
'''

# Celcius a Fahrenheit

'''
Celcius = 10

Fahrenheit = (Celcius*(9/5))+32

print(Celcius,"grados celcius equivalen a",Fahrenheit,"grados Fahrenheit")
'''

# Funciones en Python

def gradosCaF(Fahrenheit):
    Celcius = (Fahrenheit-32)*(5/9)
    print(Fahrenheit,"grados Fahrenheit equivalen a",Celcius,"grados Celcius")
gradosCaF(10)

def gradosFaC(Celcius): 
    Fahrenheit = (Celcius*(9/5))+32
    print(Celcius,"grados Celcius equivalen a",Fahrenheit,"grados Fahrenheit")
gradosFaC(50)

ejercicio = 3%2/5-8*3*15+18/8*-5
print(ejercicio)



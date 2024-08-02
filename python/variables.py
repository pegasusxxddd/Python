# !------- TEXTO(STRING) -------!
# ? de una linea
#'hola'
#"hola" 
#?multiple linea
#'''
#hola 
#como 
#estas
#'''
#""" 
#hola
#como
#estas
#"""
#TODO| EJEMPLOS:
# print('hola')
# print("hola")
# print('''hola 
# como 
# estas
# ''')
# print(""" 
# hola
# como
# estas
# """)
# input(str(""))
# !------- END TEXTO -------!
#**------------------------------------**#
# !------- NUMEROS -------!

#? NUMERO ENTERO(INT): 1, 2,3,.....
#? NUMERO DECIMAL(FLOTANTE = FLOAT): 1.2,1.3,1.4,........
#? NUMERO COMPLEJOS
#TODO| EJEMPLOS:
# Numero_int = int(input("pon un numero entero: "))
# Numero_float = float(input("pon un numero flotante: "))
# NUMERO_COMPLEJOS = 1 + 1j + 2 + 3j
# print(NUMERO_COMPLEJOS)

#HAY MAS....(https://www.mclibre.org/consultar/python/lecciones/python-operaciones-matematicas.html)

# !------- END NUMEROS -------!
#**------------------------------------**#
# !------- BOOLEANOS -------!
#? FALSE
#? TRUE
#TODO| EJEMPLOS:
# a = True
# b = False

# print(a and b)
# print(a or b)
# !------- END BOOLEANOS -------!
#**------------------------------------**#
# !------- SET -------!

#? coleccion desordenada de valores unícos.
#TODO| EJEMPLOS:
#valores_unicos = {1,2,3,3,4,4,"XD","a","c"}

#print(set(valores_unicos))

# !------- END SET -------!
#**------------------------------------**#
# !------- LISTAS -------!

#? ES UNA COLECCION DE DATOS PERO MUTABLES
#TODO| EJEMPLOS:
# a = [1, "lista", 2,3]
# a[2] = "holanda"
# print(a)
# print(a[2])
# print(a)
# print(a[0])

# !------- END LISTAS -------!
#**------------------------------------**#
# !------- TUPLAS -------!

#? ES UNA COLECCION DE DATOS PERO INMUTABLES
#TODO| EJEMPLOS:
# a = (1,4,3)
# b = ("a", 1, "aea")

# print(a)
# print(a[0])
# print(len(a))

# !------- END TUPLAS -------!
#**------------------------------------**#
# !------- DICCIONARIOS -------!

#? ES UNA COLECCION DESORDENADA DE PARES  CLAVE-VALOR 
#! CLAVE: inmutable
#! VALOR: mutable

# a = {
#     1: "que",
#     2: "so",
#     "hola": "como estas"
# }
# print(a[1])
# print(a["hola"])


#TODO| EJEMPLOS:

# !------- END DICCIONARIOS -------!
print("PC: Cual es tu nombre:")

nombre = input(str("Tu: "))

saludo = "PC: Holaaa " + nombre + " como estas"
print(saludo)
print("PC: todo bien: ")

respuesta = input(str("Tu: "))

if respuesta == "si":
    print("PC: me alegro sigue asi de feliz :V")
if respuesta == "no":
    print("PC: hayyy espero que te mejores :V")

print(f"PC: Y {nombre} cuantos años tienes:")
edad = int(input("Tu:"))

if edad > 18:
    print("PC: eres mayor de edad XDD")
if edad < 18:
    print("PC: Ahhh eres menor *se va como tu papa*")
    
print("FINNN! echo por joseph")

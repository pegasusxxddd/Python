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

#? mutables: listas, sets, diccionarios...
#? inmutables: int, float, complex, string, tuplas...

# !------ proyecto final --------!

# print("PC: Cual es tu nombre:")

# nombre = input(str("Tu: "))

# saludo = "PC: Holaaa " + nombre + " como estas"
# print(saludo)

# print("-----------")

# print("PC: todo bien: ")

# respuesta = input(str("Tu: "))

# if respuesta == "si":
#     print("PC: me alegro sigue asi de feliz :V")
# if respuesta == "no":
#     print("PC: hayyy espero que te mejores :V")

# print("-----------")

# print(f"PC: Y {nombre} cuantos años tienes:")
# edad = int(input("Tu: "))

# if edad >= 18:
#     print("PC: eres mayor de edad XDD")
# else:
#     print("PC: Ahhh eres menor *se va como tu papa*")
#     print("PC: Na mentira")

# print("-----------")

# print("PC: Que te parece si me das numeros y hago algunas operaciones matematicas yaaa...!")
# print("PC: Dame el primer numero y despues el segundo numero")

# Primer_Numero = int(input("Primer Numero: "))
# Segundo_Numero = int(input("Segundo Numero: "))

# suma = Primer_Numero + Segundo_Numero
# resta = Primer_Numero - Segundo_Numero
# multiplicacion = Primer_Numero * Segundo_Numero
# divicion = Primer_Numero / Segundo_Numero
# elevecion = Primer_Numero ** Segundo_Numero

# print("----- AHI ESTA -----")
# print(f"""Suma: {suma},
# Resta: {resta},
# Multiplicacíon: {multiplicacion}
# Divicion: {divicion},
# Elevacion: {elevecion}""")
# print("--------------------")

# print("PC: Que te parece")
# parecer = str(input("Tu: "))
# print("PC: Ahhh bueno mejor pasemos a otro tema")
print("-----------")
lista_comidas = ["Ceviche", "Papa ala huancaina", "Lomo saltado", "Pizza con piña"]
print(lista_comidas)
print("PC: Cual de estas comidas te gusta?")
print("""--------------------
La:
0
1
2
3""")
print("-----------")
comida_gustar = int(input("Tu: "))
numero_de_comida_q_gusta = comida_gustar
if comida_gustar == "3":
    print("PC: Tu estas loco no? no me agas renegar")
else: 
    print("PC: Esos si son gustos tmr")

lista_comidas[numero_de_comida_q_gusta] = lista_comidas[numero_de_comida_q_gusta] + "(riquichichichimo!)"

print(lista_comidas)
print("PC: Y cual no te gusta?...")
print("""--------------------
La:
0
1
2
3""")
print("-----------")
comida_no_gustar = int(input("Tu: "))

del lista_comidas[comida_no_gustar]
print(lista_comidas)

if comida_no_gustar == 3:
    print("Gracias por eliminar esa porqueria")
else:
    print("ummm...")
    print("-----------")
    print(f"oye oye oyee..! que haces te aceptaba y te alababa que borraras la:")
    print(lista_comidas[3])
    


print("-----------")   
print("PC: Ahora dime que mes te gusta:")
meses = {
    "Enero": "Primer mes del año, conocido por ser el inicio del nuevo año.",
    "Febrero": "Segundo mes del año, el más corto, con 28 o 29 días en años bisiestos.",
    "Marzo": "Tercer mes del año, marca el inicio de la primavera en el hemisferio norte.",
    "Abril": "Cuarto mes del año, conocido por sus lluvias primaverales.",
    "Mayo": "Quinto mes del año, a menudo asociado con la celebración del Día del Trabajador.",
    "Junio": "Fueraa gay...",
    "Julio": "Séptimo mes del año, conocido por su clima cálido y vacaciones de verano.",
    "Agosto": "Octavo mes del año, suele ser el mes más cálido en muchos lugares.",
    "Septiembre": "Noveno mes del año, inicio del otoño en el hemisferio norte.",
    "Octubre": "Décimo mes del año, conocido por el Halloween y el inicio de la temporada de cosechas.",
    "Noviembre": "Undécimo mes del año, asociado con el Día de Acción de Gracias en algunos países.",
    "Diciembre": "Duodécimo mes del año, marca el final del año y está asociado con las festividades navideñas."
}

numero_inicial = 1
for mes, significado in meses.items():
    print(f"{numero_inicial}.-{mes}")
    numero_inicial += 1
print("-----------")

mes_que_gusta = int(input("Tu: "))

if mes_que_gusta == 6:
    print(meses["Junio"])
else:
    print("fuup.. que bueno!")
print("-----------")
print("FINNN!")
print("---Made By Joseph---")

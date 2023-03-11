print("'-----------------------------------------------------------------------------'")
#Práctica estructura de control IF, captura desde teclado de variables y tipos de datos.
#primer inciso
#Realizar multiplicación con 3 variables
print("multiplicación")
multiEntero = int(input("Escribe el primer número: "))
multiEntero2 = int(input("Escribe el segundo número: "))
multiEntero3 = int(input("Escribe el tercer número: "))

resMultip = multiEntero * multiEntero2 * multiEntero3
print("Resultado de la multiplicación es: ", resMultip)

print("'-----------------------------------------------------------------------------'")
#Realizar división con 2 variables
print("división")
divEntera = int(input("Escribe el primer número: "))
divEntera2 = int(input("Escribe el segundo número: "))

resDivisión = divEntera // divEntera2
print("El resultado de la división es: ", resDivisión)

print("'-----------------------------------------------------------------------------'")
#sumar los numero multiplicados y divididos en una variable de resultado

resultados = resMultip + resDivisión
print("El resultado de la suma de la multiplicación y la división es: ", resultados)

print("'-----------------------------------------------------------------------------'")
print("Realizar inciso de float")
#Realizar exponencial con 2 variables
print("Exponente")
numExpo1 = float(input("Escribe el primer número: "))
numExpo2 = float(input("Escribe el segundo número: "))
resExpo = numExpo1 ** numExpo2
print("El resultado del exponente es: ", resExpo)

print("'-----------------------------------------------------------------------------'")
#Realizar modulo con 2 variables
print("Modulo")
numModu1 = float(input("Escribe el primer número: "))
numModu2 = float(input("Escribe el segundo número: "))
resModu = numModu1 % numModu2
print("El resultado del modulo es: ", resModu)

print("'-----------------------------------------------------------------------------'")
#restarlos en una variable de resulatados
resultados2 = resExpo - resModu
print("El resultado de la resta del exponente y el modulo es: ", resultados2)

print("'-----------------------------------------------------------------------------'")
#dividirlo entre el resultado de la suma
resultado = resultados / resultados2
print("El resultado de la división entre la resta y la suma es: ", resultado)

print("-----------------------------------------------------------------------------")

print("Realizar inciso de 'Complex'")
#Definir 4 variables complejos distintas.
numComplex1 = complex(2 + 3j)
numComplex2 = complex(7 + 12j)
numComplex3 = complex(5 + 24j)
numComplex4 = complex(20 + 2j)

print("Las variables definidas con Complex son:", numComplex1, numComplex2, numComplex3, numComplex4)

print("--------------------------------------------------------------------------------")

#Con el Carácter (String). Defina variables según número integrantes. En la variable debe almacenar el nombre de una fruta por variable.

integrante1fruta= str("Manzana")
integrante2fruta = str("Mango")
integrante3fruta = str("Sandía")
integrante4fruta = str("Papaya")
integrante5fruta = str("Melocotón")


print("-------------------------------------------------------------------------------")
print("Realizar inciso de los boleanos")
# Identificando Booleano (Bool). Se realizará en la estructura de control IF. 
# Ingresar datos desde teclado, preguntar digitar un nombre de una fruta y capturar ese dato en una variable.

integrante1Name = "Antony Eleazar Tobías Beltrán"
integrante2Name = "Andrea Alexandra Núñez Morán"
integrante3Name = "Kevin Francisco Menjivar Calderón"
integrante4Name = "Mauricio Imanol García Romero"
integrante5Name = "Franklin Geovany Gómez Valle"
# Estructura de control IF. Cada estructura definida es separada de la otra no agrupar o tratar de hacer una sola estructura de control.
#Diseñar una sentencia IF por cada fruta. Al evaluar la expresión de cada IF si la respuesta es verdadera, deberá mostrar el nombre de la fruta, nombre de un compañero.

print("frutas a escribir:", integrante1fruta +"," + integrante2fruta + ",",integrante3fruta + ",", integrante4fruta + "y", integrante5fruta)

fruta = input("Escribir nombre de fruta: ")


if fruta == "Manzana":
    print(True,"el tipo de clase es", type(True))
    print("La fruta de", integrante1Name, "es: ", integrante1fruta)

if fruta == "Mango":
    print(True, "el tipo de clase es", type(True))
    print("La fruta de", integrante2Name, "es: ", integrante2fruta)

if fruta == "Sandía":
    print(True, "el tipo de clase es", type(True))
    print("La fruta de", integrante3Name, "es: ", integrante3fruta)

if fruta == "Papaya":
    print(True,"el tipo de clase es", type(True))
    print("La fruta de", integrante4Name, "es: ", integrante4fruta)

if fruta == "Melocotón":
    print(True,"el tipo de clase es", type(True))
    print("La fruta de", integrante5Name, "es: ", integrante5fruta)


print("fin de if")
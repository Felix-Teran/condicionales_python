#!/usr/bin/env python
'''
Condicionales [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"


def ej1():
    # Ejercicios de práctica numérica

    # Comparadores
    # Ingrese dos números cualesquiera y realice las sigueintes
    # comparaciones entre ellos
    numero_1 = int(input('Ingrese el primer número:\n'))

    numero_2 = int(input('Ingrese el segundo número:\n'))

    # Compare cual de los dos números es mayor
    # Imprima en pantalla según corresponda

    if numero_1 > numero_2:
        print(numero_1, "es mayor que", numero_2)
    elif numero_1 < numero_2:
        print(numero_2, "es mayor que", numero_1)
    else:
        print(numero_1, "y", numero_2, "son iguales")

    # Verifique si el numero_1 positivo, negativo o cero
    # Imprima el resultado en cada caso

    if numero_1 > 0:
        print("El primer número es positivo")
    elif numero_1 < 0:
        print("El primer número es negativo")
    else:
        print("El primer número es cero")

    # Verifique si el numero_1 es mayor a 0 y menor a 100
    # Imprima en pantalla si se cumple o no la condición

    if numero_1 > 0 and numero_1 < 100:
        print("Se cumple la condición")
    else:
        print("No se cumple la condición")

    # Verifique si el numero_1 es menor a 10 o el numero_2
    # es mayor a -2
    # Imprima en pantalla si se cumple o no la condición

    if numero_1 < 10 or numero_2 > -2:
        print("Se cumple la condición")
    else:
        print("No se cumple la condición")


def ej2():
    # Ejemplos variables de texto

    # Comparadores
    # Ingrese dos palabras cualesquiera y realice las sigueintes
    # comparaciones entre ellas
    texto_1 = str(input('Ingrese la primera palabra:\n'))

    texto_2 = str(input('Ingrese la segunda palabra:\n'))

    # Compare cual de las dos palabras es mayor (alfabéticamente)
    # Imprima en pantalla según corresponda

    if texto_1 > texto_2:
        print("La palabra", texto_1.upper(), "es mayor alfabéticamente")
    elif texto_1 < texto_2:
        print("La palabra", texto_2.upper(), "es mayor alfabéticamente")
    else:
        print("Ambas palabras son iguales")

    # Compare cual de las dos palabras tiene mayor
    # cantidad de letras
    # Imprima en pantalla según corresponda

    if len(texto_1) > len(texto_2):
        print("{} tiene mayor cantidad de letras que {}" .format(texto_1.upper(),
                                                                 texto_2.upper()))
    elif len(texto_1) < len(texto_2):
        print("{} tiene mayor cantidad de letras que {}" .format(texto_2.upper(),
                                                                 texto_1.upper()))
    else:
        print("Ambas palabras tienen la misma cantidad de letras")

    # Verifique si la primera letra de la primera palabra
    # es mayor a la primera letra de la segunda palabra
    # Imprima en pantalla según corresponda

    if texto_1[:1] > texto_2[:1]:
        print("La 1ra letra de la palabra {} es mayor que de la palabra {}" .format(texto_1.upper(),
                                                                                    texto_2.upper()))
    elif texto_1[:1] < texto_2[:1]:
        print("La 1ra letra de la palabra {} es mayor que de la palabra {}" .format(texto_2.upper(),
                                                                                    texto_1.upper()))
    else:
        print("Las primeras letras de ambas palabras son iguales")

    copia_texto_1 = texto_1  # Copia de la variable texto_1

    # Verifique que copia_texto_1 es igual a texto_1
    # Imprima en pantalla según corresponda

    if copia_texto_1 == texto_1:
        print("La copia concuerda con la palabra original")
    else:
        print("La copia NO concuerda")

    # Verifique que copia_texto_1 es distinta a texto_2
    # Imprima en pantalla según corresponda

    if copia_texto_1 != texto_2:
        print("Esta copia NO pertenece a la segunda palabra")
    else:
        print("La copia concuerda con la segunda palabra")


def ej3():
    # Ejercicios de práctica numérica

    # Condicionales anidados
    numero_1 = 7
    numero_2 = -2

    # Verifique si el numero_1 es mayor a 5

    if numero_1 > 5:

        #   --> En caso afirmativo, verifique si el numero_2
        #       es positivo

        if numero_2 > 0:
    #       --> En caso afirmativo imprima en pantalla "Resp=1"
            print("Resp=1")
    #       --> En caso negativo imprima en pantalla   "Resp=2"
        else:
            print("Resp=2")

    #  --> En caso negativo (numero_1 no es mayor a 5)
    #      verifique si el numero_2 es mayor a 5
    else:
        
        if numero_2 > 5:
    #       --> En caso afirmativo imprima en pantalla "Resp=3"
            print("Resp=3")
    #       --> En caso negativo imprima en pantalla "Resp=4"
        else:
            print("Resp=4")

    # Verifique la calificación de un estudiante según su
    # puntaje en un examen

    puntaje = 70

    # Si el puntaje es mayor igual a 90 --> imprimir A
    if puntaje >= 90:
        print ("A")
    # Si el puntaje es mayor igual a 80 --> imprimir B
    elif puntaje >= 80:
        print("B")
    # Si el puntaje es mayor igual a 70 --> imprimir C
    elif puntaje >=70:
        print("C")
    # Si el puntaje es mayor igual a 60 --> imprimir D
    elif puntaje >=60:
        print("D")
    # Si el puntaje es manor a  60      --> imprimir F
    else:
        print("F")

    # Debe imprimir en pantalla la calificacion
    # Utilizar "if" anidados


def ej4():
    # Ejemplos variables de texto

    texto_1 = '5'
    texto_2 = '7'

    # Verifique cual cual de los dos textos es mayor alfabéticamente
    # Imprima en pantalla según corresponda

    if texto_1 > texto_2:
        print("{} es mayor alfabeticamente que {}" .format(texto_1,texto_2))
    else:
        print("{} es mayor alfabeticamente que {}" .format(texto_2,texto_1))

    # Transforma esas variables tipo texto y almacénalas
    # en nuevas variables númericas (int)

    num_1 = int(texto_1)
    num_2 = int(texto_2)

    # Repita el proceso, ¿Cuál de las nuevas variables es mayor?
    # Imprima en pantalla según corresponda

    if num_1 > num_2:
        print("{} es mayor que {}" .format(num_1,num_2))
    else:
        print("{} es mayor que {}" .format(num_2,num_1))

    # Para pensar!
    # ¿Por qué cree que texto_2 es mayor a texto_1?
    # Siendo números tiene sentido, pero son caracteres, texto,
    # aún así el operador arroja el mismo resultado que con las
    # variables numéricas, cierto? ¿Por qué creen que es así?
    # Esta pregunta estará repetida en el Campus para que puedan
    # responder.
    # NOTA: La respuesta no se encuentra en el apunte, sino en Google ;)


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    #ej1()
    #ej2()
    #ej3()
    #ej4()

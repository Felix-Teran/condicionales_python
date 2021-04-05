#!/usr/bin/env python
"""
Condicionales [Python]
Ejercicios de profundización
---------------------------
Autor: Inove Coding School
Version: 1.3

Descripcion:
Programa creado para que practiquen los conocimietos adquiridos durante la semana
"""

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.3"


def ej1():
    print("Ejercicios de práctica con números")

    """
    Realice un programa que solicite por consola 2 números
    Calcule la diferencia entre ellos e informe por pantalla
    si el resultado es positivo, negativo o cero.
    """
    numero_1 = int(input("Ingrese el primer número" "\n"))
    numero_2 = int(input("Ingrese el segundo número" "\n"))
    resta = numero_1 - numero_2

    if resta > 0:
        print("El resultado es positivo")
    elif resta < 0:
        print("El resultado es negativo")
    else:
        print("El resultado es cero")
    


def ej2():
    print("Ejercicios de práctica con números")

    """
    Realice un programa que solicite el ingreso de tres números
    enteros, y luego en cada caso informe si el número es par
    o impar.
    Para cada caso imprimir el operation en pantalla.
    """
    numero_1 = int(input("Ingrese el primer número" "\n"))
    numero_2 = int(input("Ingrese el segundo número" "\n"))
    numero_3 = int(input("Ingrese el tercer número" "\n"))
    

    lista_num = [ numero_1, numero_2, numero_3 ]

    for i in lista_num:
        if i % 2 == 0:
            print("El número", i, "es par")
        else:
            print("El número", i, "es impar")


def ej3():
    print("Ejercicios de práctica con números")

    """
    Realice una calculadora, se ingresará por línea de comando dos números
    Luego se ingresará como tercera entrada al programa el símbolo de la operación
    que se daesea ejecutr
    - Suma (+)
    - Resta (-)
    - Multiplicación (*)
    - División (/)
    - Exponente/Potencia (**)

    Se debe efectuar el cálculo correcto según la operación ingresada por consola
    Imprimir en pantalla la operación realizada y el resultado
    """
    numero_1 = float(input("Ingrese el primer número" "\n"))
    numero_2 = float(input("Ingrese el segundo número" "\n"))
    operator = str(input("Ingrese el símbolo del operador matemático" "\n"
                             "- Para Suma (+)" "\n"
                             "- Para Resta (-)" "\n"
                             "- Para Multiplicación (*)" "\n"
                             "- Para División (/)" "\n"
                             "- Para Exponente/Potencia (**)" "\n"))

    list_operator = [ "+", "-", "*", "/", "**"]

    while operator not in list_operator:
        print("Operador Incorrecto")
        operator = str(input("Ingrese el símbolo del operador matemático" "\n"
                             "- Para Suma (+)" "\n"
                             "- Para Resta (-)" "\n"
                             "- Para Multiplicación (*)" "\n"
                             "- Para División (/)" "\n"
                             "- Para Exponente/Potencia (**)" "\n"))

    if operator == "+":
            operation = numero_1 + numero_2
            print(" El resultado de {} {} {} es {}".format(numero_1, operator, numero_2, operation))
           
    elif operator == "-":
            operation = numero_1 - numero_2
            print(" El resultado de {} {} {} es {}".format(numero_1, operator, numero_2, operation))

    elif operator == "*":
            operation = numero_1 * numero_2
            print(" El resultado de {} {} {} es {}".format(numero_1, operator, numero_2, operation))

    elif operator == "/":
            operation = numero_1 / numero_2
            print(" El resultado de {} {} {} es {}".format(numero_1, operator, numero_2, operation))

    elif operator == "**":
            operation = numero_1 ** numero_2
            print("{} elevado a {} es {}".format(numero_1, numero_2, operation))

def ej4():
    print("Ejercicios de práctica con cadenas")

    """
    Realice un programa que solicite por consola 3 palabras cualesquiera
    Luego el programa debe consultar al usuario como quiere ordenar las palabras
    1 - Ordenar por orden alfabético (usando el i ">")
    2 - Ordenar por cantidad de letras (longitud de la palabra)

    Si se ingresa "1" por consola se deben ordenar las 3 palabras por orden alfabético
    e imprimir en pantalla de la mayor a la menor

    Si se ingresa "2" por consola se deben ordenar las 3 palabras por cantidad de letras
    e imprimir en pantalla de la mayor a la menor
    """

    palabra_1 = str(input("Ingrese una palabra" "\n"))
    palabra_2 = str(input("Ingrese una 2da palabra" "\n"))
    palabra_3 = str(input("Ingrese una 3ra palabra" "\n"))
    orden = int(input("Cómo quieres ordenar las palabras? Seleccione un número" "\n"
                      "1 - Ordenar por orden alfabético" "\n"
                      "2 - Ordenar por cantidad de letras (longitud de la palabra)" "\n"))
    orden_list = [palabra_1, palabra_2, palabra_3]

    while orden > 2 or orden <= 0:
        print("Opción incorrecta")
        orden = int(input("Cómo quieres ordenar las palabras?" "\n"
                      "1 - Ordenar por orden alfabético" "\n"
                      "2 - Ordenar por cantidad de letras (longitud de la palabra)" "\n"))
    if orden == 1:
        orden_list.sort(reverse=True)
        orden_list = " > ".join(orden_list)
        print(orden_list.title())

    elif orden == 2:
        orden_list.sort(key=len, reverse=True)
        orden_list = " > ".join(orden_list)
        print(orden_list.title())

def ej5():
    print("Ejercicios de práctica con números")

    """
    Realice un programa que solicite ingresar tres valores de temperatura
    De las temperaturas ingresadas por consola determinar:
    1 - ¿Cuáles de ellas es la máxima temperatura ingresada?
    2 - ¿Cuáles de ellas es la mínima temperatura ingresada?
    3 - ¿Cuál es el promedio de las temperaturas ingresadas?

    En cada caso imprimir en pantalla el resultado
    """
    temp_1 = float(input("Ingrese una temperatura" "\n"))
    temp_2 = float(input("Ingrese una 2da temperatura" "\n"))
    temp_3 = float(input("Ingrese una 3ra temperatura" "\n"))

    temp_prom = (temp_1 + temp_2 + temp_3)/3

    temp_list = [temp_1, temp_2, temp_3]
    temp_list.sort()
    
    print("La máxima temperatura ingresada es", temp_list[2], "\n"
          "La mínima temperatura ingresada es", temp_list[0], "\n"
          "El promedio de las temperaturas ingresadas es", temp_prom)



if __name__ == "__main__":
    print("Ejercicios de práctica")
    ej1()
    ej2()
    ej3()
    ej4()
    ej5()

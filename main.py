import time  # Importamos la librería time para los espacios de tiempo
import random # Importamos la librería para los puntajes aleatorios


iniciar_trivia = True  # Iniciamos la variable en True
# variables que almacenarán el número de veces que el usuario intenta nuestra trivia.
intentos = 0
puntaje = 0

# Mostrar el texto de bienvenida para quien juegue tu trivia
print("Bienvenido a mi trivia sobre la Programación")
print("Pondremos a prueba tus conocimientos")
print("Tienes", puntaje, "puntos")

while iniciar_trivia == True:  # Mientras iniciar_trivia sea True, repite:
    intentos += 1
    puntaje = random.randint(0, 10)

    print("\nIntento número:", intentos)
    input("Presiona Enter para continuar")
    time.sleep(1)  # para ayudarnos a imaginar que vamos jugando
    print("Jugando...")
    time.sleep(1)
    nombre = input("Ingresa tu nombre: ")
    for numero_carga in range(5, 0, -1):# cuenta regresiva de 5 segundos
      print(numero_carga)
      time.sleep(1)
    print("\n Hola", nombre, "responde las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Enter' para enviar tu respuesta:\n")

    # Pregunta 1
    print("1) ¿Quién creó Python?")
    # lista de la pregunta uno
    preg_uno = ["a) Guido van Rossum", "b) Larry Wall",
                "c) Yukihiro Matsumoto", "d) Rasmus Lerdoff", "e) Sun Microsystems"]
    # ciclo for recorre e imprime la lista uno
    for i in range(0, 5):
        print(preg_uno[i])
    # buble que recorre una lista de alternativas clave
    respuesta_1 = input("\nTu respuesta: ")
    while respuesta_1 not in ("a", "b", "c", "d", "e"):
        respuesta_1 = input(
            "Debes responder a, b, c d o e. Ingresa nuevamente tu respuesta: ")
    # Ahora, verificamos su respuesta para mandar un mensaje de acierto o de error
    if respuesta_1 == "a":
        puntaje += 10
        print("Muy bien", nombre, "!")
    else:
        print("Incorrecto", nombre, "!")

    input("Presiona Enter para continuar")
    print(nombre, "llevas", puntaje, "puntos")
    time.sleep(1)

    # Pregunta 2
    print("\n1) ¿Cual de estos lenguajes de programación es de más bajo nivel?")
    preg_dos = ["a) Python", "b) Java",
                "c) PHP", "d) Assembly"]
    for ii in range(0, 4):
        print(preg_dos[ii])
    respuesta_2 = input("\nTu respuesta: ")

    while respuesta_2 not in ("a", "b", "c", "d"):
        respuesta_2 = input(
            "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")

    # Ahora, verificamos su respuesta para mandar un mensaje de acierto o de error
    if respuesta_2 == "a":
        print("Incorrecto!", nombre, "Python es un lenguaje de alto nivel")
    elif respuesta_2 == "b":
        print("Incorrecto!", nombre, "Java es un lenguaje de alto nivel")
    elif respuesta_2 == "c":
        print("Incorrecto!", nombre, "PHP es un lenguaje de alto nivel")
    else:
        puntaje += 10
        print("Muy bien", nombre, "!")

    input("Presiona Enter para continuar")
    print(nombre, "llevas", puntaje, "puntos")
    time.sleep(1)

    # Pregunta 3
    print("\n1) ¿Qué hace el intérprete?")
    preg_tres = ["a) Encuentra el error.", "b) Encuentra el error y termina su trabajo.",
                 "c) Lee el código fuente de abajo hacia arriba.", "d) Lee el código fuente de arriba hacia abajo."]
    for iii in range(0, 4):
        print(preg_tres[iii])

    # Almacenamos la respuesta del usuario en la variable "respuesta_3"
    respuesta_3 = input("\nTu respuesta: ")

    while respuesta_3 not in ("a", "b", "c", "d"):
        respuesta_3 = input(
            "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")

    if respuesta_3 == "a":
        print("Totalmente incorrecto! ...")
        puntaje = puntaje / 2
    elif respuesta_3 == "d":
        print("...")
        puntaje = puntaje + 5
    elif respuesta_3 == "c":
        print("Incorrecto! ...")
        puntaje = puntaje - 5
    else:
        print("Correcto! ...")
        puntaje = puntaje * 2
    input("Presiona Enter para continuar")
    print("Excelente, has obtenido", puntaje, "puntos")
    #Carga de 10 segundos de finanlizacion
    for numero_carga in range(10, 0, -1):
        print(numero_carga)
        time.sleep(1)

    print("\n¿Deseas intentar la trivia nuevamente?")
    repetir_trivia = input(
        "Ingresa 'si' para repetir, o cualquier tecla para finalizar: ").lower()

    if repetir_trivia != "si":  # != significa "distinto"
        print("\nEspero {nombre} que lo hayas pasado bien, hasta pronto!")
        # Cambiamos el valor de iniciar_trivia a False para evitar que se repita.
        iniciar_trivia = False

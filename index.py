import random
# Juego de adivinar el número:

# 1. El juego comienza pidiendo al usuario su nombre.
# 2. Luego muestra un mensaje explicando las reglas: el jugador debe adivinar un número entre 0 y 100.
# 3. El jugador tiene un total de 8 intentos para adivinar el número secreto.
# 4. Por cada intento, el programa validará la entrada del jugador y responderá:
#    - Si el número está fuera del rango (menor que 1 o mayor que 100), mostrará un mensaje de error y pedirá otro número.
#    - Si el número es menor que el número secreto, informará que el número es demasiado bajo.
#    - Si el número es mayor que el número secreto, informará que el número es demasiado alto.
#    - Si el número es correcto, felicitará al jugador e indicará en cuántos intentos lo logró.
# 5. El juego termina si el jugador adivina el número o si se agotan los 8 intentos.

nombre = input ("cual es tu nombre?:")
reglas = "el jugador debe adivinar un número entre 0 y 100 , tiene 8 intentos, si no esta en el rango sera fin del juego."
numeroAleatorio = random.randint(0,100)

print(f"Hola {nombre}, las reglas del juego son {reglas}")
for i in range(1, 9):
    try:
        numeroEntrada =int(input(f"este es tu intento nº{i}, dame el numero:"))
    except ValueError:
        print("no es numero, no puedes jugar")
        break
    if i == 9:
        print("has llegado al limite de intentos, prueba mas suerte a la proxima")
        print(f"el numero correcto era {numeroAleatorio}")
        break
    if numeroEntrada < 0 or numeroEntrada > 100:
        print("no es un valor valido para el juego, inclumple las normas, fin del juego")
        break
    if numeroEntrada < numeroAleatorio and numeroEntrada > 0:
        print("el numero es bajo")
    if numeroEntrada > numeroAleatorio and numeroEntrada < 100:
        print("el numero es alto")
    if numeroAleatorio == numeroEntrada:
        print("enhorabuena has acertado el numero")
        print(f"NUMERO CORRECTO {numeroEntrada}")
        break
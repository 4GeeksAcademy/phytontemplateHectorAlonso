import random

# Juego del ahorcado:

# 1. Generar una lista de palabras 
# 2. La aplicacion eligira una palabra alazar 
# 3. Enseñar la cantidad de palabras que tiene la palabra secreta
# 4. Crear una funcion que nos pida una letra. 
# 5. Validar la letra y ensañar todas las que coinciden con la palabra secreta
# 6. Con cada fallo se nos restara una vida
# 7. La cantidad de vidas es de 6
# 6. El juego termina cuando el usuario haya colocado todas las letras que tiene la palabra secreta

listaPalabras =["sol", "luz", "mariposa", "tierra", "montaña", "rio", "lluvia", "viento", "fuego", "cielo"]
numeroAleatorio =  random.randint(0, len(listaPalabras)-1)
palabraAleatoria = listaPalabras[numeroAleatorio]
aciertos = []
vidas = 6

print(f"\nla palabra oculta tiene {len(palabraAleatoria)} letras")
while vidas > 0 :
    prueba = input("tu letra es:\n")
    if prueba in palabraAleatoria:
        if prueba in aciertos:
            print("ya se ha usado")
            vidas = vidas-1
        else:
            print("correcto")
            for _ in range(palabraAleatoria.count(prueba)):
                aciertos.append(prueba)   
    else:
        print("esa letra no se encuentra en el juego, sigue intentando")
        vidas = vidas-1
        print(f"todavia tienes {vidas} vidas")


    letrasRestantes = len(palabraAleatoria)-len(aciertos)
    print(f"las letras correctas son {aciertos} el total de letras son {len(palabraAleatoria)}, aun faltan {letrasRestantes}")
    print(f"todavia tienes {vidas} vidas")
    if len(aciertos) == len(palabraAleatoria):
        print(f"CORRECTO, has ganado, la palabra es {palabraAleatoria}")
        break
if vidas == 0:
    print(" te has quedado sin vidas\n ******GAME OVER******")
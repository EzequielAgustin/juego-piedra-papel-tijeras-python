# Desafío
# Se puede colocar el nombre en la segunda solicitud
# Lo ingresado por el usuario sea lowerCase de tal forma de comparar minúscula con minúscula
# Más de 1 turno con el bucle while


nombre1 = input("¿Cómo se llamará el jugador 1?")
nombre2 = input("¿Cómo se llamará el jugador 2?")

jugador1 = input("¡Hola Jugador1! ¿Qué elegís? ¿Piedra, papel o tijeras?: ")
jugador2 = input("¡Hola Jugador2! ¿Qué elegís? ¿Piedra, papel o tijeras?: ")

condicion1 = jugador1 == "piedra" and jugador2 == "tijeras"
condicion2 = jugador1 == "papel" and jugador2 == "piedra"
condicion3 = jugador1 == "tijeras" and jugador2 == "papel"


if jugador1 == jugador2:
    print("Empate!")
elif condicion1 or condicion2 or condicion3: 
    print("Ganó: ",nombre1)
else:
    print("Ganó: ",nombre2)


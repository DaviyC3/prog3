import random
print('====================================')
print('Bienvenido al juego de la adivinanza')
print('====================================')

numero_secreto = random.randrange(1, 101)

print('Seleccione el nivel de dificultad')
print('(1) Facil (2) Medio (2) Dificil')

nivel = int(input('Ingrese nivel de dificultad '))

# Establecer nivel

if (nivel == 1):
  total_intentos = 20
elif (nivel == 2):
  total_intentos = 10
else:
  total_intentos = 5

print('Numero secreto= ', numero_secreto)

for iteracion in range(1, total_intentos + 1):
  print('Intento: {} de {} '.format(iteracion, total_intentos))
  entrada = input('ngresar un numero entre 1 y 100 ')
  entrada = int(entrada)
  print('Digitaste...', entrada)
  if(entrada<1 or entrada>100):
    print('Ingresar un numero entre 1 y 100')
    continue

  # Pone si es booleano o no

  acertaste = entrada == numero_secreto  #iguales
  mayor = entrada > numero_secreto      # Si es mayor
  menor = entrada < numero_secreto      # Si es menor

  if(acertaste):
    print('Felicidades!... Adivinaste el numero')
    break
  elif(mayor):
    print('Lo siento... el numero que ingresaste es mayor')
  else:
    print('Lo siento... el numero que ingresaste es menor')

  iteracion += 1;


print('Fin del juego')
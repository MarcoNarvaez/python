import random

print('Hola, cual es tu nombre?')
nombre = input()
print('Bueno, ' + nombre + ', Estoy pensando en un numero entre el 1 y el 20')
NumeroSecreto = random.randint(1, 20)

for invitacion in range(1, 7):
    print('Elige un numero')
    invitado = int(input())

    if invitado < NumeroSecreto:
        print('Tu numero es muy bajo')
    elif invitado > NumeroSecreto:
        print('Tu numero es muy alto ')
    else:
        break #Numero correcto

if invitado == NumeroSecreto:
    print('Buen trabajo! ' + nombre + ' adivinaste el numero en ' + str(invitacion) + ' intentos')
else:
    print('Nope, el numero que estaba pensando es: ' + str(NumeroSecreto))
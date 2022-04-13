import random

print('Hola, cual es tu nombre?')
name = input()
NumeroSecreto = random.randint(1, 20)
print('Bueno, ' + name + ', Estoy pensando en un numero entre el 1 y el 20')

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
    print('Buen trabajo ' + name + 'Adivinaste el numero')
else:
    print('Nope, el numero que estaba pensando es: ' + str(NumeroSecreto))
import random

def jugar():
    usuario = input("Escoge una opcion: 'pi' para piedra, 'pa' para papel, 'ti' para tijera.\n").lower()
    computadora = random.choice(['pi','pa','ti'])
    
    if usuario == computadora:
        return 'Empate!'
    
    if ganador(usuario, computadora):
        return 'Ganaste!'
    
    return 'Perdiste'


def ganador(jugador, oponente):
    #Retorna true si gana el jugador
    #Piedra gana a tijera (pi > ti)
    #Papel gana a piedra (pa > pi)
    #Tijera gana a papel (ti > pa)
    if ((jugador == 'pi' and oponente == 'ti')
        or (jugador == 'pa' and oponente == 'pi')
        or (jugador == 'ti' and oponente == 'pa')):
        return True
    else:
        return False    

    
print(jugar())
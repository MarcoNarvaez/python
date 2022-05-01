import random
import string
from palabras import palabras
from ahorcado_diagrama import vidas_diccionario_visual

def obtener_palabra(lista_palabras):
    #seleccionar palabra al azar de la lista
    palabra = random.choice(lista_palabras)
    
    while '-' in palabra or ' ' in palabra:
        palabra = random.choice(palabras)
        
    return palabra.upper()

def ahorcado():
    print('Bienvenido al juego del Ahorcado')
    
    palabra = obtener_palabra(palabras)
    
    letras_por_adivinar = set(palabra)
    letras_adivinadas = set()
    abecedario = set(string.ascii_uppercase)
    
    vidas = 7
    
    while len(letras_por_adivinar) > 0 and vidas > 0:
        print(f"Te quedan {vidas} vidas y has usado estas letras: {' '.join(letras_adivinadas)}")
        
        #Mostrar el estado actual de la palabra
        palabra_lista = [letra if letra in letras_adivinadas else '-' for letra in palabra]
        #Mostrar estado del ahorcado
        print(vidas_diccionario_visual[vidas])
        #Mostrar las letras sepaaradas por un espacio
        print(f"Palabra: {' '.join(palabra_lista)}")
        
        letra_usuario = input("Escoge una letra: ").upper()
        
        #Si la letra escogida por el usuario esta en el abcedario y no esta en el conjunto de letras que ha sen ingresado se añade la letra al conjunto de letras ingresadas
        if letra_usuario in abecedario - letras_adivinadas:
            letras_adivinadas.add(letra_usuario)
            
            #Si letra esta en la palabra, quitar la letra del conunto de letras pendientes por adivinar, si no esta, quitar una vida al usuario
            if letra_usuario in letras_por_adivinar:
                letras_por_adivinar.remove(letra_usuario)
                print('')
            else:
                vidas -= 1
                print(f"\nTu letra, {letra_usuario} no esta en la palabra")
        #Si la letra escogida por el usuario  ya fue ingreseda
        elif letra_usuario in letras_adivinadas:
            print("\nYa escogiste esa letra. Escoge una letra nueva, por favor")
        else:
            print("\nEsta letra no es valida")   
                     
    #El juego llega a esta linea cuando se adivina todas las letras de la palabra o cuando se agotan las vidas
    
    if vidas == 0:
        print(vidas_diccionario_visual[vidas])
        print(f"\n¡Ahorcado! La palabra era: {palabra}")
    else:
        print(f"¡Excelente! Adivinaste la palabra {palabra}! ")
        
ahorcado()
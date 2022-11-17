import random

letras = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numeros = '0123456789'
simbolos = '~!@#$%^&*()_+}{"'

unir = f'{letras}{numeros}{simbolos}'
longitud = 10

clave = random.sample(unir, longitud)

password_final = ''.join(clave)

print(password_final)
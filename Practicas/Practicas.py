# alto = int(input())
# ancho = int(input())

# print('Proporciona el alto:', alto)
# print('Proporciona el ancho:', ancho)

# area = alto * ancho
# perimetro = (alto + ancho) * 2

# print('area:', area)
# print('perimetro: ', perimetro)

# adulto = 18
# persona = input()

# if persona >= adulto:
#     print('mayor')
# else:
#     print('menor')


# from math import factorial


# usuario = ('indique datos del libro: ')
# nombre_libro = input('nombre del libro: ')
# id_libro = int(input('Proporcione el ID: '))
# precio = float(input('Precio: '))
# envio = bool(input('Indica si el envio es gratis (true/false): '))

# if envio == 'true':
#     envio = True
# elif envio == 'false':
#     envio = False
# else:
#     envio = 'Valor incorrecto, escriba true/false'
    
# print(f'''
#     Nombre: {nombre_libro}
#     ID: {id_libro}
#     precio: {precio}
#     envio): {envio}
# ''')

# #Tupla

# frutas = ('naranja', 'platano', 'guayaba')

# print(len(frutas))

# #Diccionario

# diccionario = {
#     'IDE': 'Integrated Development Environment',
#     'OOP': 'Object Oriented Programming',
#     'DBMS': 'Database Management System'
# }

# ############################

# def listarTerminos(**terminos):
#     for llave, valor in terminos.items():
#         print(f'{llave}: {valor}')
        
# listarTerminos(IDE='Integrated Development Environment', PK='Primery Key')
# listarTerminos(DBMS='Database Management System')

# #Funcion recursivo

# def Factorial(numero):
#     if numero == 1:
#         return 1
#     else:
#         return numero * Factorial(numero - 1)
    
    
#Clases y objetos

class Persona:
    def __init__(self ,nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        
    def mostrar_detalle(self):
        print(f'Persona: {self.nombre}')
        
        
persona1 = Persona('Marco', 'Narvaez', 24)
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)

persona2 = Persona('Mariam', 'Velasquez', 22)
print(f'objeto: {persona2.nombre} {persona2.apellido} {persona2.edad}')
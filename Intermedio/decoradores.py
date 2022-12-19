def hola(nombre = 'Marco'):
    print('Estas dentro de la primera funcion')
    
    def saluda():
        return 'Estas dentro de la segunda funcion'
    
    def bienvenida():
        return 'Estas dentro de la tercera funcion'
    
    print(saluda())
    print(bienvenida())
    print('De vuelta a la funcion hola')

hola()

def hola(nombre="Covadonga"):
    def saluda():
        return "Estás dentro de la función saluda()"

    def bienvenida():
        return "Estás dentro de la función bienvenida()"

    if nombre == "Covadonga":
        return saluda
    else:
        return bienvenida

a = hola()
print(a)
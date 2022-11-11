def funcion_generadora():
    for i in range(10):
        yield i

for item in funcion_generadora():
    print(item)
    
def fibon(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b

for x in fibon(100):
    print(x)
    
def multiplicar(x):
    return (x*x)
def sumar(x):
    return (x+x)

funcs = [multiplicar, sumar]
for i in range(5):
    valor = list(map(lambda x: x(i), funcs))
    print(valor)

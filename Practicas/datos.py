#Lists

list('hello')

name = 'Marco'
for letter in name:
    print(letter)
    
#Palabras reservadas

#False               class               from                or
#None                continue            global              pass
#True                def                 if                  raise
#and                 del                 import              return
#as                  elif                in                  try
#assert              else                is                  while
#async               except              lambda              with
#await               finally             nonlocal            yield
#break               for                 not

#Diccionarios u objetos

eggs = {'name': 'Marco', 'age': 24, 'lastName': 'Narvaez'}
ham = {'profesion': 'Back office', 'grade': 'college'}

eggs.setdefault('color', 'blue')

list(eggs.keys()) #trae las keys
list(eggs.values()) #trae los valores
list(eggs.items()) #trae los items

for k in eggs.keys():
    print(k)
    
for v in eggs.values():
    print(v)
    
for k, v in eggs.items():
    print(k, v)

#Estructura de datos

cat = {'name': 'miko', 'age': 2, 'color': 'black'}

allCats = []

allCats.append({'name': 'yashiko', 'age': 5, 'color': 'gray'})
allCats.append({'name': 'cato', 'age': 1, 'color': 'brown'})


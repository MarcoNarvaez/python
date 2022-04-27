import pprint


message = 'Esto es un mensaje para un diccionario'
count = {} 

for character in message.upper():
    count.setdefault(character, 0)
    count[character] = count[character] + 1

rjtext = pprint.pformat(count)
print(rjtext)


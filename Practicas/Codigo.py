from email import message
import re

#Expresiones regulares

# message = 'call me 415-555-1234'

# phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# mo = phoneNumRegex.search(message)
# print(mo.group())

# # #shebang line

# # #! /usr/bin/python3

# # #metodos de string

# # spam = 'hello world'
# # spam = spam.upper()

# # print(spam)

# # answer = input()

# # if answer == 'yes':
# #     print('playing again')
    
# # spam = 'hello world'
# # spam.islower()

# # spam = 'HELLO WORLD'
# # spam.isupper()

# # 'hello123'.isalpha()

# # 'hello world'.startswith('hello')

# # 'hello world'.endswith('world')

# # ' '.join['cats','rats','bats']

# # 'my name is simon'.split()
# # 'my name is simon'.split('m')

# # 'hello'.rjust(10)
# # 'hello'.ljust(10)
# # 'hello'.center(10)

# #####################################

# from itertools import count


# def lothar(n):
#   # Solucion
#     count = 0
#     while (n != 1):
#         count = count + 1
#         if n % 2 ==0:
#             n = n / 2
#         else:
#             n = (n * 3) + 1
            
            
#     return n, count
    
# n = int(input())
# resultado, contador = lothar(n)
# print(contador)

# ########################################

# def isPhoneNumber(text):
#     if len(text) != 12:
#         return False
#     for i in range(0, 3):
#         if not text[i].isdecimal():
#             return False
#     if text[3] != '-':
#         return False
#     for i in range(4, 7):
#         if not text[i].isdecimal():
#             return False
#     if text[7] != '-':
#         return False
#     for i in range(8, 12):
#         if not text[i].isdecimal():
#             return False
#     return True

# message = 'Call me 415-555-1234 tomorrow'

# foundNumber = False
# for i in range(len(message)):
#     chunk = message[i:i+12]
#     if isPhoneNumber(chunk):
#         print('phone number found: ' + chunk)
#         foundNumber = True
# if not foundNumber:
#     print('could not find any number')

#Expresiones regulares

# r'\d\d-\d\d\d\d-\d\d\d\d' #numero de tlf expresiones
# phoneNumber = re.compile(r'd\d-\d\d\d\d-\d\d\d\d')

# mo = phoneNumber.search('Mi numero es (11)-2879-9993')
# mo.group()


# batRegex = re.compile(r'Bat(man|mobile|copter|bat|)')
# mo = batRegex.search('Batmobile lost a wheel')
# mo.group(1)


batRegex = re.compile(r'Bat(wo)?man')
mo = batRegex.search('The adventures of Batman')


batRegex = re.compile(r'Bat(wo)*man')
mo = batRegex.search('The adventures of Batman')

batRegex = re.compile(r'Bat(wo)+man')
mo = batRegex.search('The adventures of Batman')

regex = re.compile(r'\+\*\?')
regex.search('Aprendi sobre +*? sintaxis regex')

haRegex = re.compile(r'(Ha) (3)')
haRegex.search('he said "HaHaHa"')

phoneRegex = re.compile(r'd\d-\d\d\d\d-\d\d\d\d')
phoneRegex.findall()

lyrics = 'Cuántas veces te dije que si Que el amor era incierto Ahora corres te alejas de mi Cuando aún queda tiempo Por ti Por mi Si valía la pena Por ti Por mi Cerrarías la puerta de tanto dolor'
lyricsRegex = re.compile(r'\d+\s\w')
lyricsRegex(lyrics) 

vowelRegex = re.compile(r'[aeiouAEIOU]')
vowelRegex.findall('Ropocop eats baby food')
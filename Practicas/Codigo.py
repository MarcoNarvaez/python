from email import message
import re, os, shelve, shutil, traceback, logging, random, webbrowser, sys, pyperclip, requests, bs4
from selenium import webdriver

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
# #     if isPhoneNumber(chunk):
# #         print('phone number found: ' + chunk)
# #         foundNumber = True
# # if not foundNumber:
# #     print('could not find any number')

# #Expresiones regulares

# # r'\d\d-\d\d\d\d-\d\d\d\d' #numero de tlf expresiones
# # phoneNumber = re.compile(r'd\d-\d\d\d\d-\d\d\d\d')

# # mo = phoneNumber.search('Mi numero es (11)-2879-9993')
# # mo.group()


# # batRegex = re.compile(r'Bat(man|mobile|copter|bat|)')
# # mo = batRegex.search('Batmobile lost a wheel')
# # mo.group(1)


# batRegex = re.compile(r'Bat(wo)?man')
# mo = batRegex.search('The adventures of Batman')


# batRegex = re.compile(r'Bat(wo)*man')
# mo = batRegex.search('The adventures of Batman')

# batRegex = re.compile(r'Bat(wo)+man')
# mo = batRegex.search('The adventures of Batman')

# regex = re.compile(r'\+\*\?')
# regex.search('Aprendi sobre +*? sintaxis regex')

# haRegex = re.compile(r'(Ha) (3)')
# haRegex.search('he said "HaHaHa"')

# phoneRegex = re.compile(r'd\d-\d\d\d\d-\d\d\d\d')
# phoneRegex.findall()

# lyrics = 'Cuántas veces te dije que si Que el amor era incierto Ahora corres te alejas de mi Cuando aún queda tiempo Por ti Por mi Si valía la pena Por ti Por mi Cerrarías la puerta de tanto dolor'
# lyricsRegex = re.compile(r'\d+\s\w')
# lyricsRegex(lyrics) 

# vowelRegex = re.compile(r'[aeiouAEIOU]')
# vowelRegex.findall('Ropocop eats baby food')

# beginsWithHelloRegex = re.compile(r'^Hello')
# beginsWithHelloRegex.search('Hello there')

# endsWithWorldRegex = re.compile(r'world!$')
# endsWithWorldRegex.search('Hello world!')

# allDigitsRegex = re.compile(r'^\d+$')
# allDigitsRegex.search('465445645616189413486746')

# atRegex = re.compile(r'.at')
# atRegex.findall('The cat in the hat sat on the flat mat.')

# nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
# nameRegex.findall('First Name: al Last Name: Sweigart')

# serve = '<To serve humans> for dinner.>'

# nongreedy = re.compile(r'<(.*?)')
# nongreedy.findall(serve)

# prime = 'Serve the public trust. \nProtect the innocent.\nUpload the law.'
# print(prime)

# dotStar = re.compile('.*', re.DOTALL)
# dotStar.search(prime)

# vowelRegex = re.compile(r'[aeiou]', re.IGNORECASE)
# vowelRegex.findall('Al, why does your programming book talk about RopoCop so mucho?')

# namesRegex = re.compile(r'Agent \w+')
# namesRegex.findall('Agent alice gave the secret documents tto Agent Bob')

# namesRegex.sub('REDACTED','Agent alice gave the secret documents tto Agent Bob')

# namesRegex = re.compile(r'Agent (\w)\w')
# namesRegex.findall('Agent alice gave the secret documents tto Agent Bob')

# re.compile(r'''
#            \d\d-
#            \d\d\d\d-
#            \d\d\d\d''', re.VERBOSE | re.DOTALL | re.IGNORECASE)


# ############################################################################3

# #Files

# os.path.join('folder1', 'folder2', 'file.png')
# os.getcwd() #obtener un path
# os.chdir() #saber el path
# os.path.abspath() #path exacto
# os.path.isabs() #root folder
# os.path.relpath() #relative path
# os.path.dirname() #directorio primario
# os.path.basename() # extrae ultima parte
# os.path.exists() #verificar si existe una carpeta
# os.path.isfile() #verificar si hay un archivo en carpeta
# os.path.isdir() #verificar si existe una carpeta
# os.path.getsize() #verificar el t amaño de una carpeta
# os.listdir() #devuelve una lista de strings de la carpeta
# os.unlink() #eliminar un archivo
# os.rmdir() #eliminar una carpeta (solo si esta vacia)
# os.walk() #recorre toda una carpeta

# totalSize = 0
# for filename in os.listdir(''):
#     if not os.path.isfile(os.path.join('', filename)):
#         continue
#     totalSize = totalSize + os.path.getsize(os.path.join('', filename))
    
# file = open('w', 'a') #abrir un archivo
# file.read() #lee un archivo
# file.close() #borra un archivo  
# file.write('helloooo') #metodo para escribir dentro del archivo 

# shelveFile = shelve.open('mydata')
# shelveFile['cats'] = ['zophie', 'simon', 'cleo']
# shelveFile.close()
# shelveFile.keys()
# list(shelveFile.keys())
# list(shelveFile.values())

# shutil.copy('') #copia un archivo
# shutil.copytree('') #copia una carpeta
# shutil.move('') #mueve un archivo a otra carpeta
# shutil.rmtree('') #elimina toda la carpeta y su contenido

# for filename in os.listdir():
#     if filename.endswith('.txt'):
#         #os.unlink(filename) dry run
#         print(filename)
        
# for folderName, subFolders, fileNames in os.walk(''):
#     print('')
    
#     for subFolder in subFolders:
#         if 'fish' in subFolder:
#             #os.rmdir(subFolder)
#             print('rmdir on ' + folderName)
    
#     for file in fileNames:
#         if file.endswith('.py'):
#             shutil.copy(os.join(folderName, file), os.join(folderName, file + '.backup'))
            
# #############################################################################

# #Debug

# """"

# *****************
# *               *
# *               * 
# *               *
# *****************

# """

# def boxPrint(symbol, width, height):
#     if len(symbol) != 1:
#         raise Exception("'symbol' needs to a string of lenght 1")
#     if (width < 2) or (height < 2):
#         raise Exception('"width"and"height" must be greater or equal to two')
#     print(symbol * width)
    
#     for i in range(height - 2):
#         print(symbol + (' ' * width - 2) + symbol)
        
#     print(symbol * width)
    
# boxPrint('*', 15, 5)

# try:
#     raise Exception('this is a error message')
# except:
#     errorFile = open('error_log.txt', 'a')
#     errorFile.write(traceback.format_exc())
#     errorFile.close()
#     print('the traceback info was written error_log.txt')
    
# #assert False, 'this is a error message'  

# ##############################################################################

# #Logging

# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL)

# logging.debug('start pf program')

# def factorial(n):
#     logging.debug('star of factorial (%s)' % (n))
#     total = 1
#     for i in range(1, n + 1):
#         total *= i
#         logging.debug('i is %s, total is %s' (i, total))
#     logging.debug('return value is $s' % (total))
#     return total

# print(factorial(5))

# logging.debug('end pf program')

# #Debugging

# heads = 0

# for i in range (1, 1001):
#     if random.randit(0, 1) == 1:
#         heads = heads + 1
#     if i == 500:
#         print('halfway done!')
        
# print('heads came up ' + str(heads) + ' times')

# #############################################################

# #Webbrowser

# sys.argv # ['marcelotdealvear.py', '1987', 'buenos aires']

# if len(sys.argv) > 1:
#     address = ' '.join(sys.argv[1:])
# else:
#     address = pyperclip.paste()
    
# webbrowser.open()

# #Requests

# res = requests.get('https://twitter.com/home')
# res.status_code

# playFile = open('')

# for chunk in res.iter_content(10000000):
#     playFile.write(chunk)
    
    
############################################################3

#Webscraping

# def getMeliPrice(productoUrl):

#     res = requests.get(productoUrl)
#     res.raise_for_status()

#     soup = bs4.BeautifulSoup(res.text, "html.parser")
#     elems = soup.select('#root-app > div.ui-pdp > div.ui-pdp-container.ui-pdp-container--pdp > div.ui-pdp-container__row.ui-pdp--relative.ui-pdp-with--separator--fluid.pb-40 > div.ui-pdp-container__col.col-3.ui-pdp-container--column-center.pb-40 > div > div.ui-pdp-container__row.ui-pdp-with--separator--fluid.ui-pdp-with--separator--40 > div.ui-pdp-container__col.col-2.mr-32 > div.ui-pdp-price.mt-16.ui-pdp-price--size-large > div.ui-pdp-price__second-line > span > span.andes-money-amount__fraction')

#     return elems[0].text.strip()
    
# price = getMeliPrice('https://www.mercadolibre.com.ar/notebook-lenovo-ideapad-15iil05-almond-156-intel-core-i3-1005g1-8gb-de-ram-256gb-ssd-intel-uhd-graphics-g1-1366x768px-windows-10-home/p/MLA18619162#reco_item_pos=1&reco_backend=machinalis-homes-pdp-boos&reco_backend_type=function&reco_client=home_navigation-recommendations&reco_id=d51e51d5-f077-4fdb-995c-630d5daa5089&c_id=/home/navigation-recommendations/element&c_element_order=2&c_uid=87455bc1-eac4-461b-9650-631e245f6002')
# print('the price is ' + str(price))

#Selenium

browser = webdriver.Chrome(executable_path=r"chromedriver.exe")
browser.get('https://github.com/')
elem = browser.find_element_by_css_selector('#repos-container > ul > li:nth-child(1) > div > div > a')
elem.click()

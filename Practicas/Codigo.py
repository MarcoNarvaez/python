#metodos de string

spam = 'hello world'
spam = spam.upper()

print(spam)

answer = input()

if answer == 'yes':
    print('playing again')
    
spam = 'hello world'
spam.islower()

spam = 'HELLO WORLD'
spam.isupper()

'hello123'.isalpha()

'hello world'.startswith('hello')

'hello world'.endswith('world')

' '.join['cats','rats','bats']

'my name is simon'.split()
'my name is simon'.split('m')

'hello'.rjust(10)
'hello'.ljust(10)
'hello'.center(10)


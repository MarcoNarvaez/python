def celsius_fahrenheit(celsius):
    return celsius* 9/5 + 32

def fahrenheit_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

#Celsius a fahrenheit
celsius = float(input('Proporcione su valor en celsius: '))
resultado = celsius_fahrenheit(celsius)

print(f'{celsius} C a F: {resultado:.2f}')

#Fahrenheit a celsius

fahrenheit = float(input('Proporcione su valor en fahrenheit'))
resultado = fahrenheit_celsius(fahrenheit)

print(f'{fahrenheit} F a C: {resultado:.2f}')
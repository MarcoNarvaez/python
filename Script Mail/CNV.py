import win32com.client as client
import os
from datetime import datetime

#Funcion de cambio de fecha en el Excel

def Fecha():
    dia = str(datetime.today().day)
    mes = str(datetime.today().month).zfill(2)
    año = str(datetime.today().year)
    archivo = año + mes + dia +"Ag265.xls"
    return archivo

#Verificar la carpeta, el archivo y envio el mail
def Verificacion():
    file = ("C:\\Users\MarcosAlejandroNarva\OneDrive - Cocos Capital\Escritorio\CNV\\")
    file_name = Fecha()
    carpeta = os.path.isfile(file + file_name)
    if (carpeta):
        path = (file + file_name)
        outlook = client.Dispatch('Outlook.Application')
        mensaje = outlook.CreateItem(0)
        mensaje.Display()
        mensaje.To = "mnarvaez@cocos.capital"
        mensaje.Subject = "testing python script"
        Attachments = path
        mensaje.Attachments.Add(Attachments)
        mensaje.send()
    else: 
        print("No enviado")

Verificacion()
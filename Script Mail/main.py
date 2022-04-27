import pandas as pd
import win32com.client as client
from datetime import datetime

#Funcion de cambio de fecha en el Excel

def Fecha():
    dia = str(datetime.today().day)
    mes = str(datetime.today().month)
    año = str(datetime.today().year)
    archivo = año + mes + dia +"Ag265.xls"
    print("Funciona")

#Envio de Mail
path = pd.read_excel(archivo)
path_absoluto = str(path.absolute())

outlook = client.Dispatch('Outlook.Application')

mensaje = outlook.CreateItem(0)
mensaje.Display()
mensaje.To = "miturbe@cocos.capital"
mensaje.Subject = "testing python script"
mensaje.Attachments.Add(path_absoluto)
mensaje.send()
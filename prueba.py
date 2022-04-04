import pandas as pd
from datetime import date
import requests
path = 'Gara.xls'
contr = input("ingrese su contraseña: ")

s = requests.Session()
r = s.get("https://posicionesygarantias.sba.com.ar/posicionesygarantias/service/login")
print(r.status_code)

r = s.post(
    "https://posicionesygarantias.sba.com.ar/posicionesygarantias/j_spring_security_check",
    data={"j_username": "maiturbe", "j_password": contr}
)
print(r.status_code)

r = s.get("https://posicionesygarantias.sba.com.ar/posicionesygarantias/service/saldoGarantiaDisponibleTable?SaldoGarantiaDisponibleTableController_p_=1&SaldoGarantiaDisponibleTableController_mr_=25&SaldoGarantiaDisponibleTableController_e_=excel&SaldoGarantiaDisponibleTableController_tr_=true&")
with open("GARA.xls", "wb") as f:
    f.write(r.content)


#Funcion que uso para agregar los encabezados y el píe
def Insert_row(row_number, df, row_value): 
    
    start_upper = 0
    end_upper = row_number 
    start_lower = row_number 
    end_lower = df.shape[0] 
    upper_half = [*range(start_upper, end_upper, 1)] 
    lower_half = [*range(start_lower, end_lower, 1)] 
    lower_half = [x.__add__(1) for x in lower_half] 
    index_ = upper_half + lower_half 
    df.index = index_ 
    df.loc[row_number] = row_value 
    df = df.sort_index() 
    return df 

#Defino variables que voy a usar para los encabezados y nombre de archivo
dia = str(date.today().day).zfill(2)
mes = str(date.today().month).zfill(2)
año4 = str(date.today().year)
año2 = str(año4)[-2:]
hora, minu, seg = "16", "30", "30"
nombre_archivo = "Devolucion Gara " + año4 + " " + mes + " " + dia

# Importo el excel sin la primera fila que dice "Garantias disponibles y no sirve para nada"
tabla = pd.read_excel(path, skiprows=1)

# Elimino las columnas "Retirable", "utilizado" y "total" que no las necesito
tabla = tabla.drop(['Retirable', 'Utilizado', "Total"], axis=1)

# Elimino las filas que incluyen "credito - posicion colocadora" que no necesito
tabla = tabla.drop(tabla[tabla['Instrumento'].str.contains("Credito - Posicion Colocadora")].index)

# Elimino las filas que SON "Pesos" "dolar transferencia" y "Dólar" ??? CHEQUEAR QUE SE LLAMEN ASI y reseteo el index
tabla = tabla.drop(tabla[tabla['Instrumento'] == "Pesos"].index)
tabla = tabla.drop(tabla[tabla['Instrumento'] == "Dólar"].index)
tabla = tabla.drop(tabla[tabla['Instrumento'] == "Dólar Transferencia"].index)
tabla.reset_index(inplace=True, drop=True)

#Trabajo con la tabla y agrego las columnas con los caracteres que nececesito
for row in range(len(tabla)):
    tabla.loc[row,"ComitenteNueveCaracteres"] = str(tabla.loc[row,"Comitente"]).zfill(9)
    if tabla.loc[row,"ComitenteNueveCaracteres"] == ("888888888") or tabla.loc[row,"ComitenteNueveCaracteres"] == ("777777777"):
        tabla.loc[row,"ComitenteClean"] = "000001001"
    else:
        tabla.loc[row,"ComitenteClean"] = str(tabla.loc[row,"Comitente"]).zfill(9)
    tabla.loc[row,"Codigo"] = str(tabla.loc[row,"Instrumento"])[str(tabla.loc[row,"Instrumento"]).index("(")+1:str(tabla.loc[row,"Instrumento"]).index(")")].zfill(5)
    tabla.loc[row,"DisponibleEntero"] = str(tabla.loc[row,"Disponible"])[0:str(tabla.loc[row,"Disponible"]).index(".")].zfill(11)
    tabla.loc[row,"DisponibleDecimales"] = str(tabla.loc[row,"Disponible"])[str(tabla.loc[row,"Disponible"]).index(".")+1:].ljust(7,'0')
    tabla.loc[row,"Exportar"] = "1'I'R'0265'" + tabla.loc[row,"ComitenteClean"] + "'" + tabla.loc[row,"Codigo"] + "       '" + tabla.loc[row,"DisponibleEntero"] + "." + tabla.loc[row,"DisponibleDecimales"] + "'9265'" + tabla.loc[row,"ComitenteNueveCaracteres"] + "'N'00'" + dia + mes + "'0000'N"

#Creo los encabezados y pie de acuerdo al formato necesario
encabezado1 = "00Aftfaot    " + año4 + mes + dia + hora + minu  + seg + str(len(tabla)+1).zfill(9)
encabezado2 = "0" + año2 + mes + dia + "FTFAOT0265"
pie1 = "99Aftfaot    " + año4 + mes + dia + hora + minu  + seg + str(len(tabla)+1).zfill(9)

#Me armo nueva tabla solo con la columna Exportar, y le agrego encabezados y pie
df = tabla["Exportar"]
df = Insert_row(0, df, encabezado1)
df = Insert_row(1, df, encabezado2)
df = Insert_row(len(df), df, pie1)

#Exporto los resultados como txt y xls
df.to_csv(nombre_archivo+".txt", index=False, header = False)
#tabla.to_excel(nombre_archivo+".xlsx", index=False, header = True)
print("El archivo se guardó con éxito")

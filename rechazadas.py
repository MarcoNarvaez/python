import pandas as pd
from datetime import date

filePath = 'TSA.xls'

# Importo el excel
tabla = pd.read_excel(filePath)


# Funcion que uso para agregar los encabezados y el píe
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

# Defino variables que voy a usar para los encabezados y nombre de archivo
dia = str(date.today().day).zfill(2)
mes = str(date.today().month).zfill(2)
año4 = str(date.today().year)
año2 = str(año4)[-2:]
hora, minu, seg = "16", "30", "30"
nombre_archivo = "Devolucion TSA" + año4 + " " + mes + " " + dia

# Trabajo con la tabla y agrego las columnas con los caracteres que nececesito
for row in range(len(tabla)):
    tabla.loc[row, "ComitenteNueveCaracteres"] = str(tabla.loc[row, "Comitente"]).zfill(9)
    if tabla.loc[row, "ComitenteNueveCaracteres"] == ("888888888") or tabla.loc[row, "ComitenteNueveCaracteres"] == (
    "777777777"):
        tabla.loc[row, "ComitenteClean"] = "000001001"
    else:
        tabla.loc[row,"Especie"] = str(tabla.loc[row,"Especie"])[str(tabla.loc[row,"Especie"]).index("")+0:].rjust(5,'0')
        tabla.loc[row, "MontoDecimales"] = str(tabla.loc[row, "Monto"])[str(tabla.loc[row, "Monto"]).index("")+0:].rjust(11,'0')
        tabla.loc[row, "MontoEntero"] = str(tabla.loc[row, "Monto"])[0:str(tabla.loc[row,"Monto"]).index("")].zfill(7)

        tabla.loc[row, "Exportar"] = "1'I'E'07465'000010000'" + tabla.loc[row,"Especie"] +"'" + "       '" + tabla.loc[row, "MontoEntero"] + '%.2f' + "." + tabla.loc[row, "Monto"] + "'0265'" + str(tabla.loc[row, "ComitenteNueveCaracteres"]) + "'N'00'" + dia + mes + "'0000'N"

# Creo los encabezados y pie de acuerdo al formato necesario
encabezado1 = "00Aftfaot    " + año4 + mes + dia + hora + minu + seg + str(len(tabla) + 1).zfill(9)
encabezado2 = "0" + año2 + mes + dia + "FTFAOT0265"
pie1 = "99Aftfaot    " + año4 + mes + dia + hora + minu + seg + str(len(tabla) + 1).zfill(9)

# Me armo nueva tabla solo con la columna Exportar, y le agrego encabezados y pie
df = tabla["Exportar"]
df = Insert_row(0, df, encabezado1)
df = Insert_row(1, df, encabezado2)
df = Insert_row(len(df), df, pie1)

# Exporto los resultados como txt y xls
df.to_csv(nombre_archivo + ".txt", index=False, header=False)
# tabla.to_excel(nombre_archivo+".xlsx", index=False, header = True)
print("El archivo se guardó con éxito")


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

#Defino las variables a usar
remitente = 'Desde: <Nefftep79@gmail.com>'
destinatario = 'Hasta: <Mariamvelasquez27@gmail.com'
asunto = 'Probando script python'
cuerpo = 'Hola mundo'

# Creamos el objeto mensaje
mensaje = MIMEMultipart()

# Establecemos los atributos del mensaje
mensaje['Desde'] = remitente
mensaje['Hasta'] = ", ".join(destinatario)
mensaje['Cuerpo'] = asunto
 
# Agregamos el cuerpo del mensaje como objeto MIME de tipo texto
mensaje.attach(MIMEText(cuerpo, 'plan'))
 
# Abrimos el archivo que vamos a adjuntar
#archivo_adjunto = open('.../Carpeta Personal/Documentos/prueba.ods')

# Creamos un objeto MIME base
adjunto_MIME = MIMEBase('application', 'octet-stream')
# Y le cargamos el archivo adjunto
#adjunto_MIME.set_payload((archivo_adjunto).read())
# Codificamos el objeto en BASE64
#encoders.encode_base64(adjunto_MIME)
# Agregamos una cabecera al objeto
#adjunto_MIME.add_header('Content-Disposition', "attachment; filename= %s")
# Y finalmente lo agregamos al mensaje
mensaje.attach(adjunto_MIME)
 
# Creamos la conexión con el servidor
sesion_smtp = smtplib.SMTP('smtp.gmail.com', 587)
 
# Ciframos la conexión
sesion_smtp.starttls()

# Iniciamos sesión en el servidor
sesion_smtp.login('rpi.mailer.1@gmail.com','Benito77')

# Convertimos el objeto mensaje a texto
texto = mensaje.as_string()

# Enviamos el mensaje
sesion_smtp.sendmail(remitente, destinatario, texto)

# Cerramos la conexión
sesion_smtp.quit()
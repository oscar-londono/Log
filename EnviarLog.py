import includes.LogClass as Log

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import configparser
import smtplib
import sys
import os

# Instanciamos el Objeto de manejo de archivo log
Log = Log.Log(os.path.splitext(os.path.basename(sys.argv[0]))[0])
Log.Informacion("Inicio del Envio de Log")

# Leemos el archivo de la configuración
Config = configparser.ConfigParser()
Config.read('ini\config.ini')

try:
 Server = smtplib.SMTP_SSL(Config.get('MAIL_FROM','SERVER'), Config.get('MAIL_FROM','PORT'))
 Server.ehlo()
 Server.login(Config.get('MAIL_FROM','ACCOUNT'), Config.get('MAIL_FROM','PASSWORD'))
 Log.Informacion("Inicio de sesion satisfactorio")
except:
 Log.Error("Error de Inicio de Sesion (0) El correo no ha podido ser enviado")
 sys.exit()

# Cuerpo del Mensaje
Mensaje = MIMEMultipart()
Mensaje['From']    = Config.get('MAIL_FROM','NAME') + " <" + Config.get('MAIL_FROM','ACCOUNT') + ">"
Mensaje['To']      = Config.get('MAIL_TO','ACCOUNT')
Mensaje['Subject'] = "Archivos Log"
Mensaje.attach(MIMEText("Buenos Dias, Adjunto los Archivos Log, Saludos!!!", 'html'))

Directorio = os.path.dirname(os.path.realpath('__file__'))

# Agregamos el Adjunto de la Sincronizacion de Productos
Archivo = os.path.join(Directorio, '../AdaptaProSync/SincronizarProductos.log')
Archivo = os.path.abspath(os.path.realpath(Archivo))
if (os.path.exists(Archivo)):
 mimeBase = MIMEBase("application", "octet-stream")
 with open(Archivo, "rb") as file:
  mimeBase.set_payload(file.read())
 encoders.encode_base64(mimeBase)
 mimeBase.add_header('Content-Disposition', 'attachment;filename="{}"'.format(os.path.basename(Archivo)))
 Mensaje.attach(mimeBase)
 try:
  os.remove(Archivo)
  Log.Informacion("Archivo de Log {} Borrado Satisfactoriamente!!!".format(os.path.basename(Archivo)))
 except:
  Log.Error("Imposible borrar el archivo de Log {}".format(os.path.basename(Archivo)))

# Agregamos el Adjunto de la Lista PDF
Archivo = os.path.join(Directorio, '../ListaPDF/CrearLista.log')
Archivo = os.path.abspath(os.path.realpath(Archivo))
if (os.path.exists(Archivo)):
 mimeBase = MIMEBase("application", "octet-stream")
 with open(Archivo, "rb") as file:
  mimeBase.set_payload(file.read())
 encoders.encode_base64(mimeBase)
 mimeBase.add_header('Content-Disposition', 'attachment;filename="{}"'.format(os.path.basename(Archivo)))
 Mensaje.attach(mimeBase)
 try:
  os.remove(Archivo)
  Log.Informacion("Archivo de Log {} Borrado Satisfactoriamente!!!".format(os.path.basename(Archivo)))
 except:
  Log.Error("Imposible borrar el archivo de Log {}".format(os.path.basename(Archivo)))

# Agregamos el Adjunto de Log
Archivo = os.path.join(Directorio, '../Log/EnviarLog.log')
Archivo = os.path.abspath(os.path.realpath(Archivo))
if (os.path.exists(Archivo)):
 mimeBase = MIMEBase("application", "octet-stream")
 with open(Archivo, "rb") as file:
  mimeBase.set_payload(file.read())
 encoders.encode_base64(mimeBase)
 mimeBase.add_header('Content-Disposition', 'attachment;filename="{}"'.format(os.path.basename(Archivo)))
 Mensaje.attach(mimeBase)
 try:
  os.remove(Archivo)
  Log.Informacion("Archivo de Log {} Borrado Satisfactoriamente!!!".format(os.path.basename(Archivo)))
 except:
  Log.Error("Imposible borrar el archivo de Log {}".format(os.path.basename(Archivo)))

# Agregamos el Adjunto de la Sincronizacion de MercadoLibre
Archivo = os.path.join(Directorio, '../MercadoLibreSync/ActualizarInventario.log')
Archivo = os.path.abspath(os.path.realpath(Archivo))
if (os.path.exists(Archivo)):
 mimeBase = MIMEBase("application", "octet-stream")
 with open(Archivo, "rb") as file:
  mimeBase.set_payload(file.read())
 encoders.encode_base64(mimeBase)
 mimeBase.add_header('Content-Disposition', 'attachment;filename="{}"'.format(os.path.basename(Archivo)))
 Mensaje.attach(mimeBase)
 try:
  os.remove(Archivo)
  Log.Informacion("Archivo de Log {} Borrado Satisfactoriamente!!!".format(os.path.basename(Archivo)))
 except:
  Log.Error("Imposible borrar el archivo de Log {}".format(os.path.basename(Archivo)))

try:
 Server.sendmail(Config.get('MAIL_FROM','ACCOUNT'), Config.get('MAIL_TO','ACCOUNT'), Mensaje.as_string())
 Server.close()
 Log.Informacion("Correo enviado satisfactoriamente")
except:
 Log.Error("Error de Envio de Correo (0) El correo no ha podido ser enviado")

Log.Informacion("Fin del Envio de Log")
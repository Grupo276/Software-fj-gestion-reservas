#Jhoider Steban Gutierrez Devia

import re #importacion de herramienta para validar correos electronicos 
import logging #importacion de herramienta para registrar los errores en archivos logs

#la configuracion del sistema de logs
logging.basicConfig(
    filename="logs.txt", #el archivo donde se van a guardar los errores
    level=logging.ERROR, #para que solo se registren errores
    format="%(asctime)s - %(levelname)s - %(message)s" #el formato de los mensajes de log
)

class cliente: #clase cliente
    def __init__(self, nombre, documento, email): #constructor 
        #setters para validar datos antes de guardarlos
        self.set_nombre(nombre)
        self.set_documento(documento)
        self.set_email(email)
        
    #metodo para asignar y validar el nombre
    def set_nombre(self, nombre):
        #para verificar que el nombre sea texto y que no este vacio 
        try:
            if not isinstance(nombre, str) or not nombre.strip():
                raise ValueError("el nombre debe ser un texto no vacío")
            #para guardar el nombre quitando los espacios
            self._nombre = nombre.strip()
        except Exception as e: #para registrar los errores en logs
            logging.error(f"error en nombre: {e}")
            raise

    #metodo para que se asigne y se valide el documento
    def set_documento(self, documento):
        try:
            #verifica que el documento sea un numero entero positivo 
            if not isinstance(documento, int) or documento <= 0:
                raise ValueError("el documento debe ser un número entero positivo") #genera el error en caso de no cumplir la condicion
            self._documento = documento #guarda el documento
        #captura el error y lo registra en logs
        except Exception as e:
            logging.error(f"error en documento: {e}")
            raise

    #metodo para que se asigne y se valide el email
    def set_email(self, email):
        #intenta definir un patron para validar los correos electronicos
        try:
            patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
            #si el email no es texto o no cumple con el patron genera un error
            if not isinstance(email, str) or not re.match(patron, email):
                raise ValueError("El email no tiene un formato válido")
            self._email = email #aqui se guarda el email
        except Exception as e: #captura el error y lo registra en logs
            logging.error(f"error en email: {e}")
            raise
    #getter del nombre
    def get_nombre(self):
        return self._nombre
    #getter del documento
    def get_documento(self):
        return self._documento
    #getter del email
    def get_email(self):
        return self._email

    # el metodo general para la validación del cliente
    def validar(self):
        try:
            #para asegurar de que ningun dato este vacio
            if not self._nombre or not self._documento or not self._email:
                raise ValueError("datos del cliente incompletos") #lanza el error en caso de que falten datos
            return True #devuelve true si no faltan datos
        #captura los errores y los guarda en logs
        except Exception as e:
            logging.error(f"error en validación de cliente: {e}")
            raise #relanza el error
    
    #un metodo para mostrar la informacion del cliente: nombre, documento, email. 
    def __str__(self):
        return f"cliente(nombre={self._nombre}, documento={self._documento}, email={self._email})"
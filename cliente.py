from abc import ABC
import logging

# clase abstracta base
class Entidad(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar_informacion(self):
        pass

# clase cliente que hereda de entidad 
class Cliente(Entidad):
    def __init__(self, nombre, email, edad):
        super().__init__(nombre)
        # validación de datos usando setters
        self.set_nombre(nombre)
        self.set_email(email)
        self.set_edad(edad)
        logging.info(f"Cliente creado: {nombre}")

    # getters
    def get_nombre(self):
        return self.__nombre

    def get_email(self):
        return self.__email

    def get_edad(self):
        return self.__edad

    def set_nombre(self, nombre):
        if not nombre:
            logging.error("Nombre vacio")
            raise ValueError("El nombre no puede estar vacio")
        self.__nombre = nombre
# validacion del correo 
    def set_email(self, email):
        if email == "" or "@" not in email:
            logging.error("Correo invalido")
            raise ValueError("Correo invalido")
        self.__email = email
# validación de la edad 
    def set_edad(self, edad):
        if not isinstance(edad, int):
            logging.error("Edad invalida")
            raise ValueError("La edad debe ser un numero entero")

        if edad <= 0:
            logging.error("Edad menor o igual a cero")
            raise ValueError("La edad debe ser mayor a cero")

        self.__edad = edad

    def mostrar_informacion(self):
        print(f"Nombre: {self.get_nombre()}")
        print(f"Edad: {self.get_edad()}")
        print(f"Correo: {self.get_email()}")

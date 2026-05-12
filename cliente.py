# Nombre de estudiante1: Andres David Perez Narvaez
# Nombre de estudiante2: Angela Patricia Perez Corpas
# Nombre de estudiante3: Cristian Jose Ortega Paternina
# Nombre de estudiante4: Jesus Andres Salcedo Martinez
# Grupo: 213023_80
# Programa: Ingenieria de sistemas
# Código Fuente: autoría propia

from abc import ABC
import logging
import re

#clase abstracta base
class Entidad(ABC):

    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar_informacion(self):
        pass

# clase cliente que hereda de entidad 
class Cliente(Entidad):
    def __init__(self, nombre, email, edad):
        super().__init__(nombre)
        self.reservas = []
        # validación de datos usando setters
        self.set_nombre(nombre)
        self.set_email(email)
        self.set_edad(edad)
        logging.info(f"Cliente creado: {nombre}")

    # getters
    def get_nombre(self) -> str :
        return self.__nombre

    def get_email(self) -> str:
        return self.__email

    def get_edad(self)  -> int:
        return self.__edad

    def set_nombre(self, nombre: str) -> None :
        if not nombre:
            logging.error("Nombre inválido")
            raise ValueError("El nombre no puede estar vacio")
        self.__nombre = nombre
    def set_email(self, email: str) -> None :
        patron = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if not re.match(patron, email):
            logging.error("Correo inválido")
            raise ValueError("Correo inválido")

        self.__email = email

    # validación de la edad 
    def set_edad(self, edad: int)-> None:

        if not isinstance(edad, int):
            logging.error("Edad invalida")
            raise ValueError("La edad debe ser un numero entero")

        if edad <= 0:
            logging.error("Edad menor o igual a cero")
            raise ValueError("La edad debe ser mayor a cero")
        if edad >120:
            logging.error("Edad fuera de rango")
            raise ValueError ("La edad no puede ser mayor a 120")


        self.__edad = edad

    def mostrar_informacion(self) -> str:
        return (
            f"Nombre: {self.get_nombre()}\n"
            f"Edad: {self.get_edad()}\n"
            f"Correo: {self.get_email()}")

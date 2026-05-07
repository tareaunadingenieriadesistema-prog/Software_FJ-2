from abc import ABC, abstractmethod
import logging

# clase abstracta base para todos los servicios
class Servicio(ABC):
    def __init__(self, precio_base):
        # Validación del precio base 
        if precio_base <= 0:
            logging.error("Precio base inválido")
            raise ValueError("El precio debe ser mayor a cero")

        self.precio_base = precio_base

    @abstractmethod
    def calcular_costo(self, extra=0, descuento=0):
        # Método obligatorio: cada servicio lo debe implementar
        pass

    @abstractmethod
    def mostrar_descripcion(self):
        pass

# Servicio especifico: Reserva de una sala 
class ReservaSala(Servicio):
    def __init__(self, horas, precio_base):
        super().__init__(precio_base)

# validación de horas 
        if horas <= 0:
            logging.error("Horas invalidas")
            raise ValueError("Las horas deben ser mayores a cero")

        self.horas = horas

    def calcular_costo(self, extra=0, descuento=0):
        # Cálculo base: precio por hora * cantidad de horas 
        costo = (self.precio_base * self.horas) + extra
        # Aplicación de descuento porcentual
        costo -= costo * (descuento / 100)
        return costo

    def mostrar_descripcion(self):
        # mostrar información del servicio 
        print(f"Reserva de sala por {self.horas} horas")


class AlquilerEquipos(Servicio):
    def __init__(self, dias, precio_base):
        super().__init__(precio_base)
# Validación de días de alquiler 
        if dias <= 0:
            logging.error("Días inválidos")
            raise ValueError("Los días deben ser mayores a cero")
# atributo propo del alquiler 
        self.dias = dias

    def calcular_costo(self, extra=0, descuento=0):
        # Cálculo del costo del alquiler 
        costo = (self.precio_base * self.dias) + extra
        costo -= costo * (descuento / 100)
        return costo

    def mostrar_descripcion(self):
        print(f"Alquiler de equipos por {self.dias} días")

# servicio especifico: asesoria profesional 
class Asesoria(Servicio):
    def __init__(self, horas, precio_base):
        super().__init__(precio_base)
# validación de horas de asesoría
        if horas <= 0:
            logging.error("Horas invalidas")
            raise ValueError("Horas invalidas")

        self.horas = horas

    def calcular_costo(self, extra=0, descuento=0):
        # Cálculo del costo de la asesoría 
        costo = (self.precio_base * self.horas) + extra
        # Aplicación de descuento si corresponde
        costo -= costo * (descuento / 100)
        return costo

    def mostrar_descripcion(self):
        # Información del servicio
        print(f"Asesoría especializada por {self.horas} horas")

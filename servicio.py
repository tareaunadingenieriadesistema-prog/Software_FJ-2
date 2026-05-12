# Nombre de estudiante1: Andres David Perez Narvaez
# Nombre de estudiante2: Angela Patricia Perez Corpas
# Nombre de estudiante3: Cristian Jose Ortega Paternina
# Nombre de estudiante4: Jesus Andres Salcedo Martinez
# Grupo: 213023_80
# Programa: Ingenieria de sistemas
# Código Fuente: autoría propia


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

    # método general para calcular costos
    def calcular_costo(self, cantidad=1, extra=0, descuento=0):

        # descuento se maneja como porcentaje

        costo = (self.precio_base * cantidad) + extra
        costo -= costo * (descuento / 100)

        return costo

    @abstractmethod
    def mostrar_descripcion(self):
        pass


# Servicio especifico: Reserva de una sala
class ReservaSala(Servicio):

    def __init__(self, horas, precio_base):

        super().__init__(precio_base)

        # validación de horas
        if horas <= 0:
            logging.error("Horas inválidas")
            raise ValueError("Las horas deben ser mayores a cero")

        self.horas = horas

    def calcular_costo(self, extra=0, descuento=0):
        return super().calcular_costo(
            cantidad=self.horas, extra=extra, descuento=descuento
        )

    def mostrar_descripcion(self):

        return f"Reserva de sala por {self.horas} horas"


class AlquilerEquipos(Servicio):

    def __init__(self, dias, precio_base):

        super().__init__(precio_base)

        # Validación de días de alquiler
        if dias <= 0:
            logging.error("Días inválidos")
            raise ValueError("Los días deben ser mayores a cero")

        # atributo propio del alquiler
        self.dias = dias

    def calcular_costo(self, extra=0, descuento=0):
        return super().calcular_costo(
            cantidad=self.dias, extra=extra, descuento=descuento
        )

    def mostrar_descripcion(self):

        return f"Alquiler de equipos por {self.dias} días"


# servicio especifico: asesoria profesional
class Asesoria(Servicio):

    def __init__(self, horas, precio_base):

        super().__init__(precio_base)

        # validación de horas de asesoría
        if horas <= 0:
            logging.error("Horas inválidas")
            raise ValueError("Horas invalidas")

        self.horas = horas

    def calcular_costo(self, extra=0, descuento=0):
        return super().calcular_costo(
            cantidad=self.horas, extra=extra, descuento=descuento
        )

    def mostrar_descripcion(self):

        return f"Asesoría especializada por {self.horas} horas"


        self.horas = horas

    def mostrar_descripcion(self):

        return f"Asesoría especializada por {self.horas} horas"

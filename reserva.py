import logging
from enum import Enum

from cliente import Cliente
from servicio import Servicio
from excepciones import ErrorReserva, ErrorCliente

# Enum para los estados de la reserva 
class EstadoReserva(Enum):
    pendiente = "pendiente"
    confirmado = "confirmado"
    cancelado = "cancelado"

# clase que representa una reserva de un cliente para un servicio
class Reserva:
    def __init__(self, cliente, servicio, estado=EstadoReserva.pendiente):
        # Validar que el cliente sea una instancia válida
        if not isinstance(cliente, Cliente):
            logging.error("Cliente inválido")
            raise ErrorCliente("Cliente inválido")
# validar que el servicio sea una instancia válida
        if not isinstance(servicio, Servicio):
            logging.error("Servicio inválido")
            raise ErrorReserva("Servicio inválido")

        self.cliente = cliente
        self.servicio = servicio
        self.estado = estado


    def cliente_tiene_reserva_activa(self):
        for reserva in getattr (self.cliente, "reservas", []):
            if reserva.estado == EstadoReserva.confirmado:
                return True
        return False
    

# cambia el estado de la reserva a confirmado
    def confirmar(self):

   
        # Validar reserva duplicada del cliente
        if self.cliente_tiene_reserva_activa():
            logging.warning("Cliente ya tiene una reserva activa")
            raise ErrorReserva ("El cliente ya tiene una reserva activa")
        

        if self.estado == EstadoReserva.confirmado:
            logging.warning("Reserva confirmada")
            raise ErrorReserva("La reserva ya está confirmada")

        self.estado = EstadoReserva.confirmado
        logging.info("Reserva confirmada")
# Cancela la reserva 
    def cancelar(self):
        if self.estado == EstadoReserva.cancelado:
            logging.warning("Reserva cancelada")
            raise ErrorReserva("La reserva ya está cancelada")
        self.estado = EstadoReserva.cancelado
        logging.info("Reserva ya esta cancelada")
# procesa la reserva y calcula el costo total 
    def procesar(self):
        try:
            costo = self.servicio.calcular_costo(extra=10, descuento=5)

# Manejo de errores relacionados con valores inválidos
        except ValueError as e:
            logging.error(f"Error de valor: {e}")
            raise ErrorReserva("Error en procesamiento") from e
# Manejo de errores de tipo
        except TypeError as e:
            logging.error(f"Error de tipo: {e}")
            raise ErrorReserva("Error de tipo en procesamiento") from e

        else:
            self.confirmar()
            logging.info(f"Reserva procesada correctamente. Costo: {costo}")
            return costo

# muestra la información completa de la reserva 
    def mostrar_reserva(self):
        print("----- RESERVA -----")
        print(f"Estado: {self.estado.value}")

        print(self.cliente.mostrar_informacion())
        print(self.servicio.mostrar_descripcion())

        try:
            costo = self.servicio.calcular_costo()
            print(f"Costo: {costo}")

        except (ValueError, TypeError)as e:
            logging.warning(f"No se pudo calcular el costo: {e}")
            print(f"Error: {e}")

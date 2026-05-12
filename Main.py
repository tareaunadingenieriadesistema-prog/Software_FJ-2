# Nombre de estudiante1: Andres David Perez Narvaez
# Nombre de estudiante2: Angela Patricia Perez Corpas
# Nombre de estudiante3: Cristian Jose Ortega Paternina
# Nombre de estudiante4: Jesus Andres Salcedo Martinez
# Grupo: 213023_80
# Programa: Ingenieria de sistemas
# Código Fuente: autoría propia


from logger import *

from cliente import Cliente
from servicio import ReservaSala, AlquilerEquipos, Asesoria
from reserva import Reserva

clientes = []
servicios = []
reservas = []


print("===== PRUEBAS DEL SISTEMA SOFTWARE FJ =====")

# Cliente valido
try:
    cliente1 = Cliente("Angela", "angela@gmail.com", 24)
    clientes.append(cliente1)
except Exception as e:
    logging.error(e)

# Cliente valido
try:
    cliente2 = Cliente("Jesus", "Jesus@gmail.com", 30)
    clientes.append(cliente2)

except Exception as e:
    logging.error(e)

# cliente invalido
try:
    cliente3 = Cliente("", "correo", -5)
except Exception as e:
    logging.error(e)

# cliente invalido
try:
    cliente4 = Cliente("Carlos", "malcorreo", 20)
except Exception as e:
    logging.error(e)

# servicio valido
try:
    servicio1 = ReservaSala(2, 100)
    servicios.append(servicio1)
except Exception as e:
    logging.error(e)

# servicio valido

try:
    servicio2 = AlquilerEquipos(3, 50)
    servicios.append(servicio2)
except Exception as e:
    logging.error(e)


# servicio invalido

try:
    servicio3 = Asesoria(-5, 80)
except Exception as e:
    logging.error(e)

# Reserva Exitosa
try:
    reserva1 = Reserva(cliente1, servicio1)
    reservas.append(reserva1)
    reserva1.procesar()
except Exception as e:
    logging.error(e)

# Reserva exitosa

try:
    reserva2 = Reserva(cliente2, servicio2)
    reservas.append(reserva2)
    reserva2.procesar()
except Exception as e:
    logging.error(e)

# Reserva exitosa (reserva de asesorías)

try:
    servicio3 = Asesoria(2, 80)
    servicios.append(servicio3)
    reserva3 = Reserva(cliente1, servicio3)
    reservas.append(reserva3)
    reserva3.procesar()
except Exception as e:
    logging.error(e)

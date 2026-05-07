from logger import *

from cliente import Cliente
from servicio import ReservaSala, AlquilerEquipos, Asesoria
from reserva import Reserva

clientes = []
servicios = []
reservas = []

print("===== PRUEBAS DEL SISTEMA SOFTWARE FJ =====")

# CLIENTES VÁLIDOS
try:
    cliente1 = Cliente("Angela", "angela@gmail.com", 24)
    clientes.append(cliente1)
except Exception as e:
    print(e)

try:
    cliente2 = Cliente("Jesus", "Jesus@gmail.com", 30)
    clientes.append(cliente2)
except Exception as e:
    print(e)

# CLIENTES INVÁLIDOS
try:
    cliente3 = Cliente("", "correo", -5)
    clientes.append(cliente3)
except Exception as e:
    print(e)

try:
    cliente4 = Cliente("Carlos", "malcorreo", 20)
    clientes.append(cliente4)
except Exception as e:
    print(e)

# SERVICIOS VÁLIDOS
try:
    servicio1 = ReservaSala(2, 100)
    servicios.append(servicio1)
except Exception as e:
    print(e)

try:
    servicio2 = AlquilerEquipos(3, 50)
    servicios.append(servicio2)
except Exception as e:
    print(e)

try:
    servicio3 = Asesoria(5, 80)
    servicios.append(servicio3)
except Exception as e:
    print(e)

# SERVICIOS INVÁLIDOS
try:
    servicio4 = ReservaSala(-1, 100)
    servicios.append(servicio4)
except Exception as e:
    print(e)

try:
    servicio5 = Asesoria(-2, 50)
    servicios.append(servicio5)
except Exception as e:
    print(e)

# RESERVAS VÁLIDAS
try:
    reserva1 = Reserva(cliente1, servicio1)
    reservas.append(reserva1)
    print(reserva1.procesar())
except Exception as e:
    print(e)

    print(e)


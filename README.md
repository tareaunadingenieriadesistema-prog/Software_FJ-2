# Software_FJ-2
Tarea 4 de programacion
## Descripción General
Este proyecto es un sistema de gestión de reservas desarrollado en Python, diseñado para manejar clientes, servicios y reservas de manera estructurada. El sistema permite crear clientes, definir servicios (como reserva de salas, alquiler de equipos y asesorías), y gestionar reservas con validaciones, manejo de excepciones y logging. El proyecto demuestra principios de programación orientada a objetos, incluyendo herencia, abstracción y encapsulamiento.

## Objetivos del Proyecto
- Implementar un sistema de reservas que valide datos de entrada.
- Gestionar diferentes tipos de servicios con cálculos de costos dinámicos.
- Manejar estados de reservas (pendiente, confirmado, cancelado).
- Proporcionar un manejo robusto de excepciones con encadenamiento.
- Registrar operaciones mediante logging para auditoría.
- Demostrar operaciones demostrativas en el archivo Main.py.

## Estructura del Proyecto
El proyecto consta de los siguientes archivos:
- **Main.py**: Archivo principal que ejecuta pruebas del sistema, creando instancias de clientes, servicios y reservas.
- **cliente.py**: Define la clase Cliente y la clase abstracta Entidad.
- **servicio.py**: Define la clase abstracta Servicio y sus subclases concretas (ReservaSala, AlquilerEquipos, Asesoria).
- **reserva.py**: Define la clase Reserva con estados y métodos para confirmar/cancelar.
- **excepciones.py**: Define excepciones personalizadas (ErrorReserva, ErrorCliente, ErrorServicio).
- **logger.py**: Configura el sistema de logging para registrar eventos en logs.txt.
- **logs.txt**: Archivo de logs generado durante la ejecución.
- **README.md**: Documentación básica del proyecto.

## Arquitectura OOP
El proyecto sigue una arquitectura orientada a objetos con:
- **Abstracción**: Clases abstractas como Entidad y Servicio definen interfaces comunes.
- **Herencia**: Cliente hereda de Entidad; ReservaSala, AlquilerEquipos y Asesoria heredan de Servicio.
- **Encapsulamiento**: Uso de propiedades privadas (__nombre, __email) con getters y setters para validación.
- **Polimorfismo**: Métodos como mostrar_descripcion() y calcular_costo() se implementan de manera diferente en subclases.

## Jerarquía de Clases
- **Entidad (ABC)**: Clase base abstracta con atributo nombre y método mostrar_informacion().
  - **Cliente**: Hereda de Entidad. Atributos: nombre, email, edad, reservas. Métodos: getters/setters con validación, mostrar_informacion().
- **Servicio (ABC)**: Clase base abstracta con precio_base. Métodos: calcular_costo(), mostrar_descripcion() (abstracto).
  - **ReservaSala**: Hereda de Servicio. Atributos: horas. Calcula costo basado en horas.
  - **AlquilerEquipos**: Hereda de Servicio. Atributos: dias. Calcula costo basado en días.
  - **Asesoria**: Hereda de Servicio. Atributos: horas. Calcula costo basado en horas.
- **Reserva**: Clase independiente. Atributos: cliente, servicio, estado. Métodos: confirmar(), cancelar(), procesar(), mostrar_reserva().

## Características Implementadas
- Validación de datos: Nombres no vacíos, emails con regex, edades positivas, precios/horas/días positivos.
- Gestión de estados: Reservas pueden estar pendientes, confirmadas o canceladas.
- Cálculo de costos: Fórmula: (precio_base * cantidad) + extra - (costo * descuento/100).
- Logging: Registra creación de objetos, errores y operaciones en logs.txt.
- Prevención de reservas duplicadas: Un cliente no puede tener múltiples reservas activas.
- Operaciones demostrativas: Main.py incluye pruebas con clientes válidos/inválidos, servicios y reservas.

## Manejo de Excepciones
El proyecto utiliza excepciones personalizadas y manejo estructurado:
- **Excepciones Personalizadas**: ErrorReserva, ErrorCliente, ErrorServicio en excepciones.py.
- **Validación con Excepciones**: Setters lanzan ValueError para datos inválidos.
- **Try-Except en Main.py**: Captura excepciones durante creación y procesamiento, registrando errores.
- **Encadenamiento**: En Reserva.procesar(), excepciones ValueError/TypeError se encadenan a ErrorReserva usando "from e".

## Patrones de Manejo
- **Patrón de Validación**: Uso de setters para validar atributos antes de asignación.
- **Patrón de Estado**: Enum EstadoReserva para gestionar estados de reserva.
- **Patrón de Logging**: Logging centralizado para registrar eventos y errores.
- **Patrón de Abstracción**: Clases abstractas para definir contratos comunes.

## Encadenamiento de Excepciones
En el método Reserva.procesar():
- Se intenta calcular el costo, que puede lanzar ValueError o TypeError.
- Estas excepciones se capturan y se relanzan como ErrorReserva, preservando la causa original con "from e".
- Esto permite rastrear la raíz del error mientras se maneja a un nivel más alto.

## Operaciones Demostrativas
El archivo Main.py demuestra:
- Creación de clientes válidos e inválidos (manejo de excepciones).
- Creación de servicios válidos e inválidos.
- Procesamiento de reservas exitosas, incluyendo cálculo de costos.
- Logging de todas las operaciones.

## Estados de las Reservas
Las reservas tienen tres estados definidos en el Enum EstadoReserva:
- **Pendiente**: Estado inicial al crear la reserva.
- **Confirmado**: Después de procesar exitosamente, si no hay reservas activas duplicadas.
- **Cancelado**: Al cancelar la reserva.

## Cálculo de Costos
El cálculo se realiza en Servicio.calcular_costo():
- Parámetros: cantidad (horas/días), extra (monto fijo), descuento (porcentaje).
- Fórmula: costo = (precio_base * cantidad) + extra - (costo * descuento / 100)
- Ejemplos:
  - ReservaSala: precio_base=100, horas=2, extra=10, descuento=5 → (100*2)+10 - ((200+10)*0.05) = 210 - 10.5 = 199.5
  - AlquilerEquipos: Similar, basado en días.
  - Asesoria: Similar, basado en horas.

Este proyecto sirve como ejemplo educativo de OOP en Python con énfasis en validación, excepciones y logging.

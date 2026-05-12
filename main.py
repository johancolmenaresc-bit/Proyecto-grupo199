import logging

from nucleo import ErrorFinanciero, ErrorValidacion, ServicioNoDisponible
from modelos import Cliente, ReservaSala, AlquilerEquipo, AsesoriaEspecializada


class Reserva:
    """
    Integra un cliente con un servicio contratado.
    Acá vive la lógica robusta de negocio: validación, cálculo y manejo de errores.
    """

    contador_reservas = 1

    def __init__(self, cliente, servicio, duracion, descuento=0.0, **opciones):
        self.id_reserva = Reserva.contador_reservas
        Reserva.contador_reservas += 1
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.descuento = descuento
        self.opciones = opciones
        self.costo_total = 0.0

    def procesar(self):
        """
        Procesa la reserva usando try/except/else/finally.
        - try: valida y calcula.
        - except: captura errores esperados del negocio.
        - else: confirma la reserva si todo salió bien.
        - finally: deja registro siempre, haya error o no.
        """
        try:
            self._validar_datos()
            self.costo_total = self.servicio.calcular_costo(
                self.duracion,
                self.descuento,
                **self.opciones
            )

            if self.costo_total <= 0:
                raise ErrorFinanciero("El costo calculado debe ser mayor que cero.")

        except ErrorValidacion as error:
            logging.error("Reserva %s rechazada por validación: %s", self.id_reserva, error)
            print(f" Reserva {self.id_reserva} rechazada: {error}")
            return False

        except ServicioNoDisponible as error:
            logging.error("Reserva %s rechazada por servicio no disponible: %s", self.id_reserva, error)
            print(f" Reserva {self.id_reserva} rechazada: {error}")
            return False

        except ErrorFinanciero as error:
            logging.error("Reserva %s rechazada por error financiero: %s", self.id_reserva, error)
            print(f" Reserva {self.id_reserva} rechazada: {error}")
            return False

        except Exception as error:
            logging.exception("Error inesperado en reserva %s", self.id_reserva)
            print(f" Error inesperado en reserva {self.id_reserva}: {error}")
            return False

        else:
            logging.info("Reserva %s procesada correctamente", self.id_reserva)
            print(self.generar_resumen())
            return True

        finally:
            logging.info("Finalizó el intento de procesamiento de la reserva %s", self.id_reserva)

    def _validar_datos(self):
        if self.cliente is None:
            raise ErrorValidacion("La reserva debe tener un cliente.")

        if self.servicio is None:
            raise ServicioNoDisponible("La reserva debe tener un servicio.")

        if self.duracion <= 0:
            raise ErrorValidacion("La duración debe ser mayor que cero.")

        if not 0 <= self.descuento <= 0.5:
            raise ErrorFinanciero("El descuento debe estar entre 0% y 50%.")

    def generar_resumen(self):
        return (
            f" Reserva {self.id_reserva} confirmada\n"
            f"   Cliente: {self.cliente.nombre}\n"
            f"   Servicio: {self.servicio.obtener_detalle()}\n"
            f"   Duración: {self.duracion}\n"
            f"   Total: ${self.costo_total:,.2f}\n"
        )


def ejecutar_simulacion():
    """
    Ejecuta 10 operaciones para demostrar integración, polimorfismo y manejo de errores.
    """
    print("=== Simulación Software FJ ===\n")

    clientes = [
        Cliente(1, "Ana Pérez", "ana.perez@email.com", "3001112233"),
        Cliente(2, "Luis Gómez", "luis.gomez@email.com", "3002223344"),
        Cliente(3, "Camila Ruiz", "camila.ruiz@email.com", "3003334455"),
    ]

    sala_reuniones = ReservaSala("Sala Ejecutiva", 50.0, 12)
    proyector = AlquilerEquipo("Proyector 4K", 80.0, "Epson")
    asesoria = AsesoriaEspecializada("Arquitectura de Software", 120.0, "Ing. Torres")

    operaciones = [
        Reserva(clientes[0], sala_reuniones, 2, descuento=0.10),
        Reserva(clientes[1], proyector, 3, seguro_opcional=True),
        Reserva(clientes[2], asesoria, 4, descuento=0.15),
        Reserva(clientes[0], sala_reuniones, 5, es_festivo=True),
        Reserva(clientes[1], proyector, 1, descuento=0.05, seguro_opcional=False),
        Reserva(clientes[2], asesoria, 2),
        Reserva(clientes[0], sala_reuniones, 0),
        Reserva(clientes[1], None, 2),
        Reserva(clientes[2], proyector, 2, descuento=0.80),
        Reserva(clientes[0], asesoria, 1, descuento=0.20),
    ]

    exitosas = 0

    for reserva in operaciones:
        if reserva.procesar():
            exitosas += 1

    print("=== Resultado final ===")
    print(f"Operaciones ejecutadas: {len(operaciones)}")
    print(f"Reservas exitosas: {exitosas}")
    print(f"Reservas rechazadas: {len(operaciones) - exitosas}")


if __name__ == "__main__":
    ejecutar_simulacion()
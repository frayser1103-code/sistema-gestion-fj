from exceptions.errores import ReservaError
from utils.logger import log_error

class Reserva:
    def __init__(self, cliente, servicio, duracion):
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "pendiente"

    def procesar(self):
        try:
            if self.duracion <= 0:
                raise ReservaError("Duración inválida")

            costo = self.servicio.calcular_costo(self.duracion)
            self.estado = "confirmada"
            print(f"Reserva confirmada para {self.cliente.get_info()} → {costo}")

        except Exception as e:
            log_error(e)
            self.estado = "fallida"
            print("Error en la reserva")

        finally:
            print("Proceso finalizado")

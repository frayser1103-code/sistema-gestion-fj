from abc import ABC, abstractmethod
from exceptions.errores import ServicioError

class Servicio(ABC):
    def __init__(self, nombre, precio):
        if precio <= 0:
            raise ServicioError("Precio inválido")
        self.nombre = nombre
        self.precio = precio

    @abstractmethod
    def calcular_costo(self, *args, **kwargs):
        pass

    @abstractmethod
    def descripcion(self):
        pass

class ReservaSala(Servicio):
    def calcular_costo(self, horas=1, descuento=0.0):
        total = self.precio * horas
        return total - (total * (descuento / 100))

    def descripcion(self):
        return "Reserva de sala"

class AlquilerEquipo(Servicio):
    def calcular_costo(self, dias=1, descuento=0.0):
        total = self.precio * dias
        return total - (total * (descuento / 100))

    def descripcion(self):
        return "Alquiler de equipos"

class Asesoria(Servicio):
    def calcular_costo(self, horas=1, experto=False, descuento=0.0):
        total = self.precio * horas
        if experto:
            total *= 1.5
        return total - (total * (descuento / 100))

    def descripcion(self):
        return "Asesoría especializada"

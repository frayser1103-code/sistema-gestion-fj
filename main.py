from models.cliente import Cliente
from models.servicio import ReservaSala, AlquilerEquipo, Asesoria
from models.reserva import Reserva
from exceptions.errores import ClienteError, ServicioError
from utils.logger import log_error

def main():
    clientes = []
    servicios = []
    reservas = []

    try:
        clientes.append(Cliente(1, "Ana", "ana@mail.com"))
        clientes.append(Cliente(2, "Luis", "luis@mail.com"))

        try:
            clientes.append(Cliente(3, "", ""))
        except ClienteError as e:
            print("Cliente inválido:", e)
            log_error(e)

        servicios.append(ReservaSala("Sala de reuniones", 50))
        servicios.append(AlquilerEquipo("Laptop", 30))
        servicios.append(Asesoria("Consultoría", 100))

        reservas.append(Reserva(clientes[0], servicios[0], 2))
        reservas.append(Reserva(clientes[1], servicios[2], 3))
        reservas.append(Reserva(clientes[0], servicios[1], -1))

        for r in reservas:
            r.procesar()

    except Exception as e:
        print("Error crítico:", e)
        log_error(e)

if __name__ == "__main__":
    main()

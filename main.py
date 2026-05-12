from models.cliente import Cliente
from models.servicio import ReservaSala, AlquilerEquipo, Asesoria
from models.reserva import Reserva
from exceptions.errores import ClienteError, ServicioError
from utils.logger import log_error # Se inserta la clase de GestorLogs

def ejecutar_simulacion():
    clientes = []
    servicios = []
    reservas = []

    print("|| Iniciando Sistema de Gestion by Software FJ ||")

    # Operaciones de clientes - Casos del 1 a 4
    datos_clientes = [
        (1, "Ana Garcia", "ana@gmail.com"),      # Permitido
        (2, "Luis Perez", "luis@gmail.com"),     # Permitido
        (3, "", "error@gmail.com"),              # Denegado - Espacio del nombre vacio
        (4, "Carlos", "correo_mal")                # Denegado - Se valida el correo
    ]

    for id_c, nom, mail in datos_clientes:
        try:
            nuevo_cliente = Cliente(id_c, nom, mail)
        except ClienteError as e:
            print(f"[!] Error de Cliente: {e}")
            log_error(e) # log creado
        else:
            clientes.append(nuevo_cliente)
            print(f"[+] Cliente registrado: {nom}")
        finally:
            # Se completa el bloque FINALLY
            pass 

    # Operaciones de servicios - Casos del 5 a 7
    try:
        s1 = ReservaSala("Sala A", 50)
        s2 = AlquilerEquipo("Portatiles", 30)
        s3 = Asesoria("Consultoras Tecnologicas", 100)
        servicios.extend([s1, s2, s3])
        print("[+] Servicios creados correctamente.")
    except Exception as e:
        log_error(e)

    # Operaciones de las reservas y sobrecargas - Casos del 8 a 10, y entrada de errores
    print("\n--- PROCESANDO RESERVAS Y CÁLCULOS ---")
    
    # Intentos de las reservas
    intentos_reserva = [
        (0, 0, 5),   # Situacion permitida: Cliente 0, Servicio 0, 5 horas
        (1, 2, 2),   # Situacion permitida: Cliente 1, Servicio 2, 2 horas
        (0, 1, -2),  # Situacion denegada: Duracion negativa
        (1, 0, 10),  # Situacion permitida con descuento - Se simula una reserva VIP
    ]

    for idx_c, idx_s, duracion in intentos_reserva:
        try:
            #   Se simula el procesamiento de la entrada
            res = Reserva(clientes[idx_c], servicios[idx_s], duracion)
            
            # Se llama al metodo de sobrecarga
            # Se prueban diferentes formas variantes del cálculo
            if duracion > 8:
                costo = res.servicio.calcular_costo(duracion, descuento=15.0) # Se aplica el descuento
            else:
                costo = res.servicio.calcular_costo(duracion) # El precio de base
                
            res.procesar()
            reservas.append(res)
            print(f"Reserva completa - Valor total: ${costo}")

        except (IndexError, ServicioError, ValueError) as e:
            # En el caso que lo requiera se pueden agregar encadenamientos de excepciones
            print(f"[!] Error en crear la reserva: {e}")
            log_error(e)
        else:
            print("La aprobacion se ha enviado al cliente.")
        finally:
            print("Finalizacion de este proceso.")

    print(f"\n Resumen: {len(reservas)} reservas creadas correctamente.")

if __name__ == "__main__":
    try:
        ejecutar_simulacion()
    except Exception as e:
        # Registra los errores graves que genere el sistema
        print(f"ERROR GRAVE DEL SISTEMA: {e}")
        log_error(e)

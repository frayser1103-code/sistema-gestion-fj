from exceptions.errores import ClienteError

class Cliente:
    def __init__(self, id, nombre, email):
        self.__id = id
        self.__nombre = nombre
        self.__email = email
        self.__validar()

    def __validar(self):
        if not self.__nombre or not self.__email or "@" not in self.__email:
            raise ClienteError("Datos inválidos del cliente")

    def get_info(self):
        return f"{self.__nombre} ({self.__email})"

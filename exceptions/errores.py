class SistemaError(Exception):
    pass

class ClienteError(SistemaError):
    pass

class ServicioError(SistemaError):
    pass

class ReservaError(SistemaError):
    pass

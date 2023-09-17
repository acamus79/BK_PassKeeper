from cryptography.fernet import Fernet
from decouple import config

class FernetFactory:
    def __init__(self):
        self.key = config('ENCRYPTION_KEY')

    def create_fernet_instance(self):
        try:
            if not self.key or not isinstance(self.key, str):
                raise ValueError("La variable de entorno ENCRYPTION_KEY no está configurada o no es una cadena válida")
            return Fernet(self.key)
        except Exception as ex:
            raise ValueError(f"Error al crear la instancia de Fernet: {str(ex)}")

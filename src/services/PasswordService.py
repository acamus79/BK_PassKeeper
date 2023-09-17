from database.db import get_connection
from services.EncriptionService import EncryptionService
from entities.Password import Password

class PasswordService():
    
    @staticmethod 
    def encrypt_password_fields(pwd):
        pwd.url = EncryptionService.encrypt_field(pwd.url) 
        pwd.username = EncryptionService.encrypt_field(pwd.username) 
        pwd.keyword = EncryptionService.encrypt_field(pwd.keyword) 
        pwd.description = EncryptionService.encrypt_field(pwd.description) 
        pwd.category = EncryptionService.encrypt_field(pwd.category) 
        
    @classmethod
    def map_to_password(cls, row):
        """
        Mapea una fila de la base de datos a un objeto Password.
        """
        # Desencriptar los campos sensibles obtenidos de la base de datos
        url = EncryptionService.decrypt_field(row[1]) 
        username = EncryptionService.decrypt_field(row[2]) 
        keyword = EncryptionService.decrypt_field(row[3]) 
        description = EncryptionService.decrypt_field(row[4]) 
        category = EncryptionService.decrypt_field(row[5]) 
        user_id = row[6]
        password = Password(url, username, keyword, description, category, user_id)
        password.id = row[0]  # Configura el ID después de crear la instancia
        password.created_at = row[7]  # Establece la fecha de creación
        password.updated_at = row[8]  # Establece la fecha de actualización
        return password 
    
    @classmethod
    def get_all_passwords(cls):
        try:
            conn = get_connection()
            passwords = []
            with conn.cursor() as cursor:
                cursor.execute("SELECT id, url, username, keyword, description, category, user_id, created_at, updated_at FROM password")
                resulset = cursor.fetchall()
                cursor.close()
                for row in resulset:
                    password = cls.map_to_password(row)
                    passwords.append(password.to_JSON())
            conn.close()    
            return passwords
        except Exception as ex:
            raise ex
        
    @classmethod
    def get_password_byID(cls, id):
        try:
            conn = get_connection()
            with conn.cursor() as cursor:
                cursor.execute("SELECT id, url, username, keyword, description, category, user_id, created_at, updated_at FROM password WHERE id = %s",(id,))
                row = cursor.fetchone()
                #cursor.close()
                password = None
                if row is not None:
                    password = cls.map_to_password(row)
                    password = password.to_JSON()
            conn.close()    
            return password
        except Exception as ex:
            raise ex    

    @classmethod
    def get_password_byUserID(cls, user_id):
        try:
            conn = get_connection()
            passwords = []
            with conn.cursor() as cursor:
                cursor.execute("SELECT id, url, username, keyword, description, category, user_id, created_at, updated_at FROM password WHERE user_id = %s",(user_id))
                resulset = cursor.fetchall()
                cursor.close()
                for row in resulset:
                    password = cls.map_to_password(row)
                    passwords.append(password.to_JSON())
            conn.close()    
            return passwords
        except Exception as ex:
            raise ex    
        
    @classmethod
    def add_password(cls, pwd):
        try:
            conn = get_connection()
            with conn.cursor() as cursor:
                # Encriptar los campos antes de insertar en la base de datos
                cls.encrypt_password_fields(pwd)
                cursor.callproc(
                    'insert_password',
                    (
                        pwd.id, pwd.url, pwd.username, pwd.keyword, pwd.description,
                        pwd.category, pwd.user_id, pwd.created_at, pwd.updated_at
                    )
                )
                affected_rows = cursor.rowcount
                conn.commit()
            conn.close()    
            return affected_rows
        except Exception as ex:
            raise ex    
    

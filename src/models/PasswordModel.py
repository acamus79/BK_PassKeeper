from database.db import get_connection
from .entities.Password import Password

class PasswordModel():
    
    @classmethod
    def get_all_passwords(self):
        try:
            conn = get_connection()
            passwords = []
        
            with conn.cursor() as cursor:
                cursor.execute("SELECT id, url, username, keyword, description, category FROM password")
                resulset = cursor.fetchall()
                #cursor.close()
                for row in resulset:
                    object=Password(row[0], row[1], row[2], row[3], row[4], row[5])
                    passwords.append(object.to_JSON())
            
            conn.close()    
            return passwords
        
        except Exception as ex:
            raise ex
        
        
        
        
        


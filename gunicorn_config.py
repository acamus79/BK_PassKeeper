bind = '0.0.0.0:8000'  # Especifica la dirección y el puerto en el que Gunicorn debe escuchar
workers = 4  # Número de trabajadores Gunicorn
timeout = 60  # Tiempo de espera en segundos para las solicitudes

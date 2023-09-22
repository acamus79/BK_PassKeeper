bind = '0.0.0.0:8000'  # Especifica la dirección y el puerto en el que Gunicorn debe escuchar
workers = 4  # Número de trabajadores Gunicorn
timeout = 60  # Tiempo de espera en segundos para las solicitudes
preload_app = True  # Carga la aplicación antes de que se inicien los trabajadores

# Configuración adicional para encabezados proxy si es necesario
forwarded_allow_ips = '*'  # Permite todas las IPs para encabezados proxy

# Ruta al archivo de registro
accesslog = '-'  # Registra los accesos en la salida estándar

# Ruta al archivo de error
errorlog = '-'  # Registra los errores en la salida estándar

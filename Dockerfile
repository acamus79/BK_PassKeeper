FROM python:3.11

WORKDIR /code/src

# Copia el archivo de configuración de Gunicorn
COPY gunicorn_config.py /code/gunicorn_config.py

COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./src /code/src

# Ejecuta Gunicorn con la configuración proporcionada
CMD ["gunicorn", "-c", "/code/gunicorn_config.py", "main:app", "--proxy-headers"]

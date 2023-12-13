# Modelamiento-2023

Repositorio fastapi para API generadora de numeros aleatorios.

El proyecto está escrito en Python, que se comunica con una aplicación web creada usando JavaScript, CSS (Bootstrap5) y HTML mediante FastAPI.

En el directorio base se encuentran todos los códigos de cada uno de los métodos para generar números aleatorios vistos en clases.

La visualización está dentro del directorio static.

### Instalación de dependencias

Se recomienda usar un entorno virtual de Python3, y dentro de este, instalar todas las dependencias necesarias para el funcionamiento del proyecto mediante el archivo "requirements.txt", para ello ingresar el comando:

```bash
pip install requirements
```
### Para usar fastapi localmente (asumiendo que ya se tiene Python 3 o más)
```bash
pip install fastapi uvicorn
```
### para lanzar el servidor en el localhost:8000 desde uvicorn desde la terminal:
```bash
uvicorn main:app --reload
```
(desde el directorio en donde se encuentre el "main.py" que es donde se encuentra el archivo principal que funciona como interconexión entre los algoritmos realizados en Python y la aplicación Web.

### Pasos realizados para crear desplegar fastapi en vercel

En el entorno virtual, generar el archivo con los requerimientos:
pip freeze > requirements.txt

El html incrustado en el main es modificable.

Basado en el ejemplo de:
https://github.com/mabdullahadeel/vercel-fastapi-deployment.git

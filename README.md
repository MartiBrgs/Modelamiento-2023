# Modelamiento-2023

Repositorio fastapi para API generadora de numeros aleatorios

### Para usar fastapi localmente

pip install fastapi uvicorn

### para lanzar el servidor en el localhost:8000 desde uvicorn desde la terminal:

uvicorn main:app --reload

### Pasos realizados para crear desplegar fastapi en vercel

En el entorno virtual, generar el archivo con los requerimientos:
pip freeze > requirements.txt

El html incrustado en el main es modificable.

Basado en el ejemplo de:
https://github.com/mabdullahadeel/vercel-fastapi-deployment.git

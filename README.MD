
#1.Crear un entorno virtual : pip install virtualenv
#Luego llamar el virtualenv en mi caso llame la carpeta venv :virtualenv venv
#Activar la carpeta si es windows: venv\Scripts\activate
#Paquetes que se necesitan instalar
#pip install flask
#pip install flask_sqlalchemy
#pip install pymysql
#pip install marshmallow

#Nota : La bd esta en mysql crear base de datos llamada heippi-api
##ENDPOINTS 
#127.0.0.1:5000/hospitales -> Obtiene todos los hospitales registrados
#127.0.0.1:5000/hospitales (POST)-> Crea los hospitales registrados
#127.0.0.1:5000/hospitales/id (DELETE)-> elemina los hospitales registrados
#127.0.0.1:5000/hospitales/id (PUT)-> actualiza los hospitales registrados

#127.0.0.1:5000/pacientes -> Obtiene todos los hospitales registrados
#127.0.0.1:5000/pacientes (POST)-> Crea los hospitales registrados
#127.0.0.1:5000/pacientes/id (DELETE)-> elemina los hospitales registrados
#127.0.0.1:5000/pacientes/id (PUT)-> actualiza los hospitales registrados

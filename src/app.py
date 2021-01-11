#Importar todas las librerias necesarias
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow
#3Arranque del servdor y configuración de la bd
app = Flask(__name__)
app.config['SQL_ALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/heippi-api'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'false' 
#Instanciar los objetos de sql y marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

#Modelo del hospital
class Hospital(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(70), unique=True)
    direccion = db.Column(db.String(100))
    servicios = db.Column(db.String(100))
    telefono = db.Column(db.Integer)

    def __init__(self, nombre, direccion, servicios, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.servicios = servicios
        self.telefono = telefono

db.create_all()

class HospitalSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nombre', 'servicios', 'telefono')


hospital_schema = HospitalSchema()
hospitales_schema = HospitalSchema(many=True)

#Modelo del paciente
class Paciente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(70), unique=True)
    direccion = db.Column(db.String(100))
    telefono = db.Column(db.Integer)

    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
       
        self.telefono = telefono

db.create_all()

class PacienteSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nombre',  'telefono')


paciente_schema = PacienteSchema()
pacientes_schema = PacienteSchema(many=True)
##Rutas del crud Hospital
@app.route('/hospitales', methods=['Post'])
def create_hospital():
  nombre = request.json['nombre']
  direccion = request.json['direccion']
  servicios = request.json['servicios']
  telefono = request.json['telefono']

  new_hospital= Hospital(nombre, direccion, servicios, telefono)

  db.session.add(new_hospital)
  db.session.commit()

  return hospital_schema.jsonify(new_hospital)

@app.route('/hospitales', methods=['GET'])
def get_hospitales():
  all_hospitales = Hospital.query.all()
  result = hospitales_schema.dump(all_hospitales)
  return jsonify(result)

@app.route('/hospitales/<id>', methods=['GET'])
def get_hospital(id):
  hospital = Hospital.query.get(id)
  return hospital_schema.jsonify(hospital)

@app.route('/hospitales/<id>', methods=['PUT'])
def update_hospital(id):
  hospital = Hospital.query.get(id)

  nombre = request.json['nombre']
  direccion = request.json['direccion']
  servicios = request.json['servicios']
  telefono = request.json['telefono']

  hospital.nombre = nombre
  hospital.direccion = direccion
  hospital.servicios = servicios
  hospital.telefono = telefono

  db.session.commit()

  return hospital_schema.jsonify(hospital)

@app.route('/hospitales/<id>', methods=['DELETE'])
def delete_hospital(id):
  hospital = Hospital.query.get(id)
  db.session.delete(hospital)
  db.session.commit()
  return hospital_schema.jsonify(hospital)


##Fin de las rutas 


@app.route('/pacientes', methods=['Post'])
def create_paciente():
  nombre = request.json['nombre']
  direccion = request.json['direccion']
  
  telefono = request.json['telefono']

  new_paciente= Paciente(nombre, direccion,  telefono)

  db.session.add(new_paciente)
  db.session.commit()

  return paciente_schema.jsonify(new_paciente)

@app.route('/pacientes', methods=['GET'])
def get_pacientes():
  all_pacientes = Paciente.query.all()
  result = pacientes_schema.dump(all_pacientes)
  return jsonify(result)

@app.route('/pacientes/<id>', methods=['GET'])
def get_paciente(id):
  paciente = Paciente.query.get(id)
  return paciente_schema.jsonify(paciente)

@app.route('/pacientes/<id>', methods=['PUT'])
def update_paciente(id):
  paciente = Paciente.query.get(id)

  nombre = request.json['nombre']
  direccion = request.json['direccion']
  
  telefono = request.json['telefono']

  paciente.nombre = nombre
  paciente.direccion = direccion
  
  paciente.telefono = telefono

  db.session.commit()

  return paciente_schema.jsonify(paciente)

@app.route('/pacientes/<id>', methods=['DELETE'])
def delete_paciente(id):
  paciente = Paciente.query.get(id)
  db.session.delete(paciente)
  db.session.commit()
  return paciente_schema.jsonify(paciente)





@app.route('/', methods=['GET'])
def index():
    return jsonify({'message': 'Bienvenido a mi API!!'})



if __name__ == "__main__":
    app.run(debug=True)
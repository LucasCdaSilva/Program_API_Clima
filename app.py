from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from fastapi import FastAPI
import requests

app = Flask(__name__)
app.config['DEBUG']=True

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:senha@localhost/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


#Classe do modelo do banco de dados
class Cidade_api(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    temperatura = db.Column(db.Float, nullable=False)
    veloc_vent = db.Column(db.Float, nullable=False)
    press = db.Column(db.Float, nullable=False)
    humi = db.Column(db.Float, nullable=False)
    longi = db.Column(db.String, nullable=False)
    lati = db.Column(db.String, nullable=False)

db.create_all()

#Integracao do sistema com o front
@app.route('/', methods=['GET', 'POST'])
def index():
    
    try:
        url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}"
        
        api_key = "9074e0fa3d8a088ea546ebf944404123"

        search_cidade = 'Jau'
            
        data = requests.get(url.format(search_cidade, api_key)).json()

        if request.method == 'POST':
            search_cidade = request.form.get('cidade')
            
            data = requests.get(url.format(search_cidade, api_key)).json()

            db.session.add(Cidade_api(nome=search_cidade, temperatura= data['main']['temp'], veloc_vent=data['wind']['speed'], press=data['main']['pressure'],humi=data['main']['humidity'],longi=data['coord']['lon'],lati=data['coord']['lon']))
            db.session.commit()

        clima ={
                "nome" : search_cidade,
                "temp" : data['main']['temp'],
                "vel_vento" : data['wind']['speed'],
                "press" : data['main']['pressure'],
                "humi" : data['main']['humidity'],
                "lon" : data['coord']['lon'],
                "lat" : data['coord']['lat'],
                }

        return render_template('index.html',clima=clima)

    except Exception as error:
        print('Error: {}'.format(error))

@app.route('/api/<string:name>', methods=['GET'])
def home(name):
    select = Cidade_api.query.filter_by(nome=name).first()

    json_string = {
        "Nome": select.nome,
        "Temperatura": select.temperatura,
        "Velocidade do Vento": select.veloc_vent,
        "Humidade": select.humi,
        "Pressao Atmosferica": select.press,
        "Longitude": select.longi,
        "Latitude": select.lati,
    }
    
    return(json_string)



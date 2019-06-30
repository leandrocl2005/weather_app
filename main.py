#!/usr/bin/env python

# bibliotecas
from flask import Flask, render_template, request
import requests


# chave da api
API_KEY = '9e413110bb5c662ffe88e53d4338cd8a'

# modelo de requisicao
API_URL = ('http://api.openweathermap.org/data/2.5/weather?q={}&mode=json&units=metric&appid={}')

# criando o app
app = Flask(__name__)

# renderizando a página para escolha da cidade
@app.route('/')
def index():
    return render_template(
        'weather.html',
        data = [
            {'name':'Uberaba, Brazil'},
            {'name':'Campinas, Brazil'},
            {'name': 'Dubai'}
        ]
    )

# renderizando a página para mostra dos resultados
@app.route("/result" , methods=['GET', 'POST'])
def result():
    data = []
    error = None
    city = request.form.get('comp_select')
    try:
        resp = requests.get(API_URL.format(city, API_KEY)).json()
    except:
        resp = None
    if resp:
       data.append(resp)
       print(data)
    if len(data) != 2:
        error = 'Bad Response from Weather API'
    return render_template(
        'result.html',
        data=data,
        error=error)

if __name__=='__main__':
    app.run(port=5000,debug=True)

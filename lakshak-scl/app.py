from flask import Flask
from flask import render_template
import requests
import json
app= Flask(__name__)
@app.route('/')
def index():
	return render_template('index.html')
@app.route('/head')
def head():
   return render_template('head.html')
@app.route('/dictionary')
def dictionary():
    return render_template('dictionary.html')
@app.route('/<word>')
def wordfun(word):
    url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"
    querystring = {"term":word}
    headers = {
    'x-rapidapi-key': "6c448dfc38mshb6cd2cda63c8760p12ad6ajsn998216197922",
    'x-rapidapi-host': "mashape-community-urban-dictionary.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    data=json.loads(response.text)
    return render_template('word.html', data=data)
@app.route('/snake')
def snake():
	return render_template('snake.html')
@app.route('/tic')
def tic():
	return render_template('tic.html')
@app.route('/todo')
def todo():
	return render_template('todo.html')
@app.route('/timer')
def timer():
    return render_template('timer.html')

if __name__ == '__main__':
	
	app.run(host='localhost',port=3456)
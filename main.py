from flask import Flask, render_template, redirect, request,  redirect, url_for
from flask_bootstrap import Bootstrap
import requests

app = Flask(__name__)
bootstrap = Bootstrap(app)
 
@app.route('/', methods=['post', 'get'])
def index(): 
   return render_template('index.html')

@app.route('/about/')
def about():
    return render_template('about.html', )

@app.route('/details/<title>')
def details(title): 
    url = "http://api.yummly.com/v1/api/recipe/"+title+"?_app_id=dc0de3a6&_app_key=e18e7e77ab27a1004c0d89ab885b5507"
    response=requests.get(url)
    jsonRecipes = response.json() 
    return render_template('details.html' , jsonRecipes=jsonRecipes )

@app.route("/search/", methods=['POST'])
def search():
    if request.method=="POST":
        word=request.form["word"]  
    url='http://api.yummly.com/v1/api/recipes?_app_id=dc0de3a6&_app_key=e18e7e77ab27a1004c0d89ab885b5507&q='+word
    
    response=requests.get(url)
    jsonRecipes = response.json() 
    
    return render_template('search.html', jsonRecipes=jsonRecipes)

@app.route("/login/", methods=['POST'])
def login():
    msg=''
    if request.method=="POST":
        email=request.form["email"]
        password=request.form["password"]

        if email == 'ja' and password == 'flask':
           msg = 'Korisnicko ime i zaporka su ispravne'
        else:
           msg = 'Korisnicko ime i zaporka su neispravne'

    return redirect(url_for('index', message=msg))
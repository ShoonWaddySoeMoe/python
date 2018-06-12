from flask import Flask
 app = Flask(_name_)

@app.route('/')
def hello_world():
return 'Hello, World!'

 if _name_ == "_main_":
app.run()
from flask import Flask
from flask import render_template

app = Flask(_name_)

@app.route("/")
def index():
greeting = "Hello World"
return render_template("index.html", greeting=greeting)

 if _name_ == "_main_":
app.run()
ex50.py


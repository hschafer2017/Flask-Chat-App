import os 
from flask import Flask, redirect, render_template, request 
import datetime

app = Flask(__name__) 

messages = []

@app.route('/')
def get_index(): 
        return render_template('index.html')

@app.route('/login', methods = ["POST"])
def get_userpage():
    username = request.form.get('query')
    return redirect(username) 

@app.route("/<username>")
def get_name(username):
    return str(username) + str(messages) + render_template("chatpage.html")
    
    
@app.route("/<username>/<message>", methods = ["POST"])
def get_name_message(username,message):
    timing = datetime.datetime.now()
    message = timing.strftime("%H:%M") + " <strong>" + username + "</strong>" + ": " + request.form.get("message")
    messages.append(message)
    return render_template("chatpage.html") + username + str(messages).format(username,message)


app.run(host = os.getenv('IP'), port = int(os.getenv('PORT')), debug = True)

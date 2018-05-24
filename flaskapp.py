import os 
from flask import Flask, redirect, render_template, request 
import datetime

app = Flask(__name__) 

messages = []

@app.route('/')
def get_index(): 
        return "Welcome to the chat!"

@app.route('/<username>')
def get_userpage(username):
    return "<h2>Hello, {0}. You've joined the chat!</h2>".format(username)

@app.route("/<username>/<message>")
def get_name_message(username,message):
    timing = datetime.datetime.now()
    message = timing.strftime("%H:%M") + " <strong>" + username + "</strong>" + ": " + message
    messages.append(message)
    return str(messages)


app.run(host = os.getenv('IP'), port = int(os.getenv('PORT')), debug = True)
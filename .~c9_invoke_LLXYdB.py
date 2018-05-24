import os
from flask import Flask , redirect, render_template, request
import datetime

app = Flask(__name__)

messages=[]

@app.route('/')
def get_index():
    return render_template('index.html')
    
@app.route('/login', methods = ["POST"])
def get_userpage():
    username = request.form.get('query')
    return redirect(username)
    
@app.route("/<username>")
def get_name(username):
    return render_template("chatpage.html", username=username, all_the_messages = messages)

@app.route('/<username>/new', methods=['POST'])
def add_message(username):
    timing = datetime.datetime.now()
    message = timing.strftime("%H:%M") + ": " + username + ": " + request.form.get("message").format(username)
    messages.append(message)
    f = open("messages.txt", "a")  
    lines = f.write(str(messages)+"\n")
    f.close()                                      
    return redirect(username) 
    
app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)
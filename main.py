from flask import Flask, request, redirect
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__),
    'templates')

jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(template_dir))

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=['POST', 'GET'])
def login():
    template = jinja_env.get_template('login.html')
    return template.render()

@app.route('/login', methods=['POST', 'GET'])
def test():
    username = request.form['username']
    password= request.form['password']
    password_confirm = request.form['password_confirm']
    email = request.form['email']

    username_error = False
    password_error = False
    confirm_error = False
    email_error = False

    #username errors
    if len(username) < 3 or len(username) > 20:
        username_error = True
    for char in username:
        if char == " ":
            username_error = True 
        
    #password errors
    if len(password) < 3 or len(password) > 20:
        password_error = True
    for char in password:
        if char == " ":
            password_error = True
    #confirm error
    if password != password_confirm:
        confirm_error = True

    #email errors
    if email:
        period_check = False
        at_check = False
        for char in email:
            if char == " ":
                email_error = True
            if char == ".":
                period_check = True
            if char == "@":
                at_check = True
        if period_check == False or at_check == False:
            email_error = True

    #SUCESSS
    if username_error == False and password_error == False and confirm_error == False and email_error == False:
        return "<h1>Welcome " + username + "</h1>"
    else:
        template = jinja_env.get_template('login.html')
        return template.render(username = username, email = email, username_error = username_error, password_error = password_error, confirm_error = confirm_error, email_error = email_error)

app.run()
"""
Login module:
  - registration of new users;
  - authorization of registered users
"""

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/login/', methods=['post', 'get'])
def login():
    message = 'Please login or register a new user'
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

    if username == 'admin' and password == 'admin':
        message = "Login successful!"
    else:
        message = "Error! Wrong username or password"

    return render_template('login.html', message=message)

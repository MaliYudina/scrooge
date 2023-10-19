from flask import Flask, request, render_template
from flask_restful import Resource, Api
from db_process.portfolio_db import show_portfolio

# import sys
# import os
#
#
# project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
# sys.path.append(project_root)

app = Flask(__name__)
app.debug = True

# http://0.0.0.0:5000/welcome


# class topic_tags(Resource):
#     def get(self):
#         return {'hello': 'world world'}
#
# api.add_resource(topic_tags, '/')

@app.route('/')
def home():
    return "Hello, World!"  # return a string


@app.route('/welcome')
def welcome():
    return render_template('welcome.html')  # render a template

@app.route('/login')
def login():
    return render_template('login.html')  # render a template

@app.route('/register')
def register():
    return render_template('register.html')  # render a template

@app.route('/portfolio')
# @app.route('/portfolio/<data>')
def portfolio():
    data = show_portfolio()
    return render_template('portfolio.html')  # render a template




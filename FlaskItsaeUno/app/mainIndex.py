'''
Created on 18/2/2015

@author: PC06
'''
from app import app
from flask import Flask

@app.route("/")
def index():
    return "Hola mundo"


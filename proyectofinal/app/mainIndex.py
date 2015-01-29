'''
Created on 29/1/2015
jkhkhkjhkjhkj
@author: PERSONAL
'''

from app import app
from flask import Flask
#from django.shortcuts import render
from flask import render_template, request , redirect, url_for
#from ec.edu.itsae.dao import PersonaDAO



@app.route("/")
def index():
    return render_template("login.html")



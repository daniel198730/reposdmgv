'''
Created on 19/2/2015

@author: PC29
'''

from app import app
from flask import render_template, request, url_for, redirect
from ec.edu.itsae.dao import PersonaDAO



@app.route("/")
def index():
    return render_template("login.html")


@app.route("/login")
def loginX():
    
    usuario=str(request.args.get('username'))
    clave=str(request.args.get('password'))
    report=PersonaDAO.PersonaDAO().validarUsuario(usuario, clave)
    if len(report)==1:
        
        return redirect(url_for("main"))

    else :
        return redirect(url_for("index"))
    
@app.route("/main")
def main():
    return render_template("main.html")    
    
    
    


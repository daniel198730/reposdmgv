# --

'''
Created on 19/2/2015

@author: PC29
'''

from flask import Flask,render_template

app=Flask(__name__)


@app.route("/")

def inicio():
    X="Interaccion entre Python y HTML"
    return render_template("prueba.html", dato=X)


@app.route("/itsae")

def Itsae():
    return  "Hola Mundo Itsae"



if __name__ == '__main__':
    app.run("127.0.0.1", 5050, True)
    
    

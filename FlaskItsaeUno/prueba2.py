#-*- coding:utf-8 -*-
'''
Created on 18/2/2015

@author: PC06
'''
'''
from flask import Flask, render_template


app=Flask(__name__)


@app.route("/")
def inicio():
    X="Interaccion entre Python y HTML"
    print X
    return render_template("prueba.html", dato=X)


@app.route("/itsae")
def itsae():
    return "Hola Mundo Itsae"



if __name__ == '__main__':
    app.run("127.0.0.1", 5050, True)
'''
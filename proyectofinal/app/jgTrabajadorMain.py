from app import app
from ec.edu.itsae.dao import jgTrabajadorDAO
from flask import render_template, request, redirect, url_for



@app.route("/mainTrabajador")
def trabajadormain():
    
    objR=jgTrabajadorDAO.TrabajadorDAO().reportarTrabajador()
    return render_template("trabajador.html", data=objR)

@app.route("/addTrabajador", methods=['POST'])
def addTrabajador():
    idpersona=request.form.get('idpersona', type=str)
    usuario=request.form.get('usuario', type=str)
    clave=request.form.get('clave', type=str)
    estado=request.form.get('estado', type=int)
    fecha=request.form.get('fecha', type=str)
    idtipo=request.form.get('idtipo', type=str)
   
 
    jgTrabajadorDAO.TrabajadorDAO().insertarTrabajador(idpersona, usuario, clave, estado, fecha, idtipo)
    return redirect(url_for('trabajadormain')) 

    jgTrabajadorDAO.TrabajadorDAO().eliminarTrabajador(idpersona, usuario, clave, estado, fecha, idtipo)
    return redirect(url_for('trabajadormain')) 



@app.route("/buscarAutoTrabajador")
def buscarAutoTrabajador():
    usuario=str(request.args.get('term'))
    objR=jgTrabajadorDAO.TrabajadorDAO().buscarTrabajadorUsuario(usuario)
    return objR



@app.route("/buscarDatotrabajador")
def buscarDatotrabajador():
    usuario=str(request.args.get('busuario'))
    objR=jgTrabajadorDAO.TrabajadorDAO().buscarTrabajadorDato(usuario)
    return render_template("trabajador.html", data=objR)
    return objR
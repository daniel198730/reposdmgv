'''
Created on 25/2/2015

@author: PC29
'''
from ec.edu.itsae.conn import DBcon
import json
class TrabajadorDAO(DBcon.DBcon):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
        pass
    
    
    
    
    def reportarTrabajador(self):
        con=self.conexion().connect().cursor()   
        con.execute(" Select * from trabajador ")
        reporte=con.fetchall()
        return reporte
    
    def insertarTrabajador(self,idpersona, usuario, clave, estado, fecha, idtipo):
        con=self.conexion().connect()
        sql="""insert into trabajador(idpersona, usuario, clave, estado, fecha_acceso, idTipoTrabajador) values('%s', '%s', '%s', '%i', '%s', '%s')""" % (idpersona, usuario, clave, estado, fecha, idtipo)
        print sql
        with con:
            cursor=con.cursor()
            cursor.execute(sql)
            
            
    def eliminarTrabajador(self,idpersona, usuario, clave, estado, fecha, idtipo):
        con=self.conexion().connect()
        sql="""delete from trabajador(idpersona, usuario, clave, estado, fecha_acceso, idTipoTrabajador) values('%s', '%s', '%s', '%i', '%s', '%s')""" % (idpersona, usuario, clave, estado, fecha, idtipo)
        print sql
        with con:
            cursor=con.cursor()
            cursor.execute(sql)        
        
        
        
        
    def buscarTrabajadorUsuario(self, datobuscado):
        con=self.conexion().connect().cursor()   
        con.execute(""" Select CONCAT(idpersona,' ',usuario) as value, idpersona as id from trabajador where upper(CONCAT(idpersona,' ',usuario)) like upper('%s')"""  % ("%"+datobuscado+"%"))
        reporte=con.fetchall()
        columna=('value', 'id')
        lista=[]
        
        for row in reporte:
            lista.append(dict(zip(columna, row)))
            return json.dumps(lista, indent=2)
        
        
        
            
        
    def buscarTrabajadorDato(self, datobuscado):
        con=self.conexion().connect().cursor()   
        sql=""" Select * from trabajador where upper(CONCAT(idpersona,' ',usuario))
         like upper('%s')"""  % ("%"+datobuscado+"%")
        con.execute(sql)
        reporte=con.fetchall()
        return reporte     
        
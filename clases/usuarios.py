import sys
from sys import setprofile
from typing import NoReturn
import pymysql
import os
sys.path.append("C:\\RRHH\\DB\\")
import conexion as c


class usuarios:
    
    def __init__(self,nombre,apellido,dni,mail,domicilio,foto,nacimiento,puesto,disp_horaria,disp_reloc,habilidades,url,titulo_prof,educacion,exp,cv,apto):
        self.nombre=nombre
        self.apellido=apellido
        self.dni=dni
        self.mail=mail
        self.domicilio=domicilio
        self.foto=foto
        self.nacimiento=nacimiento
        self.puesto=puesto
        self.disp_horaria=disp_horaria
        self.disp_reloc=disp_reloc
        self.habilidades=habilidades
        self.url=url
        self.titulo_prof=titulo_prof
        self.educacion=educacion
        self.exp=exp
        self.cv=cv
        self.apto=apto
        print("se creo usuario correctamente")
        self.alta_usuario()



    def alta_usuario(self):
        a=c.start_connection()
        cursor=a.cursor()
        try:
            cursor.execute("USE RRHH;")
            query = "INSERT INTO usuarios(nombre,apellido,dni,mail,domicilio,foto,nacimiento,puesto,disp_horaria,disp_reloc,habilidades,url,titulo_prof,educacion,exp,cv,apto) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            values = (self.nombre,self.apellido,self.dni,self.mail,self.domicilio,self.foto,self.nacimiento,self.puesto,self.disp_horaria,self.disp_reloc,self.habilidades,self.url,self.titulo_prof,self.educacion,self.exp,self.cv,self.apto)
            cursor.execute(query,values)
            a.commit()
            print("se dio alta usuario correctamente")
        except pymysql.err.OperationalError as err:
            print("Hubo un error:", err)
        c.close_connection(a)

    def contar_filas_busqueda(param):
        a = c.start_connection()
        cursor = a.cursor()
        cursor.execute("USE RRHH;")
        query = "SELECT COUNT(*) FROM usuarios WHERE dni=%s or nombre=%s or apellido=%s or puesto=%s"
        cursor.execute(query, (param, param,param,param))
        a.commit()
        b = cursor.fetchall()
        b = str(b[0][0])
        n = int(b)
        c.close_connection(a)
        return n
    

    def buscar_user(param):
        a = c.start_connection()
        cursor = a.cursor()
        cursor.execute("USE RRHH;")
        query = ("SELECT dni,apellido,nombre,mail,puesto,apto FROM usuarios WHERE dni=%s or nombre=%s or apellido=%s or puesto=%s")
        cursor.execute(query, (param, param,param,param))
        data = cursor.fetchall()
        a.commit()
        return data
        
    def buscar_user_rows(param):
        a = c.start_connection()
        cursor = a.cursor()
        cursor.execute("USE RRHH;")
        query = ("SELECT dni,apellido,nombre,mail,puesto,apto FROM usuarios WHERE dni=%s or nombre=%s or apellido=%s or puesto=%s")
        data = cursor.execute(query, (param, param,param,param))
        a.commit()
        return data

    def mostrar_user(dni):
        a = c.start_connection()
        cursor = a.cursor()
        cursor.execute("USE RRHH;")
        query = ("SELECT nombre,apellido,dni,mail,domicilio,foto,nacimiento,puesto,disp_horaria,disp_reloc,habilidades,url,titulo_prof,educacion,exp,cv,apto FROM usuarios WHERE dni=%s")
        cursor.execute(query,dni)
        data = cursor.fetchall()
        a.commit()
        return data


    def ab_usuario_apto(dni):
        a=c.start_connection()
        cursor=a.cursor()
        try: 
            query = "UPDATE usuarios set apto= IF(apto = '0', apto + 1, apto-1) WHERE dni=%s"
            values = dni
            cursor.execute(query, values)
            a.commit()
            print("se MODIFICO usuario correctamente")
        except pymysql.err.OperationalError as err:
            print("Hubo un error:", err)
        c.close_connection(a)


    def modificar_datos_user(dniv,dnin,nombre,apellido,mail,domicilio,foto,nacimiento,puesto,disp_horaria,disp_reloc,habilidades,url,titulo_prof,educacion,exp,cv):
        a=c.start_connection()
        cursor=a.cursor()
        query = "SELECT idusuarios FROM usuarios WHERE dni=%s"
        values = dniv
        cursor.execute(query, values)
        a.commit()
        b = cursor.fetchall()
        idu = str(b[0][0])
        try:
            query = "UPDATE usuarios SET nombre=%s WHERE idusuarios=%s"
            values = (nombre,idu)
            cursor.execute(query, values)
            a.commit()
            query = "UPDATE usuarios SET apellido=%s WHERE idusuarios=%s"
            values = (apellido,idu)
            cursor.execute(query, values)
            a.commit()  
            query = "UPDATE usuarios SET dni=%s WHERE idusuarios=%s"
            values = (dnin,idu)
            cursor.execute(query, values)
            a.commit() 
            query = "UPDATE usuarios SET mail=%s WHERE idusuarios=%s"
            values = (mail,idu)
            cursor.execute(query, values)
            a.commit()
            query = "UPDATE usuarios SET domicilio=%s WHERE idusuarios=%s"
            values = (domicilio,idu)
            cursor.execute(query, values)
            a.commit()
            query = "UPDATE usuarios SET foto=%s WHERE idusuarios=%s"
            values = (foto,idu)
            cursor.execute(query, values)
            a.commit()
            query = "UPDATE usuarios SET nacimiento=%s WHERE idusuarios=%s"
            values = (nacimiento,idu)
            cursor.execute(query, values)
            a.commit()
            query = "UPDATE usuarios SET puesto=%s WHERE idusuarios=%s"
            values = (puesto,idu)
            cursor.execute(query, values)
            a.commit()
            query = "UPDATE usuarios SET disp_horaria=%s WHERE idusuarios=%s"
            values = (disp_horaria,idu)
            cursor.execute(query, values)
            a.commit()
            query = "UPDATE usuarios SET disp_reloc=%s WHERE idusuarios=%s"
            values = (disp_reloc,idu)
            cursor.execute(query, values)
            a.commit()
            query = "UPDATE usuarios SET habilidades=%s WHERE idusuarios=%s"
            values = (habilidades,idu)
            cursor.execute(query, values)
            a.commit() 
            query = "UPDATE usuarios SET url=%s WHERE idusuarios=%s"
            values = (url,idu)
            cursor.execute(query, values)
            a.commit()
            query = "UPDATE usuarios SET apellido=%s WHERE idusuarios=%s"
            values = (apellido,idu)
            cursor.execute(query, values)
            a.commit()
            query = "UPDATE usuarios SET apellido=%s WHERE idusuarios=%s"
            values = (apellido,idu)
            cursor.execute(query, values)
            a.commit()
            query = "UPDATE usuarios SET titulo_prof=%s WHERE idusuarios=%s"
            values = (titulo_prof,idu)
            cursor.execute(query, values)
            a.commit()
            query = "UPDATE usuarios SET educacion=%s WHERE idusuarios=%s"
            values = (educacion,idu)
            cursor.execute(query, values)
            a.commit()
            query = "UPDATE usuarios SET exp=%s WHERE idusuarios=%s"
            values = (exp,idu)
            cursor.execute(query, values)
            a.commit()
            query = "UPDATE usuarios SET cv=%s WHERE idusuarios=%s"
            values = (cv,idu)
            cursor.execute(query, values)
            a.commit()
            
            print("se modifico  usuario correctamente")
        except pymysql.err.OperationalError as err:
            print("Hubo un error:", err)
        c.close_connection(a)

def contar_filas():
    a = c.start_connection()
    cursor = a.cursor()
    cursor.execute("USE RRHH;")
    query = "SELECT COUNT(*) FROM usuarios"
    cursor.execute(query)
    a.commit()
    b = cursor.fetchall()
    b = str(b[0][0])
    n = int(b)
    c.close_connection(a)
    return n

def listar_user():
        a = c.start_connection()
        cursor = a.cursor()
        cursor.execute("USE RRHH;")
        try:
            query = "SELECT dni,apellido,apellido,mail,puesto,apto FROM usuarios"
            cursor.execute(query)
            user = cursor.fetchall()
            a.commit()
        except pymysql.err.OperationalError as err:
            print("Hubo un error:", err)
        c.close_connection(a)
        return user
    



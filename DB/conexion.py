import pymysql
import os

# AXIOMAS Y OBLIGACIONES A LA HORA DE LA CODIFICACION:
# se abre conexion unicamente cuando estamos por usar la base de datos y al finalizar se la cierra
# cada de vez que se usar el cursor, posteriormente se lo cierra
# para la devolucion de datos de cursor se usara fetchall e intantaneamente se lo convertira


def start_connection():  # inicia conexion a db
    h = 'localhost'
    p = 3306
    u = os.environ.get('USER_MYSQL')
    ps = os.environ.get('PASSWORD_MYSQL')
    db = os.environ.get('DB_MYSQL')
    try:
        con = pymysql.Connect(host=h, port=p, user=u, password=ps, database=db)
        print(con, "\nse creo conexion")
    except pymysql.err.OperationalError as err:
        print("Hubo un error:", err)
        
    return con


def close_connection(con):  # cierra conexion a db
    try:
        con.close()
        print("se cerro conexion\n",con)
    except pymysql.err.OperationalError as err:
        print("Hubo un error:", err)


def borrar_tabla():  # borra tablas (posible modificacion futura: ingresar el nombre de la tabla y que la borre)
    # se usa "," para mas de una
    con=start_connection()
    q1="""drop database RRHH;"""
    q2="""create database RRHH;"""
    #q = "DROP TABLE IF EXISTS productos, usuarios,alojamiento,login,matriz,datosmatriz;"
    try:
        cur = con.cursor()
        cur.execute(q1)
        cur.execute(q2)
        cur.close()
        print("se borro las tablas con exito")
    except pymysql.err.OperationalError as err:
        print("Hubo un error:", err)
    close_connection(con)

def crear_tabla():  # crea una tabla (al iniciar por primera vez el programa se crearan todas)
    con=start_connection()
    q0="""CREATE DATABASE IF NOT EXISTS RRHH;"""

    q1="""USE RRHH;"""


    q2 = """CREATE TABLE IF NOT EXISTS usuarios (
    idusuarios INT UNSIGNED AUTO_INCREMENT PRIMARY KEY NOT NULL,
    nombre VARCHAR(20) NOT NULL,
    apellido VARCHAR(20) NOT NULL,
    dni VARCHAR(20) NOT NULL,
    mail VARCHAR(50) NOT NULL
    domicilio VARCHAR(50) NOT NULL,
    foto VARCHAR(20) NOT NULL,
    nacimiento DATE NOT NULL,
    disp_horaria BINARY(1) NOT NULL,
    disp_reloc BINARY(1) NOT NULL,
    habilidades VARCHAR(50) NOT NULL,
    url VARCHAR(20) NULL,
    portafolio VARCHAR(50) NULL,
    titulo_prof VARCHAR(50) NOT NULL,
    educacion VARCHAR(50) NOT NULL,
    experiencia VARCHAR(50) NOT NULL,
    cv VARCHAR(20) NOT NULL,
    apto BINARY(1) NOT NULL
    );"""

    try:
        cur = con.cursor()
        cur.execute(q0)
        cur.execute(q1)
        cur.execute(q2)
        cur.close()
        print("se creo las tablas con exito")
    except pymysql.err.OperationalError as err:
        print("Hubo un error:", err)
    close_connection(con)



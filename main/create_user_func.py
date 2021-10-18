import sys
import os
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore
import PyQt5
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import create_user
from create_user import Ui_MainWindow
from PIL import Image
sys.path.append("C:\\proyecto-final\\CLASES\\")
import usuarios as us

defaultImg = "Error.png"

class UsuarioWindow(QMainWindow):

    def __init__(self):
        super(UsuarioWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        ############# RECIBIMOS PROPORCIONES DE LA PANTALLA ###########
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        ############## CENTRAMOS LA VENTANA #############
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

        #self.ui.pushButton_crear_usuario.clicked.connect(self.crearUser)
        self.ui.subirFoto_btn.clicked.connect(self.uploadImg)

        self.ui.crear_btn.clicked.connect(self.crearUser)

        #self.ui.pushButton_usuarios_2.clicked.connect(self.crearUser)
    
    #CREAR PRODUCTO NUEVO
    def crearUser(self):   
    
      #RECIBIR VALORES DE LA VENTANA
      apellido = self.ui.apellido_input.text()
      nom = self.ui.nombre_input.text()
      localidad = self.ui.localidad_input.text()
      dni = self.ui.dni_input.text()
      direccion = self.ui.direccion_input.text()
      provincia = self.ui.provincia_input.text()
      mail = self.ui.mail_input.text()
      telefono = self.ui.telefono_input.text()
      relocalizarse = self.ui.comboBox_relocalizarse.currentText()
      nacimiento = self.ui.nacimiento_date.date().toString("yyyy/MM/dd")
      disponibilidad = self.ui.comboBox.currentText()
      url = self.ui.url_input.text()
      educacion = self.ui.educacion_input.text()
      experiencia = self.ui.experiencia_input.toPlainText()
      titulos = self.ui.titulo_input.text()
      habilidades = self.ui.habilidades_input.text()
      

      if self.ui.radioButton_si.isCheckable():
          apto = 1
      else: apto = 0

      
      

      if nom=="" or apellido=="" or educacion or titulos or experiencia or habilidades  or telefono == "" or url =="" or provincia == "" or dni=="" or direccion =="" or localidad == ""  or dni=="" or localidad=="" or nacimiento=="":
        QtWidgets.QMessageBox.critical(self, "Error", "Ingrese todos los datos")
        return None

      if len(dni)!=8:
        QtWidgets.QMessageBox.critical(self, "Error", "Ingrese un dni existente")
        return None
      
      if disponibilidad=="Full Time":
        tipo="1"
      else:
        tipo="0"
      if relocalizarse=="Si":
        tipo="1"
      else:
        tipo="0"

      if us.ver_dni(dni) == 1:
        QtWidgets.QMessageBox.critical(self, "Error", "DNI Existente")
        return None
      else:
        user = us.usuarios(nom,apellido,dni,tipo,puesto,nacimiento,mail)
        user.alta_login(contraseña)
        self.close()
      #return(codigo,nombre,desc,cantidad,marca,venc,condicion,lote,fragil)
      


    def uploadImg(self):
        global defaultImg 
        size=(256,256)
        self.filename,ok = QFileDialog.getOpenFileName(self,"Upload Image","","Image Files (*.jpg *.png)")
        if ok:
            defaultImg = os.path.basename(self.filename)
            img=Image.open(self.filename)
            img=img.resize(size)
            img.save("C:\RRHH\img/{0}".format(defaultImg))

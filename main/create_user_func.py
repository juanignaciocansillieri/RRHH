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
sys.path.append("C:\\RRHH\\clases\\")
import usuarios as us

defaultImg = "Error.png"
curriculum = ""

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

        self.ui.subirFoto_btn.clicked.connect(self.uploadImg)
        self.ui.cargarCV_btn.clicked.connect(self.uploadCv)

        self.ui.crear_btn.clicked.connect(self.crearUser)

    
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
      educacion = self.ui.educacion_input.toPlainText()
      experiencia = self.ui.experiencia_input.toPlainText()
      titulos = self.ui.titulo_input.toPlainText()
      habilidades = self.ui.habilidades_input.toPlainText()
      puesto = self.ui.puesto_input.text()
      

      if self.ui.radioButton_si.isCheckable():
          apto = 1
      else: apto = 0

      
      

      if nom=="" or apellido=="" or educacion=="" or titulos=="" or experiencia=="" or habilidades==""  or telefono == "" or url =="" or provincia == "" or dni=="" or direccion =="" or localidad == ""  or dni=="" or localidad=="" or nacimiento=="" or puesto=="":
        QtWidgets.QMessageBox.critical(self, "Error", "Ingrese todos los datos")
        return None

      if len(dni)!=8:
        QtWidgets.QMessageBox.critical(self, "Error", "Ingrese un dni existente")
        return None
      
      if disponibilidad=="Full Time":
        disponibilidad="1"
      else:
        disponibilidad="0"
      if relocalizarse=="Si":
        relocalizarse="1"
      else:
        relocalizarse="0"

      domicilio=str(direccion+","+localidad+","+provincia)

      
      us.usuarios(nom,apellido,dni,mail,domicilio,defaultImg,nacimiento,puesto,disponibilidad,relocalizarse,habilidades,url,titulos,educacion,experiencia,curriculum,apto,telefono)
      self.close()
      


    def uploadImg(self):
        global defaultImg 
        size=(256,256)
        self.filename,ok = QFileDialog.getOpenFileName(self,"Upload Image","","Image Files (*.jpg *.png)")
        if ok:
            defaultImg = os.path.basename(self.filename)
            img=Image.open(self.filename)
            img=img.resize(size)
            img.save("C:\RRHH\img/{0}".format(defaultImg))

    def uploadCv(self):
        global curriculum 
        size=(256,256)

        self.filename,ok = QFileDialog.getOpenFileName(self,"Upload Image","","Image Files (*.jpg *.png)")
        if ok:
            curriculum = os.path.basename(self.filename)
            img=Image.open(self.filename)
            img=img.resize(size)
            img.save("C:\RRHH\cv/{0}".format(curriculum))
   

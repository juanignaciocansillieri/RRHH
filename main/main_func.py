import sys
import os
import PyQt5
from PIL import Image
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from create_user_func import UsuarioWindow as newUser
from modificar_persona import Ui_MainWindow as bmu
from main import Ui_MainWindow
sys.path.append("C:\\RRHH\\clases\\")
import usuarios as us



defaultImg = ""
codigoViejo = ""
DNI_Viejo = ""
DNI = ""
curriculum = ""

class Modern(QMainWindow):

    def __init__(self):
        super(Modern, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
        ############# RECIBIMOS PROPORCIONES DE LA PANTALLA ###########
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        ############## CENTRAMOS LA VENTANA #############
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        self.listarUsuarios()


        self.ui.btn_actualizarMov.clicked.connect(self.listarUsuarios)
        self.ui.crear_btn.clicked.connect(self.mostrarNewUser)
        self.ui.table.doubleClicked.connect(self.seleccionarusuario)

        self.ui.table.doubleClicked.connect(self.mostrarBmUser)

    def seleccionarusuario(self):
        global DNI
        seleccionarusuario = []
        for i in range(0,5):
            seleccionarusuario.append(self.ui.table.item(self.ui.table.currentRow(),i).text())
            DNI = seleccionarusuario[0]



    def mostrarBmUser(self):
        self.BM_Usuario = BM_Usuario()
        self.BM_Usuario.show()


    def mostrarNewUser(self):
        self.newUserWindow = newUser()
        self.newUserWindow.show()


    ## Listar Productos en la tabla
    def listarUsuarios(self):
        users = us.listar_user()
        n = us.contar_filas()
        self.ui.table.setRowCount(n)
        tableRow = 0

        for row in users:
                self.ui.table.setItem(
                    tableRow, 0, QtWidgets.QTableWidgetItem(row[0]))
                self.ui.table.setItem(
                    tableRow, 1, QtWidgets.QTableWidgetItem(row[1]))
                self.ui.table.setItem(
                    tableRow, 2, QtWidgets.QTableWidgetItem(row[2]))
                self.ui.table.setItem(
                    tableRow, 3, QtWidgets.QTableWidgetItem(str(row[3])))
                self.ui.table.setItem(
                    tableRow, 4, QtWidgets.QTableWidgetItem(str(row[4])))
                if str(row[5]) == "b'1'":
                    self.ui.table.setItem(
                        tableRow, 5, QtWidgets.QTableWidgetItem("Apto"))
                else:
                    self.ui.table.setItem(
                        tableRow, 5, QtWidgets.QTableWidgetItem("No Apto"))

                tableRow += 1

######################################################CLASE USUARIO#############################################################################

class BM_Usuario(QMainWindow):

    def __init__(self):
        super(BM_Usuario, self).__init__()
        self.ui = bmu()
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
        self.rellenarCampos()

        #Subir foto btn
        self.ui.actualizarFoto_btn.clicked.connect(self.uploadImg)

        #Modificar usuario btn
        #self.ui.guardarCambios_btn.clicked.connect(self.ModificarUsuario)

        

        #Mostrar Ventana
        self.show()



    #Rellenar los campos con los atributos del producto seleccionado
    def rellenarCampos(self):
        global userid
        global DNI
        global DNI_Viejo
        #global defaultImg        
        usuario = us.usuarios.mostrar_user(DNI)
        atributos = list(usuario[0])
        DNI_Viejo = atributos[0]
        self.ui.nombre_input.setText(atributos[0])
        self.ui.apellido_input.setText(atributos[1])
        self.ui.dni_input.setText(atributos[2])
        self.ui.mail_input.setText(atributos[3])

        
        a=atributos[4].split(sep=",")
        self.ui.direccion_input.setText(a[0])
        self.ui.localidad_input.setText(a[1])
        self.ui.provincia_input.setText(a[2])

        self.img = QPixmap("C:\proyecto-final\RRHH\main\img/{0}".format(atributos[5]))
        defaultImg = self.img
        self.ui.nacimiento_date.setDate(atributos[6])
        self.ui.puesto_input.setText(atributos[7])

        if atributos[8] == "b'1'":
            self.ui.comboBox.setCurrentText("Full Time")
        else:
            self.ui.comboBox.setCurrentText("Part Time")

        if atributos[9] == "b'1'":
            self.ui.comboBox_relocalizarse.setCurrentText("Si")
        else:
            self.ui.comboBox_relocalizarse.setCurrentText("No")

        self.ui.habilidades_input.setText(atributos[10])
        self.ui.url_input.setText(atributos[11])
        self.ui.titulo_input.setText(atributos[12])
        self.ui.educacion_input.setText(atributos[13])
        self.ui.experiencia_input.setText(atributos[14])

        if atributos[16] == "b'1'":
            self.ui.radioButton_si.setChecked(True)
        else: self.ui.radioButton_no.setChecked(False)
        self.ui.telefono_input.setText(atributos[17])
        
        
        
    def ModificarUsuario(self):
        global DNI_Viejo
        dni = self.ui.dni_input.text()
        nombre = self.ui.nombre_input_2.text()
        apellido = self.ui.apellido_input.text()
        tipo = self.ui.tipo_cb.currentText()
        print("tpi",tipo)
        if tipo == "Administrador": 
            tipo = 1 
        else:
            tipo = 0
        nacimiento = self.ui.nacimiento_date.date().toString("yyyy/MM/dd")
        puesto = self.ui.puesto_input.text()
        mail = self.ui.mail_input.text()
        if self.ui.pass_input.text() != "" or self.ui.pass_rep_input.text != "":
                us.usuarios.modificar_datos_user(DNI_Viejo,dni,nombre,apellido,tipo,puesto,nacimiento,mail)
          
        else:
            us.usuarios.modificar_datos_user(DNI_Viejo,dni,nombre,apellido,tipo,puesto,nacimiento,mail)

        self.close()

    def uploadImg(self):
      global defaultImg
      size =(256,256)
      self.filename,ok =QFileDialog.getOpenFileName(self,'Upload Image','','Image files (*.jpg *.png)')
      if ok:
            defaultImg = os.path.basename(self.filename)
            img=Image.open(self.filename)
            img=img.resize(size)
            img.save("C:\RRHH\main\img/{0}".format(defaultImg))
    def uploadCv(self):
      global curriculum
      size =(256,256)
      self.filename,ok =QFileDialog.getOpenFileName(self,'Upload Image','','Image files (*.jpg *.png)')
      if ok:
            curriculum = os.path.basename(self.filename)
            img=Image.open(self.filename)
            img=img.resize(size)
            img.save("C:\RRHH\main\img/{0}".format(curriculum))
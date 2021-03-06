# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'crear_persona.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(848, 398)
        MainWindow.setMaximumSize(QtCore.QSize(848, 398))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 300))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_2.setStyleSheet("background: #fff;\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setGeometry(QtCore.QRect(0, 0, 851, 400))
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 400))
        self.frame_3.setStyleSheet("border-radius: 10px;\n"
"background-color: #F9F3DF;\n"
"")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_mail = QtWidgets.QLabel(self.frame_3)
        self.label_mail.setGeometry(QtCore.QRect(230, 190, 158, 27))
        self.label_mail.setMaximumSize(QtCore.QSize(500, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        self.label_mail.setFont(font)
        self.label_mail.setStyleSheet("font-family: Roboto;\n"
"font-size: 14px;\n"
"margin-top:10px;\n"
"margin-left:10px\n"
"\n"
"")
        self.label_mail.setObjectName("label_mail")
        self.label_localidad = QtWidgets.QLabel(self.frame_3)
        self.label_localidad.setGeometry(QtCore.QRect(229, 70, 90, 27))
        self.label_localidad.setMaximumSize(QtCore.QSize(90, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        self.label_localidad.setFont(font)
        self.label_localidad.setStyleSheet("font-family: Roboto;\n"
"font-size: 14px;\n"
"color: #000;\n"
"margin-top:10px;\n"
"margin-left:10px\n"
"\n"
"")
        self.label_localidad.setObjectName("label_localidad")
        self.apellido_input = QtWidgets.QLineEdit(self.frame_3)
        self.apellido_input.setGeometry(QtCore.QRect(20, 100, 170, 25))
        self.apellido_input.setMinimumSize(QtCore.QSize(0, 0))
        self.apellido_input.setMaximumSize(QtCore.QSize(16777215, 25))
        self.apellido_input.setStyleSheet("QLineEdit{\n"
"background-color: #D7E9F7;\n"
"border: 0.5px solid #c1c1c1;\n"
"border-radius: 3px;\n"
"padding: 4 5px;\n"
"color: #e9e9;\n"
"font-family:Roboto;\n"
"font-size:13px;\n"
"font-weight: 400;\n"
"margin-left: 10px;\n"
"\n"
"}\n"
"")
        self.apellido_input.setPlaceholderText("")
        self.apellido_input.setObjectName("apellido_input")
        self.label_apellido = QtWidgets.QLabel(self.frame_3)
        self.label_apellido.setGeometry(QtCore.QRect(20, 70, 67, 27))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        self.label_apellido.setFont(font)
        self.label_apellido.setStyleSheet("font-family: Roboto;\n"
"font-size: 14px;\n"
"margin-top:10px;\n"
"margin-left:10px\n"
"\n"
"")
        self.label_apellido.setObjectName("label_apellido")
        self.label_direccion = QtWidgets.QLabel(self.frame_3)
        self.label_direccion.setGeometry(QtCore.QRect(20, 130, 90, 27))
        self.label_direccion.setMaximumSize(QtCore.QSize(90, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        self.label_direccion.setFont(font)
        self.label_direccion.setStyleSheet("font-family: Roboto;\n"
"font-size: 14px;\n"
"margin-top:10px;\n"
"margin-left:10px\n"
"\n"
"")
        self.label_direccion.setObjectName("label_direccion")
        self.label_nombre = QtWidgets.QLabel(self.frame_3)
        self.label_nombre.setGeometry(QtCore.QRect(20, 10, 71, 27))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        self.label_nombre.setFont(font)
        self.label_nombre.setStyleSheet("font-family: Roboto;\n"
"font-size: 14px;\n"
"margin-top:10px;\n"
"margin-left:10px\n"
"\n"
"")
        self.label_nombre.setObjectName("label_nombre")
        self.nombre_input = QtWidgets.QLineEdit(self.frame_3)
        self.nombre_input.setGeometry(QtCore.QRect(20, 40, 170, 25))
        self.nombre_input.setMinimumSize(QtCore.QSize(0, 0))
        self.nombre_input.setMaximumSize(QtCore.QSize(16777215, 25))
        self.nombre_input.setStyleSheet("QLineEdit{\n"
"background-color: #D7E9F7;\n"
"border: 0.5px solid #c1c1c1;\n"
"border-radius: 3px;\n"
"padding: 4 5px;\n"
"color: #e9e9;\n"
"font-family:Roboto;\n"
"font-size:13px;\n"
"font-weight: 400;\n"
"margin-left: 10px;\n"
"\n"
"}\n"
"")
        self.nombre_input.setText("")
        self.nombre_input.setPlaceholderText("")
        self.nombre_input.setObjectName("nombre_input")
        self.label_dni = QtWidgets.QLabel(self.frame_3)
        self.label_dni.setGeometry(QtCore.QRect(20, 190, 71, 27))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        self.label_dni.setFont(font)
        self.label_dni.setStyleSheet("font-family: Roboto;\n"
"font-size: 14px;\n"
"margin-top:10px;\n"
"margin-left:10px\n"
"\n"
"")
        self.label_dni.setObjectName("label_dni")
        self.label_nacimiento = QtWidgets.QLabel(self.frame_3)
        self.label_nacimiento.setGeometry(QtCore.QRect(230, 10, 151, 27))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        self.label_nacimiento.setFont(font)
        self.label_nacimiento.setStyleSheet("font-family: Roboto;\n"
"font-size: 14px;\n"
"margin-top:10px;\n"
"margin-left:10px\n"
"\n"
"")
        self.label_nacimiento.setObjectName("label_nacimiento")
        self.provincia_input = QtWidgets.QLineEdit(self.frame_3)
        self.provincia_input.setGeometry(QtCore.QRect(230, 160, 170, 25))
        self.provincia_input.setMinimumSize(QtCore.QSize(0, 0))
        self.provincia_input.setMaximumSize(QtCore.QSize(16777215, 25))
        self.provincia_input.setStyleSheet("\n"
"background-color: #D7E9F7;\n"
"border: 0.5px solid #c1c1c1;\n"
"border-radius: 3px;\n"
"padding: 4 5px;\n"
"color: #000;\n"
"font-family:Roboto;\n"
"font-size:13px;\n"
"font-weight: 400;\n"
"margin-left: 10px;\n"
"\n"
"")
        self.provincia_input.setPlaceholderText("")
        self.provincia_input.setObjectName("provincia_input")
        self.label_provincia = QtWidgets.QLabel(self.frame_3)
        self.label_provincia.setGeometry(QtCore.QRect(230, 130, 84, 27))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        self.label_provincia.setFont(font)
        self.label_provincia.setStyleSheet("font-family: Roboto;\n"
"font-size: 14px;\n"
"margin-top:10px;\n"
"margin-left:10px\n"
"\n"
"")
        self.label_provincia.setObjectName("label_provincia")
        self.nacimiento_date = QtWidgets.QDateEdit(self.frame_3)
        self.nacimiento_date.setGeometry(QtCore.QRect(230, 40, 170, 25))
        self.nacimiento_date.setStyleSheet("\n"
"background-color: #D7E9F7;\n"
"border: 0.5px solid #c1c1c1;\n"
"border-radius: 3px;\n"
"padding: 4 5px;\n"
"color: #000;\n"
"font-family:Roboto;\n"
"font-size:13px;\n"
"font-weight: 400;\n"
"margin-left: 10px;\n"
"\n"
"")
        self.nacimiento_date.setDateTime(QtCore.QDateTime(QtCore.QDate(2021, 1, 1), QtCore.QTime(0, 0, 0)))
        self.nacimiento_date.setObjectName("nacimiento_date")
        self.localidad_input = QtWidgets.QLineEdit(self.frame_3)
        self.localidad_input.setGeometry(QtCore.QRect(230, 100, 170, 25))
        self.localidad_input.setMinimumSize(QtCore.QSize(0, 0))
        self.localidad_input.setMaximumSize(QtCore.QSize(16777215, 25))
        self.localidad_input.setStyleSheet("\n"
"background-color: #D7E9F7;\n"
"border: 0.5px solid #c1c1c1;\n"
"border-radius: 3px;\n"
"padding: 4 5px;\n"
"color: #000;\n"
"font-family:Roboto;\n"
"font-size:13px;\n"
"font-weight: 400;\n"
"margin-left: 10px;\n"
"\n"
"")
        self.localidad_input.setPlaceholderText("")
        self.localidad_input.setObjectName("localidad_input")
        self.puesto_input = QtWidgets.QLineEdit(self.frame_3)
        self.puesto_input.setGeometry(QtCore.QRect(230, 220, 170, 25))
        self.puesto_input.setMinimumSize(QtCore.QSize(0, 0))
        self.puesto_input.setMaximumSize(QtCore.QSize(16777215, 25))
        self.puesto_input.setStyleSheet("\n"
"background-color: #D7E9F7;\n"
"border: 0.5px solid #c1c1c1;\n"
"border-radius: 3px;\n"
"padding: 4 5px;\n"
"color: #000;\n"
"font-family:Roboto;\n"
"font-size:13px;\n"
"font-weight: 400;\n"
"margin-left: 10px;\n"
"\n"
"")
        self.puesto_input.setText("")
        self.puesto_input.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.puesto_input.setPlaceholderText("")
        self.puesto_input.setObjectName("puesto_input")
        self.dni_input = QtWidgets.QLineEdit(self.frame_3)
        self.dni_input.setGeometry(QtCore.QRect(20, 220, 170, 25))
        self.dni_input.setMinimumSize(QtCore.QSize(0, 0))
        self.dni_input.setMaximumSize(QtCore.QSize(16777215, 25))
        self.dni_input.setStyleSheet("QLineEdit{\n"
"background-color: #D7E9F7;\n"
"border: 0.5px solid #c1c1c1;\n"
"border-radius: 3px;\n"
"padding: 4 5px;\n"
"color: #e9e9;\n"
"font-family:Roboto;\n"
"font-size:13px;\n"
"font-weight: 400;\n"
"margin-left: 10px;\n"
"\n"
"}\n"
"")
        self.dni_input.setPlaceholderText("")
        self.dni_input.setObjectName("dni_input")
        self.crear_btn = QtWidgets.QPushButton(self.frame_3)
        self.crear_btn.setGeometry(QtCore.QRect(690, 360, 121, 26))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        self.crear_btn.setFont(font)
        self.crear_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.crear_btn.setStyleSheet("QPushButton{\n"
"background-color: #F4D19B;\n"
"border-radius:5px;\n"
"font-family:Roboto;\n"
"font-size: 13px\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(71, 71, 103,180);\n"
"}")
        self.crear_btn.setObjectName("crear_btn")
        self.direccion_input = QtWidgets.QLineEdit(self.frame_3)
        self.direccion_input.setGeometry(QtCore.QRect(21, 160, 170, 25))
        self.direccion_input.setMinimumSize(QtCore.QSize(0, 0))
        self.direccion_input.setMaximumSize(QtCore.QSize(16777215, 25))
        self.direccion_input.setStyleSheet("\n"
"background-color: #D7E9F7;\n"
"border: 0.5px solid #c1c1c1;\n"
"border-radius: 3px;\n"
"padding: 4 5px;\n"
"color: #000;\n"
"font-family:Roboto;\n"
"font-size:13px;\n"
"font-weight: 400;\n"
"margin-left: 10px;\n"
"\n"
"")
        self.direccion_input.setText("")
        self.direccion_input.setPlaceholderText("")
        self.direccion_input.setObjectName("direccion_input")
        self.label_telefono = QtWidgets.QLabel(self.frame_3)
        self.label_telefono.setGeometry(QtCore.QRect(440, 10, 90, 27))
        self.label_telefono.setMaximumSize(QtCore.QSize(90, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        self.label_telefono.setFont(font)
        self.label_telefono.setStyleSheet("font-family: Roboto;\n"
"font-size: 14px;\n"
"margin-top:10px;\n"
"margin-left:10px\n"
"\n"
"")
        self.label_telefono.setObjectName("label_telefono")
        self.telefono_input = QtWidgets.QLineEdit(self.frame_3)
        self.telefono_input.setGeometry(QtCore.QRect(440, 40, 170, 25))
        self.telefono_input.setMinimumSize(QtCore.QSize(0, 0))
        self.telefono_input.setMaximumSize(QtCore.QSize(16777215, 25))
        self.telefono_input.setStyleSheet("\n"
"background-color: #D7E9F7;\n"
"border: 0.5px solid #c1c1c1;\n"
"border-radius: 3px;\n"
"padding: 4 5px;\n"
"color: #000;\n"
"font-family:Roboto;\n"
"font-size:13px;\n"
"font-weight: 400;\n"
"margin-left: 10px;\n"
"\n"
"")
        self.telefono_input.setText("")
        self.telefono_input.setPlaceholderText("")
        self.telefono_input.setObjectName("telefono_input")
        self.label_educacion = QtWidgets.QLabel(self.frame_3)
        self.label_educacion.setGeometry(QtCore.QRect(230, 250, 90, 27))
        self.label_educacion.setMaximumSize(QtCore.QSize(90, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        self.label_educacion.setFont(font)
        self.label_educacion.setStyleSheet("font-family: Roboto;\n"
"font-size: 14px;\n"
"margin-top:10px;\n"
"margin-left:10px\n"
"\n"
"")
        self.label_educacion.setObjectName("label_educacion")
        self.label_disponibilidadHoraria = QtWidgets.QLabel(self.frame_3)
        self.label_disponibilidadHoraria.setGeometry(QtCore.QRect(440, 70, 151, 27))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        self.label_disponibilidadHoraria.setFont(font)
        self.label_disponibilidadHoraria.setStyleSheet("font-family: Roboto;\n"
"font-size: 14px;\n"
"margin-top:10px;\n"
"margin-left:10px\n"
"\n"
"")
        self.label_disponibilidadHoraria.setObjectName("label_disponibilidadHoraria")
        self.comboBox = QtWidgets.QComboBox(self.frame_3)
        self.comboBox.setGeometry(QtCore.QRect(440, 100, 170, 25))
        self.comboBox.setStyleSheet("\n"
"background-color: #D7E9F7;\n"
"border: 0.5px solid #c1c1c1;\n"
"border-radius: 3px;\n"
"padding: 4 5px;\n"
"color: #000;\n"
"font-family:Roboto;\n"
"font-size:13px;\n"
"font-weight: 400;\n"
"margin-left: 10px;\n"
"\n"
"")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_relocalizarse = QtWidgets.QComboBox(self.frame_3)
        self.comboBox_relocalizarse.setGeometry(QtCore.QRect(440, 160, 170, 25))
        self.comboBox_relocalizarse.setStyleSheet("\n"
"background-color: #D7E9F7;\n"
"border: 0.5px solid #c1c1c1;\n"
"border-radius: 3px;\n"
"padding: 4 5px;\n"
"color: #000;\n"
"font-family:Roboto;\n"
"font-size:13px;\n"
"font-weight: 400;\n"
"margin-left: 10px;\n"
"\n"
"\n"
"")
        self.comboBox_relocalizarse.setObjectName("comboBox_relocalizarse")
        self.comboBox_relocalizarse.addItem("")
        self.comboBox_relocalizarse.addItem("")
        self.label_relocalizarse = QtWidgets.QLabel(self.frame_3)
        self.label_relocalizarse.setGeometry(QtCore.QRect(440, 130, 171, 27))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        self.label_relocalizarse.setFont(font)
        self.label_relocalizarse.setStyleSheet("font-family: Roboto;\n"
"font-size: 14px;\n"
"margin-top:10px;\n"
"margin-left:10px\n"
"\n"
"")
        self.label_relocalizarse.setObjectName("label_relocalizarse")
        self.label_url = QtWidgets.QLabel(self.frame_3)
        self.label_url.setGeometry(QtCore.QRect(440, 190, 158, 27))
        self.label_url.setMaximumSize(QtCore.QSize(500, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        self.label_url.setFont(font)
        self.label_url.setStyleSheet("font-family: Roboto;\n"
"font-size: 14px;\n"
"margin-top:10px;\n"
"margin-left:10px\n"
"\n"
"")
        self.label_url.setObjectName("label_url")
        self.mail_input = QtWidgets.QLineEdit(self.frame_3)
        self.mail_input.setGeometry(QtCore.QRect(440, 220, 170, 25))
        self.mail_input.setMinimumSize(QtCore.QSize(0, 0))
        self.mail_input.setMaximumSize(QtCore.QSize(16777215, 25))
        self.mail_input.setStyleSheet("\n"
"background-color: #D7E9F7;\n"
"border: 0.5px solid #c1c1c1;\n"
"border-radius: 3px;\n"
"padding: 4 5px;\n"
"color: #000;\n"
"font-family:Roboto;\n"
"font-size:13px;\n"
"font-weight: 400;\n"
"margin-left: 10px;\n"
"\n"
"")
        self.mail_input.setText("")
        self.mail_input.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.mail_input.setPlaceholderText("")
        self.mail_input.setObjectName("mail_input")
        self.labe_titulo = QtWidgets.QLabel(self.frame_3)
        self.labe_titulo.setGeometry(QtCore.QRect(20, 250, 171, 27))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        self.labe_titulo.setFont(font)
        self.labe_titulo.setStyleSheet("font-family: Roboto;\n"
"font-size: 14px;\n"
"margin-top:10px;\n"
"margin-left:10px\n"
"\n"
"")
        self.labe_titulo.setObjectName("labe_titulo")
        self.label_experiencia = QtWidgets.QLabel(self.frame_3)
        self.label_experiencia.setGeometry(QtCore.QRect(440, 250, 158, 27))
        self.label_experiencia.setMaximumSize(QtCore.QSize(500, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        self.label_experiencia.setFont(font)
        self.label_experiencia.setStyleSheet("font-family: Roboto;\n"
"font-size: 14px;\n"
"margin-top:10px;\n"
"margin-left:10px\n"
"\n"
"")
        self.label_experiencia.setObjectName("label_experiencia")
        self.cargarCV_btn = QtWidgets.QPushButton(self.frame_3)
        self.cargarCV_btn.setGeometry(QtCore.QRect(650, 310, 70, 26))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        self.cargarCV_btn.setFont(font)
        self.cargarCV_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cargarCV_btn.setStyleSheet("QPushButton{\n"
"background-color: #F4D19B;\n"
"border-radius:5px;\n"
"font-family:Roboto;\n"
"font-size: 13px\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(71, 71, 103,180);\n"
"}")
        self.cargarCV_btn.setObjectName("cargarCV_btn")
        self.subirFoto_btn = QtWidgets.QPushButton(self.frame_3)
        self.subirFoto_btn.setGeometry(QtCore.QRect(740, 310, 70, 26))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        self.subirFoto_btn.setFont(font)
        self.subirFoto_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.subirFoto_btn.setStyleSheet("QPushButton{\n"
"background-color: #F4D19B;\n"
"border-radius:5px;\n"
"font-family:Roboto;\n"
"font-size: 13px\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(71, 71, 103,180);\n"
"}")
        self.subirFoto_btn.setObjectName("subirFoto_btn")
        self.experiencia_input = QtWidgets.QTextEdit(self.frame_3)
        self.experiencia_input.setGeometry(QtCore.QRect(440, 280, 170, 100))
        self.experiencia_input.setMaximumSize(QtCore.QSize(16777215, 100))
        self.experiencia_input.setStyleSheet("\n"
"background-color: #D7E9F7;\n"
"border: 0.5px solid #c1c1c1;\n"
"border-radius: 3px;\n"
"padding: 4 5px;\n"
"color: #000;\n"
"font-family:Roboto;\n"
"font-size:13px;\n"
"font-weight: 400;\n"
"margin-left: 10px;\n"
"\n"
"")
        self.experiencia_input.setObjectName("experiencia_input")
        self.label_habilidades = QtWidgets.QLabel(self.frame_3)
        self.label_habilidades.setGeometry(QtCore.QRect(650, 10, 90, 27))
        self.label_habilidades.setMaximumSize(QtCore.QSize(90, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        self.label_habilidades.setFont(font)
        self.label_habilidades.setStyleSheet("font-family: Roboto;\n"
"font-size: 14px;\n"
"margin-top:10px;\n"
"margin-left:10px\n"
"\n"
"")
        self.label_habilidades.setObjectName("label_habilidades")
        self.label_apto = QtWidgets.QLabel(self.frame_3)
        self.label_apto.setGeometry(QtCore.QRect(650, 230, 158, 27))
        self.label_apto.setMaximumSize(QtCore.QSize(500, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        self.label_apto.setFont(font)
        self.label_apto.setStyleSheet("font-family: Roboto;\n"
"font-size: 14px;\n"
"margin-top:10px;\n"
"margin-left:10px\n"
"\n"
"")
        self.label_apto.setObjectName("label_apto")
        self.radioButton_si = QtWidgets.QRadioButton(self.frame_3)
        self.radioButton_si.setGeometry(QtCore.QRect(660, 270, 41, 20))
        self.radioButton_si.setObjectName("radioButton_si")
        self.radioButton_no = QtWidgets.QRadioButton(self.frame_3)
        self.radioButton_no.setGeometry(QtCore.QRect(710, 270, 41, 21))
        self.radioButton_no.setObjectName("radioButton_no")
        self.label_profesion = QtWidgets.QLabel(self.frame_3)
        self.label_profesion.setGeometry(QtCore.QRect(650, 170, 158, 27))
        self.label_profesion.setMaximumSize(QtCore.QSize(500, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        self.label_profesion.setFont(font)
        self.label_profesion.setStyleSheet("font-family: Roboto;\n"
"font-size: 14px;\n"
"margin-top:10px;\n"
"margin-left:10px\n"
"\n"
"")
        self.label_profesion.setObjectName("label_profesion")
        self.url_input = QtWidgets.QLineEdit(self.frame_3)
        self.url_input.setGeometry(QtCore.QRect(650, 200, 170, 25))
        self.url_input.setMinimumSize(QtCore.QSize(0, 0))
        self.url_input.setMaximumSize(QtCore.QSize(16777215, 25))
        self.url_input.setStyleSheet("\n"
"background-color: #D7E9F7;\n"
"border: 0.5px solid #c1c1c1;\n"
"border-radius: 3px;\n"
"padding: 4 5px;\n"
"color: #000;\n"
"font-family:Roboto;\n"
"font-size:13px;\n"
"font-weight: 400;\n"
"margin-left: 10px;\n"
"\n"
"")
        self.url_input.setText("")
        self.url_input.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.url_input.setPlaceholderText("")
        self.url_input.setObjectName("url_input")
        self.habilidades_input = QtWidgets.QTextEdit(self.frame_3)
        self.habilidades_input.setGeometry(QtCore.QRect(650, 40, 170, 100))
        self.habilidades_input.setMaximumSize(QtCore.QSize(16777215, 100))
        self.habilidades_input.setStyleSheet("\n"
"background-color: #D7E9F7;\n"
"border: 0.5px solid #c1c1c1;\n"
"border-radius: 3px;\n"
"padding: 4 5px;\n"
"color: #000;\n"
"font-family:Roboto;\n"
"font-size:13px;\n"
"font-weight: 400;\n"
"margin-left: 10px;\n"
"\n"
"")
        self.habilidades_input.setObjectName("habilidades_input")
        self.educacion_input = QtWidgets.QTextEdit(self.frame_3)
        self.educacion_input.setGeometry(QtCore.QRect(230, 280, 170, 100))
        self.educacion_input.setMaximumSize(QtCore.QSize(16777215, 100))
        self.educacion_input.setStyleSheet("\n"
"background-color: #D7E9F7;\n"
"border: 0.5px solid #c1c1c1;\n"
"border-radius: 3px;\n"
"padding: 4 5px;\n"
"color: #000;\n"
"font-family:Roboto;\n"
"font-size:13px;\n"
"font-weight: 400;\n"
"margin-left: 10px;\n"
"\n"
"")
        self.educacion_input.setObjectName("educacion_input")
        self.titulo_input = QtWidgets.QTextEdit(self.frame_3)
        self.titulo_input.setGeometry(QtCore.QRect(20, 280, 170, 100))
        self.titulo_input.setMaximumSize(QtCore.QSize(16777215, 100))
        self.titulo_input.setStyleSheet("\n"
"background-color: #D7E9F7;\n"
"border: 0.5px solid #c1c1c1;\n"
"border-radius: 3px;\n"
"padding: 4 5px;\n"
"color: #000;\n"
"font-family:Roboto;\n"
"font-size:13px;\n"
"font-weight: 400;\n"
"margin-left: 10px;\n"
"\n"
"")
        self.titulo_input.setObjectName("titulo_input")
        self.verticalLayout.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_mail.setText(_translate("MainWindow", "Puesto"))
        self.label_localidad.setText(_translate("MainWindow", "Localidad"))
        self.label_apellido.setText(_translate("MainWindow", "Apellido"))
        self.label_direccion.setText(_translate("MainWindow", "Domicilio"))
        self.label_nombre.setText(_translate("MainWindow", "Nombre"))
        self.label_dni.setText(_translate("MainWindow", "DNI"))
        self.label_nacimiento.setText(_translate("MainWindow", "Fecha de nacimiento"))
        self.label_provincia.setText(_translate("MainWindow", "Provincia"))
        self.crear_btn.setText(_translate("MainWindow", "Crear "))
        self.label_telefono.setText(_translate("MainWindow", "Tel??fono"))
        self.label_educacion.setText(_translate("MainWindow", "Educaci??n "))
        self.label_disponibilidadHoraria.setText(_translate("MainWindow", "Disponibiliad horaria"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Full Time"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Part Time"))
        self.comboBox_relocalizarse.setItemText(0, _translate("MainWindow", "S??"))
        self.comboBox_relocalizarse.setItemText(1, _translate("MainWindow", "No"))
        self.label_relocalizarse.setText(_translate("MainWindow", "??Puede relocalizarse?"))
        self.label_url.setText(_translate("MainWindow", "Mail"))
        self.labe_titulo.setText(_translate("MainWindow", "T??tulo(s) Profesional(es)"))
        self.label_experiencia.setText(_translate("MainWindow", "Experiencia"))
        self.cargarCV_btn.setText(_translate("MainWindow", "Cargar CV"))
        self.subirFoto_btn.setText(_translate("MainWindow", "Subir Foto"))
        self.label_habilidades.setText(_translate("MainWindow", "Habilidades"))
        self.label_apto.setText(_translate("MainWindow", "Apto"))
        self.radioButton_si.setText(_translate("MainWindow", "S??"))
        self.radioButton_no.setText(_translate("MainWindow", "No"))
        self.label_profesion.setText(_translate("MainWindow", "URL"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

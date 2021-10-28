# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(823, 671)
        MainWindow.setMinimumSize(QtCore.QSize(823, 671))
        MainWindow.setMaximumSize(QtCore.QSize(823, 671))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 821, 661))
        self.frame.setStyleSheet("background-color: rgb(249, 243, 223);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.groupBox_9 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_9.setGeometry(QtCore.QRect(0, 60, 791, 50))
        self.groupBox_9.setMinimumSize(QtCore.QSize(0, 50))
        self.groupBox_9.setStyleSheet("margin-left: 14px;\n"
"border:none")
        self.groupBox_9.setTitle("")
        self.groupBox_9.setObjectName("groupBox_9")
        self.buscar_btn = QtWidgets.QPushButton(self.groupBox_9)
        self.buscar_btn.setGeometry(QtCore.QRect(14, 9, 41, 26))
        self.buscar_btn.setMinimumSize(QtCore.QSize(0, 21))
        self.buscar_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buscar_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/Buscar_PNG.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buscar_btn.setIcon(icon)
        self.buscar_btn.setIconSize(QtCore.QSize(30, 30))
        self.buscar_btn.setObjectName("buscar_btn")
        self.Buscar_input = QtWidgets.QLineEdit(self.groupBox_9)
        self.Buscar_input.setGeometry(QtCore.QRect(50, 10, 301, 26))
        self.Buscar_input.setMinimumSize(QtCore.QSize(0, 20))
        self.Buscar_input.setStyleSheet("font-family: Roboto;\n"
"background-color: #D7E9F7\n"
"")
        self.Buscar_input.setText("")
        self.Buscar_input.setObjectName("Buscar_input")
        self.crear_btn = QtWidgets.QPushButton(self.groupBox_9)
        self.crear_btn.setGeometry(QtCore.QRect(660, 10, 100, 26))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        self.crear_btn.setFont(font)
        self.crear_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.crear_btn.setStyleSheet("QPushButton{\n"
"background-color: #D7E9F7;\n"
"border-radius:5px;\n"
"font-family:Roboto;\n"
"font-size: 13px\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(71, 71, 103,180);\n"
"}")
        self.crear_btn.setObjectName("crear_btn")
        self.btn_actualizarMov = QtWidgets.QPushButton(self.groupBox_9)
        self.btn_actualizarMov.setGeometry(QtCore.QRect(755, 13, 31, 21))
        self.btn_actualizarMov.setMinimumSize(QtCore.QSize(0, 21))
        self.btn_actualizarMov.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_actualizarMov.setStyleSheet("background: none")
        self.btn_actualizarMov.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_actualizarMov.setIcon(icon1)
        self.btn_actualizarMov.setIconSize(QtCore.QSize(40, 17))
        self.btn_actualizarMov.setObjectName("btn_actualizarMov")
        self.label_titulo = QtWidgets.QLabel(self.frame)
        self.label_titulo.setGeometry(QtCore.QRect(220, 0, 391, 61))
        self.label_titulo.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_titulo.setStyleSheet("font-family: Roboto;")
        self.label_titulo.setObjectName("label_titulo")
        self.table = QtWidgets.QTableWidget(self.frame)
        self.table.setEnabled(True)
        self.table.setGeometry(QtCore.QRect(30, 110, 770, 532))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table.sizePolicy().hasHeightForWidth())
        self.table.setSizePolicy(sizePolicy)
        self.table.setMaximumSize(QtCore.QSize(770, 16777215))
        self.table.setStyleSheet("background-color: #F4D19B")
        self.table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table.setTabKeyNavigation(False)
        self.table.setProperty("showDropIndicator", False)
        self.table.setDragDropOverwriteMode(False)
        self.table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.table.setWordWrap(False)
        self.table.setObjectName("table")
        self.table.setColumnCount(6)
        self.table.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(253, 252, 229))
        self.table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(253, 252, 229))
        self.table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(253, 252, 229))
        self.table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(253, 252, 229))
        self.table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(253, 252, 229))
        self.table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(253, 252, 229))
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.table.setHorizontalHeaderItem(5, item)
        self.table.horizontalHeader().setVisible(True)
        self.table.horizontalHeader().setDefaultSectionSize(128)
        self.table.horizontalHeader().setHighlightSections(False)
        self.table.verticalHeader().setVisible(False)
        self.table.verticalHeader().setHighlightSections(False)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Buscar_input.setPlaceholderText(_translate("MainWindow", "Buscar "))
        self.crear_btn.setText(_translate("MainWindow", "Crear"))
        self.label_titulo.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600;\">Recursos Humanos</span></p></body></html>"))
        item = self.table.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "DNI"))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Apellido"))
        item = self.table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Nombre"))
        item = self.table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Mail"))
        item = self.table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Puesto"))
        item = self.table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Apto"))
import img_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

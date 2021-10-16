
import sys

####################### PYQT ################
import PyQt5
from PIL import Image
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
#############################################

sys.path.append("C:\\RRHH\\main\\")
from main import Modern 
from login import Ui_MainWindow

admin_user=True

class LoginWindow(QMainWindow):
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)

        ############# RECIBIMOS PROPORCIONES DE LA PANTALLA ###########
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        ############## CENTRAMOS LA VENTANA #############
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        ### BOTON INGRESAR ####
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.login_btn.clicked.connect(self.verificacion)

        ## MOSTRAR ##
        self.show()

### VERIFICAR DATOS INGRESADOS LA DB ####
    def verificacion(self):
            global admin_user
            user = self.ui.user_login_input.text()
            password = self.ui.pass_login_input.text()
            usuario = l.log_in(user,password)
            
            if usuario==1:
                #inicia
                admin_user=u.ver_tipo(user)
                self.main = Modern()
                self.close()
            if usuario==2:
                #no se encuentra dni
                QtWidgets.QMessageBox.critical(self, "Error", "DNI Incorrecto")
                self.ui.user_login_input.setText("")
                self.ui.pass_login_input.setText("")
            if usuario==3:
                #contraseña incorrecta
                QtWidgets.QMessageBox.critical(self, "Error", "Contraseña Incorrecta")
                self.ui.pass_login_input.setText("")

     
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())

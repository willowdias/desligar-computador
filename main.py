
from typing import Sized
from PyQt5.QtCore import QEventLoop, QTimer
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QComboBox, QPushButton
from PyQt5.QtWidgets import (QApplication, QMainWindow, QComboBox, QCompleter, QTableView, QLabel)
import sys
import os
from telaincial import *
from cssmsgbox import*

class sistema_desligar(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.resize(400,400)
        #
        #self.ui.lineEdit.setValidator(QtGui.QIntValidator())
        self.ui.lineEdit.returnPressed.connect(self.test)
       
        self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint|QtCore.Qt.WindowCloseButtonHint|QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.ui.bt_desligar.clicked.connect(self.sistemadesligar)
        self.ui.bt_cancelar.clicked.connect(self.cancelar)
        self.ui.verticalSlider_hora.valueChanged[int].connect(self.aumenta_tempo_hora)

        #create funçoes desativa botao
        self.ui.bt_cancelar.setEnabled(False)
    def test(self):
        
        b=str(self.ui.lineEdit.text()).upper()
        self.mg=QMessageBox()
        self.mg.setText(b)
        self.mg.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.mg.setWindowTitle("DESLIGAR")
        self.mg.setWindowIcon(QtGui.QIcon("icon/4115230-cancel-close-cross-delete_114048.png"))
        self.mg.setIconPixmap(QtGui.QPixmap("icon/4115230-cancel-close-cross-delete_114048.png"))
        self.mg.setStyleSheet(msg)
        self.mg.exec_()
        self.ui.lineEdit.setText('')
    def aumenta_tempo_hora(self,value):
        self.ui.spinBox.setValue(value)
    def sistemadesligar(self):#delisgar sistema
        b=int(self.ui.spinBox.value())
        c=int(b*3600)
        import time
        
        if b==0 or c==0:
            self.ui.label.setText(str('ERRO PREENCHAR HORA'))
            self.ui.label.show()  
            self.repaint()
            time.sleep(2)
            self.ui.label.setText(str('TIME OFF'))
        else:
            
            os.system(f'shutdown -s -t {c}')
            #QtWidgets.QMessageBox.about(self, "HORARIO", f"SEU PC IRA DESLIGAR EM {b} HORA")
            self.msg = QtWidgets.QMessageBox()
            self.msg.setText(str(f"SEU PC IRA DESLIGAR EM {b} HORA\n"
                "CELULAR (69)992-702408"))            
            self.msg.setWindowTitle("DESLIGAR")
            self.msg.setWindowFlags(QtCore.Qt.FramelessWindowHint)
            self.msg.setWindowIcon(QtGui.QIcon("icon/1492790919-81power_84209.png"))
            self.msg.setIconPixmap(QtGui.QPixmap("icon/1492790919-81power_84209.png"))
            self.msg.setStyleSheet(msg)
            self.msg.exec_()
            self.ui.spinBox.setValue(0)
            self.ui.verticalSlider_hora.setValue(0)
            self.ui.bt_cancelar.setEnabled(True)
    def cancelar(self):#cancelar tempo desligar
        self.ui.bt_cancelar.setEnabled(False)
        self.mgdesligar=QtWidgets.QMessageBox()
        self.mgdesligar.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.mgdesligar.setWindowTitle("DESLIGAR")
        self.mgdesligar.setText('PROCESSO DESLIGAMENTO CANCELADO')
        self.mgdesligar.setWindowIcon(QtGui.QIcon("icon/4115230-cancel-close-cross-delete_114048.png"))
        self.mgdesligar.setIconPixmap(QtGui.QPixmap("icon/4115230-cancel-close-cross-delete_114048.png"))
        self.mgdesligar.setStyleSheet(msg)
        self.mgdesligar.exec_()
        os.system(f'shutdown -a')
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = sistema_desligar()
    ex.show()
    sys.exit(app.exec_())
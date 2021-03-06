# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lyoute-sistema/lyoute.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(392, 405)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: rgb(57, 57, 57,150);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_3 = QtWidgets.QFrame(self.frame_4)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.spinBox = QtWidgets.QSpinBox(self.frame_3)
        self.spinBox.setMinimumSize(QtCore.QSize(120, 30))
        self.spinBox.setMaximumSize(QtCore.QSize(50, 20))
        self.spinBox.setSizeIncrement(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(15)
        self.spinBox.setFont(font)
        self.spinBox.setStyleSheet("background-color:  rgb(0, 69, 116);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(43, 31, 91);\n"
"border-radius:  5px\n"
"")
        self.spinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinBox.setMaximum(24)
        self.spinBox.setSingleStep(1)
        self.spinBox.setProperty("value", 0)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout_4.addWidget(self.spinBox)
        self.verticalSlider_hora = QtWidgets.QSlider(self.frame_3)
        self.verticalSlider_hora.setMaximum(24)
        self.verticalSlider_hora.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_hora.setInvertedAppearance(False)
        self.verticalSlider_hora.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.verticalSlider_hora.setObjectName("verticalSlider_hora")
        self.horizontalLayout_4.addWidget(self.verticalSlider_hora)
        self.horizontalLayout_2.addWidget(self.frame_3)
        self.frame_5 = QtWidgets.QFrame(self.frame_4)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.spinBox_2 = QtWidgets.QSpinBox(self.frame_5)
        self.spinBox_2.setMinimumSize(QtCore.QSize(120, 30))
        self.spinBox_2.setStyleSheet("background-color:  rgb(0, 69, 116);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(43, 31, 91);\n"
"border-radius:  5px\n"
"")
        self.spinBox_2.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinBox_2.setObjectName("spinBox_2")
        self.horizontalLayout_3.addWidget(self.spinBox_2)
        self.verticalSlider = QtWidgets.QSlider(self.frame_5)
        self.verticalSlider.setMaximum(60)
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setInvertedAppearance(False)
        self.verticalSlider.setInvertedControls(False)
        self.verticalSlider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.verticalSlider.setObjectName("verticalSlider")
        self.horizontalLayout_3.addWidget(self.verticalSlider)
        self.horizontalLayout_2.addWidget(self.frame_5)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 150))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 600))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bt_cancelar = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(70)
        sizePolicy.setVerticalStretch(70)
        sizePolicy.setHeightForWidth(self.bt_cancelar.sizePolicy().hasHeightForWidth())
        self.bt_cancelar.setSizePolicy(sizePolicy)
        self.bt_cancelar.setMinimumSize(QtCore.QSize(70, 70))
        self.bt_cancelar.setMaximumSize(QtCore.QSize(50, 50))
        self.bt_cancelar.setStyleSheet("QPushButton {\n"
"    border-radius: 30px;\n"
"    background-color: rgb(52, 59, 72,150);\n"
"    border: 2px solid white;\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border: 2px solid rgb(0, 66, 124);\n"
"}")
        self.bt_cancelar.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("lyoute-sistema\\../icon/4115230-cancel-close-cross-delete_114048.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_cancelar.setIcon(icon)
        self.bt_cancelar.setIconSize(QtCore.QSize(35, 35))
        self.bt_cancelar.setObjectName("bt_cancelar")
        self.horizontalLayout.addWidget(self.bt_cancelar)
        self.bt_desligar = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bt_desligar.sizePolicy().hasHeightForWidth())
        self.bt_desligar.setSizePolicy(sizePolicy)
        self.bt_desligar.setMinimumSize(QtCore.QSize(70, 70))
        self.bt_desligar.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        self.bt_desligar.setFont(font)
        self.bt_desligar.setStyleSheet("QPushButton {\n"
"    border-radius: 30px;\n"
"    background-color: rgb(52, 59, 72,150);\n"
"    border: 2px solid white;\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border: 2px solid rgb(0, 66, 124);\n"
"}")
        self.bt_desligar.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("lyoute-sistema\\../icon/1492790919-81power_84209.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_desligar.setIcon(icon1)
        self.bt_desligar.setIconSize(QtCore.QSize(35, 35))
        self.bt_desligar.setObjectName("bt_desligar")
        self.horizontalLayout.addWidget(self.bt_desligar)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 392, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "tela"))
        self.label.setText(_translate("MainWindow", "TIME OFF"))
        self.spinBox.setSpecialValueText(_translate("MainWindow", "HORA"))
        self.bt_cancelar.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; color:#ff007f;\">Cancelar-Desligamento</span></p></body></html>"))
        self.bt_desligar.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; color:#ff007f;\">Desligar</span></p></body></html>"))

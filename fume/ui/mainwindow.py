# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1457, 678)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout_3.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../../fupa-kalender-app/kalender/ui/fupa_logo_footer.png"))
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 2, 2)
        self.frame = QtWidgets.QFrame(self.centralWidget)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame.setObjectName("frame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_13 = QtWidgets.QLabel(self.frame)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_5.addWidget(self.label_13)
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_5.addWidget(self.comboBox)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.dateEdit_3 = QtWidgets.QDateEdit(self.frame)
        self.dateEdit_3.setAcceptDrops(False)
        self.dateEdit_3.setCalendarPopup(True)
        self.dateEdit_3.setObjectName("dateEdit_3")
        self.horizontalLayout_5.addWidget(self.dateEdit_3)
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.dateEdit_4 = QtWidgets.QDateEdit(self.frame)
        self.dateEdit_4.setCalendarPopup(True)
        self.dateEdit_4.setObjectName("dateEdit_4")
        self.horizontalLayout_5.addWidget(self.dateEdit_4)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setMaximumSize(QtCore.QSize(30, 16777215))
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.label_14 = QtWidgets.QLabel(self.frame)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_5.addWidget(self.label_14)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_5.addWidget(self.label_7)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_5.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_5.addWidget(self.pushButton_4)
        self.gridLayout_3.addWidget(self.frame, 0, 2, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_3.addWidget(self.pushButton_5, 2, 0, 1, 1)
        self.pushButton_11 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout_3.addWidget(self.pushButton_11, 2, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_11 = QtWidgets.QLabel(self.centralWidget)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout.addWidget(self.label_11)
        self.lineEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralWidget)
        self.checkBox_2.setObjectName("checkBox_2")
        self.horizontalLayout.addWidget(self.checkBox_2)
        self.gridLayout_3.addLayout(self.horizontalLayout, 3, 0, 1, 2)
        self.listWidget = QtWidgets.QListWidget(self.centralWidget)
        self.listWidget.setMinimumSize(QtCore.QSize(350, 0))
        self.listWidget.setMaximumSize(QtCore.QSize(166777, 16777215))
        self.listWidget.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.listWidget.addItem(item)
        self.gridLayout_3.addWidget(self.listWidget, 4, 0, 1, 2)
        self.frame1 = QtWidgets.QFrame(self.centralWidget)
        self.frame1.setFrameShape(QtWidgets.QFrame.Box)
        self.frame1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame1.setObjectName("frame1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame1)
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_2.setContentsMargins(11, 1, 11, 11)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_10 = QtWidgets.QPushButton(self.frame1)
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout_2.addWidget(self.pushButton_10, 1, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.frame1)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 2, 0, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.frame1)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout_2.addWidget(self.pushButton_9, 1, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 2, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.frame1)
        self.label_8.setMaximumSize(QtCore.QSize(122347, 16777215))
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 0, 0, 1, 2)
        self.gridLayout_3.addWidget(self.frame1, 5, 0, 1, 2)
        self.tableView = QtWidgets.QTableView(self.centralWidget)
        self.tableView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableView.setObjectName("tableView")
        self.gridLayout_3.addWidget(self.tableView, 1, 2, 5, 1)
        MainWindow.setCentralWidget(self.centralWidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setAutoFillBackground(False)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FuME - FuPa Match Explorer"))
        self.label_13.setText(_translate("MainWindow", "Region:"))
        self.label_2.setText(_translate("MainWindow", "Von:"))
        self.label_4.setText(_translate("MainWindow", "Bis:"))
        self.label_5.setText(_translate("MainWindow", "Mannschaften:"))
        self.label_6.setText(_translate("MainWindow", "1234"))
        self.label_14.setText(_translate("MainWindow", "/"))
        self.label_3.setText(_translate("MainWindow", "Spiele:"))
        self.label_7.setText(_translate("MainWindow", "1234"))
        self.pushButton_3.setText(_translate("MainWindow", "Log"))
        self.pushButton_4.setText(_translate("MainWindow", "Einstellungen"))
        self.pushButton_5.setText(_translate("MainWindow", "importieren"))
        self.pushButton_11.setText(_translate("MainWindow", "reservieren"))
        self.label_11.setText(_translate("MainWindow", "Suche:"))
        self.checkBox_2.setText(_translate("MainWindow", "markiert"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "Noch keine Mannschaften hinzugefügt..."))
        item = self.listWidget.item(1)
        item.setText(_translate("MainWindow", "Region wählen und unten links auf konfigurieren klicken"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton_10.setText(_translate("MainWindow", "zurücksetzen"))
        self.pushButton.setText(_translate("MainWindow", "konfigurieren"))
        self.pushButton_9.setText(_translate("MainWindow", "entfernen"))
        self.pushButton_2.setText(_translate("MainWindow", "invertieren"))
        self.label_8.setText(_translate("MainWindow", "Auswahl:"))

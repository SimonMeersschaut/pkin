from PyQt5 import QtCore, QtGui, QtWidgets
from json import load, dump

with open('preferences.json', 'r') as f:
    preferences = load(f)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 585)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setHorizontalSpacing(33)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.formLayout.setWidget(
            0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.spinBox = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox.setObjectName("spinBox")
        self.spinBox.valueChanged.connect(self.setPreview)
        self.formLayout.setWidget(
            0, QtWidgets.QFormLayout.FieldRole, self.spinBox)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(
            1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.fontComboBox = QtWidgets.QFontComboBox(self.groupBox)
        self.fontComboBox.setObjectName("fontComboBox")
        self.fontComboBox.editTextChanged.connect(self.setPreview)
        self.formLayout.setWidget(
            1, QtWidgets.QFormLayout.FieldRole, self.fontComboBox)
        self.verticalLayout.addLayout(self.formLayout)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setAlignment(
            QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout.setContentsMargins(-1, -1, -1, 9)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox.setDecimals(7)
        self.doubleSpinBox.setMaximum(1.0)
        self.doubleSpinBox.setSingleStep(1e-06)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.gridLayout.addWidget(self.doubleSpinBox, 0, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.setValues()

    def setValues(self):
        self.doubleSpinBox.setValue(preferences['toflen'])
        self.spinBox.setValue(preferences['font-size'])
        self.fontComboBox.setCurrentText(preferences['font'])

    def setPreview(self):

        font = QtGui.QFont(self.fontComboBox.currentText(),
                           self.spinBox.value())
        self.label_3.setFont(font)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Settings"))
        self.groupBox.setTitle(_translate("MainWindow", "GroupBox"))
        self.label.setText(_translate("MainWindow", "font size"))
        self.label_2.setText(_translate("MainWindow", "font"))
        self.label_3.setText(_translate(
            "MainWindow", "Exaple: The quick brown fox jumps over the lazy dog"))
        self.groupBox_2.setTitle(_translate("MainWindow", "settings"))
        self.label_4.setText(_translate("MainWindow", "toflen"))

    def save(self):
        preferences['font-size'] = self.spinBox.value()
        preferences['font'] = self.fontComboBox.currentText()
        preferences['toflen'] = self.doubleSpinBox.value()
        with open('preferences.json', 'w+') as f:
            dump(preferences, f)


def open_settings():
    print('open settings')
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec_()
    ui.save()


if __name__ == "__main__":
    open_settings()

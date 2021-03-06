
from os import startfile
import threading
import pkin
from json import load, dump, dumps
from PyQt5 import QtCore, QtGui, QtWidgets
import settings
import win32gui
import win32con

# hide = win32gui.GetForegroundWindow()
# win32gui.ShowWindow(hide, win32con.SW_HIDE)

with open('preferences.json', 'r') as f:
    preferences = load(f)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        # MainWindow.setWindowIcon(QtGui.QIcon('imec.png'))
        MainWindow.setWindowIcon(QtGui.QIcon("imec.png"))
        MainWindow.resize(preferences['width'], preferences['height'])
        MainWindow.setSizeIncrement(QtCore.QSize(1, 0))
        self.MainWindow = MainWindow

        self.element1 = 'Fe'
        self.element2 = 'H'

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(15, -1, -1, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 6, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.spinBox_4 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.spinBox_4.setObjectName("spinBox_4")
        self.horizontalLayout_4.addWidget(self.spinBox_4)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_4.addWidget(self.label_10)
        self.gridLayout.addLayout(self.horizontalLayout_4, 6, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout.addWidget(self.spinBox)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout.addWidget(self.comboBox)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 1, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.spinBox_3 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.spinBox_3.setObjectName("spinBox_3")
        self.spinBox_3.setMaximum(180)
        self.horizontalLayout_3.addWidget(self.spinBox_3)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_3.addWidget(self.label_9)
        self.gridLayout.addLayout(self.horizontalLayout_3, 5, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.spinBox_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_2.setObjectName("spinBox_2")
        self.horizontalLayout_2.addWidget(self.spinBox_2)
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.horizontalLayout_2.addWidget(self.comboBox_2)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 1, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSizeConstraint(
            QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_11.setAlignment(
            QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_6.addWidget(self.label_11)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setAlignment(
            QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_6.addWidget(self.label_12)
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setAlignment(
            QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_6.addWidget(self.label_13)
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setAlignment(
            QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_6.addWidget(self.label_14)
        self.gridLayout.addLayout(self.horizontalLayout_6, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 5, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 4, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setContentsMargins(15, -1, -1, -1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.RBS_tof = QtWidgets.QLabel(self.centralwidget)
        self.RBS_tof.setObjectName("RBS_tof")
        self.gridLayout_2.addWidget(self.RBS_tof, 4, 0, 1, 1)
        self.theta_number = QtWidgets.QLabel(self.centralwidget)
        self.theta_number.setObjectName("theta_number")
        self.gridLayout_2.addWidget(self.theta_number, 0, 1, 1, 1)
        self.toflen = QtWidgets.QLabel(self.centralwidget)
        self.toflen.setObjectName("toflen")
        self.gridLayout_2.addWidget(self.toflen, 1, 0, 1, 1)
        self.toflen_number = QtWidgets.QLabel(self.centralwidget)
        self.toflen_number.setObjectName("toflen_number")
        self.gridLayout_2.addWidget(self.toflen_number, 1, 1, 1, 1)
        self.RBS_E = QtWidgets.QLabel(self.centralwidget)
        self.RBS_E.setObjectName("RBS_E")
        self.gridLayout_2.addWidget(self.RBS_E, 3, 0, 1, 1)
        self.toflen_number2 = QtWidgets.QLabel(self.centralwidget)
        self.toflen_number2.setObjectName("toflen_number2")
        self.gridLayout_2.addWidget(self.toflen_number2, 2, 1, 1, 1)
        self.RBS_E_number = QtWidgets.QLabel(self.centralwidget)
        self.RBS_E_number.setObjectName("RBS_E_number")
        self.gridLayout_2.addWidget(self.RBS_E_number, 3, 1, 1, 1)
        self.RBS_sigma = QtWidgets.QLabel(self.centralwidget)
        self.RBS_sigma.setObjectName("RBS_sigma")
        self.gridLayout_2.addWidget(self.RBS_sigma, 5, 0, 1, 1)
        self.RBS_sigma_number = QtWidgets.QLabel(self.centralwidget)
        self.RBS_sigma_number.setObjectName("RBS_sigma_number")
        self.gridLayout_2.addWidget(self.RBS_sigma_number, 5, 1, 1, 1)
        self.RBS_tof_number = QtWidgets.QLabel(self.centralwidget)
        self.RBS_tof_number.setObjectName("RBS_tof_number")
        self.gridLayout_2.addWidget(self.RBS_tof_number, 4, 1, 1, 1)
        self.theta = QtWidgets.QLabel(self.centralwidget)
        self.theta.setObjectName("theta")
        self.gridLayout_2.addWidget(self.theta, 0, 0, 1, 1)

        self.ERD_E = QtWidgets.QLabel(self.centralwidget)
        self.ERD_E.setObjectName("ERD_E")
        self.gridLayout_2.addWidget(
            self.ERD_E, 6, 0, 1, 1)
        self.ERD_E_number = QtWidgets.QLabel(self.centralwidget)
        self.ERD_E_number.setObjectName("ERD_E_number")
        self.gridLayout_2.addWidget(
            self.ERD_E_number, 6, 1, 1, 1)

        self.ERD_tof = QtWidgets.QLabel(self.centralwidget)
        self.ERD_tof.setObjectName("ERD_tof")
        self.gridLayout_2.addWidget(
            self.ERD_tof, 7, 0, 1, 1)
        self.ERD_tof_number = QtWidgets.QLabel(self.centralwidget)
        self.ERD_tof_number.setObjectName("ERD_tof_number")
        self.gridLayout_2.addWidget(
            self.ERD_tof_number, 7, 1, 1, 1)

        self.ERD_sigma = QtWidgets.QLabel(self.centralwidget)
        self.ERD_sigma.setObjectName("ERD_sigma")
        self.gridLayout_2.addWidget(
            self.ERD_sigma, 8, 0, 1, 1)
        self.ERD_sigma_number = QtWidgets.QLabel(self.centralwidget)
        self.ERD_sigma_number.setObjectName("ERD_sigma_number")
        self.gridLayout_2.addWidget(
            self.ERD_sigma_number, 8, 1, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menufile = QtWidgets.QMenu(self.menubar)
        self.menufile.setObjectName("menufile")
        self.menusettings = QtWidgets.QAction(self.menubar)
        self.menusettings.setObjectName("menusettings")
        self.menugraph = QtWidgets.QAction(self.menubar)
        self.menugraph.setObjectName("menugraph")

        # self.menusettings.triggered.connect(settings.open_settings)
        self.menuhelp = QtWidgets.QMenu(self.menubar)
        self.menuhelp.setObjectName("menuhelp")
        self.menuabout = QtWidgets.QMenu(self.menubar)
        self.menuabout.setObjectName("menuabout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionsave = QtWidgets.QAction(MainWindow)
        self.actionsave.setObjectName("actionsave")
        self.actionload = QtWidgets.QAction(MainWindow)
        self.actionload.setObjectName("actionload")
        self.actionclose = QtWidgets.QAction(MainWindow)
        self.actionclose.setObjectName("actionclose")
        self.menufile.addAction(self.actionsave)
        self.menufile.addAction(self.actionload)
        self.menufile.addSeparator()
        self.menufile.addAction(self.actionclose)
        self.menubar.addAction(self.menufile.menuAction())
        self.menubar.addAction(self.menusettings)
        self.menubar.addAction(self.menugraph)
        self.menubar.addAction(self.menuabout.menuAction())
        self.menubar.addAction(self.menuhelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pkin - Imec"))
        self.label.setText(_translate("MainWindow", "element1 (impinging)"))
        self.label_8.setText(_translate("MainWindow", "energy"))
        self.label_10.setText(_translate("MainWindow", "MeV"))
        self.label_4.setText(_translate("MainWindow", "/"))
        self.label_5.setText(_translate("MainWindow", "/"))
        self.label_9.setText(_translate("MainWindow", "degrees"))
        self.label_6.setText(_translate("MainWindow", "/"))
        self.label_7.setText(_translate("MainWindow", "/"))
        self.label_11.setText(_translate("MainWindow", "#Neutrons"))
        self.label_12.setText(_translate("MainWindow", "ElementName"))
        self.label_13.setText(_translate("MainWindow", "Z"))
        self.label_14.setText(_translate("MainWindow", "M"))
        self.label_2.setText(_translate("MainWindow", "element2 (target)"))
        self.label_3.setText(_translate("MainWindow", "theta"))

        self.ERD_E.setText(_translate('MainWindow', 'ERD_E'))
        self.ERD_tof.setText(_translate('MainWindow', 'ERD_tof'))
        self.ERD_sigma.setText(_translate('MainWindow', 'ERD_sigma'))

        self.RBS_tof.setText(_translate("MainWindow", "RBS_tof"))
        self.theta_number.setText(_translate("MainWindow", "/"))
        self.toflen.setText(_translate("MainWindow", "toflen"))
        self.toflen_number.setText(_translate("MainWindow", "/"))
        self.RBS_E.setText(_translate("MainWindow", "RBS_E"))
        self.toflen_number2.setText(_translate("MainWindow", "/"))
        self.RBS_E_number.setText(_translate("MainWindow", "/"))
        self.RBS_sigma.setText(_translate("MainWindow", "RBS_sigma"))
        self.RBS_sigma_number.setText(_translate("MainWindow", "/"))
        self.RBS_tof_number.setText(_translate("MainWindow", "/"))
        self.theta.setText(_translate("MainWindow", "theta"))
        self.menufile.setTitle(_translate("MainWindow", "file"))
        self.menuabout.setTitle(_translate("MainWindow", "about"))
        self.menusettings.setText(_translate("MainWindow", "settings"))
        self.menugraph.setText(_translate("MainWindow", "graph"))
        self.menuhelp.setTitle(_translate("MainWindow", "help"))
        self.actionsave.setText(_translate("MainWindow", "save"))
        self.actionsave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionsave.triggered.connect(self.save)
        self.actionload.setText(_translate("MainWindow", "load"))
        self.actionload.setToolTip(_translate("MainWindow", "load"))
        self.actionload.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionload.triggered.connect(self.load)
        self.menusettings.triggered.connect(self.openSettings)
        self.menugraph.triggered.connect(self.openGraph)

        self.actionclose.setText(_translate("MainWindow", "close"))
        self.load_combobox()
        self.set_actions()
        self.load(data=preferences['data'])
        self.setFontSize()
        # self.res

    def openGraph(self):
        def startFile():

            import os

            single = "'"
            double = '"'
            data = self.json_data
            print(self.json_data)
            os.system(
                f'cmd /k "python graph.py {data["name1"]} {data["name2"]} {data["theta"]} {data["E_MeV"]}"')
        t1 = threading.Thread(target=startFile)
        t1.start()

    def openSettings(self):
        import os
        os.startfile('run_settings.bat')
        # settings.open_settings

    def setFontSize(self):
        font = QtGui.QFont(preferences["font"], preferences["font-size"])
        MainWindow.setFont(font)

    # def resizeEvent(self, event):
    #    print('resize')
    #    self.updateScreen()
    #    sQMainWindow.resizeEvent(self, event)

    def calculate(self):
        def simplify(number):
            if type(number) == tuple:
                return str((round(number[0], 4), round(number[1], 4)))
            return str(round(number, 4))

        name1 = self.comboBox.currentText()
        name2 = self.comboBox_2.currentText()
        neutrons_1 = str(self.spinBox.value())
        neutrons_2 = str(self.spinBox_2.value())
        self.label_4.setText(str(self.comboBox.currentIndex()+1))
        self.label_6.setText(str(self.comboBox_2.currentIndex()+1))
        Theta_Deg = self.spinBox_3.value()
        E_MeV = self.spinBox_4.value()
        # 8print(z1, z2)
        for element in pkin.Data.data:
            if name1 == element[3] and neutrons_1 == element[0]:
                element1 = element[2]+name1
        for element in pkin.Data.data:
            if name2 == element[3] and neutrons_2 == element[0]:
                element2 = element[2]+name2
       # element1 = neutrons_1+name1
       # element2 = neutrons_2+name2
        try:
            output = pkin.pkin(element1, element2, Theta_Deg, E_MeV)
            print(output)
        except Exception as e:
            print(e)
            return None

        # display output
        self.label_5.setText(simplify(output['m1']))
        self.label_7.setText(simplify(output['m2']))

        self.theta_number.setText(simplify(output['theta'])+' radians')
        self.toflen_number.setText(simplify(output['toflen']))
        try:
            self.RBS_E_number.setText(simplify(output['RBS_E']))
            self.RBS_tof_number.setText(simplify(output['RBS_tof']))
            self.RBS_sigma_number.setText(simplify(output['RBS_sigma']))

            if 'ERD_E' in output:
                self.ERD_E_number.setText(simplify(output['ERD_E']))
                self.ERD_tof_number.setText(simplify(output['ERD_tof']))
                self.ERD_sigma_number.setText(simplify(output['ERD_sigma']))
            else:
                self.ERD_E_number.setText('')
                self.ERD_tof_number.setText('')
                self.ERD_sigma_number.setText('')
        except KeyError:
            pass
        self.json_data = {'name1': name1, 'neutrons1': neutrons_1, 'name2': name2,
                          'neutrons2': neutrons_2, 'theta': Theta_Deg, 'E_MeV': E_MeV}

    def set_actions(self):
        self.comboBox.currentTextChanged.connect(self.change_combobox)
        self.comboBox_2.currentTextChanged.connect(self.change_combobox2)
        self.spinBox.valueChanged.connect(self.change_spinbox)
        self.spinBox_2.valueChanged.connect(self.change_spinbox2)
        self.spinBox_3.valueChanged.connect(self.calculate)
        self.spinBox_4.valueChanged.connect(self.calculate)

    def change_combobox(self, value):
        print(value)
        self.element1 = value
        neutrons = int(self.get_neutrons_by_name(value))
        self.spinBox.setValue(neutrons)
        self.calculate()

    def change_spinbox(self, value):
        if self.element_has_neutrons(value, self.element1):
            pass
        else:
            element = self.get_element_by_neutrons(value)
            print(element)
            self.comboBox.setCurrentText(element)
        self.calculate()

    def change_spinbox2(self, value):
        if self.element_has_neutrons(value, self.element2):
            pass
        else:
            element = self.get_element_by_neutrons(value)
            print(element)
            self.comboBox_2.setCurrentText(element)
        self.calculate()

    def change_combobox2(self, value):
        print(value)
        self.element2 = value
        neutrons = int(self.get_neutrons_by_name(value))
        self.spinBox_2.setValue(neutrons)
        self.calculate()

    def element_has_neutrons(self, neutrons, name):
        for element in pkin.Data.data:
            if element[3] == name:
                print((element[3], name, element[0], neutrons))
                if int(element[0]) == neutrons:
                    return True
        return False

    def get_element_by_neutrons(self, neutrons):
        for element in pkin.Data.data:
            if int(element[0]) == neutrons:
                return element[3]

    def get_neutrons_by_name(self, name):
        elements = [element for element in pkin.Data.data if name == element[3]]
        print(elements)
        # keys = [float(element[5]) for element in elements]
        x = sorted(elements, key=lambda element: element[5], reverse=True)
        print(x)
        return x[0][0]
        # for element in pkin.Data.data:
        #    if element[3] == name:
        #        return element[0]

    def load_combobox(self):
        element_names = []
        for element in pkin.Data.data[1:]:
            if not(element[3] in element_names):
                element_names.append(element[3])

        for combobox in [self.comboBox, self.comboBox_2]:
            combobox.addItems(element_names)

    def settings(self):
        print('settings')

    def save(self):
        import os
        import tkinter
        root = tkinter.Tk()
        from tkinter import filedialog
        curr_directory = os.getcwd()
        name = filedialog.asksaveasfilename(
            initialdir=curr_directory, title="Choose a location to save this calculation", filetypes=(("RBS Calculation", "*.Qkin"), ('all file', '*.*')))
        root.destroy()
        print(name)
        if not('.Qkin' in name):
            name += '.Qkin'
        with open(name, 'w+') as f:
            try:
                dump(self.json_data, f)
            except AttributeError:
                dump({}, f)
        preferences['last_file'] = name
        with open('preferences.json', 'w') as f:
            dump(preferences, f)

    def load(self, name=None, data=None):

        if name == None and data == None:
            import os
            import tkinter
            root = tkinter.Tk()
            from tkinter import filedialog
            curr_directory = os.getcwd()
            name = filedialog.askopenfilename(
                initialdir=curr_directory, title="Choose the calculation to load", filetypes=[("RBS calculation", "*.Qkin")])
            root.destroy()

        try:
            if data == None:
                with open(name, 'r') as f:
                    data = load(f)
            self.spinBox_2.setValue(int(data['neutrons2']))
            self.spinBox.setValue(int(data['neutrons1']))
            self.spinBox_3.setValue(float(data['theta']))
            self.spinBox_4.setValue(float(data['E_MeV']))
        except FileNotFoundError:
            return None

        self.comboBox.setCurrentText(data['name1'])
        self.comboBox_2.setCurrentText(data['name2'])

    def save_preferences(self):
        # self.save()
        preferences['width'] = self.MainWindow.size().width()
        preferences['height'] = self.MainWindow.size().height()
        preferences['data'] = self.json_data
        with open('preferences.json', 'w+') as f:
            dump(preferences, f)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec_()
    ui.save_preferences()

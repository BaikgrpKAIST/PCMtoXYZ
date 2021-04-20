import sys
from PCMtoXYZ import *
from PyQt5.QtWidgets import QApplication, QDialog
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from MainUI import Ui_GUI
from Popup1 import Ui_Complete
from Popup2 import Ui_Err
import os

###TestVariables###
pcmlocation = "Z:\MS\TPY PCM\MS2.pcm"
DirLocation = "Z:\MS\TPY PCM"
Prefix = "conf"

def xyzgen(path, genname):
    if not os.path.exists(path):
        os.makedirs(path)
    open(path+'\\'+genname+'.xyz', 'w+')

class ProgramDesign(QDialog, Ui_GUI):
    def __init__(self):
        super().__init__()
        self.ui = Ui_GUI()
        self.ui.setupUi(self)
        self.show()
        self.ui.SaveButton.clicked.connect(self.mainftn)
        self.ui.ExitButton.clicked.connect(self.closeftn)
        self.ui.Choosefile.clicked.connect(self.chooseftn)
        self.ui.OutputB.clicked.connect(self.outputftn)


    def mainftn(self):
        global pcmlocation, DirLocation, Prefix
#        DirLocation = self.ui.OutputBox.toPlainText()
        Prefix = self.ui.PrefixBox.toPlainText()
        if pcmlocation == '' or DirLocation == '' or Prefix == '':
            global errpopup
            errpopup = Errorpopup()
        else:
            f = open(pcmlocation, "r")
            contents = f.readlines()
            numconf = 1
            for line in contents:
                string = line.split()
                if string[0] == '{PCM':
                    Filename = Prefix+str(numconf)
                    path = DirLocation + '\\' + str(Filename)
                    xyzgen(path, Filename)
                    flag = 1
                    numconf = numconf + 1
                elif flag == 1:
                    flag = 2
                    numatom = string[1]
                    xyzfile = open(path+'\\'+Filename+'.xyz', 'a')
                    xyzfile.write(str(numatom))
                    xyzfile.write('\n\n')
                elif string[0] == 'AT':
                    xyzfile.write(PCM_XYZ(int(string[2]))+' ')
                    xyzfile.write(string[3]+' '+string[4]+' '+string[5]+'\n')
            f.close()
            global ui2
            ui2 = Completepopup()

    def chooseftn(self):
        Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
        global pcmlocation
        pcmlocation = askopenfilename()
        self.ui.PCMBox.setPlainText(pcmlocation)

    def outputftn(self):
        Tk().withdraw()
        global DirLocation
        DirLocation = filedialog.askdirectory()
        self.ui.OutputBox.setPlainText(DirLocation)


    def closeftn(self):
        ui.close()

class Completepopup(QDialog, Ui_Complete):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Complete()
        self.ui.setupUi(self)
        self.show()
        self.ui.OKButton.clicked.connect(self.closeftn)

    def closeftn(self):
        ui2.close()


class Errorpopup(QDialog, Ui_Err):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Err()
        self.ui.setupUi(self)
        self.show()
        self.ui.OKButton_2.clicked.connect(self.closeftn)

    def closeftn(self):
        errpopup.close()


app = QApplication(sys.argv)
#GUI = QDialog()
ui = ProgramDesign()
#ui.setupUi(GUI)
ui.show()
#ui2 = Completepopup()
#ui2.show()
sys.exit(app.exec_())

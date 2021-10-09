
from PyQt5.QtWidgets import QApplication, QWidget,QGroupBox, QGridLayout,QDialog,QPushButton,QVBoxLayout
import sys
from PyQt5.QtGui import QIcon
from Ui_durak import Ui_DurakEkle
import main
from PyQt5 import*

gBox1 = QGroupBox() 

layout = QGridLayout()

vbox = QVBoxLayout()
gBox1.setLayout(layout)


def create_buttons(self,name):
         btn1=QPushButton("name",self)
         btn1.setFixedSize(150, 50)
         self.gridLayout_2.addWidget(btn1)
         self.grBoxStation.setLayout(self.gridLayout_2)
         btn1.show()



import sys
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget,QGroupBox, QGridLayout,QDialog,QPushButton,QVBoxLayout,QHBoxLayout
from PyQt5.uic import loadUi
from Ui_durak import Ui_DurakEkle
import vlc
import time
import mp3,jsonOku,jsonYaz,buttonCreate
import json

class DesignerGui(QDialog):  # QDialog class is inheritance

    def __init__(self):
        super().__init__()   # super ile QDialog classlarına erişiyoruz
        loadUi("durak.ui",self)
        #self.onaybtn.clicked.connect(self.hesapla)
        self.btnAracDepo.clicked.connect(mp3.Anons)
        self.hatcombobox.activated.connect(self.handleItemPressed)
        
    def handleItemPressed(self):
    #layout ta button varsa hepsini temizler
        for i in reversed(range(self.gridLayout_2.count())): 
            self.gridLayout_2.itemAt(i).widget().setParent(None)
        rota=[]
        item = self.hatcombobox.currentText()
        name='./stations/'+item+'.json'
        data =jsonOku.JsonOku(name)
        for i in data['istasyon']: 
            a=(i["istasyonadi"])
            rota.append(a) 
        positions = [(a,b) for a in range(5) for b in range(3)]   # 3 e 5 matrix oluşturmak için kullanıyoruz.
        for position ,irota in zip(positions,rota):   # zip fonksiyonu matrix oluşturmaya yarar.
            btn= QPushButton(text=irota, objectName=irota)
            btn.setFixedSize(150,50)
            btn.setFont(QFont('Arial-Black',9))
            btn.setToolTip('İstasyonlari oluşturun')
            btn.text=irota
            self.gridLayout_2.addWidget(btn,*position)
            self.grBoxStation.setLayout(self.gridLayout_2)
            ###
            
      
  
    
    def hesapla(self):
        print('eser') 
        
            

        

                        
                        
        
      

uygulama = QApplication(sys.argv)
pencere = DesignerGui()
pencere.show()
uygulama.exit(uygulama.exec_())

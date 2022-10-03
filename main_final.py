from msilib.schema import Dialog
import sys,os,subprocess,time,traceback
from PyQt5 import QtCore, QtGui, QtWidgets
import speedtest
import ssl

import threading
import urllib.request
import time
import os
from time import sleep
from tqdm import tqdm
from colorama import Fore, init
from PyQt5.QtGui import QMovie
from threading import Thread
import multithread

ssl._create_default_https_context = ssl._create_unverified_context

class StringThread(QtCore.QThread):

    str_signal = QtCore.pyqtSignal(str)
    _name = 'kik'

    def __init__(self, name):
        QtCore.QThread.__init__(self)
        self._name = name
        print("Thread Created")

    def run(self):
        self.str_signal.emit('Emitted message from StringThread. Name = ' + self._name)
        print("Done run")

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(706, 476)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color:rgb(34, 29, 51);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_test = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_test.setGeometry(QtCore.QRect(270, 380, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_test.setFont(font)
        self.pushButton_test.setStyleSheet("background-color:rgb(79, 79, 79);\n"
"color:rgb(255, 255, 255);\n"
"border-radius:6%;")
        self.pushButton_test.setObjectName("pushButton_test")

        ############################################
        
        self.pushButton_test.clicked.connect(self.test2)

        #############################################

  
   
 
        

        self.pushButton_toofast = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_toofast.setGeometry(QtCore.QRect(10, 450, 171, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_toofast.setFont(font)
        self.pushButton_toofast.setStyleSheet("background-color:rgb(79, 79, 79);\n"
"color:rgb(255, 255, 255);\n"
"border-radius:6%;")
        self.pushButton_toofast.setObjectName("pushButton_toofast")
        self.label_credits = QtWidgets.QLabel(self.centralwidget)
        self.label_credits.setGeometry(QtCore.QRect(540, 450, 161, 20))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_credits.setFont(font)
        self.label_credits.setStyleSheet("color:rgb(170, 1, 255)\n"
"\n"
"")
        self.label_credits.setObjectName("label_credits")
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(10, 30, 681, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet("color:rgb(170, 1, 255)\n"
"")
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.label_download_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_download_2.setGeometry(QtCore.QRect(160, 100, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_download_2.setFont(font)
        self.label_download_2.setStyleSheet("color:rgb(170, 1, 255)\n"
"")
        self.label_download_2.setObjectName("label_download_2")
        self.label_upload_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_upload_2.setGeometry(QtCore.QRect(160, 140, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label_upload_2.setFont(font)
        self.label_upload_2.setStyleSheet("color:rgb(170, 1, 255)\n"
"")
        self.label_upload_2.setObjectName("label_upload_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(320, 90, 231, 31))
        self.frame.setStyleSheet("background-color:rgb(212, 212, 212)")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_download = QtWidgets.QLabel(self.frame)
        self.label_download.setGeometry(QtCore.QRect(0, 0, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_download.setFont(font)
        self.label_download.setText("")
        self.label_download.setAlignment(QtCore.Qt.AlignCenter)
        self.label_download.setObjectName("label_download")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(320, 140, 231, 31))
        self.frame_2.setStyleSheet("background-color:rgb(212, 212, 212)")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_upload = QtWidgets.QLabel(self.frame_2)
        self.label_upload.setGeometry(QtCore.QRect(0, 0, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_upload.setFont(font)
        self.label_upload.setText("")
        self.label_upload.setAlignment(QtCore.Qt.AlignCenter)
        self.label_upload.setObjectName("label_upload")









        
        
        self.label_animation = QtWidgets.QLabel(self.centralwidget)
        self.label_animation.setObjectName("label_animation")
        self.label_animation.setGeometry(QtCore.QRect(290, 290, 120, 80))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label_animation.setFont(font)

        movie=QMovie('plip-walk.gif')
        self.label_animation.setMovie(movie)
        movie.start()

        #self.animationbot = QtWidgets.QFrame(self.centralwidget)
        #self.animationbot.setGeometry(QtCore.QRect(290, 290, 120, 80))
        #self.animationbot.setFrameShape(QtWidgets.QFrame.StyledPanel)
        #self.animationbot.setFrameShadow(QtWidgets.QFrame.Raised)
        #self.animationbot.setObjectName("animationbot")




        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(560, 430, 131, 20))
        self.label.setStyleSheet("color:rgb(255, 255, 255)")
        self.label.setObjectName("label")
        self.label_upload_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_upload_3.setGeometry(QtCore.QRect(160, 190, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label_upload_3.setFont(font)
        self.label_upload_3.setStyleSheet("color:rgb(170, 1, 255)\n"
"")
        self.label_upload_3.setObjectName("label_upload_3")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(320, 190, 231, 31))
        self.frame_3.setStyleSheet("background-color:rgb(212, 212, 212)")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_download_3 = QtWidgets.QLabel(self.frame_3)
        self.label_download_3.setGeometry(QtCore.QRect(0, 0, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_download_3.setFont(font)
        self.label_download_3.setText("")
        self.label_download_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_download_3.setObjectName("label_download_3")
        self.label_ping = QtWidgets.QLabel(self.frame_3)
        self.label_ping.setGeometry(QtCore.QRect(0, 0, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_ping.setFont(font)
        self.label_ping.setText("")
        self.label_ping.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ping.setObjectName("label_ping")
        self.label_host = QtWidgets.QLabel(self.centralwidget)
        self.label_host.setGeometry(QtCore.QRect(20, 250, 321, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_host.setFont(font)
        self.label_host.setStyleSheet("color:rgb(170, 255, 0)")
        self.label_host.setText("")
        self.label_host.setAlignment(QtCore.Qt.AlignCenter)
        self.label_host.setObjectName("label_host")
        self.label_sponsor = QtWidgets.QLabel(self.centralwidget)
        self.label_sponsor.setGeometry(QtCore.QRect(370, 250, 321, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_sponsor.setFont(font)
        self.label_sponsor.setStyleSheet("color:rgb(255, 255, 0)")
        self.label_sponsor.setText("")
        self.label_sponsor.setAlignment(QtCore.Qt.AlignCenter)
        self.label_sponsor.setObjectName("label_sponsor")
        self.label_status = QtWidgets.QLabel(self.centralwidget)
        self.label_status.setGeometry(QtCore.QRect(270, 430, 151, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_status.setFont(font)
        self.label_status.setStyleSheet("color:rgb(131, 0, 197)")
        self.label_status.setText("")
        self.label_status.setAlignment(QtCore.Qt.AlignCenter)
        self.label_status.setObjectName("label_status")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    
    def test2(self,Dialog):
                self.label_status.setText(str('Finding Optimal Server'))
                st = speedtest.Speedtest()
                st.get_best_server()  # Get the most optimal server available
                for i in tqdm(range(10), colour="green", desc="Finding Optimal Server"):
                        sleep(0.05)
                self.label_status.setText(str('Getting Download Speed'))
                st.download()  # Get downloading speed
                for i in tqdm(range(10), colour="cyan", desc="Getting Download Speed"):        
                        sleep(0.05)
                self.label_status.setText(str('Getting Upload Speed'))
                st.upload()  # Get uploading Speed
                for i in tqdm(range(10), colour="red", desc="Getting Upload Speed"):
                        
                        sleep(0.05)

                # Save all these elements in a dictionary
                res_dict = st.results.dict()

                # Assign to variables with an specific format
                dwnl = str(res_dict['download'])[:2] + "." + \
                str(res_dict['download'])[2:4]

                upl = str(res_dict['upload'])[:2] + "." + str(res_dict['upload'])[2:4]

                # Display results in a nice looking table using colorama features
                print("")
                
                # divider - a line in the screen with a fixed width
                print(Fore.MAGENTA + "="*80)
                print(Fore.GREEN + "INTERNET SPEED TEST RESULTS:".center(80))
                print(Fore.MAGENTA + "="*80)
                print(Fore.YELLOW +
                        f"Download: {dwnl}mbps({float(dwnl)*0.125:.2f}MBs) | Upload:{upl}mbps ({float(upl)*0.125:.2f}MBs) | Ping: {res_dict['ping']:.2f}ms".center(80))
                print(Fore.MAGENTA + "-"*80)
                print(Fore.CYAN +
                        f"HOST:{res_dict['server']['host']} | SPONSOR:{res_dict['server']['sponsor']} | LATENCY: {res_dict['server']['latency']:.2f}".center(80))
                print(Fore.MAGENTA + "-"*80)

                self.label_download.setText(dwnl+str('  Mbps'))
                self.label_upload.setText(upl+str('  Mbps'))
                self.label_ping.setText(str(res_dict['ping'])+str('  ms'))

                self.label_host.setText(str('HOST:  ')+str(res_dict['server']['host']))
                self.label_sponsor.setText(str('SPONSOR:  ')+str(res_dict['server']['sponsor']))
                

    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_test.setText(_translate("MainWindow", "START TEST"))
        self.pushButton_toofast.setText(_translate("MainWindow", "MY INTERNET IS TOO FAST ?"))
        self.label_credits.setText(_translate("MainWindow", "Speedy by Bendib Mohamed Anis"))
        self.label_title.setText(_translate("MainWindow", "Speed Tester"))
        self.label_download_2.setText(_translate("MainWindow", "Download"))
        self.label_upload_2.setText(_translate("MainWindow", "Upload"))
        self.label.setText(_translate("MainWindow", "Persistance is the key"))
        self.label_upload_3.setText(_translate("MainWindow", "Ping"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
       
    





    sys.exit(app.exec_())
# main windows standar

from PyQt5 import QtGui,QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QMessageBox
import sys
from untitled import Ui_MainWindow
from PyQt5.QtWidgets import *
import random
import os
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QUrl
import datetime
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FingureCanvas
from matplotlib.figure import Figure
import numpy as np
######################## class pour canvas plot de bases nucleique
class Canvas(FingureCanvas):

    def __init__(self, parent = None, width =5, height = 5, dpi =145):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        FingureCanvas.__init__(self, fig)
        self.setParent(parent)
        self.plot()
    def plot(self):
        nucfour=''
        with open("nuc.txt") as file:
            nucfour=file.read().split("\n")
        a=float(nucfour[0])
        t=float(nucfour[1])
        g=float(nucfour[2])
        c=float(nucfour[3])
        x = np.array([a, t, g, c])
        labels = ['A', 'T', 'G' , 'C']
        ax = self.figure.add_subplot(111)
        ax.pie(x, labels=labels)
        #ax2 = self.figure.add_subplot(333)
        #ax2.pie(x, labels=labels)

class Window(QMainWindow):

    def __init__(self):

        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
        #les buttons de graph
        self.ui.pushButton_16.hide()
        #self.ui.pushButton_17.hide()
        self.ui.pushButton_17.clicked.connect(self.showgragh)
        #manuelle de utilasation 1
        self.path = r"aide1.pdf"
        self.url = bytearray(QUrl().fromLocalFile(self.path).toEncoded()).decode()
        self.text = "<a href={}>></a>".format(self.url)
        self.ui.pushButton.setText(self.text+"?")
        self.ui.pushButton.setOpenExternalLinks(True)
        #manuelle de utilasation 2
        self.path = r"aide2.pdf"
        self.url = bytearray(QUrl().fromLocalFile(self.path).toEncoded()).decode()
        self.text = "<a href={}>></a>".format(self.url)
        self.ui.pushButton_14.setText(self.text+"?")
        self.ui.pushButton_14.setOpenExternalLinks(True)
        #manuelle de utilasation 3
        self.path = r"aide3.pdf"
        self.url = bytearray(QUrl().fromLocalFile(self.path).toEncoded()).decode()
        self.text = "<a href={}>></a>".format(self.url)
        self.ui.pushButton_15.setText(self.text+"?")
        self.ui.pushButton_15.setOpenExternalLinks(True)

        #griser les buttons
        self.ui.ValiderNbrAdn.setEnabled(False)
        self.ui.pushButton_7.setEnabled(False)
        self.ui.pushButton_13.setEnabled(False)
        self.ui.pushButton_2.setEnabled(False)
        self.ui.pushButton_3.setEnabled(False)
        self.ui.pushButton_4.setEnabled(False)
        self.ui.pushButton_5.setEnabled(False)
        self.ui.pushButton_6.setEnabled(False)
        self.ui.pushButton_8.setEnabled(False)
        self.ui.lineEdit.setPlaceholderText('#nuc')
        self.ui.lineEdit_2.setPlaceholderText('#sec')
        self.ui.listWidget_2.hide()
        # le button de sauvgarde du resultat
        self.ui.pushButton_9.clicked.connect(self.saveWindows)
        #les buttons des fonctions ARN
        self.btn_grp4= QButtonGroup()
        self.btn_grp4.setExclusive(True)
        self.btn_grp4.addButton(self.ui.pushButton_10)
        self.btn_grp4.addButton(self.ui.pushButton_11)
        self.btn_grp4.addButton(self.ui.pushButton_12)
        self.btn_grp4.buttonClicked.connect(self.FONCTIONS_ARN)
        #les buttons des fonctions ADN
        self.btn_grp3= QButtonGroup()
        self.btn_grp3.setExclusive(True)
        self.btn_grp3.addButton(self.ui.pushButton_13)
        self.btn_grp3.addButton(self.ui.pushButton_2)
        self.btn_grp3.addButton(self.ui.pushButton_3)
        self.btn_grp3.addButton(self.ui.pushButton_4)
        self.btn_grp3.addButton(self.ui.pushButton_5)
        self.btn_grp3.addButton(self.ui.pushButton_6)
        self.btn_grp3.addButton(self.ui.pushButton_8)
        self.btn_grp3.buttonClicked.connect(self.FONCTIONS_ADN)
        # les radio buttons un seul sequence plusius ADN
        self.btn_grpRADIO = QButtonGroup()
        self.btn_grpRADIO.setExclusive(True)
        self.btn_grpRADIO.addButton(self.ui.radioButton_4)# tts les sequences
        self.btn_grpRADIO.addButton(self.ui.radioButton_3)# un seule sequence
        self.btn_grpRADIO.buttonClicked.connect(self.RADIOSEQUENCE)
        #les botton de insertion de ADN
        self.btn_grp = QButtonGroup()
        self.btn_grp.setExclusive(True)
        self.btn_grp.addButton(self.ui.ValiderNbrAdn)
        self.btn_grp.addButton(self.ui.pushButton_7)
        self.btn_grp.buttonClicked.connect(self.ADN_ENTRIE)
        ########################### group de radio buttons
        self.btn_grp2 = QButtonGroup()
        self.btn_grp2.setExclusive(True)
        self.btn_grp2.addButton(self.ui.radioButton)
        self.btn_grp2.addButton(self.ui.radioButton_2)
        self.btn_grp2.buttonClicked.connect(self.RADION_ADN_ENTRIE)
        #####################################################################
        # dialog de sauvgarde les resultats
        self.d = QDialog()
        self.d.setWindowTitle("Sauvgarde")
        self.d.resize(340, 400)
        self.d.setStyleSheet("background-color: #636363;")
        self.centralwidget = QWidget(self.d)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_9 = QGroupBox(self.centralwidget)
        self.groupBox_9.setGeometry(QtCore.QRect(50, 80, 240, 231))
        self.groupBox_9.setStyleSheet("QGroupBox \n""{\n""\n""color:#c2c2c2;\n""margin: 0em;\n""  border: 1px solid #c2c2c2; \n""  border-radius: 8px;\n""} \n""")
        self.groupBox_9.setTitle("")
        self.groupBox_9.setObjectName("groupBox_9")
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(70, 70, 81, 16))
        self.label_8.setStyleSheet("font: 75 10pt \"Tw Cen MT\";\n""color:#c2c2c2;")
        self.label_8.setObjectName("label_8")
        self.save = QPushButton(self.centralwidget)
        self.save.setGeometry(QtCore.QRect(140, 320, 50, 23))
        self.save.setStyleSheet("color:\"white\";\n""background-color:#d50000;")
        self.save.setObjectName("save")
        self.checkBox_2 = QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(90, 110, 151, 21))
        self.checkBox_2.setStyleSheet("color:#c2c2c2;\n""font: 75 10pt \"Tw Cen MT\";")
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(90, 130, 151, 21))
        self.checkBox_3.setStyleSheet("color:#c2c2c2;\n""font: 75 10pt \"Tw Cen MT\";")
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QCheckBox(self.centralwidget)
        self.checkBox_4.setGeometry(QtCore.QRect(90, 150, 151, 21))
        self.checkBox_4.setStyleSheet("color:#c2c2c2;\n""font: 75 10pt \"Tw Cen MT\";")
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QCheckBox(self.centralwidget)
        self.checkBox_5.setGeometry(QtCore.QRect(90, 170, 151, 21))
        self.checkBox_5.setStyleSheet("color:#c2c2c2;\n""font: 75 10pt \"Tw Cen MT\";")
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_6 = QCheckBox(self.centralwidget)
        self.checkBox_6.setGeometry(QtCore.QRect(90, 190, 151, 21))
        self.checkBox_6.setStyleSheet("color:#c2c2c2;\n""font: 75 10pt \"Tw Cen MT\";")
        self.checkBox_6.setObjectName("checkBox_6")
        self.checkBox_7 = QCheckBox(self.centralwidget)
        self.checkBox_7.setGeometry(QtCore.QRect(90, 210, 191, 21))
        self.checkBox_7.setStyleSheet("color:#c2c2c2;\n""font: 75 10pt \"Tw Cen MT\";")
        self.checkBox_7.setObjectName("checkBox_7")
        self.checkBox_8 = QCheckBox(self.centralwidget)
        self.checkBox_8.setGeometry(QtCore.QRect(90, 230, 191, 21))
        self.checkBox_8.setStyleSheet("color:#c2c2c2;\n""font: 75 10pt \"Tw Cen MT\";")
        self.checkBox_8.setObjectName("checkBox_8")
        self.checkBox_9 = QCheckBox(self.centralwidget)
        self.checkBox_9.setGeometry(QtCore.QRect(90, 250, 191, 21))
        self.checkBox_9.setStyleSheet("color:#c2c2c2;\n""font: 75 10pt \"Tw Cen MT\";")
        self.checkBox_9.setObjectName("checkBox_9")
        ###########les noms des widgets
        self.label_8.setText( "Sauvegrader:")
        self.save.setText( "Valider")
        self.checkBox_2.setText( "ADN Reverse")
        self.checkBox_3.setText( "Frequence Bn ADN")
        self.checkBox_4.setText( "Frequence codons")
        self.checkBox_5.setText( "%GC")
        self.checkBox_6.setText( " Sequences ARN")
        self.checkBox_7.setText( "Sequence ARN apres epissage")
        self.checkBox_8.setText( "Sequences proteique")
        self.checkBox_9.setText( "La masse protéique")
        self.save.clicked.connect(self.save_resultat)
    def showgragh(self):
        def delet_file(namefile):
             if os.path.isfile(namefile):
                 os.remove(namefile)
             else:    ## Show an error ##
                 print("Error: %s file not found" % namefile)
        def write_result(result,nomfichier):#this methode is to creat a file that contain the result
            RFILE = open(nomfichier,'a')
            RFILE.write(result)
            RFILE.close()
        ######################pour designer plot
        if self.ui.textBrowser_7.toPlainText()!='':
            delet_file("nuc.txt")
            write_result(self.ui.textBrowser_7.toPlainText()+"\n","nuc.txt")
            write_result(self.ui.textBrowser_6.toPlainText()+"\n","nuc.txt")
            write_result(self.ui.textBrowser_4.toPlainText()+"\n","nuc.txt")
            write_result(self.ui.textBrowser_5.toPlainText()+"\n","nuc.txt")
            self.canvas = Canvas(self, width=8, height=4)
            self.canvas.show()
            self.ui.pushButton_16.show()
            self.ui.pushButton_16.clicked.connect(self.hidegraph)
    def hidegraph(self):
        self.canvas.hide()
    ############################################################################
    def saveWindows(self):
        self.d.exec_()
    # sauvgarder les resultats
    ############################################################################
    def save_resultat(self):
        def write_result(result,nomfichier):#this methode is to creat a file that contain the result
            RFILE = open(nomfichier,'a')
            RFILE.write(result)
            RFILE.close()
        #adn inverse
        def date():# retourner la date
            now = datetime.datetime.now()
            return str(now.strftime("%Y-%m-%d %H:%M:%S"))

        write_result("la date :"+date()+"\n","fichier_resultat.txt")
        if self.ui.radioButton_4.isChecked()==True and self.ui.textBrowser_3.toPlainText()!='':
            write_result("Sequence ADN:"+self.ui.textBrowser_3.toPlainText()+"\n","fichier_resultat.txt")
        else:
            adn_resultTAB=self.ui.textEdit.toPlainText().split("\n")
            adn_result=adn_resultTAB[0]
            write_result("Sequence ADN:"+adn_result+"\n","fichier_resultat.txt")
            pass
        if self.checkBox_2.isChecked():
            if self.ui.textEdit_4.toPlainText()!='':
                write_result("ADN inverse : "+self.ui.textEdit_4.toPlainText()+"\n","fichier_resultat.txt")#adn inversse
                pass
            pass
        if self.checkBox_3.isChecked():
            if self.ui.textBrowser_4.toPlainText()!='':
                write_result("Frequences des bases : \n","fichier_resultat.txt")
                write_result("G : "+self.ui.textBrowser_4.toPlainText()+"\n","fichier_resultat.txt")#G
                write_result("C : "+self.ui.textBrowser_5.toPlainText()+"\n","fichier_resultat.txt")#C
                write_result("A : "+self.ui.textBrowser_7.toPlainText()+"\n","fichier_resultat.txt")#A
                write_result("T : "+self.ui.textBrowser_6.toPlainText()+"\n","fichier_resultat.txt")#T
                pass
            pass
        if self.checkBox_4.isChecked():
            if self.ui.textBrowser_2.toPlainText()!='':
                write_result("Frequence de L ADN codants est :"+self.ui.textBrowser_2.toPlainText()+"\n","fichier_resultat.txt")# Frequence codons
                pass
            pass
        if self.checkBox_5.isChecked():
            if self.ui.textBrowser.toPlainText()!='':
                write_result("Taux de GC dans la sequence est :"+self.ui.textBrowser.toPlainText()+"\n","fichier_resultat.txt")#%GC
                pass
            pass
        if self.checkBox_6.isChecked():
            if self.ui.textEdit_3.toPlainText()!='':
                write_result("Sequence de ARN est :"+self.ui.textEdit_3.toPlainText()+"\n","fichier_resultat.txt")#Sequences ARN
                pass
            pass
        if self.checkBox_7.isChecked():
            if self.ui.textEdit_2.toPlainText()!='':
                write_result("Sequence ARN apres l'eppisage est: "+self.ui.textEdit_2.toPlainText()+"\n","fichier_resultat.txt")#Sequence ARN apres epissage
                pass
            pass
        if self.checkBox_8.isChecked():
            if self.ui.textBrowser_9.toPlainText()!='':
                write_result("Sequence proteique est: "+self.ui.textBrowser_9.toPlainText(),"fichier_resultat.txt")#Sequences proteique
                pass
            pass
        if self.checkBox_9.isChecked():
            if self.ui.textBrowser_8.toPlainText()!='':
                write_result("Masse proteique est: "+self.ui.textBrowser_8.toPlainText()+"\n","fichier_resultat.txt")#La masse protéique
                pass
            pass
        write_result("############################################################\n","fichier_resultat.txt")
        self.d.hide()
    ############################################################################
    #################### les fonctions sur ARN #################################
    def FONCTIONS_ARN(self,btn):
        # fonctions de read FASTA fichier
        def readFASTA(filename):
             with open(filename) as file:
                return (file.read().split('>')[1:])

        def read_FASTA_entries(filename):
            return[seq.partition('\n')for seq in readFASTA(filename)]

        def final_FASTA(filename):
            return[seq[2].replace('\n','') for seq in read_FASTA_entries(filename)]
        ############################################################## dictionaire des acides aminnees
        acide_aminee_MASS_TABLE2 = {
        'Ala': 71.03711,
        'Cys': 103.00919,
        'Asp': 115.02694,
        'Glu': 129.04259,
        'Phe': 147.06841,
        'Gly': 57.02146,
        'His': 137.05891,
        'Ile': 113.08406,
        'Lys': 128.09496,
        'Leu': 113.08406,
        'Met': 131.04049,
        'Asn': 114.04293,
        'Pro': 97.05276,
        'Gln': 128.05858,
        'Arg': 156.10111,
        'Ser': 87.03203,
        'Thr': 101.04768,
        'Val': 99.06841,
        'Trp': 186.07931,
        'Tyr': 163.06333,
        'Urp': 157.01035
        }
        ###################################################################### le dictionaire des ARN codons
        RNA_codon_tabl={'UUU': 'Phe', 'UCU': 'Ser', 'UAU': 'Tyr', 'UGU': 'Cys' , 'UUC': 'Phe', 'UCC': 'Ser', 'UAC': 'Tyr', 'UGC': 'Cys' ,
        'UUA': 'Leu', 'UCA': 'Ser', 'UAA': '---', 'UGA': '---', 'UUG': 'Leu', 'UCG': 'Ser', 'UAG': '---', 'UGG': 'Urp',
        'CUU': 'Leu', 'CCU': 'Pro', 'CAU': 'His', 'CGU': 'Arg', 'CUC': 'Leu', 'CCC': 'Pro', 'CAC': 'His', 'CGC': 'Arg',
        'CUA': 'Leu', 'CCA': 'Pro', 'CAA': 'Gln', 'CGA': 'Arg', 'CUG': 'Leu', 'CCG': 'Pro', 'CAG': 'Gln', 'CGG': 'Arg',
        'AUU': 'Ile', 'ACU': 'Thr', 'AAU': 'Asn', 'AGU': 'Ser', 'AUC': 'Ile', 'ACC': 'Thr', 'AAC': 'Asn', 'AGC': 'Ser',
        'AUA': 'Ile', 'ACA': 'Thr', 'AAA': 'Lys', 'AGA': 'Arg', 'AUG': 'Met', 'ACG': 'Thr', 'AAG': 'Lys', 'AGG': 'Arg',
        'GUU': 'Val', 'GCU': 'Ala', 'GAU': 'Asp', 'GGU': 'Gly', 'GUC': 'Val', 'GCC': 'Ala', 'GAC': 'Asp', 'GGC': 'Gly',
        'GUA': 'Val', 'GCA': 'Ala', 'GAA': 'Glu', 'GGA': 'Gly', 'GUG': 'Val', 'GCG': 'Ala', 'GAG': 'Glu', 'GGG': 'Gly'}
        if self.ui.textEdit_3.toPlainText()!='':
            arn_resultTAB=self.ui.textEdit_3.toPlainText().split("\n")
            if self.ui.textEdit_2.toPlainText()!='':
                arn_result=self.ui.textEdit_2.toPlainText()
            else:
                arn_result=arn_resultTAB[0]
                pass
            ########################################################## la masse proteique
            # message box pour effecuter l epissage avant  de calculer la masse ou avant la traduction de ARN en proteine
            if self.ui.textEdit_2.toPlainText()=='' and (btn.text()=='Calculer la masse protéique' or btn.text()=='Transcription ARN en protéines'):
                buttonReply = QMessageBox.question(self, "Attention!", "vous devez effectuer l'epissage avant!!", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if buttonReply == QMessageBox.Yes:
                    print('Yes')

                    ######################
                    try:
                        # ouvrir le fichier des introns format FASTA
                        filename = QFileDialog.getOpenFileName(self, 'Ouvrir le fichier des introns  (FASTA) ', os.getenv('HOME'))
                        FASTA_introns=final_FASTA(filename[0])
                        def epissage(ARN,introns):
                            result = ''
                            for intron in introns:
                                ARN = ARN.replace(intron, '')
                            return ARN
                        self.ui.textEdit_2.setText(str(epissage(arn_result,FASTA_introns)))
                    except Exception as e:
                        print('Exception',str(e))
                    arn_result=str(epissage(arn_result,FASTA_introns))
                    print(arn_result)
                    ######################
                else:
                    print('No')
                pass
            ####################################################### Calculer la masse protéique
            if btn.text()=='Calculer la masse protéique':
                print('Calculer la masse protéique')
                if self.ui.textBrowser_9.toPlainText()!='':
                    print('fddf')
                    prt_masse=''
                    masse=0
                    for x in range(0,len(arn_result)-len(arn_result)%3,3):
                        three_nuc=arn_result[x:x+3]
                        if x!=len(arn_result)-3:
                            if three_nuc=="UAA" or three_nuc=="UGA" or three_nuc=="UAG":
                                break
                            else:
                                #prt_masse=prt_masse+RNA_codon_tabl.get(three_nuc)
                                masse=masse+acide_aminee_MASS_TABLE2.get(RNA_codon_tabl.get(three_nuc))
                                pass
                            pass
                        pass
                    #masse=0
                    #for value in range(0,len(prt_masse),3):
                        #acide_aminee=prt_masse[value:value+3]
                        #print(acide_aminee)
                        #masse=masse+acide_aminee_MASS_TABLE2.get(acide_aminee)

                        #pass
                    self.ui.textBrowser_8.setText(str(masse))
            ########################################################### transcription arn en proteine
            if btn.text()=='Transcription ARN en protéines':
                prt=''
                for x in range(0,len(arn_result)-len(arn_result)%3,3):
                    three_nuc=arn_result[x:x+3]
                    if x!=len(arn_result)-3:
                        if three_nuc=="UAA" or three_nuc=="UGA" or three_nuc=="UAG":
                            prt=prt+"STOP"+"\n"
                            break
                        else:
                            prt=prt+RNA_codon_tabl.get(three_nuc)+"--"
                            pass
                        pass
                    pass
                self.ui.textBrowser_9.setText(prt)
                print('Transcription ARN en protéines')
            ############################################################## effctuer l epissage
            if btn.text()=='Effectuer l\'épissage d\'ARN':
                print('Effectuer l\'épissage d\'ARN')
                try:
                    filename = QFileDialog.getOpenFileName(self, 'Ouvrir le fichier des introns  (FASTA) ', os.getenv('HOME'))
                    FASTA_introns=final_FASTA(filename[0])
                    print(FASTA_introns)
                    def epissage(ARN,introns):
                        result = ''
                        for intron in introns:
                            ARN = ARN.replace(intron, '')
                        return ARN
                    self.ui.textEdit_2.setText(str(epissage(arn_result,FASTA_introns)))
                    arn_result=str(epissage(arn_result,FASTA_introns))
                except Exception as e:
                    print('Exception',str(e))
    #####################################fin des fonctions ARN ################################

    ###########################################################################################
    ################################# les fonctions sur ADN ###################################
    # fonction pour affectuer l assamblage
    def FONCTIONS_ADN(self,btn):
        def assemblage(ADNs):
            print(ADNs)
            if len(ADNs)==2:
                return ADNs[0]
            else:
                j=0
                SequenceF=ADNs[0]
                ADNs.pop(0)
                while(len(ADNs)!=0):
                    t=[]
                    for i in range(0,len(ADNs)):
                        t.append(0)
                        if not ADNs[i] in SequenceF:
                            k=len(ADNs[i])
                            while(k>0):
                                j1=SequenceF.endswith(ADNs[i][0:k])
                                if j1==True:
                                    if k>t[i]:
                                        t[i]=k
                                k=k-1
                        else:
                            ADNs.pop(i)

                    j=t[0]
                    jInd=0
                    for i1 in range(1,len(t)):
                        if t[i1]>j:
                            j=t[i1]
                            jInd=i1
                    SequenceF=SequenceF[0:len(SequenceF)-j]+ADNs[jInd]
                    ADNs.pop(jInd)

                return SequenceF
                pass

        ###############################
        ############################################################# dictionaire des adn codants
        DNA_CODON_TABLE = {
            'TTT': 'Phe',     'CTT': 'Leu',     'ATT': 'Ile',     'GTT': 'Val',
            'TTC': 'Phe',     'CTC': 'Leu',     'ATC': 'Ile',     'GTC': 'Val',
            'TTA': 'Leu',     'CTA': 'Leu',     'ATA': 'Ile',     'GTA': 'Val',
            'TTG': 'Leu',     'CTG': 'Leu',     'ATG': 'Met',     'GTG': 'Val',
            'TCT': 'Ser',     'CCT': 'Pro',     'ACT': 'Thr',     'GCT': 'Ala',
            'TCC': 'Ser',     'CCC': 'Pro',     'ACC': 'Thr',     'GCC': 'Ala',
            'TCA': 'Ser',     'CCA': 'Pro',     'ACA': 'Thr',     'GCA': 'Ala',
            'TCG': 'Ser',     'CCG': 'Pro',     'ACG': 'Thr',     'GCG': 'Ala',
            'TAT': 'Tyr',     'CAT': 'His',     'AAT': 'Asn',     'GAT': 'Asp',
            'TAC': 'Tyr',     'CAC': 'His',     'AAC': 'Asn',     'GAC': 'Asp',
            'TAA': '-',     'CAA': 'Gln',     'AAA': 'Lys',     'GAA': 'Glu',
            'TAG': '-',     'CAG': 'Gln',     'AAG,': 'Lys',     'GAG': 'Glu',
            'TGT': 'Cys',     'CGT': 'Arg',     'AGT': 'Ser',     'GGT': 'Gly',
            'TGC': 'Cys',     'CGC': 'Arg',     'AGC': 'Ser',     'GGC': 'Gly',
            'TGA': '-',     'CGA': 'Arg',     'AGA': 'Arg',     'GGA': 'Gly',
            'TGG': 'Trp',     'CGG': 'Arg',     'AGG': 'Arg',     'GGG': 'Gly'
        }

        if self.ui.textEdit.toPlainText()!='':
            adn_resultTAB=self.ui.textEdit.toPlainText().split("\n")
            if self.ui.radioButton_4.isChecked()==True and self.ui.textBrowser_3.toPlainText()!='':
                adn_result=self.ui.textBrowser_3.toPlainText()
            else:
                adn_result=adn_resultTAB[0]
            ###################
            if self.ui.radioButton_4.isChecked()==True and self.ui.textBrowser_3.toPlainText()=='' and btn.text()!='L\'assemblage des fragments ADN' and btn.text()!='Verifier Validite ADN':
                # message box pour effectuer l assemblage avant faire les tratments sur la sequence d'ADN
                buttonReply = QMessageBox.question(self, "Attention!", "Veuillez effectuer l'assemblage !!", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if buttonReply == QMessageBox.Yes:
                    print('ah ndir')
                    self.ui.textBrowser_3.setText(assemblage(adn_resultTAB))
                    adn_resultTAB=self.ui.textEdit.toPlainText().split("\n")
                    adn_result=assemblage(adn_resultTAB)
                    print(adn_result)
                else:
                    print('non mandirch')
                pass
            ###############################################Verifier Validite ADN
            if btn.text()=='Verifier Validite ADN':#si ADN vien d un fichier
                print('Verifier Validite ADN')
                def verif(adn_result_pure):
                    return len(adn_result_pure) == adn_result_pure.count("A")+adn_result_pure.count("T")+adn_result_pure.count("C")+adn_result_pure.count("G")
                if verif(adn_result):
                    self.ui.pushButton_2.setEnabled(True)
                    self.ui.pushButton_3.setEnabled(True)
                    self.ui.pushButton_4.setEnabled(True)
                    self.ui.pushButton_5.setEnabled(True)
                    self.ui.pushButton_6.setEnabled(True)
                    self.ui.pushButton_8.setEnabled(True)
                    self.ui.pushButton_13.setEnabled(False)
                    QMessageBox.about(self, "la validite de sequence", "sequence valide")
                else:
                    self.ui.pushButton_7.setEnabled(False)
                    self.ui.pushButton_13.setEnabled(False)
                    self.ui.pushButton_2.setEnabled(False)
                    self.ui.pushButton_3.setEnabled(False)
                    self.ui.pushButton_4.setEnabled(False)
                    self.ui.pushButton_5.setEnabled(False)
                    self.ui.pushButton_6.setEnabled(False)
                    self.ui.pushButton_8.setEnabled(False)
                    self.ui.textEdit.setText('')
                    QMessageBox.about(self, "la validite de sequence", "sequence no valide")


            #################################################Frequence Bn ADN
            if btn.text()=='Frequence Bn ADN':
                print('Frequence Bn ADN')
                try:
                    self.ui.textBrowser_7.setText(str(adn_result.count("A")))
                    self.ui.textBrowser_6.setText(str(adn_result.count("T")))
                    self.ui.textBrowser_4.setText(str(adn_result.count("G")))
                    self.ui.textBrowser_5.setText(str(adn_result.count("C")))
                except Exception as e:
                    print('exeption')
            ################################################# generer ARN
            if btn.text()=='Generer ARN':
                print('Generer ARN')
                ARN=''
                for nuc in adn_result:
                    if nuc=='C':
                        ARN=ARN+'G'
                    if nuc=='G':
                        ARN=ARN+'C'
                    if nuc=='A':
                        ARN=ARN+'U'
                    if nuc=='T':
                        ARN=ARN+'A'
                self.ui.textEdit_3.setText(ARN)
            ################################################# revers de ADN
            if btn.text()=='Reverse ADN':
                print('Reverse ADN')
                adnrevers=''
                for nuc in adn_result:
                    if nuc=='C':
                        adnrevers=adnrevers+'G'
                    if nuc=='G':
                        adnrevers=adnrevers+'C'
                    if nuc=='A':
                        adnrevers=adnrevers+'T'
                    if nuc=='T':
                        adnrevers=adnrevers+'A'
                self.ui.textEdit_4.setText(adnrevers)

            ################################################# le taux de CG dans la sequence
            if btn.text()=='%GC':
                print('%GC')
                def tauxCG(ADN):
                    return float(ADN.count("C")+ADN.count("G"))* 100 /len(ADN)
                self.ui.textBrowser.setText(str(tauxCG(adn_result)))
            ################################################# Fréquences de codons dans ADN
            if btn.text()==' Fréquences de codons dans ADN':
                print(' Fréquences de codons dans ADN')
                #les triple non codon ADN sont : TAA TAG TGA
                def frequencecondon(ADN):
                    cpt_condon=0
                    cpt_noncondon=0
                    for i in range(0, len(ADN)-len(ADN)%3, 3):
                        codon = ADN[i:i+3]
                        if codon in DNA_CODON_TABLE and DNA_CODON_TABLE.get(codon)!='-':
                            cpt_condon=cpt_condon+3
                    freq=(cpt_condon*100)/(len(ADN))
                    return freq
                self.ui.textBrowser_2.setText(str(frequencecondon(adn_result)))
            ################################################## assemblage des fragments ADN
            if btn.text()=='L\'assemblage des fragments ADN':
                print('L\'assemblage des fragments ADN')
                self.ui.textBrowser_3.setText(assemblage(adn_resultTAB))


#####################################################################################
############################## fin des fonctions ADN #################################
    def ADN_ENTRIE(self,btn):
        #self.ui.lineEdit.text()
        #self.ui.lineEdit_2.text()
        ############################################################################# Generer sequence ADN aleatoire
        def delet_file(namefile):
             if os.path.isfile(namefile):
                 os.remove(namefile)
             else:    ## Show an error ##
                 print("Error: %s file not found" % namefile)
        if btn.text()=='Valider':
            print('valider')
            delet_file("nuc.txt")
            #hide liste  radio buttons
            if self.ui.lineEdit.text()!='' and self.ui.lineEdit_2.text()!='':
                self.ui.listWidget_2.clear()
                self.ui.listWidget_2.hide()
                self.ui.radioButton_4.setChecked(True)
                self.ui.radioButton_3.setChecked(False)
                #si les edit texts non vide
                if self.ui.textEdit.toPlainText()!='':
                    if self.ui.textEdit_4.toPlainText()!='' or self.ui.textBrowser_9.toPlainText()!='' or  self.ui.textBrowser_8.toPlainText()!='' or self.ui.textEdit_2.toPlainText()!='' or self.ui.textEdit_3.toPlainText()!='' or self.ui.textBrowser_2.toPlainText()!='' or self.ui.textBrowser.toPlainText()!='' or self.ui.textEdit_4.toPlainText()!='' or self.ui.textBrowser_3.toPlainText()!='' or self.ui.textBrowser_4.toPlainText()!='' or self.ui.textBrowser_5.toPlainText()!='' or self.ui.textBrowser_7.toPlainText()!='' or self.ui.textBrowser_6.toPlainText()!='':
                        # message box pour savgarder les resultats precedant ou ecraser
                        buttonReply = QMessageBox.question(self, "Attention!", "vous allez ecraser vos resultat!! voulez vous Sauvegarder avant?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                        if buttonReply == QMessageBox.Yes:
                            print('sauvgarder les resultat ')
                            self.d.exec_()
                        else:
                            print('ecraser')
                            ## efacer tt les resultat precedant
                            self.ui.textEdit.setText('')#resultat de ADN
                            self.ui.textEdit_4.setText('')#adn invers
                            self.ui.textBrowser_3.setText('')#fragments adn assamnblee
                            self.ui.textBrowser_4.setText('')# nuc G
                            self.ui.textBrowser_5.setText('')# nuc C
                            self.ui.textBrowser_7.setText('')# nuc A
                            self.ui.textBrowser_6.setText('')# nuc T
                            self.ui.textBrowser.setText('') # taux GC
                            self.ui.textBrowser_2.setText('') # taux adn codants
                            self.ui.textEdit_3.setText('') # resultat ARN
                            self.ui.textEdit_2.setText('') # arn apres epissage
                            self.ui.textBrowser_8.setText('') # la masse proteique
                            self.ui.textBrowser_9.setText('') # sequence pretieque
                            # the new adn
                            adn=''
                            nbr_nuc=int(self.ui.lineEdit.text())
                            nbr_sec=int(self.ui.lineEdit_2.text())
                            nuc=["A","T","C","G"]
                            for n in range(nbr_sec):
                                for m in range(nbr_nuc):
                                    adn=adn+nuc[random.randint(0,3)]
                                adn=adn+"\n"

                            self.ui.textEdit.setText(adn)

                            ######"enableled les buttons
                            self.ui.pushButton_2.setEnabled(True)
                            self.ui.pushButton_3.setEnabled(True)
                            self.ui.pushButton_4.setEnabled(True)
                            self.ui.pushButton_5.setEnabled(True)
                            self.ui.pushButton_6.setEnabled(True)
                            self.ui.pushButton_8.setEnabled(True)


                    else:
                        adn=''
                        nbr_nuc=int(self.ui.lineEdit.text())
                        nbr_sec=int(self.ui.lineEdit_2.text())
                        nuc=["A","T","C","G"]
                        for n in range(nbr_sec):
                            for m in range(nbr_nuc):
                                adn=adn+nuc[random.randint(0,3)]
                            adn=adn+"\n"

                        self.ui.textEdit.setText(adn)

                        ######"enableled les buttons
                        self.ui.pushButton_2.setEnabled(True)
                        self.ui.pushButton_3.setEnabled(True)
                        self.ui.pushButton_4.setEnabled(True)
                        self.ui.pushButton_5.setEnabled(True)
                        self.ui.pushButton_6.setEnabled(True)
                        self.ui.pushButton_8.setEnabled(True)
                    #♥wech zedt
                else:
                    adn=''
                    nbr_nuc=int(self.ui.lineEdit.text())
                    nbr_sec=int(self.ui.lineEdit_2.text())
                    nuc=["A","T","C","G"]
                    for n in range(nbr_sec):
                        for m in range(nbr_nuc):
                            adn=adn+nuc[random.randint(0,3)]
                        adn=adn+"\n"

                    self.ui.textEdit.setText(adn)

                    ######"enableled les buttons
                    self.ui.pushButton_2.setEnabled(True)
                    self.ui.pushButton_3.setEnabled(True)
                    self.ui.pushButton_4.setEnabled(True)
                    self.ui.pushButton_5.setEnabled(True)
                    self.ui.pushButton_6.setEnabled(True)
                    self.ui.pushButton_8.setEnabled(True)
                    #supprimer les resultat precedant
            else:
                print('edit text manquante ')


        ###################################################################### sequences ADN Generer depuis un fichier FASTA
        if btn.text()=='Chemin Vers Fichier':
            #hide liste  radio buttons
            delet_file("nuc.txt")
            self.ui.listWidget_2.clear()
            self.ui.listWidget_2.hide()
            self.ui.radioButton_4.setChecked(True)
            self.ui.radioButton_3.setChecked(False)
            def readFASTA(filename):
                 with open(filename) as file:
                    return (file.read().split('>')[1:])

            def read_FASTA_entries(filename):
                return[seq.partition('\n')for seq in readFASTA(filename)]

            def final_FASTA(filename):
                return[seq[2].replace('\n','') for seq in read_FASTA_entries(filename)]
            self.ui.listWidget_2.hide()
            self.ui.radioButton_4.setChecked(False)
            self.ui.radioButton_3.setChecked(False)
            if self.ui.textEdit.toPlainText()!='':
                if self.ui.textEdit_4.toPlainText()!='' or self.ui.textBrowser_9.toPlainText()!='' or  self.ui.textBrowser_8.toPlainText()!='' or self.ui.textEdit_2.toPlainText()!='' or self.ui.textEdit_3.toPlainText()!='' or self.ui.textBrowser_2.toPlainText()!='' or self.ui.textBrowser.toPlainText()!='' or self.ui.textEdit_4.toPlainText()!='' or self.ui.textBrowser_3.toPlainText()!='' or self.ui.textBrowser_4.toPlainText()!='' or self.ui.textBrowser_5.toPlainText()!='' or self.ui.textBrowser_7.toPlainText()!='' or self.ui.textBrowser_6.toPlainText()!='':
                    # message box pour savgarder les resultats precedant ou ecraser
                    buttonReply = QMessageBox.question(self, "Attention!", "vous allez ecraser vos resultat voulez vous Sauvegarder avant?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                    if buttonReply == QMessageBox.Yes:
                        print('sauvgarder les resultat ')
                        self.d.exec_()
                    else:
                        print('ecraser')
                        ## efacer tt les resultat precedant
                        self.ui.textEdit.setText('')#resultat de ADN
                        self.ui.textEdit_4.setText('')#adn invers
                        self.ui.textBrowser_3.setText('')#fragments adn assamnblee
                        self.ui.textBrowser_4.setText('')# nuc G
                        self.ui.textBrowser_5.setText('')# nuc C
                        self.ui.textBrowser_7.setText('')# nuc A
                        self.ui.textBrowser_6.setText('')# nuc T
                        self.ui.textBrowser.setText('') # taux GC
                        self.ui.textBrowser_2.setText('') # taux adn codants
                        self.ui.textEdit_3.setText('') # resultat ARN
                        self.ui.textEdit_2.setText('') # arn apres epissage
                        self.ui.textBrowser_8.setText('') # la masse proteique
                        self.ui.textBrowser_9.setText('') # sequence pretieque
                        # new ADN
                        print('chemin vers chemin')
                        self.ui.pushButton_13.setEnabled(True)
                        self.ui.pushButton_2.setEnabled(False)
                        self.ui.pushButton_3.setEnabled(False)
                        self.ui.pushButton_4.setEnabled(False)
                        self.ui.pushButton_5.setEnabled(False)
                        self.ui.pushButton_6.setEnabled(False)
                        self.ui.pushButton_8.setEnabled(False)
                        # three methode to read a FASTA file
                        adn=''
                        try:
                            filename = QFileDialog.getOpenFileName(self, 'Open File', os.getenv('HOME'))
                            FASTA=final_FASTA(filename[0])
                            for value in FASTA:
                                adn=adn+value+"\n"
                            self.ui.textEdit.setText(adn)
                        except Exception as e:
                            print('exaption',str(e))
                else:
                    print('chemin vers chemin')
                    self.ui.pushButton_13.setEnabled(True)
                    self.ui.pushButton_2.setEnabled(False)
                    self.ui.pushButton_3.setEnabled(False)
                    self.ui.pushButton_4.setEnabled(False)
                    self.ui.pushButton_5.setEnabled(False)
                    self.ui.pushButton_6.setEnabled(False)
                    self.ui.pushButton_8.setEnabled(False)
                    # three methode to read a FASTA file
                    adn=''
                    try:
                        filename = QFileDialog.getOpenFileName(self, 'Open File', os.getenv('HOME'))
                        FASTA=final_FASTA(filename[0])
                        for value in FASTA:
                            adn=adn+value+"\n"
                        self.ui.textEdit.setText(adn)
                    except Exception as e:
                        print('exaption',str(e))


            else:
                print('chemin vers chemin')
                self.ui.pushButton_13.setEnabled(True)
                self.ui.pushButton_2.setEnabled(False)
                self.ui.pushButton_3.setEnabled(False)
                self.ui.pushButton_4.setEnabled(False)
                self.ui.pushButton_5.setEnabled(False)
                self.ui.pushButton_6.setEnabled(False)
                self.ui.pushButton_8.setEnabled(False)
                # three methode to read a FASTA file
                adn=''
                try:
                    filename = QFileDialog.getOpenFileName(self, 'Open File', os.getenv('HOME'))
                    FASTA=final_FASTA(filename[0])
                    for value in FASTA:
                        adn=adn+value+"\n"
                    self.ui.textEdit.setText(adn)
                except Exception as e:
                    print('exaption',str(e))
##################################################################################
################## radio buttons pour choisir un sequence ou touts les sequences
    def RADIOSEQUENCE(self,btn):
        if btn.text()=='Toutes les sequences':
            print('Toutes les sequences')
            if self.ui.listWidget_2.count()!=0:
                adn=''
                for value in range(self.ui.listWidget_2.count()):
                    adn=adn+self.ui.listWidget_2.item(value).text()+"\n"
                    pass
                print(adn)
                self.ui.listWidget_2.hide()
                self.ui.textEdit.setText(adn)

                pass

            ################################################################################

            #################################################################################
        if btn.text()=='Une seul sequences':
            print('Une seul sequences')
            print(self.ui.listWidget_2.count())
            if self.ui.listWidget_2.count()==0:
                print('not null')
                t=self.ui.textEdit.toPlainText().split("\n")
                if len(t)==1:
                    self.ui.listWidget_2.addItem(t[0])
                    pass
                else:
                    for value in range(len(t)-1):
                        self.ui.listWidget_2.addItem(t[value])
                        print(t[value])
                    pass
            self.ui.listWidget_2.show()
            self.ui.listWidget_2.itemClicked.connect(self.itemANDclicked)

    def RADION_ADN_ENTRIE(self,btn2):
        if btn2.text()=='Generer Sequence Aleatoire':
            self.ui.ValiderNbrAdn.setEnabled(True)
            self.ui.pushButton_7.setEnabled(False)
        if btn2.text()=='Charger Fichier':
            self.ui.pushButton_7.setEnabled(True)
            self.ui.ValiderNbrAdn.setEnabled(False)
    ######################################################
    def itemANDclicked(self,item):
        print(str(item.text()))
        if self.ui.textEdit.toPlainText()!='':
            if self.ui.textEdit_4.toPlainText()!='' or self.ui.textBrowser_9.toPlainText()!='' or  self.ui.textBrowser_8.toPlainText()!='' or self.ui.textEdit_2.toPlainText()!='' or self.ui.textEdit_3.toPlainText()!='' or self.ui.textBrowser_2.toPlainText()!='' or self.ui.textBrowser.toPlainText()!='' or self.ui.textEdit_4.toPlainText()!='' or self.ui.textBrowser_3.toPlainText()!='' or self.ui.textBrowser_4.toPlainText()!='' or self.ui.textBrowser_5.toPlainText()!='' or self.ui.textBrowser_7.toPlainText()!='' or self.ui.textBrowser_6.toPlainText()!='':
                buttonReply = QMessageBox.question(self, "Attention!", "vous allez ecraser vos resultat voulez vous Sauvegarder avant?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if buttonReply == QMessageBox.Yes:
                    print('sauvgarder les resultat ')
                    self.d.exec_()
                else:
                    print('ecraser')
                    ## efacer tt les resultat precedant
                    self.ui.textEdit.setText('')#resultat de ADN
                    self.ui.textEdit_4.setText('')#adn invers
                    self.ui.textBrowser_3.setText('')#fragments adn assamnblee
                    self.ui.textBrowser_4.setText('')# nuc G
                    self.ui.textBrowser_5.setText('')# nuc C
                    self.ui.textBrowser_7.setText('')# nuc A
                    self.ui.textBrowser_6.setText('')# nuc T
                    self.ui.textBrowser.setText('') # taux GC
                    self.ui.textBrowser_2.setText('') # taux adn codants
                    self.ui.textEdit_3.setText('') # resultat ARN
                    self.ui.textEdit_2.setText('') # arn apres epissage
                    self.ui.textBrowser_8.setText('') # la masse proteique
                    self.ui.textBrowser_9.setText('') # sequence pretieque
                    # new ADN
                    self.ui.textEdit.setText(item.text())

                pass

#################################################################################################################
App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())

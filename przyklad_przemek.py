#zaimportowane biblioteki
from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QApplication, QLabel, QLineEdit,QGridLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import sys
import matplotlib.pyplot as plt
import math
from PyQt5.QtWidgets import QMessageBox,QColorDialog


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.title='Aplikacja wizualizująca położenie punktu przecięcia "P" '  #tytuł aplikacji
        self.setWindowTitle(self.title)
        self.col1 = 'r'  #zmienna do funkcji zmiany koloru pkt
        self.setGeometry(100,100,1000,600)  #szerokoć i długosc okna
        self.show()   #wyswietla okna 
        
        # stworzenie tytulow, okien do wpisywania i przyciskow 
        oblicz=QPushButton('&Oblicz', self)
        czyszczenie=QPushButton("Wyczyść wszystko",self)
        zmianakoloru=QPushButton("Zmiana koloru", self)
        self.x_alabel=QLabel("X punktu A [m]",self) #stworzenie tytulu
        self.x_aEdit=QLineEdit() #dodanie okna do wpisywania
        self.y_alabel=QLabel("Y punktu A [m]",self)
        self.y_aEdit=QLineEdit() 
        self.x_blabel=QLabel("X punktu B [m]",self)
        self.x_bEdit=QLineEdit() 
        self.y_blabel=QLabel("Y punktu B [m]",self)
        self.y_bEdit=QLineEdit() 
        self.x_clabel=QLabel("X punktu C [m]",self)
        self.x_cEdit=QLineEdit() 
        self.y_clabel=QLabel("Y punktu C [m]",self)
        self.y_cEdit=QLineEdit() 
        self.x_dlabel=QLabel("X punktu D [m]",self)
        self.x_dEdit=QLineEdit() 
        self.y_dlabel=QLabel("Y punktu D [m]",self)
        self.y_dEdit=QLineEdit() 
        self.x_plabel=QLabel("X punktu P [m]",self)
        self.x_pEdit = QLineEdit()
        self.y_plabel=QLabel("Y punktu P [m]",self)
        self.y_pEdit = QLineEdit()
        self.danelabel=QLabel("Wpisz dane:",self)
        self.wyniklabel=QLabel("Wynik:",self)
        self.polozenielabel=QLabel("Położenie punktu P:",self)
        self.polozenieEdit = QLineEdit()
        self.dlugosclabel=QLabel("Długości odcinków:",self)
        self.dlugoscABlabel=QLabel("A - B [m]",self)
        self.dlugoscABEdit=QLineEdit() 
        self.dlugoscCDlabel=QLabel("C - D [m]",self)
        self.dlugoscCDEdit=QLineEdit() 
        
        #wyswietlenie wspolrzednych punktu P
        self.x_pEdit.readonly = True #pozwala tylko na odczyt tekstu pola
        self.x_pEdit.setToolTip('Wpisz <b>liczby</b> i wybierz działanie...')        
        self.y_pEdit.readonly = True 
        self.y_pEdit.setToolTip('Wpisz <b>liczby</b> i wybierz działanie...')
        #wyswietlenie polozenia punktu
        self.polozenieEdit.readonly = True 
        self.polozenieEdit.setToolTip('Wpisz <b>liczby</b> i wybierz działanie...')
        #wyswietlenie dlugosci odcinkow
        self.dlugoscABEdit.readonly = True 
        self.dlugoscABEdit.setToolTip('Wpisz <b>liczby</b> i wybierz działanie...')        
        self.dlugoscCDEdit.readonly = True 
        self.dlugoscCDEdit.setToolTip('Wpisz <b>liczby</b> i wybierz działanie...')
        
        #dodanie wykresu do aplikacji
        self.figure=plt.figure()
        self.canvas=FigureCanvas(self.figure)
        
        #ustawienie tytulow, okien do wpisywania, wykresu i przyciskow
        grid=QGridLayout()
        grid.addWidget(self.danelabel, 0, 0)
        grid.addWidget(self.x_alabel, 1, 0)
        grid.addWidget(self.x_aEdit, 1, 1) 
        grid.addWidget(self.y_alabel,2,0)
        grid.addWidget(self.y_aEdit,2,1) 
        grid.addWidget(self.x_blabel, 3, 0)
        grid.addWidget(self.x_bEdit, 3, 1) 
        grid.addWidget(self.y_blabel,4,0)
        grid.addWidget(self.y_bEdit,4,1) 
        grid.addWidget(self.x_clabel, 5, 0)
        grid.addWidget(self.x_cEdit, 5, 1) 
        grid.addWidget(self.y_clabel,6,0)
        grid.addWidget(self.y_cEdit,6,1) 
        grid.addWidget(self.x_dlabel, 7, 0)
        grid.addWidget(self.x_dEdit, 7, 1) 
        grid.addWidget(self.y_dlabel,8,0)
        grid.addWidget(self.y_dEdit,8,1) 
        grid.addWidget(oblicz,9,0,1,2)
        grid.addWidget(zmianakoloru,10,0,1,2)
        grid.addWidget(self.canvas,0,2,-1,-1)
        grid.addWidget(self.wyniklabel, 11, 0)
        grid.addWidget(self.x_plabel,12,0)
        grid.addWidget(self.x_pEdit,12,1)
        grid.addWidget(self.y_plabel,13,0)
        grid.addWidget(self.y_pEdit,13,1)
        grid.addWidget(self.polozenielabel, 14, 0)
        grid.addWidget(self.polozenieEdit,15,0,1,2)
        grid.addWidget(self.dlugosclabel, 16, 0)
        grid.addWidget(self.dlugoscABlabel,17,0)
        grid.addWidget(self.dlugoscABEdit,17,1)
        grid.addWidget(self.dlugoscCDlabel,18,0)
        grid.addWidget(self.dlugoscCDEdit,18,1)
        grid.addWidget(czyszczenie,19,0,1,2)
        self.setLayout(grid)
        
        #połączenie przycisku (signal) z akcją (slot)
        oblicz.clicked.connect(self.funkcja_oblicz)
        czyszczenie.clicked.connect(self.czyszczenie_pol)
        zmianakoloru.clicked.connect(self.zmianakoloru)
        
    #funkcja zmieniajaca kolor
    def zmianakoloru(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.col1 = color.name()
            self.funkcja_oblicz()    
        
    #funkcja realizujaca algorytm
    def funkcja_oblicz(self):
        nadawca=self.sender()
        try:
           x_a=float(self.x_aEdit.text())
           y_a=float(self.y_aEdit.text())
           x_b=float(self.x_bEdit.text())
           y_b=float(self.y_bEdit.text())
           x_c=float(self.x_cEdit.text())
           y_c=float(self.y_cEdit.text())
           x_d=float(self.x_dEdit.text())
           y_d=float(self.y_dEdit.text())
           warunek= " "
           if nadawca.text()=="&Oblicz":
               dxAB=float(x_b-x_a)
               dyAB=float(y_b-y_a)
               dxCD=float(x_d-x_c)
               dyCD=float(y_d-y_c)
               dxAC=float(x_c-x_a)
               dyAC=float(y_c-y_a)
               if (float((dxAB*dyCD)-(dyAB*dxCD)))==0:
                   #dodatkowe okienko pojawiające się w momencie pojawienia się złych danych
                   QMessageBox.warning(self, "Błąd", "Brak rozwiązania - odcinki są równoległe", QMessageBox.Ok)
               else:
                   t1=float((dxAC*dyCD-dyAC*dxCD)/(dxAB*dyCD-dyAB*dxCD))
                   t2=float((dxAC*dyAB-dyAC*dxAB)/(dxAB*dyCD-dyAB*dxCD))
                   x_p=round((x_a+t1*dxAB),3)  #wspolrzedne punktu P z zaokragleniem do 3 miejsc
                   y_p=round((y_a+t1*dyAB),3)
                   
                   self.figure.clear() 
                   let=["A","B","C","D","P"]
                   X=[x_a,x_b,x_c,x_d,x_p]
                   Y=[y_a,y_b,y_c,y_d,y_p]           
                   ax =self.figure.add_subplot(111)
                   ax.set_ylabel('Współrzędna Y')
                   ax.set_xlabel('Współrzędna X')
                   ax.scatter(X,Y,color='red')  #pkt A,B,C,D jako kropka
                   ax.scatter(x_p,y_p,color='blue', marker='o')  #pkt P jako kropka
                   ax.plot([x_a,x_b],[y_a,y_b], color=self.col1) #prosta AB
                   ax.plot([x_c,x_d],[y_c,y_d], color='green') #prosta CD
        
                   if 0<=t1<=1 and 0<=t2<=1:
                      warunek=str("Punkt przecięcia leży wewnątrz obu odcinków")
                   elif 0<=t1<=1 and t2<0 :
                      warunek=str("Punkt  przecięcia leży na odcinku AB i na przedłużeniu odcinka CD")
                      ax.plot([x_c,x_p],[y_c,y_p],linestyle='--',color='black',linewidth=0.3)  # C-P
                   elif 0<=t1<=1 and t2>1:
                      warunek=str("Punkt  przecięcia leży na odcinku AB i na przedłużeniu odcinka CD")
                      ax.plot([x_d,x_p],[y_d,y_p],linestyle='--',color='black',linewidth=0.3)  # D-P
                   elif 0<=t2<=1 and t1<0 :
                      warunek=str("Punkt przecięcia leży na odcinku CD i na przedłużeniu odcinka AB")
                      ax.plot([x_a,x_p],[y_a,y_p],linestyle='--',color='black',linewidth=0.3)  # A-P
                   elif 0<=t2<=1 and t1>1:
                      warunek=str("Punkt przecięcia leży na odcinku CD i na przedłużeniu odcinka AB")
                      ax.plot([x_b,x_p],[y_b,y_p],linestyle='--',color='black',linewidth=0.3)  # B-P
                   else:
                      warunek=str("Punkt przecięcia leży na przedłużeniu odcinków")
                      ax.plot([x_a,x_p],[y_a,y_p],linestyle='--',color='black',linewidth=0.3)  # A-P
                      ax.plot([x_d,x_p],[y_d,y_p],linestyle='--',color='black',linewidth=0.3)  # D-P
               d_AB=round(math.sqrt(dxAB*dxAB+dyAB*dyAB),3) #obliczenie odleglosci z zaokragleniem do 3 miejsc
               d_CD=round(math.sqrt(dxCD*dxCD+dyCD*dyCD),3)
               self.dlugoscABEdit.setText(str(d_AB))  #przekazuje wynik do przypisanych okien
               self.dlugoscCDEdit.setText(str(d_CD))
               self.x_pEdit.setText(str(x_p)) 
               self.y_pEdit.setText(str(y_p)) 
               self.polozenieEdit.setText(str(warunek))
        
               #pokazanie na wykresie nazw punktow i ich wspolrzednych
           for (x,y,l) in zip(X,Y,enumerate(let)):
               ax.annotate("{}({};{})".format(l[1],x,y), xy=(x,y))
           self.canvas.draw() #odswiezenie wykresu
                #dodatkowe okienko pojawiające się w momencie pojawienia się złych danych
        except ValueError:
            QMessageBox.warning(self, "Błąd", "Nieprawidłowe dane - spróbuj jeszcze raz!", QMessageBox.Ok)
               
        #zapis wspolrzednych do pliku txt
        A=str('A')
        B=str('B')
        C=str('C')
        D=str('D')
        P=str('P')
        plik=open('Współrzędne punktów.txt','w+')
        szer = 47
        plik.write("-" * szer)
        plik.write("\n|{:^15}|{:^14}|{:^14}|\n".format('Nazwa punktu','X [m]','Y [m]'))
        plik.write("-" * szer)
        plik.write("\n|{:^15}| {:12.3f} | {:12.3f} | " .format(A,x_a,y_a))
        plik.write("\n|{:^15}| {:12.3f} | {:12.3f} | " .format(B,x_b,y_b))
        plik.write("\n|{:^15}| {:12.3f} | {:12.3f} | " .format(C,x_c,y_c))
        plik.write("\n|{:^15}| {:12.3f} | {:12.3f} | " .format(D,x_d,y_d))
        plik.write("\n|{:^15}| {:12.3f} | {:12.3f} | " .format(P,x_p,y_p))
        plik.close()
    
    #funkcja usuwajaca dana z pol    
    def czyszczenie_pol(self):
        self.x_aEdit.clear()
        self.y_aEdit.clear()
        self.x_bEdit.clear()
        self.y_bEdit.clear()
        self.x_cEdit.clear()
        self.y_cEdit.clear()
        self.x_dEdit.clear()
        self.y_dEdit.clear()
        self.x_pEdit.clear()
        self.y_pEdit.clear()
        self.polozenieEdit.clear()
        self.figure.clear()
        self.canvas.draw()
        self.dlugoscABEdit.clear()
        self.dlugoscCDEdit.clear()
    
if __name__ == '__main__':
    if not QApplication.instance():  #zapobiega restartowaniu konsoli
        app=QApplication(sys.argv)
    else:
        app=QApplication.instance
    window = Window()
    window.show()
    sys.exit(app.exec_())
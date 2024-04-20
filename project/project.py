import sys
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QCheckBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QLinearGradient, QBrush

#app = QApplication([])
#win = QWidget()
#win.resize(500, 500)
#win.setWindowTitle("AITour Agency")



class App(QMainWindow):
    
    def __init__(self):
        super().__init__()
        uic.loadUi('project.ui', self)

        self.LONButton.clicked.connect(self.london)
        self.HawaiButton.clicked.connect(self.havaii)
        self.KyivButton.clicked.connect(self.kyiv)
        self.LAButton.clicked.connect(self.los_A)
        self.CarrButton.clicked.connect(self.caribbean)
        self.NichnePhoto.clicked.connect(self.nichnaphotka)
        global a
        a = ""
    def fon(self):
        self.fon_label.setPixmap(QPixmap('fon.jpg'))

    def london(self):
        global a
        a = "london"
        self.label.setPixmap(QPixmap('london.jpg'))
        self.label_2.setText("Ло́ндон — столиця Англії та Сполученого\n Королівства, розташована на річці\n Темза. Середмістя Лондона є фінансовим і\n комерційним центром Сполученого Королівства\n Великої Британії та Північної Ірландії.")

    def havaii(self):
        global a
        a = "havaii"
        self.label.setPixmap(QPixmap('Hawaii.jpg'))
        self.label_2.setText("Гава́ї — штат США з 21-го серпня 1959 р. на\n Гавайських островах у Тихому океані.\n Острови штату, які в XIX столітті мали назву\n островів Сендвіча, розташовані на відстані\n 3700 км від північноамериканського материка.")
                             
    def kyiv(self):
        global a
        a = "kyiv"
        self.label.setPixmap(QPixmap('download.jpg'))
        self.label_2.setText("Ки́їв — столиця та найбільше місто України.\n Розташований у середній течії Дніпра, у\n північній Наддніпрянщині. Політичний,\n соціально-економічний, транспортний,\n освітньо-науковий, історичний, культурний та\n духовний центр України.")

    def los_A(self):
        global a
        a = "los_A"
        self.label.setPixmap(QPixmap('LA.jpg'))
        self.label_2.setText("Лос-А́нджелес — міська агломерація та порт на\n південному заході Каліфорнії, друге за\n чисельністю населення місто у США. Голлівуд,\n центр кіноіндустрії з 1911 року; обсерваторії в\n Маунт-Вілсон і Маунт-Паломар; Діснейленд;\n музей мистецтв Джона-Пола Гетті.")

    def caribbean(self):
        global a
        a = "caribbean"
        self.label.setPixmap(QPixmap('caribbean.jpg'))
        self.label_2.setText("Кари́би — група островів в Атлантичному\n океані між Північною і Південною Америкою.\n Належить до Північної Америки. Численні\n бухти островів є зручними гаванями.")

    def nichnaphotka(self):

        if a == "london":
            self.label.setPixmap(QPixmap('london_night.jpg'))
            self.label_2.setText("Ло́ндон — столиця Англії та Сполученого\n Королівства, розташована на річці\n Темза. Середмістя Лондона є фінансовим і\n комерційним центром Сполученого Королівства\n Великої Британії та Північної Ірландії.")
    
        elif a == "havaii":
            self.label.setPixmap(QPixmap('Hawaii_night.jpg'))
            self.label_2.setText("Гава́ї — штат США з 21-го серпня 1959 р. на\n Гавайських островах у Тихому океані.\n Острови штату, які в XIX столітті мали назву\n островів Сендвіча, розташовані на відстані\n 3700 км від північноамериканського материка.")

        elif a == "kyiv":
            self.label.setPixmap(QPixmap('kyiv_night.jpg'))
            self.label_2.setText("Ки́їв — столиця та найбільше місто України.\n Розташований у середній течії Дніпра, у\n північній Наддніпрянщині. Політичний,\n соціально-економічний, транспортний,\n освітньо-науковий, історичний, культурний та\n духовний центр України.")

        elif a == "los_A":
            self.label.setPixmap(QPixmap('LA_night.jpg'))
            self.label_2.setText("Лос-А́нджелес — міська агломерація та порт на\n південному заході Каліфорнії, друге за\n чисельністю населення місто у США. Голлівуд,\n центр кіноіндустрії з 1911 року; обсерваторії в\n Маунт-Вілсон і Маунт-Паломар; Діснейленд;\n музей мистецтв Джона-Пола Гетті.")

        elif a == "caribbean":
            self.label.setPixmap(QPixmap('caribbean_night.jpg'))
            self.label_2.setText("Кари́би — група островів в Атлантичному\n океані між Північною і Південною Америкою.\n Належить до Північної Америки. Численні\n бухти островів є зручними гаванями.")





















if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec())

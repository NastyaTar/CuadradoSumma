import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QMainWindow
from random import randint
from PyQt5 import uic


class Winner(QWidget):
    def __init__(self):
        super().__init__()
        self.winn()

    def winn(self):
        self.win = QPushButton('Вы выиграли!!!', self)
        self.win.move(20, 700)
        self.win.resize(100, 20)
        self.win.setStyleSheet("background-color: red")


class Level5(QWidget):
    def __init__(self):
        super().__init__()
        self.buttons()

    def buttons(self):
        self.setGeometry(400, 100, 550, 650)
        self.setWindowTitle('Уровень 5x5')
        self.setStyleSheet("background-color: black")
        self.karta = randint(1, 10)
        self.pole = {1: [16, 19, 7, 16, 18,
                         10, 4, 7, 1, 6, 9, 10,
                         20, 9, 5, 1, 8, 7, 20,
                         15, 5, 6, 8, 2, 2, 15,
                         20, 7, 7, 6, 2, 3, 20,
                         11, 4, 1, 6, 6, 7, 11,
                         16, 19, 7, 16, 18],
                     2: [12, 9, 14, 28, 15,
                         15, 3, 5, 8, 9, 3, 15,
                         25, 6, 8, 2, 9, 2, 25,
                         12, 9, 3, 7, 5, 4, 12,
                         20, 9, 1, 7, 5, 7, 20,
                         6, 3, 3, 6, 5, 3, 6,
                         12, 9, 14, 28, 15],
                     3: [14, 19, 8, 15, 18,
                         10, 1, 6, 3, 2, 7, 10,
                         9, 2, 7, 7, 2, 2, 9,
                         17, 3, 9, 8, 7, 5, 17,
                         17, 7, 2, 1, 6, 2, 17,
                         21, 6, 1, 7, 5, 9, 21,
                         14, 19, 8, 15, 18, ],
                     4: [24, 11, 11, 11, 8,
                         14, 5, 9, 2, 1, 7, 14,
                         7, 4, 7, 1, 6, 1, 7,
                         6, 3, 6, 3, 3, 4, 6,
                         21, 7, 9, 4, 8, 1, 21,
                         17, 9, 2, 4, 2, 3, 17,
                         24, 11, 11, 11, 8, ],
                     5: [28, 3, 15, 17, 13,
                         12, 9, 2, 6, 1, 1, 12,
                         11, 3, 1, 7, 2, 3, 11,
                         14, 3, 4, 4, 2, 9, 14,
                         24, 8, 1, 7, 9, 3, 24,
                         15, 8, 2, 1, 6, 2, 15,
                         28, 3, 15, 17, 13],
                     6: [8, 17, 9, 22, 10,
                         10, 1, 7, 1, 9, 5, 10,
                         11, 2, 5, 5, 4, 2, 11,
                         21, 1, 2, 6, 7, 6, 21,
                         18, 8, 8, 1, 2, 8, 18,
                         6, 7, 2, 2, 2, 2, 6,
                         8, 17, 9, 22, 10],
                     7: [10, 24, 19, 19, 25,
                         23, 9, 9, 2, 3, 8, 23,
                         22, 9, 5, 8, 6, 8, 22,
                         16, 5, 7, 9, 7, 8, 16,
                         17, 2, 9, 8, 7, 8, 17,
                         19, 1, 6, 2, 3, 9, 19,
                         10, 24, 19, 19, 25],
                     8: [16, 6, 14, 25, 10,
                         2, 3, 4, 1, 2, 2, 2,
                         21, 3, 2, 8, 8, 1, 21,
                         9, 4, 3, 2, 8, 3, 9,
                         18, 6, 4, 7, 8, 4, 18,
                         21, 3, 7, 4, 7, 7, 21,
                         16, 6, 14, 25, 10],
                     9: [16, 11, 16, 4, 20,
                         9, 2, 5, 7, 2, 9, 9,
                         19, 3, 4, 2, 3, 9, 19,
                         5, 2, 7, 6, 1, 2, 5,
                         12, 9, 2, 2, 4, 1, 12,
                         22, 9, 5, 9, 3, 8, 22,
                         16, 11, 16, 4, 20],
                     10: [12, 14, 14, 16, 14,
                          17, 5, 5, 9, 5, 7, 17,
                          23, 5, 5, 6, 5, 7, 23,
                          4, 4, 8, 4, 5, 9, 4,
                          13, 5, 1, 3, 5, 6, 13,
                          13, 2, 9, 1, 1, 3, 13,
                          12, 14, 14, 16, 14]}

        self.win = QPushButton('Удачи!!!', self)
        self.win.move(90, 620)
        self.win.resize(370, 20)
        self.win.setStyleSheet("background-color: red")
        self.win.clicked.connect(self.menu)

        self.btn01 = QPushButton(str(self.pole[self.karta][0]), self)
        self.btn01.resize(70, 70)
        self.btn01.move(90, 80)
        self.btn01.setStyleSheet("background-color: gray")
        self.btn01.clicked.connect(self.summa)

        self.btn02 = QPushButton(str(self.pole[self.karta][1]), self)
        self.btn02.resize(70, 70)
        self.btn02.move(165, 80)
        self.btn02.clicked.connect(self.summa)
        self.btn02.setStyleSheet("background-color: gray")

        self.btn03 = QPushButton(str(self.pole[self.karta][2]), self)
        self.btn03.resize(70, 70)
        self.btn03.move(240, 80)
        self.btn03.setStyleSheet("background-color: gray")
        self.btn03.clicked.connect(self.summa)

        self.btn04 = QPushButton(str(self.pole[self.karta][3]), self)
        self.btn04.resize(70, 70)
        self.btn04.move(315, 80)
        self.btn04.setStyleSheet("background-color: gray")
        self.btn04.clicked.connect(self.summa)

        self.btn05 = QPushButton(str(self.pole[self.karta][4]), self)
        self.btn05.resize(70, 70)
        self.btn05.move(390, 80)
        self.btn05.setStyleSheet("background-color: gray")
        self.btn05.clicked.connect(self.summa)

        self.btn10 = QPushButton(str(self.pole[self.karta][5]), self)
        self.btn10.resize(70, 70)
        self.btn10.move(15, 155)
        self.btn10.setStyleSheet("background-color:gray")
        self.btn10.clicked.connect(self.summa)

        self.btn11 = QPushButton(str(self.pole[self.karta][6]), self)
        self.btn11.resize(70, 70)
        self.btn11.move(90, 155)
        self.btn11.setStyleSheet("background-color:#00FFF5")
        self.btn11.clicked.connect(self.change_color)

        self.btn12 = QPushButton(str(self.pole[self.karta][7]), self)
        self.btn12.resize(70, 70)
        self.btn12.move(165, 155)
        self.btn12.setStyleSheet("background-color:#00FFF5")
        self.btn12.clicked.connect(self.change_color)

        self.btn13 = QPushButton(str(self.pole[self.karta][8]), self)
        self.btn13.resize(70, 70)
        self.btn13.move(240, 155)
        self.btn13.setStyleSheet("background-color:#00FFF5")
        self.btn13.clicked.connect(self.change_color)

        self.btn14 = QPushButton(str(self.pole[self.karta][9]), self)
        self.btn14.resize(70, 70)
        self.btn14.move(315, 155)
        self.btn14.setStyleSheet("background-color:#00FFF5")
        self.btn14.clicked.connect(self.change_color)

        self.btn15 = QPushButton(str(self.pole[self.karta][10]), self)
        self.btn15.resize(70, 70)
        self.btn15.move(390, 155)
        self.btn15.setStyleSheet("background-color:#00FFF5")
        self.btn15.clicked.connect(self.change_color)

        self.btn16 = QPushButton(str(self.pole[self.karta][11]), self)
        self.btn16.resize(70, 70)
        self.btn16.move(465, 155)
        self.btn16.setStyleSheet("background-color: gray")
        self.btn16.clicked.connect(self.summa)

        self.btn20 = QPushButton(str(self.pole[self.karta][12]), self)
        self.btn20.resize(70, 70)
        self.btn20.move(15, 230)
        self.btn20.setStyleSheet("background-color: gray")
        self.btn20.clicked.connect(self.summa)

        self.btn21 = QPushButton(str(self.pole[self.karta][13]), self)
        self.btn21.resize(70, 70)
        self.btn21.move(90, 230)
        self.btn21.setStyleSheet("background-color:#00FFF5")
        self.btn21.clicked.connect(self.change_color)

        self.btn22 = QPushButton(str(self.pole[self.karta][14]), self)
        self.btn22.resize(70, 70)
        self.btn22.move(165, 230)
        self.btn22.setStyleSheet("background-color:#00FFF5")
        self.btn22.clicked.connect(self.change_color)

        self.btn23 = QPushButton(str(self.pole[self.karta][15]), self)
        self.btn23.resize(70, 70)
        self.btn23.move(240, 230)
        self.btn23.setStyleSheet("background-color:#00FFF5")
        self.btn23.clicked.connect(self.change_color)

        self.btn24 = QPushButton(str(self.pole[self.karta][16]), self)
        self.btn24.resize(70, 70)
        self.btn24.move(315, 230)
        self.btn24.setStyleSheet("background-color:#00FFF5")
        self.btn24.clicked.connect(self.change_color)

        self.btn25 = QPushButton(str(self.pole[self.karta][17]), self)
        self.btn25.resize(70, 70)
        self.btn25.move(390, 230)
        self.btn25.setStyleSheet("background-color:#00FFF5")
        self.btn25.clicked.connect(self.change_color)

        self.btn26 = QPushButton(str(self.pole[self.karta][18]), self)
        self.btn26.resize(70, 70)
        self.btn26.move(465, 230)
        self.btn26.setStyleSheet("background-color: gray")
        self.btn26.clicked.connect(self.summa)

        self.btn30 = QPushButton(str(self.pole[self.karta][19]), self)
        self.btn30.resize(70, 70)
        self.btn30.move(15, 305)
        self.btn30.setStyleSheet("background-color: gray")
        self.btn30.clicked.connect(self.summa)

        self.btn31 = QPushButton(str(self.pole[self.karta][20]), self)
        self.btn31.resize(70, 70)
        self.btn31.move(90, 305)
        self.btn31.setStyleSheet("background-color:#00FFF5")
        self.btn31.clicked.connect(self.change_color)

        self.btn32 = QPushButton(str(self.pole[self.karta][21]), self)
        self.btn32.resize(70, 70)
        self.btn32.move(165, 305)
        self.btn32.setStyleSheet("background-color:#00FFF5")
        self.btn32.clicked.connect(self.change_color)

        self.btn33 = QPushButton(str(self.pole[self.karta][22]), self)
        self.btn33.resize(70, 70)
        self.btn33.move(240, 305)
        self.btn33.setStyleSheet("background-color:#00FFF5")
        self.btn33.clicked.connect(self.change_color)

        self.btn34 = QPushButton(str(self.pole[self.karta][23]), self)
        self.btn34.resize(70, 70)
        self.btn34.move(315, 305)
        self.btn34.setStyleSheet("background-color:#00FFF5")
        self.btn34.clicked.connect(self.change_color)

        self.btn35 = QPushButton(str(self.pole[self.karta][24]), self)
        self.btn35.resize(70, 70)
        self.btn35.move(390, 305)
        self.btn35.setStyleSheet("background-color:#00FFF5")
        self.btn35.clicked.connect(self.change_color)

        self.btn36 = QPushButton(str(self.pole[self.karta][25]), self)
        self.btn36.resize(70, 70)
        self.btn36.move(465, 305)
        self.btn36.setStyleSheet("background-color: gray")
        self.btn36.clicked.connect(self.summa)

        self.btn40 = QPushButton(str(self.pole[self.karta][26]), self)
        self.btn40.resize(70, 70)
        self.btn40.move(15, 380)
        self.btn40.setStyleSheet("background-color: gray")
        self.btn40.clicked.connect(self.summa)

        self.btn41 = QPushButton(str(self.pole[self.karta][27]), self)
        self.btn41.resize(70, 70)
        self.btn41.move(90, 380)
        self.btn41.setStyleSheet("background-color:#00FFF5")
        self.btn41.clicked.connect(self.change_color)

        self.btn42 = QPushButton(str(self.pole[self.karta][28]), self)
        self.btn42.resize(70, 70)
        self.btn42.move(165, 380)
        self.btn42.setStyleSheet("background-color:#00FFF5")
        self.btn42.clicked.connect(self.change_color)

        self.btn43 = QPushButton(str(self.pole[self.karta][29]), self)
        self.btn43.resize(70, 70)
        self.btn43.move(240, 380)
        self.btn43.setStyleSheet("background-color:#00FFF5")
        self.btn43.clicked.connect(self.change_color)

        self.btn44 = QPushButton(str(self.pole[self.karta][30]), self)
        self.btn44.resize(70, 70)
        self.btn44.move(315, 380)
        self.btn44.setStyleSheet("background-color:#00FFF5")
        self.btn44.clicked.connect(self.change_color)

        self.btn45 = QPushButton(str(self.pole[self.karta][31]), self)
        self.btn45.resize(70, 70)
        self.btn45.move(390, 380)
        self.btn45.setStyleSheet("background-color:#00FFF5")
        self.btn45.clicked.connect(self.change_color)

        self.btn46 = QPushButton(str(self.pole[self.karta][32]), self)
        self.btn46.resize(70, 70)
        self.btn46.move(465, 380)
        self.btn46.setStyleSheet("background-color: gray")
        self.btn46.clicked.connect(self.summa)

        self.btn50 = QPushButton(str(self.pole[self.karta][33]), self)
        self.btn50.resize(70, 70)
        self.btn50.move(15, 455)
        self.btn50.setStyleSheet("background-color: gray")
        self.btn50.clicked.connect(self.summa)

        self.btn51 = QPushButton(str(self.pole[self.karta][34]), self)
        self.btn51.resize(70, 70)
        self.btn51.move(90, 455)
        self.btn51.setStyleSheet("background-color:#00FFF5")
        self.btn51.clicked.connect(self.change_color)

        self.btn52 = QPushButton(str(self.pole[self.karta][35]), self)
        self.btn52.resize(70, 70)
        self.btn52.move(165, 455)
        self.btn52.setStyleSheet("background-color:#00FFF5")
        self.btn52.clicked.connect(self.change_color)

        self.btn53 = QPushButton(str(self.pole[self.karta][36]), self)
        self.btn53.resize(70, 70)
        self.btn53.move(240, 455)
        self.btn53.setStyleSheet("background-color: #00FFF5")
        self.btn53.clicked.connect(self.change_color)

        self.btn54 = QPushButton(str(self.pole[self.karta][37]), self)
        self.btn54.resize(70, 70)
        self.btn54.move(315, 455)
        self.btn54.setStyleSheet("background-color:#00FFF5")
        self.btn54.clicked.connect(self.change_color)

        self.btn55 = QPushButton(str(self.pole[self.karta][38]), self)
        self.btn55.resize(70, 70)
        self.btn55.move(390, 455)
        self.btn55.setStyleSheet("background-color:#00FFF5")
        self.btn55.clicked.connect(self.change_color)

        self.btn56 = QPushButton(str(self.pole[self.karta][39]), self)
        self.btn56.resize(70, 70)
        self.btn56.move(465, 455)
        self.btn56.setStyleSheet("background-color: gray")
        self.btn56.clicked.connect(self.summa)

        self.btn61 = QPushButton(str(self.pole[self.karta][40]), self)
        self.btn61.resize(70, 70)
        self.btn61.move(90, 530)
        self.btn61.setStyleSheet("background-color: gray")
        self.btn61.clicked.connect(self.summa)

        self.btn62 = QPushButton(str(self.pole[self.karta][41]), self)
        self.btn62.resize(70, 70)
        self.btn62.move(165, 530)
        self.btn62.setStyleSheet("background-color: gray")
        self.btn62.clicked.connect(self.summa)

        self.btn63 = QPushButton(str(self.pole[self.karta][42]), self)
        self.btn63.resize(70, 70)
        self.btn63.move(240, 530)
        self.btn63.setStyleSheet("background-color: gray")
        self.btn63.clicked.connect(self.summa)

        self.btn64 = QPushButton(str(self.pole[self.karta][43]), self)
        self.btn64.resize(70, 70)
        self.btn64.move(315, 530)
        self.btn64.setStyleSheet("background-color: gray")
        self.btn64.clicked.connect(self.summa)

        self.btn65 = QPushButton(str(self.pole[self.karta][44]), self)
        self.btn65.resize(70, 70)
        self.btn65.move(390, 530)
        self.btn65.setStyleSheet("background-color: gray")
        self.btn65.clicked.connect(self.summa)

        self.btn000 = QPushButton('Начать заново', self)
        self.btn000.resize(145, 70)
        self.btn000.move(90, 5)
        self.btn000.setStyleSheet("background-color:#BB7BFF")
        self.btn000.clicked.connect(self.repeat)

        self.btn001 = QPushButton('Вернуться в главное\n меню', self)
        self.btn001.resize(145, 70)
        self.btn001.move(315, 5)
        self.btn001.setStyleSheet("background-color:#BB7BFF")
        self.btn001.clicked.connect(self.menu)

        self.color = {self.btn11: 'b', self.btn12: 'b', self.btn13: 'b', self.btn14: 'b', self.btn15: 'b',
                      self.btn21: 'b', self.btn22: 'b', self.btn23: 'b', self.btn24: 'b', self.btn25: 'b',
                      self.btn31: 'b', self.btn32: 'b', self.btn33: 'b', self.btn34: 'b', self.btn35: 'b',
                      self.btn41: 'b', self.btn42: 'b', self.btn43: 'b', self.btn44: 'b', self.btn45: 'b',
                      self.btn51: 'b', self.btn52: 'b', self.btn53: 'b', self.btn54: 'b', self.btn55: 'b'}
        self.suma = {(self.btn01, self.btn61): [[self.btn11, self.btn21, self.btn31,
                                                 self.btn41, self.btn51], 0, self.btn61.text()],
                     (self.btn02, self.btn62): [[self.btn12, self.btn22, self.btn32,
                                                 self.btn42, self.btn52], 0, self.btn62.text()],
                     (self.btn03, self.btn63): [[self.btn13, self.btn23, self.btn33,
                                                 self.btn43, self.btn53], 0, self.btn63.text()],
                     (self.btn04, self.btn64): [[self.btn14, self.btn24, self.btn34,
                                                 self.btn44, self.btn54], 0, self.btn64.text()],
                     (self.btn05, self.btn65): [[self.btn15, self.btn25, self.btn35,
                                                 self.btn45, self.btn55], 0, self.btn65.text()],
                     (self.btn10, self.btn16): [[self.btn11, self.btn12, self.btn13,
                                                 self.btn14, self.btn15], 0, self.btn16.text()],
                     (self.btn20, self.btn26): [[self.btn21, self.btn22, self.btn23,
                                                 self.btn24, self.btn25], 0, self.btn26.text()],
                     (self.btn30, self.btn36): [[self.btn31, self.btn32, self.btn33,
                                                 self.btn34, self.btn35], 0, self.btn36.text()],
                     (self.btn40, self.btn46): [[self.btn41, self.btn42, self.btn43,
                                                 self.btn44, self.btn45], 0, self.btn46.text()],
                     (self.btn50, self.btn56): [[self.btn51, self.btn52, self.btn53,
                                                 self.btn54, self.btn55], 0, self.btn56.text()]}

    def change_color(self):
        if self.color[self.sender()] == 'b':
            self.sender().setStyleSheet('background-color:#BB7BFF')
            self.color[self.sender()] = 'p'
        else:
            self.sender().setStyleSheet('background-color:#00FFF5')
            self.color[self.sender()] = 'b'
        for i in list(self.suma.keys()):
            s = 0
            for j in self.suma[i][0]:
                if self.color[j] == 'p':
                    s += int(j.text())
            self.suma[i][1] = s
            if s == int(self.suma[i][2]):
                i[0].setStyleSheet("background-color: white")
                i[1].setStyleSheet("background-color: white")
            else:
                i[0].setStyleSheet("background-color: grey")
                i[1].setStyleSheet("background-color: grey")
        if all([self.suma[k][1] == int(self.suma[k][2]) for k in list(self.suma.keys())]):
            w = Winner()
            w.show()

    def summa(self):
        for i in list(self.suma.keys()):
            if self.sender() in i and len(self.suma[i]) == 3:
                i[0].setText(str(self.suma[i][1]) + '/' + self.suma[i][2])
                i[1].setText(str(self.suma[i][1]) + '/' + self.suma[i][2])
                self.suma[i].append(0)
            elif self.sender() in i and len(self.suma[i]) == 4:
                self.suma[i].pop(3)
                i[0].setText(self.suma[i][-1])
                i[1].setText(self.suma[i][-1])

    def menu(self):
        self.close()

    def repeat(self):
        for i in list(self.color.keys()):
            self.color[i] = 'b'
            i.setStyleSheet('background-color:#00FFF5')
        for j in list(self.suma.keys()):
            self.suma[j][1] = 0
            j[0].setStyleSheet('background-color:grey')
            j[1].setStyleSheet('background-color:grey')

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtWidgets import QLCDNumber, QLineEdit, QRadioButton
from random import randint


class Level6(QWidget):
    def __init__(self):
        super().__init__()
        self.buttons6()

    def buttons6(self):
        self.setGeometry(400, 100, 620, 720)
        self.setWindowTitle('Уровень 6x6')
        self.setStyleSheet("background-color: black")
        self.karta6 = randint(1, 10)
        self.pole6 = {1: [10, 14, 22, 23, 21, 14,
                          13, 4, 6, 9, 2, 4, 4, 13,
                          15, 9, 1, 4, 8, 1, 1, 15,
                          9, 2, 1, 1, 1, 2, 4, 9,
                          19, 1, 5, 8, 4, 6, 4, 19,
                          26, 6, 7, 4, 1, 7, 5, 26,
                          22, 8, 4, 8, 9, 5, 8, 22,
                          10, 14, 22, 23, 21, 14],
                      2: [13, 29, 27, 24, 18, 23,
                          22, 5, 8, 4, 4, 1, 1, 22,
                          30, 5, 7, 6, 5, 8, 6, 30,
                          9, 4, 9, 9, 2, 5, 7, 9,
                          17, 2, 9, 5, 6, 9, 9, 17,
                          21, 1, 4, 4, 9, 4, 8, 21,
                          35, 3, 8, 4, 9, 6, 8, 35,
                          13, 29, 27, 24, 18, 23, ],
                      3: [12, 22, 15, 19, 26, 22,
                          38, 6, 9, 6, 8, 9, 8, 38,
                          17, 1, 1, 9, 2, 6, 8, 17,
                          19, 1, 8, 3, 3, 4, 8, 19,
                          13, 1, 9, 6, 5, 4, 1, 13,
                          13, 2, 5, 1, 7, 3, 5, 13,
                          16, 3, 1, 7, 9, 4, 1, 16,
                          12, 22, 15, 19, 26, 22],
                      4: [19, 24, 27, 16, 9, 16,
                          19, 5, 9, 2, 5, 4, 4, 19,
                          15, 1, 3, 9, 2, 5, 1, 15,
                          8, 2, 4, 2, 5, 1, 3, 8,
                          27, 7, 5, 2, 6, 7, 8, 27,
                          16, 5, 3, 8, 1, 1, 3, 16,
                          26, 7, 1, 8, 2, 5, 9, 26,
                          19, 24, 27, 16, 9, 16],
                      5: [25, 24, 18, 14, 3, 20,
                          5, 4, 9, 1, 5, 2, 5, 5,
                          24, 8, 1, 5, 8, 2, 5, 24,
                          22, 5, 3, 7, 1, 6, 6, 22,
                          13, 6, 7, 1, 3, 3, 2, 13,
                          16, 4, 5, 1, 4, 4, 7, 16,
                          24, 4, 8, 9, 2, 1, 9, 24,
                          25, 24, 18, 14, 3, 20],
                      6: [24, 8, 26, 18, 19, 28,
                          31, 7, 9, 6, 9, 9, 6, 31,
                          17, 6, 4, 1, 6, 4, 7, 17,
                          15, 9, 9, 1, 2, 2, 3, 15,
                          23, 7, 2, 7, 6, 5, 3, 23,
                          13, 2, 5, 9, 1, 1, 8, 13,
                          24, 5, 2, 9, 7, 4, 9, 24,
                          24, 8, 26, 18, 19, 28],
                      7: [21, 15, 9, 25, 19, 6,
                          8, 4, 2, 1, 6, 7, 3, 8,
                          10, 5, 1, 7, 4, 3, 6, 10,
                          25, 6, 7, 1, 4, 7, 5, 25,
                          20, 1, 7, 2, 7, 3, 2, 20,
                          17, 5, 2, 5, 5, 1, 1, 17,
                          15, 5, 4, 2, 5, 8, 3, 15,
                          21, 15, 9, 25, 19, 6],
                      8: [19, 20, 26, 18, 16, 9,
                          22, 9, 7, 6, 8, 5, 1, 22,
                          20, 1, 9, 9, 3, 1, 1, 20,
                          1, 2, 2, 1, 4, 7, 8, 1,
                          22, 5, 2, 5, 5, 6, 1, 22,
                          26, 9, 4, 8, 7, 1, 6, 26,
                          17, 4, 6, 3, 6, 3, 1, 17,
                          19, 20, 26, 18, 16, 9],
                      9: [38, 21, 25, 23, 15, 18,
                          24, 6, 6, 4, 2, 6, 5, 24,
                          26, 1, 9, 9, 8, 9, 8, 26,
                          33, 9, 3, 6, 7, 8, 33,
                          25, 9, 1, 9, 9, 8, 6, 25,
                          17, 6, 2, 8, 7, 2, 2, 17,
                          15, 8, 5, 9, 2, 2, 2, 15,
                          38, 21, 25, 23, 15, 18],
                      10: [11, 28, 33, 16, 18, 30,
                           18, 7, 5, 9, 3, 2, 8, 18,
                           23, 2, 7, 6, 3, 7, 7, 23,
                           27, 4, 7, 8, 3, 9, 8, 27,
                           25, 4, 6, 7, 2, 7, 9, 25,
                           23, 4, 8, 5, 5, 5, 5, 23,
                           20, 2, 6, 3, 6, 4, 1, 20,
                           11, 28, 33, 16, 18, 30]}

        self.win = QPushButton('Удачи!!!', self)
        self.win.move(90, 690)
        self.win.resize(445, 20)
        self.win.setStyleSheet("background-color: red")
        self.win.clicked.connect(self.menu)

        self.btn016 = QPushButton(str(self.pole6[self.karta6][0]), self)
        self.btn016.resize(70, 70)
        self.btn016.move(90, 80)
        self.btn016.setStyleSheet("background-color: gray")
        self.btn016.clicked.connect(self.summa6)

        self.btn026 = QPushButton(str(self.pole6[self.karta6][1]), self)
        self.btn026.resize(70, 70)
        self.btn026.move(165, 80)
        self.btn026.clicked.connect(self.summa6)
        self.btn026.setStyleSheet("background-color: gray")

        self.btn036 = QPushButton(str(self.pole6[self.karta6][2]), self)
        self.btn036.resize(70, 70)
        self.btn036.move(240, 80)
        self.btn036.setStyleSheet("background-color: gray")
        self.btn036.clicked.connect(self.summa6)

        self.btn046 = QPushButton(str(self.pole6[self.karta6][3]), self)
        self.btn046.resize(70, 70)
        self.btn046.move(315, 80)
        self.btn046.setStyleSheet("background-color: gray")
        self.btn046.clicked.connect(self.summa6)

        self.btn056 = QPushButton(str(self.pole6[self.karta6][4]), self)
        self.btn056.resize(70, 70)
        self.btn056.move(390, 80)
        self.btn056.setStyleSheet("background-color: gray")
        self.btn056.clicked.connect(self.summa6)

        self.btn066 = QPushButton(str(self.pole6[self.karta6][5]), self)
        self.btn066.resize(70, 70)
        self.btn066.move(465, 80)
        self.btn066.setStyleSheet("background-color: gray")
        self.btn066.clicked.connect(self.summa6)

        self.btn106 = QPushButton(str(self.pole6[self.karta6][6]), self)
        self.btn106.resize(70, 70)
        self.btn106.move(15, 155)
        self.btn106.setStyleSheet("background-color:gray")
        self.btn106.clicked.connect(self.summa6)

        self.btn116 = QPushButton(str(self.pole6[self.karta6][7]), self)
        self.btn116.resize(70, 70)
        self.btn116.move(90, 155)
        self.btn116.setStyleSheet("background-color:#00FFF5")
        self.btn116.clicked.connect(self.change_color6)

        self.btn126 = QPushButton(str(self.pole6[self.karta6][8]), self)
        self.btn126.resize(70, 70)
        self.btn126.move(165, 155)
        self.btn126.setStyleSheet("background-color:#00FFF5")
        self.btn126.clicked.connect(self.change_color6)

        self.btn136 = QPushButton(str(self.pole6[self.karta6][9]), self)
        self.btn136.resize(70, 70)
        self.btn136.move(240, 155)
        self.btn136.setStyleSheet("background-color:#00FFF5")
        self.btn136.clicked.connect(self.change_color6)

        self.btn146 = QPushButton(str(self.pole6[self.karta6][10]), self)
        self.btn146.resize(70, 70)
        self.btn146.move(315, 155)
        self.btn146.setStyleSheet("background-color:#00FFF5")
        self.btn146.clicked.connect(self.change_color6)

        self.btn156 = QPushButton(str(self.pole6[self.karta6][11]), self)
        self.btn156.resize(70, 70)
        self.btn156.move(390, 155)
        self.btn156.setStyleSheet("background-color:#00FFF5")
        self.btn156.clicked.connect(self.change_color6)

        self.btn166 = QPushButton(str(self.pole6[self.karta6][12]), self)
        self.btn166.resize(70, 70)
        self.btn166.move(465, 155)
        self.btn166.setStyleSheet("background-color:#00FFF5")
        self.btn166.clicked.connect(self.change_color6)

        self.btn176 = QPushButton(str(self.pole6[self.karta6][13]), self)
        self.btn176.resize(70, 70)
        self.btn176.move(540, 155)
        self.btn176.setStyleSheet("background-color: gray")
        self.btn176.clicked.connect(self.summa6)

        self.btn206 = QPushButton(str(self.pole6[self.karta6][14]), self)
        self.btn206.resize(70, 70)
        self.btn206.move(15, 230)
        self.btn206.setStyleSheet("background-color: gray")
        self.btn206.clicked.connect(self.summa6)

        self.btn216 = QPushButton(str(self.pole6[self.karta6][15]), self)
        self.btn216.resize(70, 70)
        self.btn216.move(90, 230)
        self.btn216.setStyleSheet("background-color:#00FFF5")
        self.btn216.clicked.connect(self.change_color6)

        self.btn226 = QPushButton(str(self.pole6[self.karta6][16]), self)
        self.btn226.resize(70, 70)
        self.btn226.move(165, 230)
        self.btn226.setStyleSheet("background-color:#00FFF5")
        self.btn226.clicked.connect(self.change_color6)

        self.btn236 = QPushButton(str(self.pole6[self.karta6][17]), self)
        self.btn236.resize(70, 70)
        self.btn236.move(240, 230)
        self.btn236.setStyleSheet("background-color:#00FFF5")
        self.btn236.clicked.connect(self.change_color6)

        self.btn246 = QPushButton(str(self.pole6[self.karta6][18]), self)
        self.btn246.resize(70, 70)
        self.btn246.move(315, 230)
        self.btn246.setStyleSheet("background-color:#00FFF5")
        self.btn246.clicked.connect(self.change_color6)

        self.btn256 = QPushButton(str(self.pole6[self.karta6][19]), self)
        self.btn256.resize(70, 70)
        self.btn256.move(390, 230)
        self.btn256.setStyleSheet("background-color:#00FFF5")
        self.btn256.clicked.connect(self.change_color6)

        self.btn266 = QPushButton(str(self.pole6[self.karta6][20]), self)
        self.btn266.resize(70, 70)
        self.btn266.move(465, 230)
        self.btn266.setStyleSheet("background-color:#00FFF5")
        self.btn266.clicked.connect(self.change_color6)

        self.btn276 = QPushButton(str(self.pole6[self.karta6][21]), self)
        self.btn276.resize(70, 70)
        self.btn276.move(540, 230)
        self.btn276.setStyleSheet("background-color: gray")
        self.btn276.clicked.connect(self.summa6)

        self.btn306 = QPushButton(str(self.pole6[self.karta6][22]), self)
        self.btn306.resize(70, 70)
        self.btn306.move(15, 305)
        self.btn306.setStyleSheet("background-color: gray")
        self.btn306.clicked.connect(self.summa6)

        self.btn316 = QPushButton(str(self.pole6[self.karta6][23]), self)
        self.btn316.resize(70, 70)
        self.btn316.move(90, 305)
        self.btn316.setStyleSheet("background-color:#00FFF5")
        self.btn316.clicked.connect(self.change_color6)

        self.btn326 = QPushButton(str(self.pole6[self.karta6][24]), self)
        self.btn326.resize(70, 70)
        self.btn326.move(165, 305)
        self.btn326.setStyleSheet("background-color:#00FFF5")
        self.btn326.clicked.connect(self.change_color6)

        self.btn336 = QPushButton(str(self.pole6[self.karta6][25]), self)
        self.btn336.resize(70, 70)
        self.btn336.move(240, 305)
        self.btn336.setStyleSheet("background-color:#00FFF5")
        self.btn336.clicked.connect(self.change_color6)

        self.btn346 = QPushButton(str(self.pole6[self.karta6][26]), self)
        self.btn346.resize(70, 70)
        self.btn346.move(315, 305)
        self.btn346.setStyleSheet("background-color:#00FFF5")
        self.btn346.clicked.connect(self.change_color6)

        self.btn356 = QPushButton(str(self.pole6[self.karta6][27]), self)
        self.btn356.resize(70, 70)
        self.btn356.move(390, 305)
        self.btn356.setStyleSheet("background-color:#00FFF5")
        self.btn356.clicked.connect(self.change_color6)

        self.btn366 = QPushButton(str(self.pole6[self.karta6][28]), self)
        self.btn366.resize(70, 70)
        self.btn366.move(465, 305)
        self.btn366.setStyleSheet("background-color:#00FFF5")
        self.btn366.clicked.connect(self.change_color6)

        self.btn376 = QPushButton(str(self.pole6[self.karta6][29]), self)
        self.btn376.resize(70, 70)
        self.btn376.move(540, 305)
        self.btn376.setStyleSheet("background-color: gray")
        self.btn376.clicked.connect(self.summa6)

        self.btn406 = QPushButton(str(self.pole6[self.karta6][30]), self)
        self.btn406.resize(70, 70)
        self.btn406.move(15, 380)
        self.btn406.setStyleSheet("background-color: gray")
        self.btn406.clicked.connect(self.summa6)

        self.btn416 = QPushButton(str(self.pole6[self.karta6][31]), self)
        self.btn416.resize(70, 70)
        self.btn416.move(90, 380)
        self.btn416.setStyleSheet("background-color:#00FFF5")
        self.btn416.clicked.connect(self.change_color6)

        self.btn426 = QPushButton(str(self.pole6[self.karta6][32]), self)
        self.btn426.resize(70, 70)
        self.btn426.move(165, 380)
        self.btn426.setStyleSheet("background-color:#00FFF5")
        self.btn426.clicked.connect(self.change_color6)

        self.btn436 = QPushButton(str(self.pole6[self.karta6][33]), self)
        self.btn436.resize(70, 70)
        self.btn436.move(240, 380)
        self.btn436.setStyleSheet("background-color:#00FFF5")
        self.btn436.clicked.connect(self.change_color6)

        self.btn446 = QPushButton(str(self.pole6[self.karta6][34]), self)
        self.btn446.resize(70, 70)
        self.btn446.move(315, 380)
        self.btn446.setStyleSheet("background-color:#00FFF5")
        self.btn446.clicked.connect(self.change_color6)

        self.btn456 = QPushButton(str(self.pole6[self.karta6][35]), self)
        self.btn456.resize(70, 70)
        self.btn456.move(390, 380)
        self.btn456.setStyleSheet("background-color:#00FFF5")
        self.btn456.clicked.connect(self.change_color6)

        self.btn466 = QPushButton(str(self.pole6[self.karta6][36]), self)
        self.btn466.resize(70, 70)
        self.btn466.move(465, 380)
        self.btn466.setStyleSheet("background-color:#00FFF5")
        self.btn466.clicked.connect(self.change_color6)

        self.btn476 = QPushButton(str(self.pole6[self.karta6][37]), self)
        self.btn476.resize(70, 70)
        self.btn476.move(540, 380)
        self.btn476.setStyleSheet("background-color: gray")
        self.btn476.clicked.connect(self.summa6)

        self.btn506 = QPushButton(str(self.pole6[self.karta6][38]), self)
        self.btn506.resize(70, 70)
        self.btn506.move(15, 455)
        self.btn506.setStyleSheet("background-color: gray")
        self.btn506.clicked.connect(self.summa6)

        self.btn516 = QPushButton(str(self.pole6[self.karta6][39]), self)
        self.btn516.resize(70, 70)
        self.btn516.move(90, 455)
        self.btn516.setStyleSheet("background-color:#00FFF5")
        self.btn516.clicked.connect(self.change_color6)

        self.btn526 = QPushButton(str(self.pole6[self.karta6][40]), self)
        self.btn526.resize(70, 70)
        self.btn526.move(165, 455)
        self.btn526.setStyleSheet("background-color:#00FFF5")
        self.btn526.clicked.connect(self.change_color6)

        self.btn536 = QPushButton(str(self.pole6[self.karta6][41]), self)
        self.btn536.resize(70, 70)
        self.btn536.move(240, 455)
        self.btn536.setStyleSheet("background-color: #00FFF5")
        self.btn536.clicked.connect(self.change_color6)

        self.btn546 = QPushButton(str(self.pole6[self.karta6][42]), self)
        self.btn546.resize(70, 70)
        self.btn546.move(315, 455)
        self.btn546.setStyleSheet("background-color:#00FFF5")
        self.btn546.clicked.connect(self.change_color6)

        self.btn556 = QPushButton(str(self.pole6[self.karta6][43]), self)
        self.btn556.resize(70, 70)
        self.btn556.move(390, 455)
        self.btn556.setStyleSheet("background-color:#00FFF5")
        self.btn556.clicked.connect(self.change_color6)

        self.btn566 = QPushButton(str(self.pole6[self.karta6][44]), self)
        self.btn566.resize(70, 70)
        self.btn566.move(465, 455)
        self.btn566.setStyleSheet("background-color:#00FFF5")
        self.btn566.clicked.connect(self.change_color6)

        self.btn576 = QPushButton(str(self.pole6[self.karta6][45]), self)
        self.btn576.resize(70, 70)
        self.btn576.move(540, 455)
        self.btn576.setStyleSheet("background-color: grey")
        self.btn576.clicked.connect(self.summa6)

        self.btn606 = QPushButton(str(self.pole6[self.karta6][46]), self)
        self.btn606.resize(70, 70)
        self.btn606.move(15, 530)
        self.btn606.setStyleSheet("background-color: gray")
        self.btn606.clicked.connect(self.summa6)

        self.btn616 = QPushButton(str(self.pole6[self.karta6][47]), self)
        self.btn616.resize(70, 70)
        self.btn616.move(90, 530)
        self.btn616.setStyleSheet("background-color:#00FFF5")
        self.btn616.clicked.connect(self.change_color6)

        self.btn626 = QPushButton(str(self.pole6[self.karta6][48]), self)
        self.btn626.resize(70, 70)
        self.btn626.move(165, 530)
        self.btn626.setStyleSheet("background-color:#00FFF5")
        self.btn626.clicked.connect(self.change_color6)

        self.btn636 = QPushButton(str(self.pole6[self.karta6][49]), self)
        self.btn636.resize(70, 70)
        self.btn636.move(240, 530)
        self.btn636.setStyleSheet("background-color:#00FFF5")
        self.btn636.clicked.connect(self.change_color6)

        self.btn646 = QPushButton(str(self.pole6[self.karta6][50]), self)
        self.btn646.resize(70, 70)
        self.btn646.move(315, 530)
        self.btn646.setStyleSheet("background-color:#00FFF5")
        self.btn646.clicked.connect(self.change_color6)

        self.btn656 = QPushButton(str(self.pole6[self.karta6][51]), self)
        self.btn656.resize(70, 70)
        self.btn656.move(390, 530)
        self.btn656.setStyleSheet("background-color:#00FFF5")
        self.btn656.clicked.connect(self.change_color6)

        self.btn666 = QPushButton(str(self.pole6[self.karta6][52]), self)
        self.btn666.resize(70, 70)
        self.btn666.move(465, 530)
        self.btn666.setStyleSheet("background-color:#00FFF5")
        self.btn666.clicked.connect(self.change_color6)

        self.btn676 = QPushButton(str(self.pole6[self.karta6][53]), self)
        self.btn676.resize(70, 70)
        self.btn676.move(540, 530)
        self.btn676.setStyleSheet("background-color: gray")
        self.btn676.clicked.connect(self.summa6)

        self.btn71 = QPushButton(str(self.pole6[self.karta6][54]), self)
        self.btn71.resize(70, 70)
        self.btn71.move(90, 605)
        self.btn71.setStyleSheet("background-color: gray")
        self.btn71.clicked.connect(self.summa6)

        self.btn72 = QPushButton(str(self.pole6[self.karta6][55]), self)
        self.btn72.resize(70, 70)
        self.btn72.move(165, 605)
        self.btn72.setStyleSheet("background-color: gray")
        self.btn72.clicked.connect(self.summa6)

        self.btn73 = QPushButton(str(self.pole6[self.karta6][56]), self)
        self.btn73.resize(70, 70)
        self.btn73.move(240, 605)
        self.btn73.setStyleSheet("background-color: gray")
        self.btn73.clicked.connect(self.summa6)

        self.btn74 = QPushButton(str(self.pole6[self.karta6][57]), self)
        self.btn74.resize(70, 70)
        self.btn74.move(315, 605)
        self.btn74.setStyleSheet("background-color: gray")
        self.btn74.clicked.connect(self.summa6)

        self.btn75 = QPushButton(str(self.pole6[self.karta6][58]), self)
        self.btn75.resize(70, 70)
        self.btn75.move(390, 605)
        self.btn75.setStyleSheet("background-color: gray")
        self.btn75.clicked.connect(self.summa6)

        self.btn76 = QPushButton(str(self.pole6[self.karta6][59]), self)
        self.btn76.resize(70, 70)
        self.btn76.move(465, 605)
        self.btn76.setStyleSheet("background-color: gray")
        self.btn76.clicked.connect(self.summa6)

        self.btn0006 = QPushButton('Начать заново', self)
        self.btn0006.resize(145, 70)
        self.btn0006.move(90, 5)
        self.btn0006.setStyleSheet("background-color:#BB7BFF")
        self.btn0006.clicked.connect(self.repeat6)

        self.btn0016 = QPushButton('Вернуться в главное\n меню', self)
        self.btn0016.resize(145, 70)
        self.btn0016.move(390, 5)
        self.btn0016.setStyleSheet("background-color:#BB7BFF")
        self.btn0016.clicked.connect(self.menu)

        self.color6 = {self.btn116: 'b', self.btn126: 'b', self.btn136: 'b', self.btn146: 'b', self.btn156: 'b',
                       self.btn166: 'b',
                       self.btn216: 'b', self.btn226: 'b', self.btn236: 'b', self.btn246: 'b', self.btn256: 'b',
                       self.btn266: 'b',
                       self.btn316: 'b', self.btn326: 'b', self.btn336: 'b', self.btn346: 'b', self.btn356: 'b',
                       self.btn366: 'b',
                       self.btn416: 'b', self.btn426: 'b', self.btn436: 'b', self.btn446: 'b', self.btn456: 'b',
                       self.btn466: 'b',
                       self.btn516: 'b', self.btn526: 'b', self.btn536: 'b', self.btn546: 'b', self.btn556: 'b',
                       self.btn566: 'b',
                       self.btn616: 'b', self.btn626: 'b', self.btn636: 'b', self.btn646: 'b', self.btn656: 'b',
                       self.btn666: 'b'}
        self.suma6 = {(self.btn016, self.btn71): [[self.btn116, self.btn216, self.btn316,
                                                   self.btn416, self.btn516, self.btn616], 0, self.btn71.text()],
                      (self.btn026, self.btn72): [[self.btn126, self.btn226, self.btn326,
                                                   self.btn426, self.btn526, self.btn626], 0, self.btn72.text()],
                      (self.btn036, self.btn73): [[self.btn136, self.btn236, self.btn336,
                                                   self.btn436, self.btn536, self.btn636], 0, self.btn73.text()],
                      (self.btn046, self.btn74): [[self.btn146, self.btn246, self.btn346,
                                                   self.btn446, self.btn546, self.btn646], 0, self.btn74.text()],
                      (self.btn056, self.btn75): [[self.btn156, self.btn256, self.btn356,
                                                   self.btn456, self.btn556, self.btn656], 0, self.btn75.text()],
                      (self.btn066, self.btn76): [[self.btn166, self.btn266, self.btn366,
                                                   self.btn466, self.btn566, self.btn666], 0, self.btn76.text()],
                      (self.btn106, self.btn176): [[self.btn116, self.btn126, self.btn136,
                                                    self.btn146, self.btn156, self.btn166], 0, self.btn176.text()],
                      (self.btn206, self.btn276): [[self.btn216, self.btn226, self.btn236,
                                                    self.btn246, self.btn256, self.btn266], 0, self.btn276.text()],
                      (self.btn306, self.btn376): [[self.btn316, self.btn326, self.btn336,
                                                    self.btn346, self.btn356, self.btn366], 0, self.btn376.text()],
                      (self.btn406, self.btn476): [[self.btn416, self.btn426, self.btn436,
                                                    self.btn446, self.btn456, self.btn466], 0, self.btn476.text()],
                      (self.btn506, self.btn576): [[self.btn516, self.btn526, self.btn536,
                                                    self.btn546, self.btn556, self.btn566], 0, self.btn576.text()],
                      (self.btn606, self.btn676): [[self.btn616, self.btn626, self.btn636,
                                                    self.btn646, self.btn656, self.btn666], 0, self.btn676.text()]}

    def change_color6(self):
        if self.color6[self.sender()] == 'b':
            self.sender().setStyleSheet('background-color:#BB7BFF')
            self.color6[self.sender()] = 'p'
        else:
            self.sender().setStyleSheet('background-color:#00FFF5')
            self.color6[self.sender()] = 'b'
        for i in list(self.suma6.keys()):
            s = 0
            for j in self.suma6[i][0]:
                if self.color6[j] == 'p':
                    s += int(j.text())
            self.suma6[i][1] = s
            if s == int(self.suma6[i][2]):
                i[0].setStyleSheet("background-color: white")
                i[1].setStyleSheet("background-color: white")
            else:
                i[0].setStyleSheet("background-color: grey")
                i[1].setStyleSheet("background-color: grey")
        if all([self.suma6[k][1] == int(self.suma6[k][2]) for k in list(self.suma6.keys())]):
            self.win.setText('Вы выиграли!!!')
            dc = [j.disconnect() for j in self.color6]
            dco = [i.disconnect() for j in self.suma6.keys() for i in j]

    def summa6(self):
        for i in list(self.suma6.keys()):
            if self.sender() in i and len(self.suma6[i]) == 3:
                i[0].setText(str(self.suma6[i][1]) + '/' + self.suma6[i][2])
                i[1].setText(str(self.suma6[i][1]) + '/' + self.suma6[i][2])
                self.suma6[i].append(0)
            elif self.sender() in i and len(self.suma6[i]) == 4:
                self.suma6[i].pop(3)
                i[0].setText(self.suma6[i][-1])
                i[1].setText(self.suma6[i][-1])

    def repeat6(self):
        for i in list(self.color6.keys()):
            self.color6[i] = 'b'
            i.setStyleSheet('background-color:#00FFF5')
        for j in list(self.suma6.keys()):
            self.suma6[j][1] = 0

    def menu(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    s = Level6()
    s.show()
    sys.exit(app.exec())

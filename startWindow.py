import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from Five import Level5
from start import Ui_Contin
from Six import Level6
from Instruction import Ui_Instruction


class Starting(QMainWindow, Ui_Contin, Ui_Instruction):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.x5.clicked.connect(self.open5)
        self.x6.clicked.connect(self.open6)
        self.cont.clicked.connect(self.conti)
        self.what.clicked.connect(self.instruction)
        self.L5 = Level5()
        self.L6 = Level6()
        self.In = Ui_Instruction()

    def open5(self):
        self.L5.show()

    def open6(self):
        self.L6.show()

    def instruction(self):
        self.In.show()

    def conti(self):
        pass


app = QApplication(sys.argv)
st = Starting()
st.show()
sys.exit(app.exec_())

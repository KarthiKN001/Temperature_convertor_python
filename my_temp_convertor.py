from PyQt5.QtWidgets import *
from temp_convertor import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("TEMPERATURE CONVERTOR")
        self.temp_nums = []

        self.ktoc_btn.clicked.connect(self.k_to_c)
        self.ktof_btn.clicked.connect(self.k_to_f)
        self.ctof_btn.clicked.connect(self.c_to_f)
        self.ctok_btn.clicked.connect(self.c_to_k)
        self.ftoc_btn.clicked.connect(self.f_to_c)
        self.ftok_btn.clicked.connect(self.f_to_k)
        self.clear_btn.pressed.connect(self.clear_fields)
        self.nine_btn.pressed.connect(lambda: self.num_press('9'))
        self.eight_btn.pressed.connect(lambda: self.num_press('8'))
        self.seven_btn.pressed.connect(lambda: self.num_press('7'))
        self.six_btn.pressed.connect(lambda: self.num_press('6'))
        self.five_btn.pressed.connect(lambda: self.num_press('5'))
        self.four_btn.pressed.connect(lambda: self.num_press('4'))
        self.three_btn.pressed.connect(lambda: self.num_press('3'))
        self.two_btn.pressed.connect(lambda: self.num_press('2'))
        self.one_btn.pressed.connect(lambda: self.num_press('1'))
        self.zero_btn.pressed.connect(lambda: self.num_press('0'))
        self.dot_btn.pressed.connect(lambda: self.num_press('.'))
        self.minus_btn.pressed.connect(lambda: self.num_press('-'))

    def num_press(self, key_number):
        self.temp_nums.append(key_number)
        temp_string = ''.join(self.temp_nums)
        self.input_field.setText(temp_string)

    def k_to_c(self):
        given = ''.join(self.temp_nums)
        result1 = float(given) - 273.15
        result2 = str(result1)
        self.result_field.insert(result2)

    def k_to_f(self):
        given = ''.join(self.temp_nums)
        result = (float(given) - 273.15) * 1.8 + 32
        result = str(result)
        self.result_field.setText(result)

    def c_to_f(self):
        given = ''.join(self.temp_nums)
        result = (float(given) * 1.8) + 32
        result = str(result)
        self.result_field.setText(result)

    def c_to_k(self):
        given = ''.join(self.temp_nums)
        result = (float(given) + 273.15)
        result = str(result)
        self.result_field.setText(result)

    def f_to_c(self):
        given = ''.join(self.temp_nums)
        result = (float(given) - 32) * 0.555555555
        result = str(result)
        self.result_field.setText(result)

    def f_to_k(self):
        given = ''.join(self.temp_nums)
        result = (float(given) - 32) * 0.555555555 + 273.15
        result = str(result)
        self.result_field.setText(result)

    def clear_fields(self):
        self.result_field.clear()
        self.input_field.clear()
        self.temp_nums = []


app = QApplication([])
window = MainWindow()
window.show()
app.setStyle(QStyleFactory.create("Fusion"))
app.exec()

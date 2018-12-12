import sys                                             #
import math                                            #
from PyQt5.QtWidgets import QApplication, QMainWindow  # импрот необходимых для работы модулей
from uk import Ui_Universal_calculator                 # (некоторые из них я придумал сам)
import Number                                          #


class MyWidget(QMainWindow, Ui_Universal_calculator):
    def __init__(self):  # инициализация кнопок
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run_1)
        self.pushButton_2.clicked.connect(self.run_2)
        self.pushButton_3.clicked.connect(self.run_3)
        self.pushButton_4.clicked.connect(self.run_4)
        self.pushButton_5.clicked.connect(self.run_5)
        self.pushButton_6.clicked.connect(self.run_6)
        self.pushButton_7.clicked.connect(self.run_7)
        self.pushButton_8.clicked.connect(self.run_8)
        self.pushButton_9.clicked.connect(self.run_9)
        self.pushButton_18.clicked.connect(self.run_10)
        self.pushButton_10.clicked.connect(self.run_11)
        self.pushButton_12.clicked.connect(self.run_12)
        self.pushButton_14.clicked.connect(self.run_13)
        self.pushButton_13.clicked.connect(self.run_14)
        self.pushButton_16.clicked.connect(self.run_15)
        self.pushButton_11.clicked.connect(self.run_16)
        self.pushButton_15.clicked.connect(self.run_17)
        self.pushButton_17.clicked.connect(self.run_18)
        self.pushButton_19.clicked.connect(self.run_19)
        self.pushButton_20.clicked.connect(self.run_20)
        self.pushButton_21.clicked.connect(self.run_21)
        self.pushButton_22.clicked.connect(self.run_22)
        self.pushButton_23.clicked.connect(self.run_23)
        self.pushButton_24.clicked.connect(self.run_24)
        self.pushButton_25.clicked.connect(self.run_25)
        self.pushButton_26.clicked.connect(self.run_26)
        self.pushButton_27.clicked.connect(self.run_27)
        self.pushButton_28.clicked.connect(self.run_28)
        self.pushButton_29.clicked.connect(self.run_29)
        self.pushButton_30.clicked.connect(self.run_30)
        self.pushButton_31.clicked.connect(self.run_31)
        self.pushButton_32.clicked.connect(self.run_32)
        self.pushButton_33.clicked.connect(self.run_33)
        self.pushButton_34.clicked.connect(self.run_34)
        self.pushButton_35.clicked.connect(self.run_35)
        self.pushButton_36.clicked.connect(self.run_36)
        self.pushButton_37.clicked.connect(self.run_37)
        self.pushButton_38.clicked.connect(self.run_38)
        self.pushButton_39.clicked.connect(self.run_39)
        self.pushButton_40.clicked.connect(self.run_40)
        self.pushButton_41.clicked.connect(self.run_41)
        self.pushButton_42.clicked.connect(self.run_42)
        self.pushButton_43.clicked.connect(self.run_43)
        self.pushButton_44.clicked.connect(self.run_44)
        self.pushButton_45.clicked.connect(self.run_45)

    def run_1(self):  # сумма x и у
        try:
            if '.' in self.lineEdit.text():
                x = float(self.lineEdit.text())
            else:
                x = int(self.lineEdit.text())
            if '.' in self.lineEdit_2.text():
                y = float(self.lineEdit_2.text())
            else:
                y = int(self.lineEdit_2.text())
            self.lcdNumber.display(x + y)
        except Exception:
            self.lcdNumber.display('Error')

    def run_2(self):  # разность x и у
        try:
            if '.' in self.lineEdit.text():
                x = float(self.lineEdit.text())
            else:
                x = int(self.lineEdit.text())
            if '.' in self.lineEdit_2.text():
                y = float(self.lineEdit_2.text())
            else:
                y = int(self.lineEdit_2.text())
            self.lcdNumber.display(x - y)
        except Exception:
            self.lcdNumber.display('Error')

    def run_3(self):  # произведение x и у
        try:
            if '.' in self.lineEdit.text():
                x = float(self.lineEdit.text())
            else:
                x = int(self.lineEdit.text())
            if '.' in self.lineEdit_2.text():
                y = float(self.lineEdit_2.text())
            else:
                y = int(self.lineEdit_2.text())
            self.lcdNumber.display(x * y)
        except Exception:
            self.lcdNumber.display('Error')

    def run_4(self):  # деление x и у
        try:
            if '.' in self.lineEdit.text():
                x = float(self.lineEdit.text())
            else:
                x = int(self.lineEdit.text())
            if '.' in self.lineEdit_2.text():
                y = float(self.lineEdit_2.text())
            else:
                y = int(self.lineEdit_2.text())
            self.lcdNumber.display(x / y)
        except Exception:
            self.lcdNumber.display('Error')

    def run_5(self):  # возведение x в степень у
        try:
            if '.' in self.lineEdit.text():
                x = float(self.lineEdit.text())
            else:
                x = int(self.lineEdit.text())
            if '.' in self.lineEdit_2.text():
                y = float(self.lineEdit_2.text())
            else:
                y = int(self.lineEdit_2.text())
            self.lcdNumber.display(x ** y)
        except Exception:
            self.lcdNumber.display('Error')

    def run_6(self):  # квадратный корень х
        try:
            if ',' in self.lineEdit.text():
                self.lineEdit.text().replace(',', '.')
            if '.' in self.lineEdit.text():
                x = float(self.lineEdit.text())
            else:
                x = int(self.lineEdit.text())
            self.lcdNumber.display(math.sqrt(x))
        except Exception:
            self.lcdNumber.display('Error')

    def run_7(self):  # квадратный корень у
        try:
            if '.' in self.lineEdit_2.text():
                y = float(self.lineEdit_2.text())
            else:
                y = int(self.lineEdit_2.text())
            self.lcdNumber.display(math.sqrt(y))
        except Exception:
            self.lcdNumber.display('Error')

    def run_8(self):  # факториал x
        try:
            if '.' in self.lineEdit.text():
                x = float(self.lineEdit.text())
            else:
                x = int(self.lineEdit.text())
            self.lcdNumber.display(math.factorial(x))
        except Exception:
            self.lcdNumber.display('Error')

    def run_9(self):  # факториал у
        try:
            if '.' in self.lineEdit_2.text():
                y = float(self.lineEdit_2.text())
            else:
                y = int(self.lineEdit_2.text())
            self.lcdNumber.display(math.factorial(y))
        except Exception:
            self.lcdNumber.display('Error')

    def run_10(self):  # -х
        try:
            self.lcdNumber.display('-' + self.lineEdit.text())
        except Exception:
            self.lcdNumber.display('Error')

    def run_11(self):  # -у
        try:
            self.lcdNumber.display('-' + self.lineEdit_2.text())
        except Exception:
            self.lcdNumber.display('Error')

    def run_12(self):  # перевод х из процентного значения
        try:
            if '.' in self.lineEdit.text():
                x = float(self.lineEdit.text())
            else:
                x = int(self.lineEdit.text())
            self.lcdNumber.display(x / 100)
        except Exception:
            self.lcdNumber.display('Error')

    def run_13(self):  # перевод у из процентного значения
        try:
            if '.' in self.lineEdit_2.text():
                y = float(self.lineEdit_2.text())
            else:
                y = int(self.lineEdit_2.text())
            self.lcdNumber.display(y / 100)
        except Exception:
            self.lcdNumber.display('Error')

    def run_14(self):  # возведение х в квадрат
        try:
            if '.' in self.lineEdit.text():
                x = float(self.lineEdit.text())
            else:
                x = int(self.lineEdit.text())
            self.lcdNumber.display(x ** 2)
        except Exception:
            self.lcdNumber.display('Error')

    def run_15(self):  # возведение у в квадрат
        try:
            if '.' in self.lineEdit_2.text():
                y = float(self.lineEdit_2.text())
            else:
                y = int(self.lineEdit_2.text())
            self.lcdNumber.display(y ** 2)
        except Exception:
            self.lcdNumber.display('Error')

    def run_16(self):  # возведение х в куб
        try:
            if '.' in self.lineEdit.text():
                x = float(self.lineEdit.text())
            else:
                x = int(self.lineEdit.text())
            self.lcdNumber.display(x ** 3)
        except Exception:
            self.lcdNumber.display('Error')

    def run_17(self):  # возведение у в куб
        try:
            if '.' in self.lineEdit_2.text():
                y = float(self.lineEdit_2.text())
            else:
                y = int(self.lineEdit_2.text())
            self.lcdNumber.display(y ** 3)
        except Exception:
            self.lcdNumber.display('Error')

    def run_18(self):  # вывод числа пи
        self.lcdNumber.display(math.pi)

    def run_19(self):  # деление 1 на х
        try:
            if '.' in self.lineEdit.text():
                x = float(self.lineEdit.text())
            else:
                x = int(self.lineEdit.text())
            self.lcdNumber.display(1 / x)
        except Exception:
            self.lcdNumber.display('Error')

    def run_20(self):  # деление 1 на у
        try:
            if '.' in self.lineEdit_2.text():
                y = float(self.lineEdit_2.text())
            else:
                y = int(self.lineEdit_2.text())
            self.lcdNumber.display(1 / y)
        except Exception:
            self.lcdNumber.display('Error')

    def run_21(self):  # возведение 10 в степень х
        try:
            if '.' in self.lineEdit.text():
                x = float(self.lineEdit.text())
            else:
                x = int(self.lineEdit.text())
            self.lcdNumber.display(10 ** x)
        except Exception:
            self.lcdNumber.display('Error')

    def run_22(self):   # возведение 10 в степень у
        try:
            if '.' in self.lineEdit_2.text():
                y = float(self.lineEdit_2.text())
            else:
                y = int(self.lineEdit_2.text())
            self.lcdNumber.display(10 ** y)
        except Exception:
            self.lcdNumber.display('Error')

    def run_23(self):  # модуль х
        try:
            if '.' in self.lineEdit.text():
                x = float(self.lineEdit.text())
            else:
                x = int(self.lineEdit.text())
            self.lcdNumber.display(math.fabs(x))
        except Exception:
            self.lcdNumber.display('Error')

    def run_24(self):  # модуль у
        try:
            if '.' in self.lineEdit_2.text():
                y = float(self.lineEdit_2.text())
            else:
                y = int(self.lineEdit_2.text())
            self.lcdNumber.display(math.fabs(y))
        except Exception:
            self.lcdNumber.display('Error')

    def run_25(self):  # округление х до ближайшего большего числа
        try:
            if '.' in self.lineEdit.text():
                x = float(self.lineEdit.text())
            else:
                x = int(self.lineEdit.text())
            self.lcdNumber.display(math.ceil(x))
        except Exception:
            self.lcdNumber.display('Error')

    def run_26(self):  # округление у до ближайшего большего числа
        try:
            if '.' in self.lineEdit_2.text():
                y = float(self.lineEdit_2.text())
            else:
                y = int(self.lineEdit_2.text())
            self.lcdNumber.display(math.ceil(y))
        except Exception:
            self.lcdNumber.display('Error')

    def run_27(self):  # основание натурального логарифма
        self.lcdNumber.display(math.e)

    def run_28(self):  # возвращает число, имеющее модуль такой же, как и у числа х, а знак - как у числа у.
        try:
            if '.' in self.lineEdit.text():
                x = float(self.lineEdit.text())
            else:
                x = int(self.lineEdit.text())
            if '.' in self.lineEdit_2.text():
                y = float(self.lineEdit_2.text())
            else:
                y = int(self.lineEdit_2.text())
            self.lcdNumber.display(math.copysign(x, y))
        except Exception:
            self.lcdNumber.display('Error')

    def run_29(self):  # округление х вниз
        try:
            if '.' in self.lineEdit_2.text():
                x = float(self.lineEdit.text())
            else:
                x = int(self.lineEdit.text())
            self.lcdNumber.display(math.floor(x))
        except Exception:
            self.lcdNumber.display('Error')

    def run_30(self):  # округление у вниз
        try:
            if '.' in self.lineEdit_2.text():
                y = float(self.lineEdit_2.text())
            else:
                y = int(self.lineEdit_2.text())
            self.lcdNumber.display(math.floor(y))
        except Exception:
            self.lcdNumber.display('Error')

    def run_31(self):  # целочисленное деление х на у
        try:
            if '.' in self.lineEdit_2.text():
                x = float(self.lineEdit.text())
            else:
                x = int(self.lineEdit.text())
            if '.' in self.lineEdit_2.text():
                y = float(self.lineEdit_2.text())
            else:
                y = int(self.lineEdit_2.text())
            self.lcdNumber.display(x // y)
        except Exception:
            self.lcdNumber.display('Error')

    def run_32(self):  # остаток от деления х на у
        try:
            if ',' in self.lineEdit.text():
                self.lineEdit.text().replace(',', '.')
            if '.' in self.lineEdit_2.text():
                x = float(self.lineEdit.text())
            else:
                x = int(self.lineEdit.text())
            if '.' in self.lineEdit_2.text():
                y = float(self.lineEdit_2.text())
            else:
                y = int(self.lineEdit_2.text())
            self.lcdNumber.display(math.fmod(x, y))
        except Exception:
            self.lcdNumber.display('Error')

    def run_33(self):  # целочисленное деление у на х (функция для лентяев)
        try:
            if ',' in self.lineEdit.text():
                self.lineEdit.text().replace(',', '.')
            if '.' in self.lineEdit_2.text():
                x = float(self.lineEdit.text())
            else:
                x = int(self.lineEdit.text())
            if '.' in self.lineEdit_2.text():
                y = float(self.lineEdit_2.text())
            else:
                y = int(self.lineEdit_2.text())
            self.lcdNumber.display(y // x)
        except Exception:
            self.lcdNumber.display('Error')

    def run_34(self):  # остаток от деления у на х (функция для лентяев)
        try:
            if ',' in self.lineEdit.text():
                self.lineEdit.text().replace(',', '.')
            if '.' in self.lineEdit_2.text():
                x = float(self.lineEdit.text())
            else:
                x = int(self.lineEdit.text())
            if '.' in self.lineEdit_2.text():
                y = float(self.lineEdit_2.text())
            else:
                y = int(self.lineEdit_2.text())
            self.lcdNumber.display(math.fmod(y, x))
        except Exception:
            self.lcdNumber.display('Error')

    def run_35(self):  # разность у и х (функция для лентяев)
        try:
            if ',' in self.lineEdit.text():
                self.lineEdit.text().replace(',', '.')
            if '.' in self.lineEdit.text():
                x = float(self.lineEdit.text())
            else:
                x = int(self.lineEdit.text())
            if '.' in self.lineEdit_2.text():
                y = float(self.lineEdit_2.text())
            else:
                y = int(self.lineEdit_2.text())
            self.lcdNumber.display(y - x)
        except Exception:
            self.lcdNumber.display('Error')

    def run_36(self):  # возвращает число, имеющее модуль такой же, как и у числа у, а знак - как у числа х.
        # (функция для лентяев)
        try:
            if ',' in self.lineEdit.text():
                self.lineEdit.text().replace(',', '.')
            if '.' in self.lineEdit.text():
                x = float(self.lineEdit.text())
            else:
                x = int(self.lineEdit.text())
            if '.' in self.lineEdit_2.text():
                y = float(self.lineEdit_2.text())
            else:
                y = int(self.lineEdit_2.text())
            self.lcdNumber.display(math.copysign(y, x))
        except Exception:
            self.lcdNumber.display('Error')

    def run_37(self):  # усекает значение х до целого.
        try:
            if ',' in self.lineEdit.text():
                self.lineEdit.text().replace(',', '.')
            if '.' in self.lineEdit.text():
                x = float(self.lineEdit.text())
            else:
                x = int(self.lineEdit.text())
            self.lcdNumber.display(math.trunc(x))
        except Exception:
            self.lcdNumber.display('Error')

    def run_38(self):  # усекает значение у до целого.
        try:
            if '.' in self.lineEdit.text():
                y = float(self.lineEdit_2.text())
            else:
                y = int(self.lineEdit_2.text())
            self.lcdNumber.display(math.trunc(y))
        except Exception:
            self.lcdNumber.display('Error')

    def run_39(self):  # е в степени х
        try:
            if ',' in self.lineEdit.text():
                self.lineEdit.text().replace(',', '.')
            if '.' in self.lineEdit.text():
                x = float(self.lineEdit.text())
            else:
                x = int(self.lineEdit.text())
            self.lcdNumber.display(math.exp(x))
        except Exception:
            self.lcdNumber.display('Error')

    def run_40(self):  # е в степени у
        try:
            if '.' in self.lineEdit.text():
                y = float(self.lineEdit_2.text())
            else:
                y = int(self.lineEdit_2.text())
            self.lcdNumber.display(math.exp(y))
        except Exception:
            self.lcdNumber.display('Error')

    def run_41(self):  # (e в степени х) - 1. При X → 0 точнее, чем math.exp(х)-1.
        try:
            if ',' in self.lineEdit.text():
                self.lineEdit.text().replace(',', '.')
            if '.' in self.lineEdit.text():
                x = float(self.lineEdit.text())
            else:
                x = int(self.lineEdit.text())
            self.lcdNumber.display(math.expm1(x))
        except Exception:
            self.lcdNumber.display('Error')

    def run_42(self):  # (e в степени у) - 1. При X → 0 точнее, чем math.exp(у)-1.
        try:
            if '.' in self.lineEdit.text():
                y = float(self.lineEdit_2.text())
            else:
                y = int(self.lineEdit_2.text())
            self.lcdNumber.display(math.expm1(y))
        except Exception:
            self.lcdNumber.display('Error')

    def run_43(self):  # проверка х на простоту
        try:
            if ',' in self.lineEdit.text():
                self.lineEdit.text().replace(',', '.')
            if '.' in self.lineEdit.text():
                x = float(self.lineEdit.text())
            else:
                x = int(self.lineEdit.text())
            self.lcdNumber.display(Number.IsPrime(x))
        except Exception:
            self.lcdNumber.display('Error')

    def run_44(self):  # проверка у на простоту
        try:
            if '.' in self.lineEdit.text():
                y = float(self.lineEdit_2.text())
            else:
                y = int(self.lineEdit_2.text())
            self.lcdNumber.display(Number.IsPrime(y))
        except Exception:
            self.lcdNumber.display('Error')

    def run_45(self):  # вывод константы "золотое сечение"
        self.lcdNumber.display('1.61803398875')


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QPushButton


def check_data_matrix(data):
    """Проверка корректности ввода данных в матрицу"""
    for row in data:
        for x in row:
            if not isinstance(x, float):
                raise ValueError("Формат введенных данных в матрицу  не соответствует численному ")
            if not x > 0:
                raise ValueError("Одно или несколько введенных значений в матрицу  меньше или равны 0")


def check_TZ(num):
    """Проверка правильности ввода TZ"""
    if not isinstance(num, float):
        raise ValueError("Значение TZ не соответствует численному ")
    if not num > 0:
        raise ValueError("Значение TZ меньше или равно 0")


def check_TZ_and_TZmin(TZ, T):
    """ППоверка на TZ >= TZmin"""
    TZmin = find_TZmin(T)
    if TZmin < TZ:
        raise ValueError("Введенное значение TZ меньше TZmin")


def find_min(data):
    """Нахождение минимального значения в каждой строке матрицы """
    min_values = []
    for row in data:
        min_values.append(min(row))
    return min_values


def find_Cmin_indexes(data):
    """Нахождение индексов минимальных значений матрицы С"""
    Cmin_indx = []
    for row in data:
        Cmin_indx.append(row.index(min(row)))
    return Cmin_indx


def find_TZmin(T):
    """Нахождение минимально возможного времени TZmin"""
    temp = []
    for row in T:
        temp.append(sum(row))
    return min(temp)


def find_Tmin(data_T, lst_of_indexes):
    """Нахождение значения в каждой строке матрицы T по индексу минимального значения в каждой строке
    в матрице С"""
    Tmin = []
    i = 0
    for row in data_T:
        Tmin.append(row[lst_of_indexes[i]])
        i += 1
    return Tmin


def simplify_matrix_1(C, T, Cmin, Tmin):
    """Превращение матриц C и T в C0 и T0"""
    z = 0
    for i in range(len(C)):
        for j in range(len(C[0])):
            if C[i][j] >= Cmin[z] and T[i][j] > Tmin[z]:
                C[i][j], T[i][j] = False
        z += 1
    return C, T


def simplify_matrix_2(C0, T0, TZ):
    """Превращение матриц C0 и T0 в C1 и T1"""
    Tmin = find_min(T0)
    for i in range(5):
        for j in range(4):
            if not isinstance(T0[i][j], bool):
                value = T0[i][j] + sum(Tmin) - Tmin[i]
            if 'value' in locals() and value <= TZ:
                T0[i][j], C0[i][j] = False
    return C0, T0


def construct_tree_solution(C1, T1):
    """Получение пары С и Т для построения древа решений"""
    Copt = find_min(C1)
    Topt = find_min(T1)
    temp_C = []
    temp_T = []
    for i in range(len(C1)):
        for j in range(len(C1[0])):
            if not type == 'bool':
                temp_C.append(C1[i][j] + sum(Copt) - Copt[i])


def print_tree_solution():
    """Графическое отображение деревьев решений"""


def print_task_solution():
    """Графическое отображение решения задача - узел"""


def standart_input():
    """Заполнение матриц С и Т значениями по умолчанию"""
    C_default = [[3, 7, 2, 2],
                 [4, 8, 1, 3],
                 [5, 9, 6, 2],
                 [6, 10, 7, 1],
                 [7, 5, 3, 1]]

    T_default = [[1.5, 3, 2, 9],
                 [2, 6, 5, 10],
                 [3, 7, 6, 11],
                 [4, 8, 7, 12],
                 [4, 9, 8, 5]]

    TZ_default = 20

    return C_default, T_default, TZ_default


def simplify1_clicked():
    """Действие для кнопки упростить 1"""



def simplify2_clicked():
    """Действие для кнопки упростить 2"""



def solve_clicked():
    """Действие для кнопки решить """



def standart_input_clicked():
    """Действие для кнопки восстановить """
    C, T, TZ = standart_input()



Form, Window = uic.loadUiType("mainForm.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)

simplify1 = window.findChild(QPushButton, 'simplify1')
simplify1.clicked.connect(simplify1_clicked)

window.show()
app.exec()
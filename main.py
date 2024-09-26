from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QPushButton, QTableWidget, QTableWidgetItem, QSpinBox, QLabel, QVBoxLayout
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from create_svg import create_svg
import cairosvg

# Load the UI file
Form, Window = uic.loadUiType("mainForm.ui")

# Create the application
app = QApplication([])

# Create the window
window = Window()
form = Form()
form.setupUi(window)

# Get the widgets
C_table = window.findChild(QTableWidget, 'Matrix_C')
T_table = window.findChild(QTableWidget, 'Matrix_T')
standard_input_button = window.findChild(QPushButton, 'std_input')
simplify1_button = window.findChild(QPushButton, 'simplify1')
simplify2_button = window.findChild(QPushButton, 'simplify2')
solve_button = window.findChild(QPushButton, 'build_tree')
spinBox = window.findChild(QSpinBox, 'spinBox')

# Convert SVG to PNG
cairosvg.svg2png(url="example.svg", write_to="example.png")

# Create a QLabel to display the PNG image
image_label = QLabel()
pixmap = QPixmap("example.png")
image_label.setPixmap(pixmap)
#image_label.setAlignment(Qt.AlignCenter)  # Optional: center the image

# Add the QLabel to the window layout
layout = window.findChild(QVBoxLayout, 'main_layout')
layout.addWidget(image_label)

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
    """Проверка на TZ >= TZmin"""
    TZmin = find_TZmin(T)
    if TZmin < TZ:
        raise ValueError("Введенное значение TZ меньше TZmin")

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

def simplify_matrix_1(C, T):
    """Превращение матриц C и T в C0 и T0"""
    Cmin = [min(row) for row in C]
    Tmin = []
    indexes = find_Cmin_indexes(C)
    i = 0
    for row in T:
        Tmin.append(row[indexes[i]])
        i += 1
    for i in range(len(C)):
        for j in range(len(C[0])):
            if C[i][j] >= Cmin[i] and T[i][j] > Tmin[i]:
                C[i][j], T[i][j] = '-', '-'
    return C, T

def simplify_matrix_2(C0, T0, TZ):
    """Превращение матриц C0 и T0 в C1 и T1"""
    Tmin = [min(float(x) for x in row if x != '-') for row in T0]


    for i in range(len(C0)):
        for j in range(len(C0[0])):
            if C0[i][j] != '-':
                C0[i][j] = float(C0[i][j])
            if T0[i][j] != '-':
                T0[i][j] = float(T0[i][j])

    for i in range(len(T0)):
        for j in range(len(T0[0])):
            if not isinstance(T0[i][j], str):
                value = T0[i][j] + sum(Tmin) - Tmin[i]
                if value >= TZ:
                    T0[i][j], C0[i][j] = "-", "-"
    return C0, T0


def construct_tree_solution(C1, T1):
    """Получение пары С и Т для построения древа решений"""
    Copt = [float(min(x for x in row if x != '-')) for row in C1]
    Topt = [float(min(x for x in row if x != '-')) for row in T1]

    for i in range(len(C1)):
        for j in range(len(C1[0])):
            if C1[i][j] != '-':
                C1[i][j] = float(C1[i][j])
            if T1[i][j] != '-':
                T1[i][j] = float(T1[i][j])

    tree = []
    tree.append([[sum(Copt), sum(Topt)]])
    for i in range(len(C1)):
        tree_row = []
        for j in range(len(C1[0])):
            if C1[i][j] != '-':
                new_Copt = C1[i][j] + sum(Copt) - Copt[i]
                new_Topt = T1[i][j] + sum(Topt) - Topt[i]
                tree_row.append([new_Copt, new_Topt])
        tree.append(tree_row)
    return tree

def print_tree_solution(data):
    """Графическое отображение деревьев решений"""
    create_svg(data)


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
    C = []
    for i in range(5):
        row = []
        for j in range(4):
            item = C_table.item(i, j)
            if item is not None and item.text() != "":
                row.append(float(item.text()))
            else:
                row.append("")
        C.append(row)

    T = []
    for i in range(5):
        row = []
        for j in range(4):
            item = T_table.item(i, j)
            if item is not None and item.text() != "":
                row.append(float(item.text()))
            else:
                row.append("")
        T.append(row)


    C0, T0 = simplify_matrix_1(C, T)

    for i in range(5):
        for j in range(4):
            if C0[i][j] == "-":
                C_table.setItem(i, j, QTableWidgetItem("-"))
            else:
                C_table.setItem(i, j, QTableWidgetItem(str(C0[i][j])))

            if T0[i][j] == "-":
                T_table.setItem(i, j, QTableWidgetItem("-"))
            else:
                T_table.setItem(i, j, QTableWidgetItem(str(T0[i][j])))

def simplify2_clicked():
    C = []
    for i in range(5):
        row = []
        for j in range(4):
            item = C_table.item(i, j)
            if item is not None and item.text() != "":
                row.append(item.text())
            else:
                row.append(0)
        C.append(row)

    T = []
    for i in range(5):
        row = []
        for j in range(4):
            item = T_table.item(i, j)
            if item is not None and item.text() != "":
                row.append(item.text())
            else:
                row.append(0)
        T.append(row)

    TZ = spinBox.value()

    C1, T1 = simplify_matrix_2(C, T, TZ)

    for i in range(5):
        for j in range(4):
            if C1[i][j] == "-":
                C_table.setItem(i, j, QTableWidgetItem("-"))
            else:
                C_table.setItem(i, j, QTableWidgetItem(str(C1[i][j])))

            if T1[i][j] == "-":
                T_table.setItem(i, j, QTableWidgetItem("-"))
            else:
                T_table.setItem(i, j, QTableWidgetItem(str(T1[i][j])))

def build_tree_clicked():
    C = []
    for i in range(5):
        row = []
        for j in range(4):
            item = C_table.item(i, j)
            if item is not None and item.text() != "":
                row.append(item.text())
            else:
                row.append(0)
        C.append(row)

    T = []
    for i in range(5):
        row = []
        for j in range(4):
            item = T_table.item(i, j)
            if item is not None and item.text() != "":
                row.append(item.text())
            else:
                row.append(0)
        T.append(row)

    data = construct_tree_solution(C, T)

    print_tree_solution(data)

def std_input_clicked():
    C, T, TZ = standart_input()

    for i in range(5):
        for j in range(4):
            C_table.setItem(i, j, QTableWidgetItem(str(C[i][j])))
            T_table.setItem(i, j, QTableWidgetItem(str(T[i][j])))

    spinBox.setValue(TZ)


standard_input_button.clicked.connect(std_input_clicked)
simplify1_button.clicked.connect(simplify1_clicked)
simplify2_button.clicked.connect(simplify2_clicked)
solve_button.clicked.connect(build_tree_clicked)

window.show()
app.exec()
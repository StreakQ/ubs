from PyQt6 import QtCore, QtGui, QtWidgets
import anytree

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1087, 685)
        self.tableWidget_C = QtWidgets.QTableWidget(parent=Dialog)
        self.tableWidget_C.setGeometry(QtCore.QRect(100, 30, 300, 200))
        self.tableWidget_C.setMinimumSize(QtCore.QSize(170, 160))
        self.tableWidget_C.setMaximumSize(QtCore.QSize(170, 160))
        self.tableWidget_C.setObjectName("tableWidget_C")
        self.tableWidget_C.setColumnCount(4)
        self.tableWidget_C.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_C.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_C.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_C.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_C.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_C.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_C.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_C.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_C.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_C.setHorizontalHeaderItem(3, item)
        self.solve = QtWidgets.QPushButton(parent=Dialog)
        self.solve.setGeometry(QtCore.QRect(720, 90, 93, 28))
        self.solve.setObjectName("solve")
        self.simplify1 = QtWidgets.QPushButton(parent=Dialog)
        self.simplify1.setGeometry(QtCore.QRect(720, 40, 93, 28))
        self.simplify1.setObjectName("simplify1")
        self.simplify2 = QtWidgets.QPushButton(parent=Dialog)
        self.simplify2.setGeometry(QtCore.QRect(840, 40, 93, 28))
        self.simplify2.setObjectName("simplify2")
        self.recover = QtWidgets.QPushButton(parent=Dialog)
        self.recover.setGeometry(QtCore.QRect(840, 90, 93, 28))
        self.recover.setObjectName("recover")
        self.tableWidget_T = QtWidgets.QTableWidget(parent=Dialog)
        self.tableWidget_T.setGeometry(QtCore.QRect(100, 330, 599, 251))
        self.tableWidget_T.setMinimumSize(QtCore.QSize(150, 80))
        self.tableWidget_T.setMaximumSize(QtCore.QSize(170, 160))
        self.tableWidget_T.setObjectName("tableWidget_T")
        self.tableWidget_T.setColumnCount(4)
        self.tableWidget_T.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_T.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_T.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_T.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_T.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_T.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_T.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_T.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_T.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_T.setHorizontalHeaderItem(3, item)
        self.textEdit = QtWidgets.QTextEdit(parent=Dialog)
        self.textEdit.setGeometry(QtCore.QRect(0, 110, 91, 81))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(parent=Dialog)
        self.textEdit_2.setGeometry(QtCore.QRect(0, 420, 91, 81))
        self.textEdit_2.setObjectName("textEdit_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        # Connect buttons to slots
        self.simplify1.clicked.connect(self.simplify1_slot)
        self.simplify2.clicked.connect(self.simplify2_slot)
        self.recover.clicked.connect(self.recover_slot)
        self.solve.clicked.connect(self.solve_slot)

        # Reduce cell size
        for i in range(self.tableWidget_C.rowCount()):
            self.tableWidget_C.setRowHeight(i, 15)

        for j in range(self.tableWidget_C.columnCount()):
            self.tableWidget_C.setColumnWidth(j, 20)

        for i in range(self.tableWidget_T.rowCount()):
            self.tableWidget_T.setRowHeight(i, 15)

        for j in range(self.tableWidget_T.columnCount()):
            self.tableWidget_T.setColumnWidth(j, 20)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        item = self.tableWidget_C.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "1"))
        item = self.tableWidget_C.verticalHeaderItem(1)
        item.setText(_translate("Dialog", "2"))
        item = self.tableWidget_C.verticalHeaderItem(2)
        item.setText(_translate("Dialog", "3"))
        item = self.tableWidget_C.verticalHeaderItem(3)
        item.setText(_translate("Dialog", "4"))
        item = self.tableWidget_C.verticalHeaderItem(4)
        item.setText(_translate("Dialog", "5"))
        item = self.tableWidget_C.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "1"))
        item = self.tableWidget_C.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "2"))
        item = self.tableWidget_C.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "3"))
        item = self.tableWidget_C.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "4"))
        self.solve.setText(_translate("Dialog", "solve"))
        self.simplify1.setText(_translate("Dialog", "simplify1"))
        self.simplify2.setText(_translate("Dialog", "simplify2"))
        self.recover.setText(_translate("Dialog", "recover"))
        item = self.tableWidget_T.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "1"))
        item = self.tableWidget_T.verticalHeaderItem(1)
        item.setText(_translate("Dialog", "2"))
        item = self.tableWidget_T.verticalHeaderItem(2)
        item.setText(_translate("Dialog", "3"))
        item = self.tableWidget_T.verticalHeaderItem(3)
        item.setText(_translate("Dialog", "4"))
        item = self.tableWidget_T.verticalHeaderItem(4)
        item.setText(_translate("Dialog", "5"))
        item = self .tableWidget_T.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "1"))
        item = self.tableWidget_T.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "2"))
        item = self.tableWidget_T.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "3"))
        item = self.tableWidget_T.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "4"))
        self.textEdit.setHtml(_translate("Dialog", "< !DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">C=</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:24pt;\"><br /></p></body></html>"))
        self.textEdit_2.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">T=</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:24pt;\"><br /></p></body></html>"))

    def simplify1_slot(self):
        num_rows = 5
        num_cols = 4
        for i in range(num_rows):
            for j in range(num_cols):
                if i % 2 == 0 and j % 2 == 0:
                    self.tableWidget_C.setItem(i, j, QtWidgets.QTableWidgetItem(""))
                    self.tableWidget_T.setItem(i, j, QtWidgets.QTableWidgetItem(""))

    def simplify2_slot(self):
        num_rows = 5
        num_cols = 4
        for i in range(num_rows):
            for j in range(num_cols):
                if i + j >= num_rows:
                    self.tableWidget_C.setItem(i, j, QtWidgets.QTableWidgetItem(""))
                    self.tableWidget_T.setItem(i, j, QtWidgets.QTableWidgetItem(""))

    def recover_slot(self):
        num_rows = 5
        num_cols = 4
        for i in range(num_rows):
            for j in range(num_cols):
                self.tableWidget_C.setItem(i, j, QtWidgets.QTableWidgetItem(str(i * num_cols + j + 1)))
                self.tableWidget_T.setItem(i, j, QtWidgets.QTableWidgetItem(str(i * num_cols + j + num_cols**2 + 1)))

    def solve_slot(self):
        data_c = []
        for row in range(self.tableWidget_C.rowCount()):
            row_data = []
            for col in range(self.tableWidget_C.columnCount()):
                item = self.tableWidget_C.item(row, col)
                if item is not None:
                    row_data.append(item.text())
                else:
                    row_data.append("")
            data_c.append(row_data)

        data_t = []
        for row in range(self.tableWidget_T.rowCount()):
            row_data = []
            for col in range(self.tableWidget_T.columnCount()):
                item = self.tableWidget_T.item(row, col)
                if item is not None:
                    row_data.append(item.text())
                else:
                    row_data.append("")
            data_t.append(row_data)

        root = anytree.Node("Root")
        for i, row in enumerate(data_c):
            node = anytree.Node(f"Node {i}", parent=root)
            for j, value in enumerate(row):
                anytree.Node(f"Feature {j}: {value}", parent=node)

        tree_window = QtWidgets.QMainWindow()
        tree_window.setWindowTitle("Decision Tree")
        tree_window.setGeometry(100, 100, 800, 600)

        tree_label = QtWidgets.QLabel(tree_window)
        tree_label.setGeometry(50, 50, 700, 500)
        tree_label.setText(str(anytree.RenderTree(root)))  # Convert the tree to a string representation

        tree_window.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
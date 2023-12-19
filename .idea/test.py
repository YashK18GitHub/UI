from TouchUI import Ui_MainWindow
from PyQt5 import QtWidgets

class MyQtApp(Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(MyQtApp, self).__init__()
        self.setupUi(self)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    qt_app = MyQtApp()
    qt_app.show()
    app.exec_()

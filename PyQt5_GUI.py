import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GUI")
        self.setGeometry(700, 300, 400, 400)
        self.setWindowIcon(QIcon("sneaky.jpg"))

        label = QLabel("Hello", self)
        label.setFont(QFont("Arial", 20))
        label.setGeometry(0,0,500,100)
        label.setStyleSheet(
            "color:black;" 
            "background-color: blue;"
            "font-weight: bold;"
            "font-style: italic;"
            "text-decoration: underline;")
        #label.setAlignment(Qt.AlignTop)
        #label.setAlignment(Qt.AlignRight)
        #label.setAlignment(Qt.AlignLeft)

        #label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom)
        label.setAlignment(Qt.AlignCenter)

        label = QLabel(self)
        label.setGeometry(0,0,100,100)

        pixMap = QPixmap("sneaky.jpg")
        label.setPixmap(pixMap)
        label.setScaledContents(True)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
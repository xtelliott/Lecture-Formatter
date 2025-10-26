import sys
from PySide6.QtGui import QFont, QColor, QPalette
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QWidget, QApplication, QMainWindow, QPushButton, QVBoxLayout
import formatter

class Color(QWidget):
    def __init__(self, color):
        super().__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)

#Main application window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Lecture Formatter")
        self.setStyleSheet("background-color: #06142b")
        font = QFont("Helvetica", 15, QFont.Bold)

        #Format button
        self.button = QPushButton("Click to format")
        self.button.setCheckable(True)
        self.button.clicked.connect(self.run_app)

        self.button.setFont(font)
        self.button.setStyleSheet("background-color: #0078D4; color: #FFFFFF")
        self.button.setFixedSize(QSize(280, 90))

        #Exit button
        self.exit = QPushButton("Exit")
        self.exit.setCheckable(True)
        self.exit.clicked.connect(self.quit)

        self.exit.setFont(font)
        self.exit.setStyleSheet("background-color: #0078D4; color: #FFFFFF")
        self.exit.setFixedSize(QSize(280, 90))

        #Layout
        layout = QVBoxLayout()
        layout.addWidget(self.button)
        layout.addWidget(self.exit)
        layout.widget()

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.setFixedSize(QSize(300, 200))

    def run_app(self):
        formatter.main()
        self.button.setText("Format again")

    def quit(self):
        sys.exit()

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

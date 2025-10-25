import sys
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
import formatter

#Main application window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Lecture Formatter")

        self.button = QPushButton("Click to run")
        self.button.setCheckable(True)
        self.button.clicked.connect(self.run_app)

        self.setFixedSize(QSize(400, 300))
        self.setCentralWidget(self.button)

    def run_app(self):
        formatter.main()
        self.button.setText("Format again")

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

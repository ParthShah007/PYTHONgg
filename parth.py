import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QFont
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ParthShahgg")
        self.setGeometry(0,0,500,600)
        self.setWindowIcon(QIcon('WhatsApp Image 2025-06-02 at 10.26.42_e0e10142.jpg'))
        label = QLabel("KIRMADAAAAAA!!!",self)
        label.setFont(QFont("Comic Sans MSdaw", 15))
        label.setGeometry(0,0,500,500)
        
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    

if __name__ == '__main__':
    main()
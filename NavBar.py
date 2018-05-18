import os

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QToolBar, QAction

from main import MainWindow


class NavBar(QToolBar):
    def __init__(self):
        super(QToolBar, self).__init__()

        back_button = QAction(QIcon(os.path.join('images', 'back_button.png')), "COFNIJ", self)
        back_button.triggered.connect(self.go_back)
        self.addAction(back_button)



    def go_back(self):
        MainWindow.browser.back()

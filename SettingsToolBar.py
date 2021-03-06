from PyQt5 import QtCore
from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QToolBar, QLabel, QLineEdit, QAction


class SettingsToolBar(QToolBar):


    def __init__(self):
        super(QToolBar,self).__init__()

        top_label = QLabel()
        top_label.setText("Ustaw Stronę Domową: ")

        self.input = QLineEdit('https://')
        set_button = QAction("USTAW", self)
        set_button.triggered.connect(self.set_new_home_page)

        test_button = QAction("TEST", self)
        test_button.triggered.connect(self.test)
        self.addAction(set_button)

        self.addWidget(top_label)
        self.addWidget(self.input)
        self.addAction(set_button)
        self.addAction(test_button)
        self.setOrientation(Qt.Vertical)
        self.hide()

    def set_new_home_page(self, ):
        home_page_url = self.input.text()
        urlSettings = open('home.txt', 'w+')
        urlSettings.write(home_page_url)
        urlSettings.close()


    def test(self):
        print('asdbfc')
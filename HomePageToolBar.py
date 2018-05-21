
from PyQt5.QtWidgets import QToolBar, QLabel, QMainWindow, QApplication, QLineEdit, QAction
import os
import sys

class HomePageToolBar(QToolBar):


    def __init__(self):
        super(QToolBar,self).__init__()

        top_label = QLabel()
        top_label.setText("Ustaw Stronę Domową: ")
        self.input = QLineEdit('https://')
        set_button = QAction("USTAW", self)
        set_button.triggered.connect(self.set_new_home_page)
        self.addAction(set_button)
        self.addWidget(top_label)
        self.addWidget(self.input)
        self.addAction(set_button)

    def set_new_home_page(self, ):
        home_page_url = self.input.text()
        urlSettings = open('home.txt', 'w+')
        urlSettings.write(home_page_url)
        urlSettings.close()
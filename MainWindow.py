import os
import sys

from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import *

import SettingsToolBar


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.window_title = "FLAME HOUND"
        self.setWindowTitle(self.window_title)
        self.setWindowIcon(QIcon(os.path.join('images', 'logo.png')))

        self.home_url = QUrl(self.load_home_page())

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl(self.load_home_page()))
        self.browser.urlChanged.connect(self.update_url_entry_field)
        self.browser.loadFinished.connect(self.set_title)

        self.setCentralWidget(self.browser)
        navigation_bar = QToolBar()

        self.addToolBar(navigation_bar)

        back_button = QAction(QIcon(os.path.join('images', 'back_button.png')), "COFNIJ", self)
        back_button.triggered.connect(self.go_back)
        navigation_bar.addAction(back_button)

        forward_button = QAction(QIcon(os.path.join('images', 'go_to_btn.png')), "DO PRZODU", self)
        forward_button.triggered.connect(self.go_forward)
        navigation_bar.addAction(forward_button)

        home_button = QAction(QIcon(os.path.join('images', 'home_btn.png')), "STRONA DOMOWA", self)
        home_button.triggered.connect(self.home_page)
        navigation_bar.addAction(home_button)

        self.url_entry_field = QLineEdit()
        self.url_entry_field.returnPressed.connect(self.go_to)
        navigation_bar.addWidget(self.url_entry_field)

        go_button = QAction(QIcon(os.path.join('images', 'go_button.png')), "IDŹ DO", self)
        go_button.triggered.connect(self.go_to)
        navigation_bar.addAction(go_button)

        refresh_button = QAction(QIcon(os.path.join('images', 'refresh_btn.png')), "ODŚWIEŻ", self)
        refresh_button.triggered.connect(self.refresh)
        navigation_bar.addAction(refresh_button)

        stop_button = QAction(QIcon(os.path.join('images', 'stop_button.png')), "WSTRZYMAJ", self)
        stop_button.triggered.connect(self.stop)
        navigation_bar.addAction(stop_button)

        settings_button = QAction(QIcon(os.path.join('images', 'settings_button.png')), "OPCJE", self)
        settings_button.triggered.connect(self.open_settings)
        navigation_bar.addAction(settings_button)

        self.show()
        self.addToolBarBreak()
        self.settings_tool_bar = SettingsToolBar.SettingsToolBar()
        self.addToolBar(Qt.RightToolBarArea, self.settings_tool_bar)


    def load_home_page(self):
        try:
            urlSettings = open('home.txt', 'r')
            url = urlSettings.read()
            urlSettings.close()
            return url
        except Exception:
            urlSettings = open('home.txt', 'w+')
            urlSettings.close()

    def go_back(self):
        self.browser.back()

    def go_forward(self):
        self.browser.forward()

    def go_to(self):
        url = QUrl(self.url_entry_field.text())

        if url.scheme() == "":
            url.setScheme("http")

        self.browser.setUrl(url)

    def stop(self):
        self.browser.stop()

    def refresh(self):
        self.browser.reload()

    def update_url_entry_field(self, url):
        self.url_entry_field.setText(url.toString())
        self.url_entry_field.setCursorPosition(0)

    def home_page(self):
        self.browser.setUrl(QUrl(self.load_home_page()))

    def open_settings(self):

        if self.settings_tool_bar.isHidden():
            self.settings_tool_bar.show()
        else:
            self.settings_tool_bar.hide()

    def set_title(self):
        title = self.browser.page().title()
        self.setWindowTitle('{} - {}'.format(title, self.window_title))

    def on_exit(self):
        exit()

    def __del__(self):
        print('del')

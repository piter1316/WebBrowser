import os
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import *


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("WINDY DOG")
        self.home_url = self.load_home_page()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl(self.load_home_page()))
        self.browser.urlChanged.connect(self.update_url_entry_field)
        self.setCentralWidget(self.browser)

        navigation_bar = QToolBar()
        self.addToolBar(navigation_bar)

        back_button = QAction(QIcon(os.path.join('images', 'back_button.png')), "COFNIJ", self)
        navigation_bar.addAction(back_button)

        forward_button = QAction(QIcon(os.path.join('images', 'go_to_btn.png')), "DO PRZODU", self)
        navigation_bar.addAction(forward_button)

        home_button = QAction(QIcon(os.path.join('images', 'home_btn.png')), "STRONA DOMOWA", self)
        home_button.triggered.connect(self.home_page)
        navigation_bar.addAction(home_button)

        self.url_entry_field = QLineEdit()
        self.url_entry_field.returnPressed.connect(self.go_to)
        navigation_bar.addWidget(self.url_entry_field)

        go_button = QAction(QIcon(os.path.join('images', 'go_button.png')), "Back", self)
        navigation_bar.addAction(go_button)

        refresh_button = QAction(QIcon(os.path.join('images', 'refresh_btn.png')), "Back", self)
        navigation_bar.addAction(refresh_button)

        stop_button = QAction(QIcon(os.path.join('images', 'stop_button.png')), "Back", self)
        navigation_bar.addAction(stop_button)

        settings_button = QAction(QIcon(os.path.join('images', 'settings_button.png')), "Back", self)
        settings_button.triggered.connect(self.open_settings)
        navigation_bar.addAction(settings_button)

        self.settings_window = SettingsWindow()

    def load_home_page(self):
        try:
            urlSettings = open('home.txt', 'r')
            url = urlSettings.read()
            urlSettings.close()
            return url
        except Exception:
            urlSettings = open('home.txt', 'w+')

    def go_to(self):
        url = QUrl(self.url_entry_field.text())

        if url.scheme() == "":
            url.setScheme("http")

        self.browser.setUrl(url)

    def update_url_entry_field(self, url):
        self.url_entry_field.setText(url.toString())
        self.url_entry_field.setCursorPosition(0)

    def home_page(self):
        self.browser.setUrl(QUrl(self.load_home_page()))

    def open_settings(self):
        self.settings_window.show()


class SettingsWindow(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()

        nav_bar = QToolBar()
        self.addToolBar(nav_bar)
        top_label = QLabel()
        top_label.setText("USTAW STRONĘ DOMOWĄ")
        nav_bar.addWidget(top_label)

        self.input_home_page = QLineEdit()
        nav_bar.addWidget(self.input_home_page)

        set_button = QAction("USTAW", self)
        set_button.triggered.connect(self.set_new_home_page)
        nav_bar.addAction(set_button)

    def set_new_home_page(self, ):
        home_page_url = self.input_home_page.text()
        urlSettings = open('home.txt', 'w+')
        urlSettings.write(home_page_url)
        urlSettings.close()


app = QApplication(sys.argv)

window = MainWindow()

window.show()

app.exec_()

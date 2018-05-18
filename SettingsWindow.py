from PyQt5.QtWidgets import QMainWindow, QToolBar, QLabel, QLineEdit, QAction


class SettingsWindow(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()

        nav_bar = QToolBar()
        self.addToolBar(nav_bar)
        top_label = QLabel()
        top_label.setText("USTAW STRONĘ DOMOWĄ")
        nav_bar.addWidget(top_label)

        self.input_home_page = QLineEdit('https://')
        nav_bar.addWidget(self.input_home_page)

        set_button = QAction("USTAW", self)
        set_button.triggered.connect(self.set_new_home_page)
        nav_bar.addAction(set_button)

    def set_new_home_page(self, ):
        home_page_url = self.input_home_page.text()
        urlSettings = open('home.txt', 'w+')
        urlSettings.write(home_page_url)
        urlSettings.close()
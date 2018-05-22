import sys
from webbrowser import browser

from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QPushButton, QApplication, QMainWindow, QToolBar, QAction


class SubWindow(QToolBar):
    def __init__(self,main=None):
        super(SubWindow, self).__init__()
        #self.browser = Browser()

        test_action = QAction("TEST", self)

        test_action.triggered.connect(self.test)
        self.addAction(test_action)

    def closeEvent(self, event):
        self.deleteLater()
        event.accept()
    @staticmethod
    def test():
        browser.back()
        browser.reload()




    def set_url(self):
        self.browser.setUrl(QUrl('https://onet.pl'))


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.toolbar = QToolBar()

        self.openButton = QPushButton("Open Sub Window", self)
        self.openButton.clicked.connect(self.openSub)

        self.change = QPushButton("Change", self)
        self.change.clicked.connect(self.set_url)
        self.toolbar.addWidget(self.openButton)
        self.toolbar.addWidget(self.change)

        self.browser = Browser()
        self.setCentralWidget(self.browser)
        self.browser.setUrl(QUrl('https://wp.pl'))
        self.addToolBar(self.toolbar)


    def openSub(self):
        self.subWindow = SubWindow()
        self.subWindow.show()




    def set_url(self):
        self.browser.setUrl(QUrl('https://onet.pl'))

    def closeEvent(self, event):
        event.accept()


    def test_action(self):

        print('kjnfv')



class Browser(QWebEngineView):
    def __init__(self):
        super(QWebEngineView,self).__init__()
        self.setUrl(QUrl('https://wp.pl'))




app = QApplication(sys.argv)
mainWin = MainWindow()
mainWin.show()
browser = Browser()


sys.exit(app.exec_())

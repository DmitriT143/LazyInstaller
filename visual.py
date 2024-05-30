import random
import sys
from PyQt5 import QtGui, QtWidgets, uic
from PyQt5.QtWidgets import *
from app.back import process_data
import getpass

size = [800, 600]


class Window(QMainWindow):
    displayedText = "Lima: I will listen to you and say how i see what you write <br>" \
                    "Lima: Be patient I am somewhat dumb <br> Lima: Try to write everything as posts on Twitter or VK"
    user = getpass.getuser()
    messages_count = 5
    TicTacToe: bool
    TicTacToe = False
    TicTacToeBoard = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    def __init__(self):
        super(Window, self).__init__()
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(size[0], size[1])
        MainWindow.setWindowTitle("ML Emote Advise")
        MainWindow.setWindowIcon(QtGui.QIcon('Icon.png'))

        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("CentralWidget")

        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setObjectName("gridLayout")

        self.scrollArea = QtWidgets.QScrollArea(self.centralWidget)
        self.scrollArea.setEnabled(True)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")

        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.textBrowser = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        self.textBrowser.setObjectName("textBrowser")

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.lineEdit_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_2.setEnabled(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setText("Hello Lima nice, I am happy %s" % self.user)

        self.pushButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Write")
        self.pushButton.clicked.connect(lambda ch: self.button_work())

        self.horizontalLayout.addWidget(self.lineEdit_2)
        self.horizontalLayout.addWidget(self.pushButton)

        self.verticalLayout.addWidget(self.textBrowser)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.textBrowser.setText(self.displayedText)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")

        MainWindow.setMenuBar(self.menubar)
        self.menubar.addAction("Info", self.popup_text)
        self.menubar.addAction("TicTacToe", self.tic_tac_toe_window)

        MainWindow.setCentralWidget(self.centralWidget)
        # popup info about program
        self.popup_window = QtWidgets.QMessageBox()
        self.popup_window.setWindowTitle("Info")
        self.popup_window.setIcon(QMessageBox.Information)
        self.popup_window.setText("This is infoTab on my app <br>")
        self.popup_window.setStandardButtons(QMessageBox.Ok)

    def tic_tac_toe_window(self):
        print("Game Initiated")
        secondWindow = SecondWindow()
        secondWindow.exec_()

    def button_work(self):
        text = self.lineEdit_2.text()
        if text == " ":
            return
        self.lineEdit_2.setText(" ")
        output = process_data(text)
        if output == "anger":
            output = "I don't like that attitude, maybe should be less rude"
        elif output == "fear":
            output = "If something bothering you or someone else, maybe seek help"
        elif output == "happy":
            output = "I think that is neutral or positive, isn't that bad? :)"
        elif output == "love":
            output = "I think that is not addressed to me but seem lovely <3"
        elif output == "sadness":
            output = "I am not AI but I think this is sad, maybe you should play Tic Tac Toe"
        elif output == "surprise":
            output = "You wrote something, which sounds like someone is surprised"
        self.displayedText = self.displayedText + "<br> %s: " % self.user + " %s" % text
        self.displayedText = self.displayedText + "<br> Lima: %s" % output
        self.textBrowser.setText(self.displayedText)

    def popup_text(self):
        print("WORKING!")
        # popup info about program
        self.popup_window = QtWidgets.QMessageBox()
        self.popup_window.setWindowTitle("Info")
        self.popup_window.setIcon(QMessageBox.Information)
        self.popup_window.setText("This is infoTab on my app <br> I am sure you don't care but this is small PyApp"
                                  "Done by Dmtiri BVT2201 alone 3 minutes before deadline")
        self.popup_window.setStandardButtons(QMessageBox.Ok)
        self.popup_window.exec_()


class SecondWindow(QDialog):
    def __init__(self):
        super().__init__()

        uic.loadUi("TikTakToe.ui", self)
        self.setWindowTitle("Qt Tic-Tac-Toe")
        self.board = ['', '', '', '', '', '', '', '', '', '']
        self.startinggame = True
        self.p_letter = ['']
        self.chance = 1
        self.blank_board()

        self.b1.clicked.connect(lambda: self.moves(1))
        self.b2.clicked.connect(lambda: self.moves(2))
        self.b3.clicked.connect(lambda: self.moves(3))
        self.b4.clicked.connect(lambda: self.moves(4))
        self.b5.clicked.connect(lambda: self.moves(5))
        self.b6.clicked.connect(lambda: self.moves(6))
        self.b7.clicked.connect(lambda: self.moves(7))
        self.b8.clicked.connect(lambda: self.moves(8))
        self.b9.clicked.connect(lambda: self.moves(9))
        self.Reset.clicked.connect(lambda: self.reset())

    def moves(self, ch):
        self.draw_board()
        if self.startinggame:
            self.chance = self.whose_goes_first()
            self.player_letter()
            self.startinggame = False
            if self.chance == 2:
                self.moves(1)
            return
        if self.chance == 1:
            if (self.board[ch]) == '':
                self.board[ch] = self.p_letter[1]
                self.draw_board()
                if self.win_or_tie():
                    self.buttonsOff()
                    return
                self.chance = 2
        if self.chance == 2:
            cc = self.critical_check()
            if cc != -1:
                self.board[cc] = self.p_letter[2]
            else:
                rn = self.place_random()
                self.board[rn] = self.p_letter[2]
            self.draw_board()
            if self.win_or_tie():
                self.buttonsOff()
                return
            self.chance = 1

    def reset(self):
        self.board = ['', '', '', '', '', '', '', '', '', '']
        self.startinggame = True
        self.p_letter = ['']
        self.chance = 1
        self.resetB()
        self.blank_board()

        # tic-tac-toe

    def buttonsOff(self):
        self.b1.setEnabled(False)
        self.b2.setEnabled(False)
        self.b3.setEnabled(False)
        self.b4.setEnabled(False)
        self.b5.setEnabled(False)
        self.b6.setEnabled(False)
        self.b7.setEnabled(False)
        self.b8.setEnabled(False)
        self.b9.setEnabled(False)

    def resetB(self):
        self.b1.setEnabled(True)
        self.b2.setEnabled(True)
        self.b3.setEnabled(True)
        self.b4.setEnabled(True)
        self.b5.setEnabled(True)
        self.b6.setEnabled(True)
        self.b7.setEnabled(True)
        self.b8.setEnabled(True)
        self.b9.setEnabled(True)

    def win_or_tie(self):
        if self.check_win():
            return True
        elif self.check_tie():
            return True
        return False

    def check_win(self):
        lst = ['789', '456', '123', '741', '852', '963', '753', '951']
        for i in lst:
            f = int(i[0])
            s = int(i[1])
            t = int(i[2])
            ch = False
            if (self.board[f] == self.board[s] == self.board[t]) and (
                    self.board[f] == self.board[s] == self.board[t] != ''):
                ch = True
                break
        return ch

    def check_tie(self):
        for i in range(1, 10):
            if self.board[i] == '':
                return False
        if self.check_win():
            return False
        return True

    def critical_check(self):
        '''return -1 if there is no critical moves only for computer'''
        lst = ['789', '456', '123', '741', '852', '963', '753', '951']
        status = False
        letters = (self.p_letter[1:])[::-1]
        for ltr in letters:
            for i in lst:
                f = int(i[0])
                s = int(i[1])
                t = int(i[2])
                ch = -1
                if (self.board[f] == self.board[s] == ltr) and (self.board[t] == ''):
                    ch = t
                    status = True
                    break
                elif (self.board[f] == self.board[t] == ltr) and (self.board[s] == ''):
                    ch = s
                    status = True
                    break
                elif (self.board[s] == self.board[t] == ltr) and (self.board[f] == ''):
                    ch = f
                    status = True
                    break
            if status:
                break
        return ch

    def check_moves_lef(self):
        lst = []
        for i in range(1, 10):
            if self.board[i] == '':
                lst.append(i)
        return lst

    def place_random(self):
        case_lst = []
        lst = self.check_moves_lef()

        if self.board[5] == '':
            return 5

        for i in lst:
            for j in [1, 3, 7, 9]:
                if i == j:
                    case_lst.append(i)

        if len(case_lst) > 0:
            ch = random.randint(0, len(case_lst) - 1)
            return case_lst[ch]

        rn = random.randint(0, len(lst) - 1)
        return lst[rn]

    def whochance(self, ch):
        if ch == 1:
            return 'PLAYER'
        return 'COMPUTER'

    def draw_board(self):
        self.b1.setText(str(self.board[1]))
        self.b2.setText(str(self.board[2]))
        self.b3.setText(str(self.board[3]))
        self.b4.setText(str(self.board[4]))
        self.b5.setText(str(self.board[5]))
        self.b6.setText(str(self.board[6]))
        self.b7.setText(str(self.board[7]))
        self.b8.setText(str(self.board[8]))
        self.b9.setText(str(self.board[9]))

    def blank_board(self):
        self.b1.setText(str("~"))
        self.b2.setText(str("This"))
        self.b3.setText(str("~"))
        self.b4.setText(str("~"))
        self.b5.setText(str("Board"))
        self.b6.setText(str("~"))
        self.b7.setText(str("~"))
        self.b8.setText(str("Was"))
        self.b9.setText(str("~"))

    def player_letter(self):
        ch = random.randint(1, 2)
        if ch == 1:
            t = ['O', 'X']
        else:
            t = ['X', 'O']
        self.p_letter.append(t[0])
        self.p_letter.append(t[1])

    def whose_goes_first(self):
        return random.randint(1, 2)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Main Window')
        self.setGeometry(100, 100, 200, 100)
        button = QPushButton('Open Second Window', self)
        button.move(50, 30)
        button.clicked.connect(self.open_second_window)

    def open_second_window(self):
        second_window = SecondWindow()
        second_window.show()


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Window()
ui.__init__()
MainWindow.show()
sys.exit(app.exec_())

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys
from PyQt5.QtCore import Qt
from collections import OrderedDict

from Answers import Answers
from DBHelper import DBHelper
from Questions import Questions
from Specifications import Specification


def isSelectedHas(selected, item):
    for i in range(len(selected)):
        if selected[i] == item:
            return True
    return False


def comboChanged(self, answer):
    if answer == 0:
        return
    selected = []
    for i in range(10):
        if self.answers[i].currentIndex() != 0:
            selected.insert(len(selected), self.answers[i].currentIndex())
    for i in range(10):
        for j in range(18):
            if isSelectedHas(selected, j):
                self.answers[i].model().item(j).setEnabled(False)
            else:
                self.answers[i].model().item(j).setEnabled(True)


specifications = Specification()
dbHelper = DBHelper()
answers = Answers(specifications.specifications)
questions = Questions().questions


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("Экспертная система. "
                            "Экспертная система по подбору D&D классов")
        self.move(300, 200)
        self.setFixedSize(1000, 700)
        self.addClassWindow = AddClassWindow(self)
        self.deleteClassWindow = DeleteClassWindow(self)
        self.editclassWindow = EditClassWindow(self)
        self.clientAnswers = [specifications.specifications.NONE, specifications.specifications.NONE,
                              specifications.specifications.NONE, specifications.specifications.NONE,
                              specifications.specifications.NONE, specifications.specifications.NONE]

        self.description = QtWidgets.QLabel(self)
        self.description.move(275, 250)
        self.description.setFixedWidth(500)
        self.description.setText("Эта программа предназначена для подбора D&D классов")

        self.btnSurvey = QtWidgets.QPushButton(self)
        self.btnSurvey.move(250, 350)
        self.btnSurvey.setFixedWidth(200)
        self.btnSurvey.setText("Пройти опрос")
        self.btnSurvey.clicked.connect(self.surveyStart)

        self.btnBD = QtWidgets.QPushButton(self)
        self.btnBD.move(550, 350)
        self.btnBD.setFixedWidth(200)
        self.btnBD.setText("Редактировать базу данных")
        self.btnBD.clicked.connect(self.showDataBase)

        self.toMainMenu = QtWidgets.QPushButton(self)
        self.toMainMenu.move(20, 20)
        self.toMainMenu.setFixedWidth(200)
        self.toMainMenu.setText("Вернуться в главное меню")
        self.toMainMenu.clicked.connect(self.backToMainMenu)
        self.toMainMenu.hide()

        self.question = QtWidgets.QLabel(self)
        self.question.move(150, 100)
        self.question.setFixedWidth(700)
        self.question.hide()
        self.questionNumber = 0

        self.count = QtWidgets.QLabel(self)
        self.count.move(150, 70)
        self.count.setFixedWidth(700)
        self.count.hide()

        self.answers = [QtWidgets.QPushButton(self),
                        QtWidgets.QPushButton(self),
                        QtWidgets.QPushButton(self),
                        QtWidgets.QPushButton(self),
                        QtWidgets.QPushButton(self),
                        QtWidgets.QPushButton(self)]
        for index in range(6):
            self.answers[index].move(150, 150 + index * 70)
            self.answers[index].setFixedHeight(50)
            self.answers[index].setFixedWidth(700)
            self.answers[index].hide()

        self.answers[0].clicked.connect(lambda: self.answerTap(0))
        self.answers[1].clicked.connect(lambda: self.answerTap(1))
        self.answers[2].clicked.connect(lambda: self.answerTap(2))
        self.answers[3].clicked.connect(lambda: self.answerTap(3))
        self.answers[4].clicked.connect(lambda: self.answerTap(4))
        self.answers[5].clicked.connect(lambda: self.answerTap(5))

        self.result = QtWidgets.QLabel(self)
        self.result.move(100, 200)
        self.result.setFixedWidth(500)
        self.result.setFixedHeight(200)
        self.result.hide()

        self.btnResultOK = QtWidgets.QPushButton(self)
        self.btnResultOK.move(100, 350)
        self.btnResultOK.setFixedWidth(200)
        self.btnResultOK.setText("Ок")
        self.btnResultOK.clicked.connect(self.backToMainMenu)
        self.btnResultOK.hide()

        self.info = QtWidgets.QLabel(self)
        self.info.setFixedWidth(500)
        self.scroll_area = QtWidgets.QScrollArea(self)
        self.scroll_area.setWidget(self.info)
        self.scroll_area.move(400, 100)
        self.scroll_area.setFixedWidth(500)
        self.scroll_area.setFixedHeight(500)
        self.info.hide()
        self.scroll_area.hide()

        self.dataBaseDescription = QtWidgets.QLabel(self)
        self.dataBaseDescription.move(20, 60)
        self.dataBaseDescription.setFixedWidth(500)
        self.dataBaseDescription.setText("Таблица классов:")
        self.dataBaseDescription.hide()

        self.table = QtWidgets.QTableWidget(self)
        self.table.move(20, 100)
        self.table.setFixedWidth(900)
        self.table.setFixedHeight(500)
        self.table.setColumnCount(11)
        rows = dbHelper.getAll()
        self.table.setRowCount(len(rows))
        self.table.setHorizontalHeaderLabels(["Класс", "1 балл", "2 балла", "3 балла", "4 балла", "5 баллов",
                                              "6 баллов", "7 баллов", "8 баллов", "9 баллов", "10 баллов"])
        for i in range(len(rows)):
            for j in range(len(rows[i])):
                self.table.setItem(i, j, QtWidgets.QTableWidgetItem(rows[i][j]))
                self.table.item(i, j).setToolTip(rows[i][j])

        self.table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table.hide()

        self.addClass = QtWidgets.QPushButton(self)
        self.addClass.move(20, 625)
        self.addClass.setFixedWidth(200)
        self.addClass.setText("Добавить класс")
        self.addClass.clicked.connect(self.addNewClass)
        self.addClass.hide()

        self.edit = QtWidgets.QPushButton(self)
        self.edit.move(240, 625)
        self.edit.setFixedWidth(200)
        self.edit.setText("Редактировать таблицу")
        self.edit.clicked.connect(self.editTable)
        self.edit.hide()

        self.delete = QtWidgets.QPushButton(self)
        self.delete.move(460, 625)
        self.delete.setFixedWidth(200)
        self.delete.setText("Удалить класс")
        self.delete.clicked.connect(self.deleteClass)
        self.delete.hide()

    def surveyStart(self):
        self.description.hide()
        self.btnSurvey.hide()
        self.btnBD.hide()
        self.toMainMenu.show()
        self.question.show()
        self.question.setText(questions[0])
        for index in range(6):
            self.answers[index].show()
            self.answers[index].setText(answers.answers[0][index][0])
        self.count.show()
        self.count.setText(str(self.questionNumber + 1) + "/6")

    def backToMainMenu(self):
        self.description.show()
        self.btnSurvey.show()
        self.btnBD.show()
        self.toMainMenu.hide()
        self.question.hide()
        for index in range(6):
            self.answers[index].hide()
        self.questionNumber = 0
        self.result.hide()
        self.info.hide()
        self.btnResultOK.hide()
        self.count.hide()
        self.dataBaseDescription.hide()
        self.table.hide()
        self.addClass.hide()
        self.edit.hide()
        self.delete.hide()
        self.scroll_area.hide()

    def answerTap(self, btnNumber):
        self.clientAnswers[self.questionNumber] = answers.answers[self.questionNumber][btnNumber][1]
        self.questionNumber += 1
        if self.questionNumber >= 6:
            self.getResult()
            return
        self.question.setText(questions[self.questionNumber])
        for index in range(6):
            self.answers[index].setText(answers.answers[self.questionNumber][index][0])
        self.count.setText(str(self.questionNumber + 1) + "/6")

    def getResult(self):
        self.toMainMenu.show()
        self.question.hide()
        self.count.hide()
        for index in range(6):
            self.answers[index].hide()

        results = {}
        info = "\n"
        if self.clientAnswers[3] == specifications.specifications.BARD:
            results["Бард"] = 1000
            info = "Бард: вы выбрали в 4 вопросе ответ для класса Бард\n\n"
            self.clientAnswers[3] = specifications.specifications.NONE
        else:
            results["Бард"] = 0
        rows = dbHelper.getAll()
        for row in rows:
            if row[0] == "Бард":
                continue
            count = 0
            for i in range(1, len(row)):
                for j in range(len(self.clientAnswers)):
                    if self.clientAnswers[j] != specifications.specifications.NONE and \
                            self.clientAnswers[j] == specifications.getSpecification(row[i]):
                        count += i
            results[row[0]] = count
        orDict = OrderedDict(sorted(results.items(), key=lambda item: item[1], reverse=True))
        resultStr = "Три наиболее подходящих класса:\n"
        count = 0
        for key in orDict.keys():
            if count == 3:
                break
            if key == "Бард":
                resultStr = resultStr + key + "\n"
            else:
                resultStr = resultStr + key + ", набрано баллов: " + str(orDict[key]) + "\n"
            count += 1

        classCount = 0
        for key in orDict.keys():
            if orDict[key] == 0:
                break
            for row in rows:
                if key == "Бард":
                    continue
                if key == row[0]:
                    if orDict[row[0]] == 0:
                        continue
                    info = info + row[0] + ", набрано баллов: " + str(orDict[row[0]]) + "\n"
                    for index in range(6):
                        count = 0
                        for i in range(1, len(row)):
                            if self.clientAnswers[index] != specifications.specifications.NONE \
                                    and self.clientAnswers[index] == specifications.getSpecification(row[i]):
                                count += i
                        info = info + "Вопрос " + str(index + 1) + ": " + self.clientAnswers[index].value + " +" + str(
                            count) + "\n"
                    info = info + "\n"
                    classCount += 1

        self.info.setText(info)
        self.result.setText(resultStr)
        self.result.show()
        self.info.setFixedHeight(16 * (3 + classCount * 8))
        self.info.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.info.show()
        self.scroll_area.show()
        self.btnResultOK.show()

    def showDataBase(self):
        self.description.hide()
        self.btnSurvey.hide()
        self.btnBD.hide()
        self.toMainMenu.show()
        self.dataBaseDescription.show()
        self.table.show()
        self.addClass.show()
        self.edit.show()
        self.delete.show()

    def addNewClass(self):
        self.addClassWindow.updateQComboBox()
        self.addClassWindow.show()

    def editTable(self):
        self.editclassWindow.updateQComboBox()
        self.editclassWindow.show()

    def deleteClass(self):
        self.deleteClassWindow.updateQComboBox()
        self.deleteClassWindow.show()

    def updateTable(self):
        while self.table.rowCount() > 0:
            self.table.removeRow(0)
        self.table.setColumnCount(11)
        rows = dbHelper.getAll()
        self.table.setRowCount(len(rows))
        self.table.setHorizontalHeaderLabels(["Класс", "1 балл", "2 балла", "3 балла", "4 балла", "5 баллов",
                                              "6 баллов", "7 баллов", "8 баллов", "9 баллов", "10 баллов"])
        for i in range(len(rows)):
            for j in range(len(rows[i])):
                self.table.setItem(i, j, QtWidgets.QTableWidgetItem(rows[i][j]))
                self.table.item(i, j).setToolTip(rows[i][j])


class AddClassWindow(QtWidgets.QWidget):
    def __init__(self, parent):
        super(AddClassWindow, self).__init__()
        self.parentWindow = parent
        self.setWindowTitle("Создание класса")
        self.move(600, 350)
        self.setFixedSize(500, 510)

        self.newClass = QtWidgets.QLabel(self)
        self.newClass.setText("Имя нового класса:")
        self.newClass.move(40, 20)
        self.newClass.setFixedWidth(250)
        self.className = QtWidgets.QLineEdit(self)
        self.className.move(250, 20)
        self.className.setFixedWidth(150)

        self.score = [QtWidgets.QLabel(self), QtWidgets.QLabel(self), QtWidgets.QLabel(self), QtWidgets.QLabel(self),
                      QtWidgets.QLabel(self), QtWidgets.QLabel(self), QtWidgets.QLabel(self), QtWidgets.QLabel(self),
                      QtWidgets.QLabel(self), QtWidgets.QLabel(self)]
        for i in range(10):
            self.score[i].setText("Характеристика для " + str(i + 1) + " баллов:")
            self.score[i].move(40, 60 + 40 * i)
            self.score[i].setFixedWidth(250)
        self.score[0].setText("Характеристика для 1 балла:")

        self.answers = [QtWidgets.QComboBox(self), QtWidgets.QComboBox(self), QtWidgets.QComboBox(self),
                        QtWidgets.QComboBox(self),
                        QtWidgets.QComboBox(self), QtWidgets.QComboBox(self), QtWidgets.QComboBox(self),
                        QtWidgets.QComboBox(self),
                        QtWidgets.QComboBox(self), QtWidgets.QComboBox(self)]
        for i in range(10):
            self.answers[i].move(250, 60 + 40 * i)
            self.addAnswer(self.answers[i])

        self.answers[0].currentIndexChanged[int].connect(lambda: comboChanged(self, self.answers[0].currentIndex()))
        self.answers[1].currentIndexChanged[int].connect(lambda: comboChanged(self, self.answers[1].currentIndex()))
        self.answers[2].currentIndexChanged[int].connect(lambda: comboChanged(self, self.answers[2].currentIndex()))
        self.answers[3].currentIndexChanged[int].connect(lambda: comboChanged(self, self.answers[3].currentIndex()))
        self.answers[4].currentIndexChanged[int].connect(lambda: comboChanged(self, self.answers[4].currentIndex()))
        self.answers[5].currentIndexChanged[int].connect(lambda: comboChanged(self, self.answers[5].currentIndex()))
        self.answers[6].currentIndexChanged[int].connect(lambda: comboChanged(self, self.answers[6].currentIndex()))
        self.answers[7].currentIndexChanged[int].connect(lambda: comboChanged(self, self.answers[7].currentIndex()))
        self.answers[8].currentIndexChanged[int].connect(lambda: comboChanged(self, self.answers[8].currentIndex()))
        self.answers[9].currentIndexChanged[int].connect(lambda: comboChanged(self, self.answers[9].currentIndex()))

        self.save = QtWidgets.QPushButton(self)
        self.save.move(40, 460)
        self.save.setFixedWidth(200)
        self.save.setText("Сохранить класс")
        self.save.clicked.connect(self.saveAnswer)

    def addAnswer(self, answer):
        for specification in specifications.specifications:
            if specification.value != specifications.specifications.BARD.value:
                answer.addItem(specification.value)
        answer.setCurrentIndex(0)

    def saveAnswer(self):
        dbHelper.addItem(self.className.text(), self.answers[0].currentText(), self.answers[1].currentText(),
                         self.answers[2].currentText(), self.answers[3].currentText(), self.answers[4].currentText(),
                         self.answers[5].currentText(), self.answers[6].currentText(), self.answers[7].currentText(),
                         self.answers[8].currentText(), self.answers[9].currentText())
        self.parentWindow.updateTable()
        for i in range(10):
            self.addAnswer(self.answers[i])
        self.hide()

    def updateQComboBox(self):
        self.className.clear()
        for answer in self.answers:
            answer.setCurrentIndex(0)
            for i in range(18):
                answer.model().item(i).setEnabled(True)


class DeleteClassWindow(QtWidgets.QWidget):
    def __init__(self, parent):
        super(DeleteClassWindow, self).__init__()
        self.parentWindow = parent
        self.setWindowTitle("Удаление класса")
        self.move(600, 350)
        self.setFixedSize(350, 130)

        self.deleteText = QtWidgets.QLabel(self)
        self.deleteText.setText("Выберите класс для удаления:")
        self.deleteText.move(40, 20)
        self.deleteText.setFixedWidth(250)

        self.answer = QtWidgets.QComboBox(self)
        self.answer.move(40, 50)

        self.delete = QtWidgets.QPushButton(self)
        self.delete.move(40, 80)
        self.delete.setFixedWidth(200)
        self.delete.setText("Удалить класс")
        self.delete.clicked.connect(self.deleteClass)

    def updateQComboBox(self):
        self.answer.clear()
        rows = dbHelper.getAll()
        for i in range(len(rows)):
            self.answer.addItem(rows[i][0])
        self.answer.setCurrentIndex(0)

    def deleteClass(self):
        dbHelper.deleteItem(self.answer.currentText())
        self.parentWindow.updateTable()
        self.hide()


class EditClassWindow(QtWidgets.QWidget):
    def __init__(self, parent):
        super(EditClassWindow, self).__init__()
        self.parentWindow = parent
        self.setWindowTitle("Редактирование таблицы")
        self.move(600, 350)
        self.setFixedSize(500, 550)

        self.editDescription = QtWidgets.QLabel(self)
        self.editDescription.setText("Выберите класс для редактирования:")
        self.editDescription.move(40, 20)
        self.editDescription.setFixedWidth(250)
        self.editClass = QtWidgets.QComboBox(self)
        self.editClass.move(300, 20)

        rows = dbHelper.getAll()
        for i in range(len(rows)):
            self.editClass.addItem(rows[i][0])
        self.editClass.setCurrentIndex(0)

        self.newSpecificationsText = QtWidgets.QLabel(self)
        self.newSpecificationsText.setText("Выберите новые характеристики:")
        self.newSpecificationsText.move(40, 60)
        self.newSpecificationsText.setFixedWidth(250)

        self.score = [QtWidgets.QLabel(self), QtWidgets.QLabel(self), QtWidgets.QLabel(self), QtWidgets.QLabel(self),
                      QtWidgets.QLabel(self), QtWidgets.QLabel(self), QtWidgets.QLabel(self), QtWidgets.QLabel(self),
                      QtWidgets.QLabel(self), QtWidgets.QLabel(self)]
        for i in range(10):
            self.score[i].setText("Характеристика для " + str(i + 1) + " баллов:")
            self.score[i].move(40, 100 + 40 * i)
            self.score[i].setFixedWidth(250)
        self.score[0].setText("Характеристика для 1 балла:")

        self.answers = [QtWidgets.QComboBox(self), QtWidgets.QComboBox(self), QtWidgets.QComboBox(self),
                        QtWidgets.QComboBox(self),
                        QtWidgets.QComboBox(self), QtWidgets.QComboBox(self), QtWidgets.QComboBox(self),
                        QtWidgets.QComboBox(self),
                        QtWidgets.QComboBox(self), QtWidgets.QComboBox(self)]
        for i in range(10):
            self.answers[i].move(250, 100 + 40 * i)
            self.addAnswer(self.answers[i])

        self.answers[0].currentIndexChanged[int].connect(lambda: comboChanged(self, self.answers[0].currentIndex()))
        self.answers[0].currentIndexChanged[int].connect(lambda: comboChanged(self, self.answers[0].currentIndex()))
        self.answers[1].currentIndexChanged[int].connect(lambda: comboChanged(self, self.answers[1].currentIndex()))
        self.answers[2].currentIndexChanged[int].connect(lambda: comboChanged(self, self.answers[2].currentIndex()))
        self.answers[3].currentIndexChanged[int].connect(lambda: comboChanged(self, self.answers[3].currentIndex()))
        self.answers[4].currentIndexChanged[int].connect(lambda: comboChanged(self, self.answers[4].currentIndex()))
        self.answers[5].currentIndexChanged[int].connect(lambda: comboChanged(self, self.answers[5].currentIndex()))
        self.answers[6].currentIndexChanged[int].connect(lambda: comboChanged(self, self.answers[6].currentIndex()))
        self.answers[7].currentIndexChanged[int].connect(lambda: comboChanged(self, self.answers[7].currentIndex()))
        self.answers[8].currentIndexChanged[int].connect(lambda: comboChanged(self, self.answers[8].currentIndex()))
        self.answers[9].currentIndexChanged[int].connect(lambda: comboChanged(self, self.answers[9].currentIndex()))

        self.save = QtWidgets.QPushButton(self)
        self.save.move(40, 500)
        self.save.setFixedWidth(200)
        self.save.setText("Сохранить класс")
        self.save.clicked.connect(self.saveAnswer)

    def comboChanged(self, answer):
        if answer == 0:
            return
        selected = []
        for i in range(10):
            if self.answers[i].currentIndex() != 0:
                selected.insert(len(selected), self.answers[i].currentIndex())
        for i in range(10):
            for j in range(18):
                if isSelectedHas(selected, j):
                    self.answers[i].model().item(j).setEnabled(False)
                else:
                    self.answers[i].model().item(j).setEnabled(True)

    def addAnswer(self, answer):
        for specification in specifications.specifications:
            if specification.value != specifications.specifications.BARD.value:
                answer.addItem(specification.value)
        answer.setCurrentIndex(0)

    def saveAnswer(self):
        dbHelper.updateItem(self.answers[0].currentText(), self.answers[1].currentText(), self.answers[2].currentText(),
                            self.answers[3].currentText(), self.answers[4].currentText(), self.answers[5].currentText(),
                            self.answers[6].currentText(), self.answers[7].currentText(), self.answers[8].currentText(),
                            self.answers[9].currentText(), self.editClass.currentText())
        for answer in self.answers:
            answer.setCurrentIndex(0)
        self.parentWindow.updateTable()
        self.hide()

    def updateQComboBox(self):
        self.editClass.clear()
        rows = dbHelper.getAll()
        for i in range(len(rows)):
            self.editClass.addItem(rows[i][0])
        self.editClass.setCurrentIndex(0)
        for answer in self.answers:
            answer.setCurrentIndex(0)
            for i in range(18):
                answer.model().item(i).setEnabled(True)


def application():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()
dbHelper.close()

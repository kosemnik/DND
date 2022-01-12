from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys
import sqlite3
from enum import Enum
from PyQt5.QtCore import Qt
from collections import OrderedDict


class Specifications(Enum):
    NONE = "-"
    ATHLETICS = "Атлетика"
    ACROBATICS = "Акробатика"
    HANDSLEIGHT = "Ловкость рук"
    STEALTH = "Скрытность"
    MAGIC = "Магия"
    HISTORY = "История"
    INVESTIGATION = "Расследование"
    NATURE = "Природа"
    RELIGION = "Религия"
    ANIMALSTREATMENT = "Обращение с животными"
    INSIGHT = "Проницательность"
    MEDICINE = "Медицина"
    PERCEPTION = "Восприятие"
    SURVIVAL = "Выживание"
    CHEATNG = "Обман"
    BULLYING = "Запугивание"
    PERFORMANCE = "Выступление"
    PERSUASION = "Убеждение"
    BARD = "Бард"


specifications = Specifications


def getSpecification(specification):
    if specification == "-":
        return specifications.NONE
    if specification == "Атлетика":
        return specifications.ATHLETICS
    if specification == "Акробатика":
        return specifications.ACROBATICS
    if specification == "Ловкость рук":
        return specifications.HANDSLEIGHT
    if specification == "Скрытность":
        return specifications.STEALTH
    if specification == "Магия":
        return specifications.MAGIC
    if specification == "История":
        return specifications.HISTORY
    if specification == "Расследование":
        return specifications.INVESTIGATION
    if specification == "Природа":
        return specifications.NATURE
    if specification == "Религия":
        return specifications.RELIGION
    if specification == "Обращение с животными":
        return specifications.ANIMALSTREATMENT
    if specification == "Проницательность":
        return specifications.INSIGHT
    if specification == "Медицина":
        return specifications.MEDICINE
    if specification == "Восприятие":
        return specifications.PERCEPTION
    if specification == "Выживание":
        return specifications.SURVIVAL
    if specification == "Обман":
        return specifications.CHEATNG
    if specification == "Запугивание":
        return specifications.BULLYING
    if specification == "Выступление":
        return specifications.PERFORMANCE
    return specifications.PERSUASION


db = sqlite3.connect('Classes.db')
cursor = db.cursor()

questions = ["В путешествии Вы встретили раненого монстра. Ваша первая мысль?",
             "На Ваших глазах невинного осудили,  обязав выплатить огромный штраф. Ваши действия?",
             "Вам поручили достать некий предмет у человека, что усердно не хочет его отдавать. "
             "\nТак же упомянули, что не стоит применять насилие. Ваши действия?",
             "Как-то идя по улице, Вы нашли кошелек с приличной суммой денег и неподалеку от него увидели девушку, "
             "\nкоторая суетливо просматривала аллею в поисках чего-то. Что Вы сделаете?",
             "Проходя по ночным улицам города мимо одного из переулков, Вы замечаете как несколько "
             "\nбандитов пристают к парнишке. Что Вы будете делать?",
             "Двигаясь по лесу, Вы обнаруживаете себя окруженным большой стаей диких и крупных волков. "
             "\nКак лучше с ними сражаться?"]

answer1 = [["Я помогу бедному созданию восстановиться.", specifications.MEDICINE],
           ["Раненый? Это значит, что сокровища рядом будет легче забрать!", specifications.INVESTIGATION],
           ["Попытаюсь найти следы того, кто его ранил, и выследить его.", specifications.SURVIVAL],
           ["Отлично! Из его частей можно сделать ценные ингредиенты.", specifications.NATURE],
           ["Возможно, сейчас это существо будет более уязвимым к моим заклинаниям.", specifications.MAGIC],
           ["Лучше буду держаться подальше, это может быть ловушка.", specifications.PERCEPTION]]

answer2 = [["Дам денег в долг.", specifications.INSIGHT],
           ["Подлечу на своём скакуне, перекину бедолагу через седло и "
           "\nгалопом унесусь в закат. Пусть попробуют догонят!", specifications.ANIMALSTREATMENT],
           ["Предложу подать апелляцию и свою помощь в ее подготовке.", specifications.HISTORY],
           ["Невиновность еще нужно доказать. Впрочем, разберусь по ситуации.", specifications.INVESTIGATION],
           ["Попробую найти компромисс.", specifications.PERSUASION],
           ["Прокляну.", specifications.MAGIC]]

answer3 = [["Попытаюсь уговорить отдать предмет, если не получится, то сворую его.", specifications.HANDSLEIGHT],
           ["Проберусь в его дом, незаметно возьму предмет, а затем также "
           "\nнезаметно верну, когда потребность в нём отпадёт.", specifications.STEALTH],
           ["Угощу его расслабляющим чаем из трав, которые собрал недавно, "
           "\nв надежде, что теперь с ним будет проще договориться.", specifications.NATURE],
           ["Вызову его на дуэль. Проигравший отдает ценный предмет.", specifications.ATHLETICS],
           ["Так или иначе решу вопрос дипломатическим способом.", specifications.PERSUASION],
           ["Намекну, что отдать предмет - самый безобидный вариант для него и его семьи.", specifications.BULLYING]]

answer4 = [["Спрошу у неё не потеряла ли она что-то.", specifications.INSIGHT],
           ["Прикарманю найденное добро и благополучно покину аллею.", specifications.HANDSLEIGHT],
           ["Подбегу к ней, торжественно вручу потерянную вещь и, поцеловав её руку, приглашу на свидание!", specifications.BARD],
           ["Возьму вознаграждение за находку, оставшуюся сумму верну девушке.", specifications.CHEATNG],
           ["Вспомню догматы своей религии и поступлю в соответствии с ними.", specifications.RELIGION],
           ["Известный мне фамильный герб выдает в девушке дворянку. "
           "\nЭта сумма малая потеря для неё, пусть деньги достанутся тому, кому они нужнее.", specifications.HISTORY]]

answer5 = [["Буду держаться неподалеку, чтобы вовремя оказать помощь пострадавшим.", specifications.MEDICINE],
           ["Вмешаюсь в разговор со словами: 'Что за шум, а драки нет? Сейчас устрою'", specifications.ATHLETICS],
           ["Скроюсь с того места, вдруг и меня привлекут?", specifications.STEALTH],
           ["Отвлеку бандитов на себя. В паркуре мне нет равных!", specifications.ACROBATICS],
           ["Прикинусь одним из них и прибегу с криками: 'Пацаны, шухер!'", specifications.CHEATNG],
           ["С угрожающим видом встану между парнем и бандитами и посмотрю хватит ли теперь у них смелости.", specifications.BULLYING]]

answer6 = [["Попробую расположить их к себе, у меня как раз осталась куриная ножка с обеда.", specifications.ANIMALSTREATMENT],
           ["Рыба гниет с головы, так что сначала убью вожака и самых крупных, а мелочь сама разбежится.", specifications.SURVIVAL],
           ["Сделаю через них сальто, выбравшись из окружения, взберусь на дерево и сбегу, прыгая по кронам.", specifications.ACROBATICS],
           ["Я был готов к этому! Теперь у зверюг нет шансов!", specifications.PERCEPTION],
           ["Выход есть всегда и, возможно, в этот раз мне на него укажет мой покровитель.", specifications.RELIGION],
           ["Воспользуюсь огненной магией, чтобы напугать их, все животные боятся огня.", specifications.MAGIC]]

answers = [answer1, answer2, answer3, answer4, answer5, answer6]


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("Экспертная система. "
                            "Создание класса в настольной игре D&D")
        self.setGeometry(300, 200, 1000, 700)
        self.addClassWindow = AddClassWindow(self)
        self.deleteClassWindow = DeleteClassWindow(self)
        self.editclassWindow = EditClassWindow(self)
        self.clientAnswers = [specifications.NONE, specifications.NONE, specifications.NONE,
                        specifications.NONE, specifications.NONE, specifications.NONE]

        self.description = QtWidgets.QLabel(self)
        self.description.move(275, 250)
        self.description.setFixedWidth(500)
        self.description.setText("Эта программа преназначена для создания класса"
                                 "в настольной игре D&D")

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
        cursor.execute("SELECT * FROM `Классы`")
        rows = cursor.fetchall()
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
            self.answers[index].setText(answers[0][index][0])
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
        self.clientAnswers[self.questionNumber] = answers[self.questionNumber][btnNumber][1]
        self.questionNumber += 1
        if self.questionNumber >= 6:
            self.getResult()
            return
        self.question.setText(questions[self.questionNumber])
        for index in range(6):
            self.answers[index].setText(answers[self.questionNumber][index][0])
        self.count.setText(str(self.questionNumber + 1) + "/6")

    def getResult(self):
        self.toMainMenu.show()
        self.question.hide()
        self.count.hide()
        for index in range(6):
            self.answers[index].hide()

        results = {}
        info = "\n"
        if self.clientAnswers[3] == specifications.BARD:
            results["Бард"] = 1000
            info = "Бард: вы выбрали в 4 вопросе ответ для класса Бард\n\n"
            self.clientAnswers[3] = specifications.NONE
        else:
            results["Бард"] = 0
        cursor.execute("SELECT * FROM `Классы`")
        rows = cursor.fetchall()
        for row in rows:
            if row[0] == "Бард":
                continue
            count = 0
            for i in range(1, len(row)):
                for j in range(len(self.clientAnswers)):
                    if self.clientAnswers[j] != specifications.NONE and self.clientAnswers[j] == getSpecification(row[i]):
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
                if key == row[0]:
                    if orDict[row[0]] == 0:
                        continue
                    info = info + row[0] + ", набрано баллов: " + str(orDict[row[0]]) + "\n"
                    for index in range(6):
                        count = 0
                        for i in range(1, len(row)):
                            if self.clientAnswers[index] != specifications.NONE and self.clientAnswers[index] == getSpecification(row[i]):
                                count += i
                        info = info + "Вопрос " + str(index + 1) + ": " + self.clientAnswers[index].value + " +" + str(
                            count) + "\n"
                    info = info + "\n"
                    classCount += 1

        self.info.setText(info)
        self.result.setText(resultStr)
        self.result.show()
        self.info.setFixedHeight(16*(3 + classCount*8))
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
        cursor.execute("SELECT * FROM [Классы]")
        rows = cursor.fetchall()
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
        self.setGeometry(600, 350, 500, 510)

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
            self.score[i].move(40, 60 + 40*i)
            self.score[i].setFixedWidth(250)
        self.score[0].setText("Характеристика для 1 балла:")

        self.answers = [QtWidgets.QComboBox(self), QtWidgets.QComboBox(self), QtWidgets.QComboBox(self), QtWidgets.QComboBox(self),
                        QtWidgets.QComboBox(self), QtWidgets.QComboBox(self), QtWidgets.QComboBox(self), QtWidgets.QComboBox(self),
                        QtWidgets.QComboBox(self), QtWidgets.QComboBox(self)]
        for i in range (10):
            self.answers[i].move(250, 60 + 40*i)
            self.addAnswer(self.answers[i])

        self.save = QtWidgets.QPushButton(self)
        self.save.move(40, 460)
        self.save.setFixedWidth(200)
        self.save.setText("Сохранить класс")
        self.save.clicked.connect(self.saveAnswer)

    def addAnswer(self, answer):
        for specification in specifications:
            if specification.value != Specifications.BARD.value:
                answer.addItem(specification.value)
        answer.setCurrentIndex(0)

    def saveAnswer(self):
        className = self.className.text()
        answer1 = self.answers[0].currentText()
        answer2 = self.answers[1].currentText()
        answer3 = self.answers[2].currentText()
        answer4 = self.answers[3].currentText()
        answer5 = self.answers[4].currentText()
        answer6 = self.answers[5].currentText()
        answer7 = self.answers[6].currentText()
        answer8 = self.answers[7].currentText()
        answer9 = self.answers[8].currentText()
        answer10 = self.answers[9].currentText()
        values = (className, answer1, answer2, answer3, answer4, answer5,
                  answer6, answer7, answer8, answer9, answer10)
        sqlite_insert_query = """INSERT INTO [Классы]
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""
        cursor.execute(sqlite_insert_query, values)
        db.commit()
        self.parentWindow.updateTable()
        for i in range(10):
            self.addAnswer(self.answers[i])
        self.hide()

    def updateQComboBox(self):
        self.className.clear()
        for answer in self.answers:
            answer.setCurrentIndex(0)


class DeleteClassWindow(QtWidgets.QWidget):
    def __init__(self, parent):
        super(DeleteClassWindow, self).__init__()
        self.parentWindow = parent
        self.setWindowTitle("Удаление класса")
        self.setGeometry(600, 350, 350, 130)

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
        cursor.execute("SELECT * FROM `Классы`")
        rows = cursor.fetchall()
        for i in range(len(rows)):
            self.answer.addItem(rows[i][0])
        self.answer.setCurrentIndex(0)

    def deleteClass(self):
        cursor.execute("""DELETE FROM [Классы] WHERE Class = ?""", (self.answer.currentText(),))
        db.commit()
        self.parentWindow.updateTable()
        self.hide()


class EditClassWindow(QtWidgets.QWidget):
    def __init__(self, parent):
        super(EditClassWindow, self).__init__()
        self.parentWindow = parent
        self.setWindowTitle("Редактирование таблицы")
        self.setGeometry(600, 350, 500, 550)

        self.editDescription = QtWidgets.QLabel(self)
        self.editDescription.setText("Выберите класс для редактирования:")
        self.editDescription.move(40, 20)
        self.editDescription.setFixedWidth(250)
        self.editClass = QtWidgets.QComboBox(self)
        self.editClass.move(300, 20)
        cursor.execute("SELECT * FROM [Классы]")
        rows = cursor.fetchall()
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

        self.answers = [QtWidgets.QComboBox(self), QtWidgets.QComboBox(self), QtWidgets.QComboBox(self), QtWidgets.QComboBox(self),
                        QtWidgets.QComboBox(self), QtWidgets.QComboBox(self), QtWidgets.QComboBox(self), QtWidgets.QComboBox(self),
                        QtWidgets.QComboBox(self), QtWidgets.QComboBox(self)]
        for i in range(10):
            self.answers[i].move(250, 100 + 40 * i)
            self.addAnswer(self.answers[i])

        self.save = QtWidgets.QPushButton(self)
        self.save.move(40, 500)
        self.save.setFixedWidth(200)
        self.save.setText("Сохранить класс")
        self.save.clicked.connect(self.saveAnswer)

    def addAnswer(self, answer):
        for specification in specifications:
            if specification.value != Specifications.BARD.value:
                answer.addItem(specification.value)
        answer.setCurrentIndex(0)

    def saveAnswer(self):
        className = self.editClass.currentText()
        answer1 = self.answers[0].currentText()
        answer2 = self.answers[1].currentText()
        answer3 = self.answers[2].currentText()
        answer4 = self.answers[3].currentText()
        answer5 = self.answers[4].currentText()
        answer6 = self.answers[5].currentText()
        answer7 = self.answers[6].currentText()
        answer8 = self.answers[7].currentText()
        answer9 = self.answers[8].currentText()
        answer10 = self.answers[9].currentText()
        cursor.execute("""UPDATE [Классы] SET [1 score] = ?, [2 score] = ?, [3 score] = ?, [4 score] = ?, 
        [5 score] = ?, [6 score] = ?, [7 score] = ?, [8 score] = ?, [9 score] = ?, [10 score] = ? WHERE Class = ?""",
                       (answer1, answer2, answer3, answer4, answer5, answer6, answer7, answer8, answer9, answer10, className))
        db.commit()
        for answer in self.answers:
            answer.setCurrentIndex(0)
        self.parentWindow.updateTable()
        self.hide()

    def updateQComboBox(self):
        self.editClass.clear()
        cursor.execute("SELECT * FROM `Классы`")
        rows = cursor.fetchall()
        for i in range(len(rows)):
            self.editClass.addItem(rows[i][0])
        self.editClass.setCurrentIndex(0)
        for answer in self.answers:
            answer.setCurrentIndex(0)


def application():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()
db.close()

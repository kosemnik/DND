from enum import Enum


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
    PERSUASION = "Убеждение"
    BARD = "Бард"


class Specification:
    def __init__(self):
        self.specifications = Specifications

    def getSpecification(self, specification):
        if specification == "-":
            return self.specifications.NONE
        if specification == "Атлетика":
            return self.specifications.ATHLETICS
        if specification == "Акробатика":
            return self.specifications.ACROBATICS
        if specification == "Ловкость рук":
            return self.specifications.HANDSLEIGHT
        if specification == "Скрытность":
            return self.specifications.STEALTH
        if specification == "Магия":
            return self.specifications.MAGIC
        if specification == "История":
            return self.specifications.HISTORY
        if specification == "Расследование":
            return self.specifications.INVESTIGATION
        if specification == "Природа":
            return self.specifications.NATURE
        if specification == "Религия":
            return self.specifications.RELIGION
        if specification == "Обращение с животными":
            return self.specifications.ANIMALSTREATMENT
        if specification == "Проницательность":
            return self.specifications.INSIGHT
        if specification == "Медицина":
            return self.specifications.MEDICINE
        if specification == "Восприятие":
            return self.specifications.PERCEPTION
        if specification == "Выживание":
            return self.specifications.SURVIVAL
        if specification == "Обман":
            return self.specifications.CHEATNG
        if specification == "Запугивание":
            return self.specifications.BULLYING
        return self.specifications.PERSUASION

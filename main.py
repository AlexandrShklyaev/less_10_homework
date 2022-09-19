import json
import random


class Question:
    """    Question(text:str, answer:str, difficult:int)    """

    def __init__(self, text: str, answer: str, difficult: int) -> None:
        self.text = text
        self.difficult = difficult
        self.answer = answer
        self.is_getting = False
        self.user_answer: str = ''
        self.total: int = int(self.difficult) * 10  # в задании просили вычислить здесь

    def append_answer(self, answer: str) -> None:
        """"""
        self.user_answer = answer

    def get_points(self) -> int:
        return self.total

    def is_correct(self) -> bool:
        return self.answer == self.user_answer

    def build_question(self, ind: int) -> str:  # дополнитель передаю ind - номер вопроса
        return f"Вопрос #{ind}: {self.text}\n Сложность: {self.difficult}/5"

    def build_feedback(self) -> str:  # объединил методы фидбека в один
        if self.answer == self.user_answer:
            return f"Ответ верный, получено {self.total} баллов"
        return f"Ответ неверный, верный ответ {self.answer}"


def load_questions() -> list:
    """  Функция возвращает данные из файла question.json  ->:return: list   """
    with open("question.json", encoding="utf-8") as file:
        return json.load(file)


def get_questions() -> list:
    """  Функция формирует новый список объектов класса Question ->:return: list   """
    questions = []
    dict_questions = load_questions()
    for each in dict_questions:
        new_question = Question(each["q"], each["a"], int(each["d"]))
        questions.append(new_question)
    return questions


def get_total(questions: list) -> None:
    """ Подсчёт и вывод статистики """
    total = 0
    count = 0
    for question in questions:
        if question.is_correct():
            total += question.get_points()
            count += 1
    print("-" * 20)
    print("Вот и все!")
    print(f"Отвечено {count} вопроса из {len(questions)}")
    print(f"Набранно {total} баллов")


def main() -> None:
    questions = get_questions()  # получим списов объектов типа Question
    random.shuffle(questions)  # перемешаем вопросы
    ind = 0  # номер вопроса (опционально)
    for question in questions:
        ind += 1
        print(question.build_question(ind))  # выведем вопрос и баллы за него
        question.append_answer(input("введите ваш ответ: "))  # добавим в текущий объект ответ пользователя
        print(question.build_feedback())  # получим и выведем результат
        print("=" * 40)
    get_total(questions)  # выведем общую статистику


if __name__ == '__main__':
    main()

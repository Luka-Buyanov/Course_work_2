from abc import ABC, abstractmethod
from typing import Any

import requests


class BaseClass(ABC):
    """Абстрактный класс для работы с API от hh.ru"""

    @abstractmethod
    def load_vacancies(self, *args: Any, **kwargs: Any) -> Any:
        """Метод реализующий вызов API и запрос вакансий"""

        pass


class HH(BaseClass):
    """Класс получает информацию о вакансиях с сайта HeadHunter"""

    def __init__(self) -> None:
        """Инициализатор класса"""

        self.__url = "https://api.hh.ru/vacancies"
        self.__headers = {"User-Agent": "HH-User-Agent"}
        self.__params = {"text": "", "page": 0, "per_page": 100}
        self.__vacancies = []  # конечный список, в который складываются вакансии list[dict]

    def load_vacancies(self, name: str) -> Any:
        """Метод загрузки данных вакансий из API сервиса"""

        self.__params["text"] = name
        while self.__params.get("page") != 20:
            response = requests.get(self.__url, headers=self.__headers, params=self.__params)
            vacancies = response.json()["items"]
            self.__vacancies.extend(vacancies)
            self.__params["page"] += 1

        return self.__vacancies


class Vacancy:
    __list_vacancies: list = []
    __slots__ = ("__name", "__url", "__text", "__salary")

    def __init__(
        self,
        name: str = "Нет значения",
        url: str = "Нет значения",
        salary: str | None | dict = "Нет значения",
        text: str = "Нет значения",
    ):
        self.__name = name
        self.__url = url
        self.__salary = salary
        self.__text = text

        vacancies = {"name": self.__name, "url": self.__url, "salary": self.__salary, "text": self.__text}
        self.__list_vacancies.append(vacancies)

    @staticmethod
    def __validate(salary) -> dict:
        """Метод валидации зарплаты"""
        if salary is None:
            return {"from": 0, "to": 0}
        if isinstance(salary, str):
            # Пытаемся разделить строку зарплаты, например, "100000 - 150000"
            try:
                from_salary, to_salary = map(int, salary.split(" - "))
                return {"from": from_salary, "to": to_salary}
            except ValueError:
                # Если деление не удалось, возвращаем значения по умолчанию
                return {"from": 0, "to": 0}
        elif isinstance(salary, dict):
            # Убеждаемся, что ключи 'from' и 'to' присутствуют
            from_salary = salary.get("from", 0)
            to_salary = salary.get("to", 0)
            return {"from": from_salary, "to": to_salary}
        else:
            # Если тип данных неожиданный, возвращаем значения по умолчанию
            return {"from": 0, "to": 0}

    def __compare(self, other):

        self_salary_to = self.__salary.get("to", 0)
        other_salary_to = other.__salary.get("to", 0)
        self_salary_from = self.__salary.get("from", 0)
        other_salary_from = other.__salary.get("from", 0)
        return self_salary_to >= other_salary_to, self_salary_from >= other_salary_from

    @classmethod
    def cast_to_object_list(cls, list_vacancies):
        """Метод добавления вакансий из списка вакансий"""
        for vacancy_data in list_vacancies:
            # Валидируем зарплату
            salary = cls.__validate(vacancy_data.get("salary"))
            text = vacancy_data.get("text", "Не указан")
            # Если snippet является словарем, извлекаем требование
            if isinstance(text, dict):
                text = text.get("requirement", "")
            # Создаем экземпляр вакансии
            cls(
                name=vacancy_data.get("name", "Не указан"),
                url=vacancy_data.get("url", "Не указан"),
                salary=salary,
                text=text,
            )
        return cls.__list_vacancies

    @classmethod
    def filter_salary(cls, from_salary: int = 0, to_salary: int = 9999999):

        for vacancy in cls.__list_vacancies:
            if vacancy["salary"].get("from", 0) >= from_salary and vacancy["salary"].get("to", 0) <= to_salary:
                print(vacancy)

    @classmethod
    def list_of_vacancy(cls):

        return cls.__list_vacancies

    @classmethod
    def clear_list(cls):
        cls.__list_vacancies = []

    @property
    def name(self):
        return self.__name

    @property
    def url(self):
        return self.__url

    @property
    def salary(self):
        return self.__salary

    @property
    def text(self):
        return self.__text

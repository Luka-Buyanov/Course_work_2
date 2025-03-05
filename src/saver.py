import json
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any, Dict, List

from src.classes import Vacancy


class VacancyStorage(ABC):
    """Абстрактный класс для работы с файлами, который позволит сохранять вакансии, читать их и удалять.
    Реализуем его для работы с JSON."""

    @abstractmethod
    def add_vacancy(self, vacancies: List[Vacancy]):
        pass

    @abstractmethod
    def get_vacancy(self, criteria: Dict):
        pass

    @abstractmethod
    def delete_vacancy(self, criteria: Dict):
        pass


class JSONSaver(VacancyStorage):
    def __init__(self, file_path: str = "data/vacancies.json") -> None:
        self.__file_path = Path(file_path)
        if not self.__file_path.exists():
            self._save_data([])  # Создаём пустой JSON, если файла нет

    def _load_data(self) -> List[Dict]:
        """Приватный метод для загрузки данных из JSON-файла."""
        try:
            with open(self.__file_path, "r", encoding="utf-8") as file:
                content = file.read().strip()
                return json.loads(content) if content else []  # Загружаем только если не пусто
        except FileNotFoundError:
            return []
        except Exception as e:
            print(f"Ошибка при чтении файла: {e}")  # Обработка других возможных ошибок
            return []  # Возвращаем пустой список

    def _save_data(self, data: List[Any]) -> None:
        """Приватный метод для сохранения данных в JSON-файл."""
        try:
            with open(self.__file_path, "w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Ошибка при сохранении данных в файл: {e}")

    def add_vacancy(self, vacancies: List[Vacancy]) -> None:
        """Добавляет список вакансий в JSON - файл, избегая дублирования."""
        data = self._load_data()
        for vacancy in vacancies:
            if type(vacancy) == json:
                vacancy_dict = vacancy
            else:
                vacancy_dict = vacancy.to_dict()
            if vacancy_dict not in data:  # Проверяем, нет ли уже такой вакансии
                data.append(vacancy_dict)  # Добавляем вакансию, если её нет в списке
        self._save_data(data)

    def get_vacancy(self, criteria: Dict) -> List[Dict]:
        """Возвращает список вакансий, которые соответствуют заданным критериям."""
        data = self._load_data()
        result = []
        for item in data:
            if all(item.get(key) == value for key, value in criteria.items()):
                result.append(item)
        return result

    def delete_vacancy(self, criteria: Dict) -> None:
        """Удаляет вакансии, соответствующие заданным критериям, из JSON-файла."""
        data = self._load_data()
        data = [item for item in data if not all(item.get(key) == value for key, value in criteria.items())]
        self._save_data(data)

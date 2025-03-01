import json

from src.saver import JSONSaver


def test_add_vacancies(temp_json_file, vacancy_1, vacancy_2):
    """Тестирование метода add_vacancies класса JSONVSaver.  Проверяет, что после добавления вакансий в
    JSON-файл, количество записей соответствует добавленным вакансиям и данные корректно сохраняются."""
    storage = JSONSaver(temp_json_file)
    storage.add_vacancy([vacancy_1, vacancy_2])

    with open(temp_json_file, "r", encoding="utf-8") as file:
        data = json.load(file)

    assert len(data) == 2
    assert data[0]["name"] == vacancy_1.name
    assert data[1]["name"] == vacancy_2.name


def test_get_vacancies(temp_json_file, vacancy_1, vacancy_2):
    """Тестирование метода get_vacancies класса JSONVSaver. Проверяет, что метод возвращает корректную вакансию
    по заданным критериям."""
    storage = JSONSaver(temp_json_file)
    storage.add_vacancy([vacancy_1, vacancy_2])

    result = storage.get_vacancy({"name": "Python Developer"})
    assert len(result) == 2
    assert result[0]["name"] == "Python Developer"


def test_delete_vacancies(temp_json_file, vacancy_1, vacancy_2):
    """Тестирование метода delete_vacancies класса JSONVSaver. Проверяет, что
    после удаления вакансий файл остаётся пустым."""
    storage = JSONSaver(temp_json_file)
    storage.add_vacancy([vacancy_1, vacancy_2])

    storage.delete_vacancy({"name": "Python Developer"})
    data = storage._load_data()

    assert len(data) == 0

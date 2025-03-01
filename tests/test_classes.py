from unittest.mock import patch

from src.classes import HH, Vacancy


@patch("requests.get")
def test_head_hunter_api_requests(test_requests_api):
    """Тест проверяющий корректность создания объекта класса HH"""

    obj_api = HH()
    assert type(obj_api) is HH


def test_init_vacancy(test_add_vacancy):
    """Тест проверяющий корректность добавления вакансии"""

    assert test_add_vacancy.name == "Python Developer"
    assert test_add_vacancy.url == "<https://hh.ru/vacancy/123456>"
    assert test_add_vacancy.salary == {"from": 100000, "to": 150000}
    assert test_add_vacancy.text == "Требования: опыт работы от 3 лет..."

    Vacancy().clear_list()


def test_list_vacancies(test_add_vacancy, test_result_filtered_vacancy):
    """Тест проверяющий корректность фильтровки вакансий"""

    assert test_add_vacancy.list_of_vacancy()[0] == test_result_filtered_vacancy

    Vacancy().clear_list()


def test_filtered_salary_vacancy(capsys, vacancy_1, vacancy_2, test_result_filtered_vacancy):
    """Тест проверяющий корректность фильтрации по зарплате"""

    assert len(Vacancy.list_of_vacancy()) == 2

    Vacancy.filter_salary(0, 150000)
    message = capsys.readouterr()
    assert message.out.strip() == f"{test_result_filtered_vacancy}"

    Vacancy().clear_list()


def test_ge_vacancy(capsys, vacancy_1, vacancy_2):
    """Тест проверяющий корректность сравнения по верхнему порогу зарплаты"""

    print(Vacancy.__ge__(vacancy_2, vacancy_1))
    message = capsys.readouterr()
    assert message.out.strip() == "True"

    Vacancy().clear_list()


def test_cast_to_object_list(test_cast_to_object_vacancy, test_cast_to_add_vacancy):
    """Тест проверяющий корректность добавления вакансий из списка"""

    Vacancy().clear_list()
    Vacancy.cast_to_object_list(test_cast_to_object_vacancy)
    assert Vacancy.list_of_vacancy() == test_cast_to_add_vacancy

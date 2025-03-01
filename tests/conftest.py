import os

import pytest

from src.classes import Vacancy


@pytest.fixture
def test_requests_api():
    return [
        {
            "id": "91773507",
            "premium": "false",
            "name": "Разработчик JavaScript / Разработчик на платформе",
            "department": "null",
            "has_test": "false",
            "response_letter_required": "false",
            "area": {"id": "4", "name": "Новосибирск", "url": "https://api.hh.ru/areas/4"},
            "salary": "null",
            "type": {"id": "open", "name": "Открытая"},
            "address": {
                "city": "Новосибирск",
                "street": "Октябрьская магистраль",
                "building": "4",
                "lat": 55.022567,
                "lng": 82.930086,
                "description": "null",
                "raw": "Новосибирск, Октябрьская магистраль, 4",
                "metro": {
                    "station_name": "Октябрьская",
                    "line_name": "Ленинская",
                    "station_id": "52.298",
                    "line_id": "52",
                    "lat": 55.018789,
                    "lng": 82.939007,
                },
                "metro_stations": [
                    {
                        "station_name": "Октябрьская",
                        "line_name": "Ленинская",
                        "station_id": "52.298",
                        "line_id": "52",
                        "lat": 55.018789,
                        "lng": 82.939007,
                    },
                    {
                        "station_name": "Площадь Ленина",
                        "line_name": "Ленинская",
                        "station_id": "52.297",
                        "line_id": "52",
                        "lat": 55.029941,
                        "lng": 82.92069,
                    },
                ],
                "id": "906680",
            },
            "response_url": "null",
            "sort_point_distance": "null",
            "published_at": "2024-07-29T12:14:00+0300",
            "created_at": "2024-07-29T12:14:00+0300",
            "archived": "false",
            "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=91773507",
            "show_logo_in_search": "null",
            "insider_interview": "null",
            "url": "https://api.hh.ru/vacancies/91773507?host=hh.ru",
            "alternate_url": "https://hh.ru/vacancy/91773507",
            "relations": [],
            "employer": {
                "id": "3034828",
                "name": "Смарт консалтинг",
                "url": "https://api.hh.ru/employers/3034828",
                "alternate_url": "https://hh.ru/employer/3034828",
                "logo_urls": {
                    "original": "https://img.hhcdn.ru/employer-logo-original/1063302.png",
                    "90": "https://img.hhcdn.ru/employer-logo/5873841.png",
                    "240": "https://img.hhcdn.ru/employer-logo/5873842.png",
                },
                "vacancies_url": "https://api.hh.ru/vacancies?employer_id=3034828",
                "accredited_it_employer": "true",
                "trusted": "true",
            },
            "snippet": {
                "requirement": "Базовые знания JavaScript."
                " Будет здорово, если ты: - Имеешь базовые знания HTML, "
                "CSS. - Имеешь базовые знания SQL. -аналитический склад ума. -",
                "responsibility": "Мы - сибирская аккредитованная IT-компания полного цикла "
                "(от идеи до разработки, внедрения программного обеспечения, "
                "сервисного сопровождения, "
                'вплоть до этапа "похорон...',
            },
            "contacts": "null",
            "schedule": {"id": "fullDay", "name": "Полный день"},
            "working_days": [],
            "working_time_intervals": [],
            "working_time_modes": [],
            "accept_temporary": "false",
            "professional_roles": [{"id": "96", "name": "Программист, разработчик"}],
            "accept_incomplete_resumes": "false",
            "experience": {"id": "noExperience", "name": "Нет опыта"},
            "employment": {"id": "full", "name": "Полная занятость"},
            "adv_response_url": "null",
            "is_adv_vacancy": "false",
            "adv_context": "null",
        }
    ]


@pytest.fixture
def test_add_vacancy():
    return Vacancy(
        "Python Developer",
        "<https://hh.ru/vacancy/123456>",
        {"from": 100000, "to": 150000},
        "Требования: опыт работы от 3 лет...",
    )


@pytest.fixture
def vacancy_1():
    return Vacancy(
        name="Python Developer",
        url="<https://hh.ru/vacancy/123456>",
        salary={"from": 100000, "to": 150000},
        text="Требования: опыт работы от 3 лет...",
    )


@pytest.fixture
def vacancy_2():
    return Vacancy(
        name="Python Developer",
        url="<https://hh.ru/vacancy/123456>",
        salary={"from": 100000, "to": 160000},
        text="Требования: опыт работы от 3 лет...",
    )


@pytest.fixture
def test_result_filtered_vacancy():
    return {
        "name": "Python Developer",
        "url": "<https://hh.ru/vacancy/123456>",
        "salary": {"from": 100000, "to": 150000},
        "text": "Требования: опыт работы от 3 лет...",
    }


@pytest.fixture
def test_cast_to_object_vacancy():
    return [
        {
            "name": "Python",
            "url": "<https://hh.ru/vacancy/1234561>",
            "salary": {"from": 100000, "to": 150000},
            "text": {"requirement": "Требования: опыт работы от 1 лет..."},
        },
        {
            "name": "Developer",
            "url": "<https://hh.ru/vacancy/123452>",
            "salary": {"from": 110000, "to": 160000},
            "text": {"requirement": "Требования: опыт работы от 2 лет..."},
        },
        {
            "name": "Python Developer",
            "url": "<https://hh.ru/vacancy/123453>",
            "salary": {"from": 120000, "to": 170000},
            "text": {"requirement": "Требования: опыт работы от 3 лет..."},
        },
    ]


@pytest.fixture
def test_cast_to_add_vacancy():
    return [
        {
            "name": "Python",
            "url": "<https://hh.ru/vacancy/1234561>",
            "salary": {"from": 100000, "to": 150000},
            "text": "Требования: опыт работы от 1 лет...",
        },
        {
            "name": "Developer",
            "url": "<https://hh.ru/vacancy/123452>",
            "salary": {"from": 110000, "to": 160000},
            "text": "Требования: опыт работы от 2 лет...",
        },
        {
            "name": "Python Developer",
            "url": "<https://hh.ru/vacancy/123453>",
            "salary": {"from": 120000, "to": 170000},
            "text": "Требования: опыт работы от 3 лет...",
        },
    ]


@pytest.fixture
def temp_json_file(tmp_path):
    """Фикстура для создания временного JSON-файла в тестах."""
    file = tmp_path / "test_vacancies.json"
    yield file
    if file.exists():
        os.remove(file)

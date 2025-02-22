from src.classes import HH, Vacancy
from src.saver import JSONSaver


# Функция для взаимодействия с пользователем
def user_interaction():
    platforms = HH()
    storage = JSONSaver("data/vacancies.json")
    search_query = input("Введите поисковый запрос: ")
    vacancies = HH.load_vacancies(platforms, search_query)
    vacancy_list = Vacancy.cast_to_object_list(vacancies)
    storage.add_vacancy(vacancy_list)
    print(f"Добавлено {len(vacancy_list)} вакансий.")

    top_n = int(input("Введите количество вакансий для вывода в топ N: "))

    vacancy_list = vacancy_list[0:top_n]
    print(vacancy_list)

    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()

    filtered_vacancies = []
    for vacancy in vacancy_list:
        for word in filter_words:
            name = vacancy.get("name", "")
            snippet = vacancy.get("snippet", "")

            if not isinstance(name, str):
                name = ""
            if not isinstance(snippet, str):
                snippet = ""

            if word.lower() in name.lower() or word.lower() in snippet.lower():
                filtered_vacancies.append(vacancy)

    print(filtered_vacancies)


if __name__ == "__main__":
    user_interaction()

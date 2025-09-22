# QA Automation Project: Stellar Burgers

## 📋 Описание проекта
Проект по автоматизации для веб-сайта Stellar Burgers. Он включает совокупное тестирование, а именно это функционал регистрации, авторизации, личного кабинета и конструктора бургеров.

## 🚀 Технологии
- **Python 3.13**
- **Pytest** - фреймворк для тестирования
- **Selenium WebDriver** - автоматизация браузера
- **Page Object Pattern** - паттерн проектирования

## 📁 Структура проекта
qa_Sprint_5/
├── test/ # Папка с автотестами
│ ├── test_1_successful_registration.py
│ ├── test_2_none_password.py
│ ├── test_3_none_name.py
│ ├── test_4_none_email.py
│ ├── test_5_invalid_password_len_5.py
│ ├── test_6_registration_with_the_same_data.py
│ ├── test_7_invalid_email.py
│ ├── test_8_entrance.py
│ ├── test_9_transition.py
│ ├── test_10_testing_exit_button.py
│ └── test_11_constructor.py
│
├── README.md # Документация
├── locators.py # Локаторы элементов
├── .pytest_cache/ # Кэш Pytest
├── conftest.py # Фикстуры Pytest
├── data.py # Генерация тестовых данных
├── pycache/ # Кэш Python
└── fixtures/ # Тестовые данные и фикстуры

text

Тестовое покрытие

# Тесты регистрации и авторизации
- Успешная регистрация
- Валидация пароля
- Валидация email
- Регистрация с существующими данными
- Тесты восстановления пароля

# Тесты личного кабинета
- Вход в личный кабинет
- Навигация по профилю
- Тестирование кнопки выхода

# Тесты конструктора бургеров
- Переключение разделов: Булки, Соусы, Начинки
- Функциональность кнопок
- Навигация по логотипу

Установка и запуск

1. Установка зависимостей
```bash
pip install -r requirements.txt
2. Запуск всех тестов
bash
python -m pytest test/ -v -s
3. Запуск конкретного теста
bash
python -m pytest test/test_1_successful_registration.py -v -s
4. Запуск с отчетом
bash
python -m pytest test/ -v --html=report.html 
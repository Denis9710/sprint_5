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
│ ├── test_1_сhecking_registration.py
│ ├── test_2_registration_none_password.py
│ ├── test_3_registration_none_name.py
│ ├── test_4_registration_none_email.py
│ ├── test_5_password_len_errors.py
│ ├── test_6_registrations_with_duplicate.py
│ ├── test_7_invalid_email.py
│ ├── test_8_entrance_button_in_form_registration.py
│ ├── test_9_entrance_button_in_form_restore_pass.py
│ ├── test_10_button_log_in.py
│ ├── test_11_entrance_button_personal_account.py
│ ├── test_12_transition_from_your_personal_account_to_the_designer.py
│ ├── test_13_transition_personal_account.py
│ ├── test_14_Click_on_the_Stellar_Burgers_logo_to_access_the_website.py
│ ├── test_15_testing_exit_button.py
│ └── test_16_constructor.py
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
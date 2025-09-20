from selenium.webdriver.common.by import By

#Текущие ссылки
class URL:
    # Форма входа на сайт бургерной
    current_url_entrance = 'https://stellarburgers.nomoreparties.site/login'
    # Главная страница бургерной
    current_url_home_page = 'https://stellarburgers.nomoreparties.site/' 
    # Переход в личный кабинет
    current_url_personal_account = 'https://stellarburgers.nomoreparties.site/account/profile'
    # Лента заказов бургерной
    current_url_order_feed = 'https://stellarburgers.nomoreparties.site/feed'
    # Регистрация на сайте 
    current_url_form_signup = 'https://stellarburgers.nomoreparties.site/register'
    # Восстановить пароль на сайте 
    current_url_recovery_password = 'https://stellarburgers.nomoreparties.site/forgot-password'



# Кнопки которые находятся на главной странице бургерной
class BUTTON:
    # Кнопка "логотип"
    logo_button = (By.XPATH, '//a[@href="/"]') 
    # Кнопка "войти в аккаунт"
    entrance_in_account = (By.XPATH, './/button[text() = "Войти в аккаунт"]')       
    # Кнопка "личного кабинета"
    personal_account_button = (By.XPATH, './/p[text() = "Личный Кабинет"]')
    # Кнопка "конструктор"
    constructor_button = (By.XPATH, '//p[text() = "Конструктор"]')
    # Кнопка "оформить заказ"
    place_an_order = (By.XPATH, './/button[text() = "Оформить заказ"]')
    # Кнопка "лента заказов"
    order_feed_button = (By.XPATH, '//p[text() = "Лента Заказов"]')
    # Кнопка "выйти из аккаунт"
    exit_from_account = (By.XPATH, './/button[text() = "Выход"]')

# Форма регистрации на сайте бургерной
class SIGNUP:
    # Поле "Имя"
    field_name = (By.XPATH, './/label[text() = "Имя"]/following-sibling::input')
    # Поле "email"
    field_email = (By.XPATH, './/label[text() = "Email"]/following-sibling::input')
    # Поле "Пароль"
    field_password2 = (By.XPATH, './/label[text() = "Пароль"]/following-sibling::input')
    # Кнопка "Зарегестрироваться"
    button_signup = (By.XPATH, './/form//button[text()="Зарегистрироваться"]')
    # Кнопка "Войти"
    entrance_button2 = (By.XPATH, './/a[@class="Auth_link__1fOlj" and text()= "Войти"]')
    # Надпись при дублирование данных при регестрации 
    text_during_dubbing = (By.XPATH, './/p[text()= "Такой пользователь уже существует"]')

# Форма входа на сайт бургерной
class ENTRANCE:
    # Поле "email"
    field_email = (By.XPATH, '//input[@name="name"]')
    field_password = (By.XPATH, './/h2[text() = "Вход"]/following::input[@type="password"]')
    # Кнопка "войти"
    entrance_button1 = (By.XPATH, './/button[@class = "button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa" and text() = "Войти"]')
    # Кнопка "зарегестрироваться"
    signup = (By.XPATH, './/a[@class="Auth_link__1fOlj" and text()= "Зарегистрироваться"]')
    # Кнопка "восстановить пароль"
    restore_password = (By.XPATH, './/a[@class="Auth_link__1fOlj" and text() = "Восстановить пароль"]')
    # Текст "некорректный пароль"
    invalid_password = (By.XPATH, './/p[text() = "Некорректный пароль"]')

# Форма восстановления пароля 
class RESTORE:
    field_email1 = (By.XPATH, './/h2[text() = "Восстановление пароля"]/following::input[@type="text"]')
    button_restore = (By.XPATH, './/h2[text() = "Восстановление пароля"]/following::button[text() = "Восстановить"]')
    entrance_button3 = (By.CLASS_NAME, 'Auth_link__1fOlj' )


#Конструктор 
class KON:
    # Булки
    button_buns = (By.XPATH, '//span[text()="Булки"]')
    # Соусы
    button_sauces = (By.XPATH, '//span[text()="Соусы"]')
    # Начинка
    button_fillings = (By.XPATH, '//span[text()="Начинки"]')
    active_tabl =  (By.CSS_SELECTOR, ".tab_tab_type_current__2BEPc")

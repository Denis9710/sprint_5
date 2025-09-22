import pytest
from locators import URL, KON
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestTab:
    @pytest.mark.parametrize('text, tab_locators', [
        ("Булки", KON.button_buns),
        ("Соусы", KON.button_sauces),
        ("Начинки", KON.button_fillings)
    ])
    def test_tab_switching(self, driver, text, tab_locators):
        driver.get(URL.current_url_home_page)
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(tab_locators))
        driver.find_element(*tab_locators).click()
        active_tab = driver.find_element(*KON.active_tabl)
        assert text in active_tab.text

    def test_sauces_tab(self, driver):
        driver.get(URL.current_url_home_page)
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(KON.button_sauces))
        driver.find_element(*KON.button_sauces).click()
        active_tab = driver.find_element(*KON.active_tabl)
        assert "Соусы" in active_tab.text

    def test_buns_tab(self, driver):
        driver.get(URL.current_url_home_page)
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(KON.button_buns))
        driver.find_element(*KON.button_buns).click()
        active_tab = driver.find_element(*KON.active_tabl)
        assert "Булки" in active_tab.text

    def test_fillings_tab(self, driver):
        driver.get(URL.current_url_home_page)
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(KON.button_fillings))
        driver.find_element(*KON.button_fillings).click()
        active_tab = driver.find_element(*KON.active_tabl)
        assert "Начинки" in active_tab.text
import time
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from tests.settings import valid_google_email, valid_google_password
from pages.auth_page import AuthPage
from pages.confirm_order_page import ConfirmOrder
from pages.product_page import ProductPage
from selenium import webdriver


driver = webdriver.Chrome()# Получение объекта веб-драйвера для браузера Chrome
wait = WebDriverWait(driver,2)# Стандартное ожидание

"""Запуск драйвера и открытие страницы авторизации"""
@pytest.fixture
def load_auth_page():
    url = "https://accounts.google.com/o/oauth2/v2/auth/" \
          "oauthchooseaccount?client_id=438567566819-3k1nk9qd" \
          "1vr39c42rmjr0dh24ngth0s4.apps.googleusercontent.com&" \
          "response_type=code&scope=openid%20email%20profile&redirect" \
          "_uri=https%3A%2F%2Fthirdparty.aliexpress.com%2Fggcallback." \
          "htm&state=iL7E8xPldkLkhvvMuLiwtlLofJ7jPTZ489rl2fpSfRQI%2FF4I" \
          "nm77rApP%2B%2FV11Oonu8S%2B1A1HFl4%3D&flowName=GeneralOAuthFlow"
    driver.get(url)

    yield

    driver.quit()

"""15 Проверка увеличения количества товара"""
def test_plus_one(load_auth_page):
    page = AuthPage(driver)
    # Ввод логина
    page.email = valid_google_email
    # Ожидание кнопки "Далее" с последующим нажатием
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "VfPpkd-RLmnJb")))
    page.proceed_btn_login.click()
    # Ожидание окна ввода пароля
    time.sleep(5)
    # Ввод пароля
    page.password = valid_google_password
    page.proceed_btn_pass.click()
    # Ожидание загрузки главной страницы
    time.sleep(5)
    # Переход на страницу продукта
    url = "https://aliexpress.ru/item/1005003908584589." \
          "html?spm=a2g2w.productlist.search_results." \
          "0.689c70ffO4v5rQ&sku_id=12000029726689934"
    driver.get(url)
    page = ProductPage(driver)
    # Прокрутка страницы до искомого элемента
    ActionChains(driver).scroll_by_amount(0, 500).perform()
    # Нажатие на кнопку "Купить сейчас"
    page.buy_now_btn.click()
    page = ConfirmOrder(driver)
    time.sleep(5)
    # Два нажатия на кнопку "+"
    page.plus_button.click()
    page.plus_button.click()
    time.sleep(5)
    # Проверка на счетчика на соответствие ожидаемому значению
    assert page.amount.get_attribute('value') == '3'

"""16. Проверка уменьшения количества товара"""
def test_minus_one(load_auth_page):
    page = AuthPage(driver)
    # Ввод логина
    page.email = valid_google_email
    # Ожидание кнопки "Далее" с последующим нажатием
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "VfPpkd-RLmnJb")))
    page.proceed_btn_login.click()
    # Ожидание окна ввода пароля
    time.sleep(5)
    # Ввод пароля
    page.password = valid_google_password
    page.proceed_btn_pass.click()
    # Ожидание загрузки главной страницы
    time.sleep(5)
    # Переход на страницу продукта
    url = "https://aliexpress.ru/item/1005003908584589." \
          "html?spm=a2g2w.productlist.search_results.0." \
          "689c70ffO4v5rQ&sku_id=12000029726689934"
    driver.get(url)
    page = ProductPage(driver)
    # Прокрутка страницы до искомого элемента
    ActionChains(driver).scroll_by_amount(0, 500).perform()
    # Нажатие на кнопку "Купить сейчас"
    page.buy_now_btn.click()
    page = ConfirmOrder(driver)
    time.sleep(5)
    # Два нажатия на кнопку "+" и одно на кнопку "-"
    page.plus_button.click()
    page.plus_button.click()
    page.minus_button.click()
    time.sleep(5)
    # Проверка на счетчика на соответствие ожидаемому значению
    assert page.amount.get_attribute('value') == '2'

"""17. Негативный тест. Проверка уменьшения количества товара меньше 1"""
def test_minus_one_negative(load_auth_page):
    page = AuthPage(driver)
    # Ввод логина
    page.email = valid_google_email
    # Ожидание кнопки "Далее" с последующим нажатием
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "VfPpkd-RLmnJb")))
    page.proceed_btn_login.click()
    # Ожидание окна ввода пароля
    time.sleep(5)
    # Ввод пароля
    page.password = valid_google_password
    page.proceed_btn_pass.click()
    # Ожидание загрузки главной страницы
    time.sleep(5)
    # Переход на страницу продукта
    url = "https://aliexpress.ru/item/1005003908584589.html?spm=a2g2w." \
          "productlist.search_results.0.689c70ffO4v5rQ&sku_id=12000029726689934"
    driver.get(url)
    page = ProductPage(driver)
    # Прокрутка страницы до искомого элемента
    ActionChains(driver).scroll_by_amount(0, 500).perform()
    # Нажатие на кнопку "Купить сейчас"
    page.buy_now_btn.click()
    page = ConfirmOrder(driver)
    time.sleep(5)
    # Одно нажатие на кнопку "-"
    page.minus_button.click()
    time.sleep(5)
    # Проверка на счетчика на соответствие ожидаемому значению
    assert page.amount.get_attribute('value') == '1'

"""18. Негативный тест. Проверка увеличения количества товара сверх доступного"""
def test_plus_one_negative(load_auth_page):
    page = AuthPage(driver)
    # Ввод логина
    page.email = valid_google_email
    # Ожидание кнопки "Далее" с последующим нажатием
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "VfPpkd-RLmnJb")))
    page.proceed_btn_login.click()
    # Ожидание окна ввода пароля
    time.sleep(5)
    # Ввод пароля
    page.password = valid_google_password
    page.proceed_btn_pass.click()
    # Ожидание загрузки главной страницы
    time.sleep(5)
    # Переход на страницу продукта
    url = "https://aliexpress.ru/item/1005003908584589.html?spm=a2g2w" \
          ".productlist.search_results.0.689c70ffO4v5rQ&sku_id=12000029726689934"
    driver.get(url)
    page = ProductPage(driver)
    # Прокрутка страницы до искомого элемента
    ActionChains(driver).scroll_by_amount(0, 500).perform()
    # Нажатие на кнопку "Купить сейчас"
    page.buy_now_btn.click()
    page = ConfirmOrder(driver)
    time.sleep(5)
    # Нажатие на кнопку "+" до тех пор пока количество не перестанет увеличиваться
    current_value = 0
    next_value = 1
    while next_value > current_value:
        page.plus_button.click()
        current_value += 1
        next_value = int(page.amount.get_attribute('value'))
    time.sleep(5)
    # Проверка на счетчика на соответствие ожидаемому значению
    assert page.amount.get_attribute('value') == str(current_value)

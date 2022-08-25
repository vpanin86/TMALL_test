import time
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.main_page import MainPage
from pages.auth_page import AuthPage
from pages.cart_page import CartPage
from pages.product_page import ProductPage
from tests.settings import valid_google_email, valid_google_password



driver = webdriver.Chrome()# Получение объекта веб-драйвера для браузера Chrome
wait = WebDriverWait(driver,10)# Стандартное ожидание

"""Запуск драйвера и открытие страницы авторизации"""
@pytest.fixture
def load_auth_page():
    url = "https://accounts.google.com/o/oauth2/v2/auth/" \
          "oauthchooseaccount?client_id=438567566819-3k1nk9q" \
          "d1vr39c42rmjr0dh24ngth0s4.apps.googleusercontent.com&" \
          "response_type=code&scope=openid%20email%20profile&redirect_" \
          "uri=https%3A%2F%2Fthirdparty.aliexpress.com%2Fggcallback.htm&state" \
          "=iL7E8xPldkLkhvvMuLiwtlLofJ7jPTZ489rl2fpSfRQI%2FF4Inm77rApP%2B%2FV11O" \
          "onu8S%2B1A1HFl4%3D&flowName=GeneralOAuthFlow"
    driver.get(url)

    yield

    driver.quit()

"""10. Проверка удаления товара из корзины"""
def test_delete_from_cart(load_auth_page):
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
          "html?spm=a2g2w.productlist.search_results.0.689c" \
          "70ffO4v5rQ&sku_id=12000029726689934"
    driver.get(url)
    page = ProductPage(driver)
    # Прокрутка страницы до искомого элемента
    ActionChains(driver).scroll_by_amount(0, 500).perform()
    page.add_to_cart_button.click()
    time.sleep(5)
    url = "https://shoppingcart.aliexpress.ru/shopcart/shopcartDetail" \
          ".htm?spm=a2g2w.detail.1000002.4.60d87bcbXc2fdG&_ga=2.236671105" \
          ".105933283.1660891296-1056514360.1660891296"
    driver.get(url)
    page = CartPage(driver)
    # Удаление товара
    page.delete_item.click()
    time.sleep(5)
    # Подтверждение удаления
    page.confirm_del_btn.click()
    time.sleep(5)
    # Проверка на наличие элемента, характерного для пустой корзины
    assert page.empty_cart.get_attribute('class') == 'Shoppingcart' \
                                                     'States_CartState__defaultEmpty__1ww0f'

"""11. Проверка увеличения количества товара"""
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
    url = "https://aliexpress.ru/item/1005003908584589" \
          ".html?spm=a2g2w.productlist.search_results." \
          "0.689c70ffO4v5rQ&sku_id=12000029726689934"
    driver.get(url)
    page = ProductPage(driver)
    # Прокрутка страницы до искомого элемента
    ActionChains(driver).scroll_by_amount(0, 500).perform()
    # Нажатие на кнопку "Добавить в корзину"
    page.add_to_cart_button.click()
    time.sleep(5)
    url = "https://shoppingcart.aliexpress.ru/shopcart/shopcartDetail" \
          ".htm?spm=a2g2w.detail.1000002.4.60d87bcbXc2fdG&_ga=2.236671105" \
          ".105933283.1660891296-1056514360.1660891296"
    driver.get(url)
    page = CartPage(driver)
    time.sleep(5)
    # Два нажатия на кнопку "+"
    page.plus_button.click()
    page.plus_button.click()
    time.sleep(5)
    # Проверка счетчика на ожидаемое значение
    assert page.amount.get_attribute('value') == '3'

"""12. Проверка уменьшения количества товара"""
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
          "html?spm=a2g2w.productlist.search_results." \
          "0.689c70ffO4v5rQ&sku_id=12000029726689934"
    driver.get(url)
    page = ProductPage(driver)
    # Прокрутка страницы до искомого элемента
    ActionChains(driver).scroll_by_amount(0, 500).perform()
    # Нажатие на кнопку "Добавить в корзину"
    page.add_to_cart_button.click()
    time.sleep(5)
    url = "https://shoppingcart.aliexpress.ru/shopcart/shopcartDetail" \
          ".htm?spm=a2g2w.detail.1000002.4.60d87bcbXc2fdG&_ga=2.236671105" \
          ".105933283.1660891296-1056514360.1660891296"
    driver.get(url)
    page = CartPage(driver)
    time.sleep(5)
    # Два нажатия на кнопку "+" и одно нажатие на кнопку "-"
    page.plus_button.click()
    page.plus_button.click()
    page.minus_button.click()
    time.sleep(5)
    # Проверка счетчика на ожидаемое значение
    assert page.amount.get_attribute('value') == '2'

"""13. Негативный тест. Проверка уменьшения количества товара меньше 1"""
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
    page = MainPage(driver)
    # Переход на страницу продукта
    url = "https://aliexpress.ru/item/1005003908584589.html?spm=a2g2w" \
          ".productlist.search_results.0.689c70ffO4v5rQ&sku_id=12000029726689934"
    driver.get(url)
    page = ProductPage(driver)
    # Прокрутка страницы до искомого элемента
    ActionChains(driver).scroll_by_amount(0, 500).perform()
    page.add_to_cart_button.click()
    time.sleep(5)
    url = "https://shoppingcart.aliexpress.ru/shopcart/shopcartDetail" \
          ".htm?spm=a2g2w.detail.1000002.4.60d87bcbXc2fdG&_ga=2.236671105" \
          ".105933283.1660891296-1056514360.1660891296"
    driver.get(url)
    page = CartPage(driver)
    time.sleep(5)
    # Одно нажатие на кнопку "-"
    page.minus_button.click()
    time.sleep(5)
    # Проверка счетчика на ожидаемое значение
    assert page.amount.get_attribute('value') == '1'

"""14. Негативный тест. Проверка увеличения количества товара сверх доступного"""
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
    url = "https://aliexpress.ru/item/1005003908584589." \
          "html?spm=a2g2w.productlist.search_results." \
          "0.689c70ffO4v5rQ&sku_id=12000029726689934"
    driver.get(url)
    page = ProductPage(driver)
    # Прокрутка страницы до искомого элемента
    ActionChains(driver).scroll_by_amount(0, 500).perform()
    page.add_to_cart_button.click()
    time.sleep(5)
    url = "https://shoppingcart.aliexpress.ru/shopcart/" \
          "shopcartDetail.htm?spm=a2g2w.detail.1000002.4." \
          "60d87bcbXc2fdG&_ga=2.236671105.105933283." \
          "1660891296-1056514360.1660891296"
    driver.get(url)
    page = CartPage(driver)
    time.sleep(5)
    # Нажатие на кнопку "+" до тех пор пока количество не перестанет увеличиваться
    current_value = 0
    next_value = 1
    while next_value > current_value:
        page.plus_button.click()
        current_value += 1
        next_value = int(page.amount.get_attribute('value'))
    time.sleep(5)
    # Проверка счетчика на ожидаемое значение
    assert page.amount.get_attribute('value') == str(current_value)


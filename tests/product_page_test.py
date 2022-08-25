import time
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.auth_page import AuthPage
from pages.cart_page import CartPage
from pages.product_page import ProductPage
from pages.confirm_order_page import ConfirmOrder
from tests.settings import valid_google_email, valid_google_password


driver = webdriver.Chrome()# Получение объекта веб-драйвера для браузера Chrome
wait = WebDriverWait(driver,10)# Стандартное ожидание

"""Запуск драйвера и открытие стартовой страницы T-MALL"""
@pytest.fixture
def load_product_page():
    url = "https://aliexpress.ru/item/1005003908584589." \
          "html?spm=a2g2w.productlist.search_results." \
          "0.689c70ffO4v5rQ&sku_id=12000029726689934"
    driver.get(url)

    yield

    driver.quit()

"""Загрузка страницы авторизации"""
@pytest.fixture
def load_auth_page():
    url = "https://accounts.google.com/o/oauth2/v2/" \
          "auth/oauthchooseaccount?client_id=438567566819-" \
          "3k1nk9qd1vr39c42rmjr0dh24ngth0s4.apps.googleusercontent" \
          ".com&response_type=code&scope=openid%20email%20profile&redirect" \
          "_uri=https%3A%2F%2Fthirdparty.aliexpress.com%2Fggcallback." \
          "htm&state=iL7E8xPldkLkhvvMuLiwtlLofJ7jPTZ489rl2fpSfRQI%2FF4Inm77" \
          "rApP%2B%2FV11Oonu8S%2B1A1HFl4%3D&flowName=GeneralOAuthFlow"
    driver.get(url)

"""26. Проверка увеличения количества товара"""
def test_plus_one(load_product_page):
    page = ProductPage(driver)
    # Прокрутка страницы до искомого элемента
    ActionChains(driver).scroll_by_amount(0, 500).perform()
    # Два нажатия кнопки "+"
    page.plus_button.click()
    page.plus_button.click()
    # Считывание и проверка счетчика
    assert page.amount.text == '3'

"""27. Проверка уменьшения количества товара"""
def test_minus_one(load_product_page):
    page = ProductPage(driver)
    # Прокрутка страницы до искомого элемента
    ActionChains(driver).scroll_by_amount(0, 500).perform()
    # Два нажатия кнопки "+", одно нажатие кнопки "-"
    page.plus_button.click()
    page.plus_button.click()
    page.minus_button.click()
    # Считывание и проверка счетчика
    assert page.amount.text == '2'

"""28. Негативный тест. Проверка уменьшения количества товара меньше 1"""
def test_minus_one_negative(load_product_page):
    page = ProductPage(driver)
    # Прокрутка страницы до искомого элемента
    ActionChains(driver).scroll_by_amount(0, 500).perform()
    # Одно нажатие кнопки "-"
    page.minus_button.click()
    # Считывание и проверка счетчика
    assert page.amount.text == '1'

"""29. Проверка увеличения количества товара до максимального значения"""
def test_max_amount(load_product_page):
    page = ProductPage(driver)
    # Прокрутка страницы до искомого элемента
    ActionChains(driver).scroll_by_amount(0, 500).perform()
    str_max = page.max_amount.text.split(' ')
    max = int(str_max[0])
    # Нажатие кнопки "+" до предельного значения количества товара
    for i in range(1, max):
        page.plus_button.click()
    # Проверка останова счетчика
    assert page.amount.text == str_max[0]

"""30. Негативный тест. Проверка увеличения количества товара до максимального значения"""
def test_max_amount_negative(load_product_page):
    page = ProductPage(driver)
    # Прокрутка страницы до искомого элемента
    ActionChains(driver).scroll_by_amount(0, 500).perform()
    str_max = page.max_amount.text.split(' ')
    max = int(str_max[0])
    # Нажатие кнопки "+" выше предельного значения количества товара
    for i in range(1, max+1):
        page.plus_button.click()
    # Проверка останова счетчика
    assert page.amount.text == str_max[0]

"""31. Проверка изменения комплектации"""
def test_change_set(load_product_page):
    page = ProductPage(driver)
    # Прокрутка страницы до искомого элемента
    ActionChains(driver).scroll_by_amount(0, 500).perform()
    # Переключение комплекта
    page.set_selector.click()
    # Проверка соответствия текста селектора и метки
    assert page.set_selector.text == page.label_set_selector.text

"""32. Проверка изменения цвета"""
def test_change_color(load_product_page):
    page = ProductPage(driver)
    # Прокрутка страницы до искомого элемента
    ActionChains(driver).scroll_by_amount(0, 500).perform()
    # Переключение комплекта
    page.color_selector.click()
    # Проверка соответствия текста селектора и метки
    assert page.label_color_selector.text == '8GB 128GB Purple'

"""33. Проверка добавления товара в корзину"""
def test_add_to_cart(load_auth_page):
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
    page.add_to_cart_button.click()
    time.sleep(5)
    url = "https://shoppingcart.aliexpress.ru/shopcart/shopcartDetail." \
          "htm?spm=a2g2w.detail.1000002.4.60d87bcbXc2fdG&_ga=2.236671105." \
          "105933283.1660891296-1056514360.1660891296"
    driver.get(url)
    page = CartPage(driver)
    assert page.item_card.get_attribute('class') == 'ShoppingcartItemList' \
                                                    '_ProductCard__productContainer__1nl31'

"""34. Проверка перехода на страницу оплаты"""
def test_buy_now(load_auth_page):
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
    # Проверка наличия характерного элемента страницы покупки
    assert page.delivery_header.text == 'Адрес доставки'

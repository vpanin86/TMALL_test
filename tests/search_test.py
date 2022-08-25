import time
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.search_page import SearchPage
from pages.app_page import AppPages
from selenium import webdriver


driver = webdriver.Chrome()# Получение объекта веб-драйвера для браузера Chrome
wait = WebDriverWait(driver,2)# Стандартное ожидание

"""Запуск драйвера и открытие стартовой страницы T-MALL"""
@pytest.fixture(autouse=True)
def load_main_page():
    url = "https://aliexpress.ru/brands/xiaomi?ltype=wholesale&d=y&origin=y&SearchText=xiaomi"
    driver.get(url)

    yield

    driver.quit()

"""35. Проверка элемента checkbox 'Бесплатная доставка'"""
def test_free_delivery():
    page = SearchPage(driver)
    time.sleep(5)
    # Нажатие на checkbox "Бесплатная доставка"
    page.checkbox_free_delivery.click()
    # Проверка наличия аттрибута бесплатной доставки у товара
    assert page.free_delivery_string.get_attribute("class") == 'snow-price' \
                                                               '_SnowPrice__freeDelivery__bz77le'

"""36. Проверка элемента checkbox 'Четыре звезды'"""
def test_four_stars():
    page = SearchPage(driver)
    time.sleep(5)
    # Нажатие на checkbox "Четыре звезды"
    page.checkbox_four_stars.click()
    # Проверка оценки товара
    assert float(page.stars_amount.text.replace(',','.')) > 4.0

"""37. Позитивная проверка фильтра цены """
def test_positive_price():
    page = SearchPage(driver)
    original_window = driver.current_window_handle
    # Введение значений фильтра
    page.min_price_input = '20000'
    page.max_price_input = '30000'
    page.price_button.click()
    time.sleep(5)
    # Переход на страницу товара
    page.product_link.click()
    wait.until(EC.number_of_windows_to_be(2))
    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break
    time.sleep(5)
    # Считывание цены товара
    price_str = page.product_price.text.replace('руб','')
    price_str = price_str.replace(' ', '')
    price_str = price_str.replace(',', '')
    price_str = price_str.replace('.', '')
    price_str = int(price_str)
    # Проверка попадания цены товара в диапазон
    assert 2000000 < price_str < 3000000

"""38. Негативная проверка фильтра цены"""
def test_negative_price():
    page = SearchPage(driver)
    original_window = driver.current_window_handle
    # Введение значений фильтра
    page.min_price_input = '30000' # В поле минимального значения пишется максимальное
    page.max_price_input = '20000' # В поле максимального значения пишется минимальное
    page.price_button.click()
    time.sleep(5)
    page.product_link.click()
    # Переход на страницу товара
    wait.until(EC.number_of_windows_to_be(2))
    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break
    time.sleep(5)
    # Считывание цены товара
    price_str = page.product_price.text.replace('руб', '')
    price_str = price_str.replace(' ', '')
    price_str = price_str.replace(',', '')
    price_str = price_str.replace('.', '')
    price_str = int(price_str)
    # Проверка попадания цены товара в диапазон
    assert 2000000 < price_str < 3000000

"""39. Проверка перехода на страницу загрузки приложения"""
def test_app_download():
    page = SearchPage(driver)
    original_window = driver.current_window_handle
    # Переход на страницу загрузки приложения
    page.app_download_link.click()
    wait.until(EC.number_of_windows_to_be(2))
    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break
    page = AppPages(driver)
    time.sleep(5)
    # Проверка наличия характерного элемента для страницы загрузки приложения
    assert page.google_play_button.get_attribute('class') == 'android-link'







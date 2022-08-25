import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.main_page import MainPage
from pages.auth_page import AuthPage
from pages.hotsales_page import HotSalesPage
from pages.cart_page import CartPage
from pages.search_page import SearchPage
from pages.category_page import CategoryPage


driver = webdriver.Chrome()# Получение объекта веб-драйвера для браузера Chrome
wait = WebDriverWait(driver, 10)# Стандартное ожидание

"""Запуск драйвера и открытие стартовой страницы T-MALL"""
@pytest.fixture(autouse=True)
def load_main_page():
    url = "https://promotion.aliexpress.ru/wow/gcp/aer/channel/aer/tmall_localization/7pcZWCh8tW?wh_weex=true&_immersiveMode=true&wx_navbar_hidden=true&wx_navbar_transparent=true&ignoreNavigationBar=true&wx_statusbar_hidden=true"
    driver.get(url)

    yield

    driver.quit()

"""40. Проверка загрузки главной страницы"""
def test_load_main_page():
    page = MainPage(driver)
    # Ожидание появления контейнера заголовка страницы
    wait.until(EC.presence_of_element_located((By.ID, "header-wrap.container")))
    # Проверка наличия логотипа tmall
    assert page.logo.get_attribute('class') == 'logo-base'

"""41. Проверка загрузки страницы авторизации google"""
def test_auth_google_page():
    page = MainPage(driver)
    # Фиксация текущего окна
    original_window = driver.current_window_handle
    # Ожидание появления контейнера с авторизацией через соцсети
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "user-account-info")))
    # Перевод курсора на вход через соцсети
    ActionChains(driver).move_to_element(page.user_acc_pnl).perform()
    # Ожидание появления кнопки 'Войти через Google'
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "nus-icon.nus-google")))
    # Нажатие на кнопку "Вход через Google
    page.google_sign_btn.click()
    # Ожидание нового окна и переключение фокуса на новое окно
    wait.until(EC.number_of_windows_to_be(2))
    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break
    page = AuthPage(driver)
    # Считывание id тела страницы и проверка его на соответствие ожидаемому
    assert page.google_auth_body.get_attribute('id') == 'yDmH0d'

"""42. Проверка перехода на страницу распродаж"""
def test_hot_product():
    page = MainPage(driver)
    # Фиксация текущего окна
    original_window = driver.current_window_handle
    # Ожидание появления контейнера заголовка страницы
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "rax-view")))
    # Переход по ссылке на страницу распродаж
    page.hot_product.click()
    wait.until(EC.number_of_windows_to_be(2))
    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break
    page = HotSalesPage(driver)
    # Проверка наличия характерного элемента для страницы распродаж
    assert page.hot_sales_banner.get_attribute('class') == 'rax-view box'

"""43. Проверка перехода в корзину"""
def test_cart():
    page = MainPage(driver)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "nav-cart.nav-cart-box")))
    # Переход в раздел "Корзина"
    page.cart_link.click()
    wait.until(EC.presence_of_element_located((By.ID, "__aer_root__")))
    page = CartPage(driver)
    # Проверка характерного элемента в разделе "Корзина"
    assert page.empty_cart.get_attribute('class') == 'ShoppingcartStates' \
                                                     '_CartState__defaultEmpty__1ww0f'

"""44. Проверка поисковой строки"""
def test_search():
    page = MainPage(driver)
    # Ввод текста в посиковую строку
    page.search_input = 'xiaomi'
    page.search_button.click()
    page = SearchPage(driver)
    # Проверка наличия товара по поисковому запросу
    assert page.data_product.get_attribute('data-product-id') != ''

"""45. Проверка перехода на страницу авторизации через vk"""
def test_vk_auth_page():
    page = MainPage(driver)
    # Фиксация текущего окна
    original_window = driver.current_window_handle
    # Ожидание появления контейнера с авторизацией через соцсети
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "user-account-info")))
    # Перевод курсора на вход через соцсети
    ActionChains(driver).move_to_element(page.user_acc_pnl).perform()
    # Ожидание появления кнопки 'Войти через Google'
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "nus-icon.nus-google")))
    # Нажатие на кнопку "Вход через Google"
    page.vk_sign_btn.click()
    # Ожидание нового окна и переключение фокуса на новое окно
    wait.until(EC.number_of_windows_to_be(2))
    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break
    page = AuthPage(driver)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "oauth_head")))
    # Проверка характерного аттрибута страницы авторизации через vk
    assert page.vk_logo.get_attribute("class") == "oauth_logo fl_l"

"""46. Проверка перехода по категориям"""
def test_catogory():
    page = MainPage(driver)
    # Переход по ссылке в категорию "Электроника"
    page.electronic_link.click()
    page = CategoryPage(driver)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "text")))
    # Проверка характерного элемента для категории "Электроника"
    assert page.phone_link.text == 'Телефоны'































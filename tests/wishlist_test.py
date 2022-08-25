import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from pages.auth_page import AuthPage
from pages.main_page import MainPage
from pages.wishlist_page import WishListPage
from pages.search_page import SearchPage
from pages.product_page import ProductPage
from tests.settings import valid_google_email, valid_google_password


driver = webdriver.Chrome()# Получение объекта веб-драйвера для браузера Chrome
wait = WebDriverWait(driver,10)# Стандартное ожидание


"""Запуск драйвера и открытие страницы авторизации"""
@pytest.fixture(autouse=True)
def load_main_page():
    url = "https://accounts.google.com/o/oauth2/v2/auth/" \
          "oauthchooseaccount?client_id=438567566819-3k1nk9qd1vr" \
          "39c42rmjr0dh24ngth0s4.apps.googleusercontent.com&response" \
          "_type=code&scope=openid%20email%20profile&redirect_uri=" \
          "https%3A%2F%2Fthirdparty.aliexpress.com%2Fggcallback." \
          "htm&state=iL7E8xPldkLkhvvMuLiwtlLofJ7jPTZ489rl2fpSfRQI%" \
          "2FF4Inm77rApP%2B%2FV11Oonu8S%2B1A1HFl4%3D&flowName=GeneralOAuthFlow"
    driver.get(url)

    yield

    driver.quit()

"""47. Проверка перехода в виш-лист"""
def test_wish_list():
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
    # Переход на страницу виш-листа
    page.wish_list.click()
    page = WishListPage(driver)
    time.sleep(5)
    # Проверка наличия заголовка 'Мои желания'
    assert page.wishlist_header.text == 'Мои желания'

"""48. Проверка добавления товара в виш-лист"""
def test_wish_list_add():
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
    original_window = driver.current_window_handle
    # Ввод текста в посиковую строку
    page.search_input = 'xiaomi'
    page.search_button.click()
    page = SearchPage(driver)
    page.data_product.click()
    # Ожидание нового окна и переключение фокуса на новое окно
    wait.until(EC.number_of_windows_to_be(2))
    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break
    page = ProductPage(driver)
    # Прокрутка страницы до искомого элемента
    ActionChains(driver).scroll_by_amount(0, 500).perform()
    time.sleep(5)
    page.like_2.click()
    time.sleep(5)
    # Проверка сообщения о добавлении товара в виш-лист
    assert page.item_added.text == 'Добавлено в' or 'Добавлено в'

"""49. Проверка добавления товара в виш-лист"""
def test_wish_list_del():
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
    original_window = driver.current_window_handle
    # Ввод текста в посиковую строку
    page.search_input = 'xiaomi'
    page.search_button.click()
    page = SearchPage(driver)
    page.data_product.click()
    # Ожидание нового окна и переключение фокуса на новое окно
    wait.until(EC.number_of_windows_to_be(2))
    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break
    page = ProductPage(driver)
    # Прокрутка страницы до искомого элемента
    ActionChains(driver).scroll_by_amount(0, 500).perform()
    time.sleep(5)
    # Добавление товара в виш-лист
    page.like_2.click()
    time.sleep(5)
    url = 'https://my.aliexpress.ru/wishlist/wish_list_product_list.htm?currentGroupId=0'
    driver.get(url)
    driver.maximize_window()
    page = WishListPage(driver)
    page.del_btn.click()
    # Проверка на наличие элемента пустого виш-листа
    assert page.empty_wishlist.text == 'Вы ещё ничего не добавили в список желаний. Выберите что-нибудь'

"""50. Проверка создания своего списка желания"""
def test_my_wishlist():
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
    original_window = driver.current_window_handle
    # Ввод текста в посиковую строку
    page.search_input = 'xiaomi'
    page.search_button.click()
    page = SearchPage(driver)
    page.data_product.click()
    # Ожидание нового окна и переключение фокуса на новое окно
    wait.until(EC.number_of_windows_to_be(2))
    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break
    page = ProductPage(driver)
    # Прокрутка страницы до искомого элемента
    ActionChains(driver).scroll_by_amount(0, 500).perform()
    time.sleep(5)
    page.like_2.click()
    time.sleep(5)
    url = 'https://my.aliexpress.ru/wishlist/wish_list_product_list.htm?currentGroupId=0'
    driver.get(url)
    driver.maximize_window()
    time.sleep(5)
    page = WishListPage(driver)
    # Создание своего списка виш-листа
    page.create_list.click()
    time.sleep(5)
    page.input_wishlist = 'Мой список'
    page.input_btn.click()
    time.sleep(5)
    # Проверка наличия созданного списка
    assert page.my_list.text == 'Мой список'

"""51. Проверка удаления своего списка желания"""
def test_my_wishlist_del():
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
    original_window = driver.current_window_handle
    # Ввод текста в посиковую строку
    page.search_input = 'xiaomi'
    page.search_button.click()
    page = SearchPage(driver)
    page.data_product.click()
    # Ожидание нового окна и переключение фокуса на новое окно
    wait.until(EC.number_of_windows_to_be(2))
    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break
    page = ProductPage(driver)
    # Прокрутка страницы до искомого элемента
    ActionChains(driver).scroll_by_amount(0, 500).perform()
    time.sleep(5)
    page.like_2.click()
    time.sleep(5)
    url = 'https://my.aliexpress.ru/wishlist/wish_list_product_list.htm?currentGroupId=0'
    driver.get(url)
    driver.maximize_window()
    time.sleep(5)
    page = WishListPage(driver)
    # Создание своего списка виш-листа
    page.create_list.click()
    time.sleep(5)
    page.input_wishlist = 'Мой список'
    time.sleep(5)
    page.input_btn.click()
    time.sleep(5)
    # Проверка наличия созданного списка
    assert page.my_list.text == 'Мой список'
    page.my_list.click()
    time.sleep(5)
    page.edit_list.click()
    time.sleep(5)
    # Удаление списка
    page.del_list.click()
    time.sleep(5)
    page.del_list_again.click()
    time.sleep(5)
    # Проверка отсутствия созданного списка
    assert page.my_list.text != 'Мой список'











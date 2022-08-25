import time
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.main_page import MainPage
from pages.auth_page import AuthPage
from pages.app_page import AppPages
from pages.customer_protection_page import CustomerProtectionPage
from pages.customer_service_page import CustomerServicePage
from pages.complaint_page import ComplaintPage
from pages.ali_page import AliPage
from selenium import webdriver
from tests.settings import valid_google_email, valid_google_password


driver = webdriver.Chrome()# Получение объекта веб-драйвера для браузера Chrome
wait = WebDriverWait(driver,2)# Стандартное ожидание

"""Запуск драйвера и открытие стартовой страницы T-MALL"""
@pytest.fixture(autouse=True)
def load_main_page():
    url = "https://promotion.aliexpress.ru/wow/gcp/aer" \
          "/channel/aer/tmall_localization/7pcZWCh8tW?wh_" \
          "weex=true&_immersiveMode=true&wx_navbar_hidden=" \
          "true&wx_navbar_transparent=true&ignoreNavigationBar" \
          "=true&wx_statusbar_hidden=true"
    driver.get(url)

    yield

    driver.quit()

"""19. Проверка перехода на страницу защиты покупателя"""
def test_customer_protection():
    page = MainPage(driver)
    # Переход по ссылке
    page.customer_protection_link.click()
    page = CustomerProtectionPage(driver)
    # Проверка на наличие характерного элемента требуемой страницы
    assert page.customer_header.text == 'ГАРАНТИЯ ВОЗВРАТА'

"""20. Проверка выбора региона доставки и валюты"""
def test_delivery_region():
    page = MainPage(driver)
    # Выбор валюты и региона доставки
    page.region_switcher.click()
    page.address_selector.click()
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "css_flag.css_af")))
    page.country_list_item.click()
    page.save_button_country.click()
    time.sleep(5)
    # Проверка валюты
    assert page.currency_element.text == 'USD'

"""21. Проверка перехода по ссылке на глобальную версию сайта"""
def test_global_site_link():
    page = MainPage(driver)
    # Переход по ссылке на глобальную версию сайта
    page.global_site_link.click()
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "TopHeadV2_TopHeadV2__textHead__1c1dq")))
    # Проверка на наличие англоязычного текста
    assert page.account_eng.text == 'Account'

"""22. Проверка перехода по ссылке на страницу службы поддержки"""
def test_support_link():
    page = MainPage(driver)
    # Переход по ссылке на страницу службы поддержки
    ActionChains(driver).move_to_element(page.help_header).perform()
    page.support_link.click()
    page = CustomerServicePage(driver)
    # Проверка на наличие характерного заголовка
    assert page.customer_service_header.text == 'Сервис Покупателя'

"""23. Проверка перехода по ссылке на страницу споров и жалоб"""
def test_complaint_page():
    url = "https://accounts.google.com/o/oauth2/v2/auth/" \
          "oauthchooseaccount?client_id=438567566819-3k1nk9q" \
          "d1vr39c42rmjr0dh24ngth0s4.apps.googleusercontent." \
          "com&response_type=code&scope=openid%20email%20profile" \
          "&redirect_uri=https%3A%2F%2Fthirdparty.aliexpress.com%2" \
          "Fggcallback.htm&state=iL7E8xPldkLkhvvMuLiwtlLofJ7jPTZ489rl" \
          "2fpSfRQI%2FF4Inm77rApP%2B%2FV11Oonu8S%2B1A1HFl4%3D&flowName" \
          "=GeneralOAuthFlow"
    driver.get(url)
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
    ActionChains(driver).move_to_element(page.help_header_2).perform()
    # Переход по ссылке на страницу споров и жалоб
    page.complaint_link.click()
    page = ComplaintPage(driver)
    # Проверка на наличие характерного элемента страницы споров и жалоб
    assert page.dispute_button.text == 'Open Dispute'

"""24. Проверка перехода на страницу загрузки приложения"""
def test_app_download():
    page = MainPage(driver)
    # Переход по ссылке на страницу загрузки приложения
    page.app_download_link.click()
    page = AppPages(driver)
    # Проверка на наличие характерного элемента страницы загрузки приложения
    assert page.google_play_button.get_attribute('class') == 'android-link'

"""25. Проверка перехода на страницу aliexpress"""
def test_vk_auth():
    page = MainPage(driver)
    # Переход по ссылке на страницу aliexpress
    page.ali_link.click()
    page = AliPage(driver)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "Header_Logo__mainLogo__1gbu2")))
    # Проверка на наличие характерного элемента страницы AliExpress
    assert page.ali_slogan.text == 'Покупай умнее, живи веселее!'








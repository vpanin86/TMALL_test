import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from pages.auth_page import AuthPage
from pages.main_page import MainPage
from pages.help_center_page import HelpCenterPage
from tests.settings import valid_google_email, valid_google_password,\
                    invalid_google_email, invalid_google_password, phone,\
                    first_name, last_name



driver = webdriver.Chrome()
wait = WebDriverWait(driver,10)

"""Запуск драйвера и открытие страницы авторизации"""
@pytest.fixture(autouse=True)
def load_auth_page():
    url = "https://accounts.google.com/o/oauth2/v2/auth/" \
          "oauthchooseaccount?client_id=438567566819-3k1nk9qd" \
          "1vr39c42rmjr0dh24ngth0s4.apps.googleusercontent.com&re" \
          "sponse_type=code&scope=openid%20email%20profile&redirect_" \
          "uri=https%3A%2F%2Fthirdparty.aliexpress.com%2Fggcallback." \
          "htm&state=iL7E8xPldkLkhvvMuLiwtlLofJ7jPTZ489rl2fpSfRQI%2FF4I" \
          "nm77rApP%2B%2FV11Oonu8S%2B1A1HFl4%3D&flowName=GeneralOAuthFlow"
    driver.get(url)

    yield

    #driver.quit()

"""1. Проверка авторизации через Google с валидными данными"""
def test_valid_gmail_auth():
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
    # Проверка наличия текста, характерного для авторизованного пользователя
    assert page.my_profile.text == 'Мой Профиль' or 'Профиль'

"""2. Проверка авторизации через Google с НЕвалидным паролем"""
def test_invalid_pass_gmail_auth():
    page = AuthPage(driver)
    # Ввод логина
    page.email = valid_google_email
    # Ожидание кнопки "Далее" с последующим нажатием
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "VfPpkd-RLmnJb")))
    page.proceed_btn_login.click()
    # Ожидание окна ввода пароля
    wait.until(EC.presence_of_element_located((By.ID, "password")))
    # Ввод пароля
    page.password = invalid_google_password
    page.proceed_btn_pass.click()
    # Проверка реакции системы на невалидный пароль
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "VfPpkd-vQzf8d")))
    assert page.invalid_pass.get_attribute('class') == 'EjBTad'

"""3. Проверка авторизации через Google с НЕвалидным логином"""
def test_invalid_login_gmail_auth():
    page = AuthPage(driver)
    # Ввод логина
    page.email = invalid_google_email
    # Ожидание кнопки "Далее" с последующим нажатием
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "VfPpkd-RLmnJb")))
    page.proceed_btn_login.click()
    # Проверка реакции системы на невалидный логин
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "o6cuMc")))
    assert page.invalid_login.text == 'Не удалось найти аккаунт Google.'

"""4. Проверка выхода из аккаунта"""
def test_quit():
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
    # Перевод курсора на вход через соцсети
    ActionChains(driver).move_to_element(page.user_acc_pnl_2).perform()
    # Нажатие на кнопку 'выход'
    page.quit_link.click()
    time.sleep(5)
    # Проверка наличия кнопки 'Войти'
    assert page.button_sign_in.text == 'Войти'

"""5. Проверка работы элемента checkbox 'показать пароль'"""
def test_checkbox():
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
    # Нажатие на checkbox
    page.checkbox.click()
    # Проверка аттрибута ввода строки пароля
    assert page.password.get_attribute('type') == 'text'

"""6. Проверка скрытия символов пароля после ввода email"""
def test_hidden_pass():
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
    # Проверка аттрибута ввода строки пароля
    assert page.password.get_attribute('type') == 'password'

"""7. Проверка перехода на страницу восстановления аккаунта"""
def test_acc_restore():
    page = AuthPage(driver)
    # Нажатие на кнопку "Забыли пароль"
    page.forgot_email_link.click()
    time.sleep(5)
    # Ввод имени и фамилии
    page.id_user = phone
    page.proceed_btn_pass_2.click()
    time.sleep(5)
    page.user_firstname = first_name
    page.user_lastname = last_name
    page.proceed_btn_pass_3.click()
    time.sleep(5)
    # Запрос на отправку кода
    page.send_btn.click()
    time.sleep(5)
    # Проверка попадания на страницу с вводом кода
    assert page.show_code_header.text == 'Укажите код'


"""8. Проверка перехода на страницу help-center"""
def test_help_center_link():
    page = AuthPage(driver)
    # Фиксация текущего окна
    original_window = driver.current_window_handle
    page.help_center_link.click()
    # Ожидание нового окна и переключение фокуса на новое окно
    wait.until(EC.number_of_windows_to_be(2))
    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break
    page = HelpCenterPage(driver)
    # Проверка заголовка страницы
    assert page.help_center_header.text == 'Help Center'

"""9. Проверка выбора языка"""
def test_language():
    page = AuthPage(driver)
    # Активация выпадающего списка
    page.list_box.click()
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "vRMGwf.oJeWuf")))
    # Выбор английского языка
    page.english.click()
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "ahT6S")))
    # Проверка заголовка
    assert page.sign_in_header_eng.text == 'Sign in'

import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from config import correct_email, correct_password, correct_phone_number, incorrect_password, \
    correct_login, correct_ls


@pytest.fixture(autouse=True)
def testing():
    # инициализация драйвера
    selenium = webdriver.Chrome()
    selenium.implicitly_wait(10)
    # открытие сайта
    selenium.get('https://b2c.passport.rt.ru')

    yield selenium
    selenium.quit()


# проверка, что пользователь может перейти на страницу авторизации
def test_authorization_1(testing):
    selenium = testing
    # открытие сайта
    selenium.get('https://b2c.passport.rt.ru')

    element = WebDriverWait(selenium, 10).until(EC.visibility_of_element_located((By.ID, 'kc-login')))

    assert selenium.find_element(By.TAG_NAME, 'h1').text == 'Авторизация', print('Test failed')
    assert selenium.find_element(By.ID, 'kc-login'), print('Test failed')


# проверка, что на странице авторизации есть продуктовый слоган
def test_authorization_2(testing):
    selenium = testing
    # открытие сайта
    selenium.get('https://b2c.passport.rt.ru')

    element = WebDriverWait(selenium, 10).until(EC.visibility_of_element_located((By.ID, 'kc-login')))

    assert selenium.find_element(By.TAG_NAME, 'p').text == 'Персональный помощник в цифровом мире Ростелекома', \
        print('Test failed')


# проверка, что доступна вкладка авторизации по номеру
def test_authorization_3(testing):
    selenium = testing
    # открытие сайта
    selenium.get('https://b2c.passport.rt.ru')

    element = WebDriverWait(selenium, 10).until(EC.visibility_of_element_located((By.ID, 'kc-login')))

    # таб "Телефон"
    selenium.find_element(By.ID, 't-btn-tab-phone').click()
    time.sleep(5)

    assert selenium.find_element(By.ID, 't-btn-tab-phone').text == 'Телефон', print('Test failed')


# проверка, что доступна вкладка авторизации по логину
def test_authorization_4(testing):
    selenium = testing
    # открытие сайта
    selenium.get('https://b2c.passport.rt.ru')

    element = WebDriverWait(selenium, 10).until(EC.visibility_of_element_located((By.ID, 'kc-login')))

    # таб "Логин"
    selenium.find_element(By.ID, 't-btn-tab-login').click()
    time.sleep(5)

    assert selenium.find_element(By.ID, 't-btn-tab-login').text == 'Логин', print('Test failed')


# проверка, что доступна вкладка авторизации по почте
def test_authorization_5(testing):
    selenium = testing
    # открытие сайта
    selenium.get('https://b2c.passport.rt.ru')

    element = WebDriverWait(selenium, 10).until(EC.visibility_of_element_located((By.ID, 'kc-login')))

    # таб "Почта"
    selenium.find_element(By.ID, 't-btn-tab-mail').click()
    time.sleep(5)

    assert selenium.find_element(By.ID, 't-btn-tab-mail').text == 'Почта', print('Test failed')


# проверка, что доступна вкладка авторизации по лицевому счету
def test_authorization_6(testing):
    selenium = testing
    # открытие сайта
    selenium.get('https://b2c.passport.rt.ru')

    element = WebDriverWait(selenium, 10).until(EC.visibility_of_element_located((By.ID, 'kc-login')))

    # таб "Лицевой счёт"
    selenium.find_element(By.ID, 't-btn-tab-ls').click()
    time.sleep(5)

    assert selenium.find_element(By.ID, 't-btn-tab-ls').text == 'Лицевой счёт', print('Test failed')


# проверка, что пользователь может войти в аккаунт с помощью корректно введённых данных (мобильный телефон и пароль)
def test_authorization_7(testing):
    selenium = testing
    # открытие сайта
    selenium.get('https://b2c.passport.rt.ru')

    element = WebDriverWait(selenium, 10).until(EC.visibility_of_element_located((By.ID, 'kc-login')))

    # нажать на "Телефон"
    selenium.find_element(By.ID, 't-btn-tab-phone').click()
    # ввод корректного номера телефона
    selenium.find_element(By.ID, 'username').send_keys(correct_phone_number)
    # ввод корректного пароля
    selenium.find_element(By.ID, 'password').send_keys(correct_password)
    # нажимаем на кнопку "Войти"
    selenium.find_element(By.XPATH, '//button[@type="submit"]').click()
    time.sleep(5)

    assert selenium.find_element(By.TAG_NAME, 'h3').text == 'Учетные данные', print('Test failed')


# проверка, что пользователь может войти в аккаунт с помощью корректно введённых данных (электронная почта и пароль)
def test_authorization_8(testing):
    selenium = testing
    # открытие сайта
    selenium.get('https://b2c.passport.rt.ru')

    element = WebDriverWait(selenium, 10).until(EC.visibility_of_element_located((By.ID, 'kc-login')))

    # нажать на "Почта"
    selenium.find_element(By.ID, 't-btn-tab-mail').click()
    # ввод корректного e-mail
    selenium.find_element(By.ID, 'username').send_keys(correct_email)
    # ввод корректного пароля
    selenium.find_element(By.ID, 'password').send_keys(correct_password)
    # нажимаем на кнопку "Войти"
    selenium.find_element(By.XPATH, '//button[@type="submit"]').click()
    time.sleep(5)

    assert selenium.find_element(By.TAG_NAME, 'h3').text == 'Учетные данные', print('Test failed')


# проверка, что пользователь может войти в аккаунт с помощью корректно введённых данных (логин и пароль)
def test_authorization_9(testing):
    selenium = testing
    # открытие сайта
    selenium.get('https://b2c.passport.rt.ru')

    element = WebDriverWait(selenium, 10).until(EC.visibility_of_element_located((By.ID, 'kc-login')))

    # нажать на "Почта"
    selenium.find_element(By.ID, 't-btn-tab-login').click()
    # ввод корректного e-mail
    selenium.find_element(By.ID, 'username').send_keys(correct_login)
    # ввод корректного пароля
    selenium.find_element(By.ID, 'password').send_keys(correct_password)
    # нажимаем на кнопку "Войти"
    selenium.find_element(By.XPATH, '//button[@type="submit"]').click()
    time.sleep(5)

    assert selenium.find_element(By.TAG_NAME, 'h3').text == 'Учетные данные', print('Test failed')
    
    
# проверка, что пользователь может войти в аккаунт с помощью корректно введённых данных (лицевой счет и пароль)
def test_authorization_10(testing):
    selenium = testing
    # открытие сайта
    selenium.get('https://b2c.passport.rt.ru')

    element = WebDriverWait(selenium, 10).until(EC.visibility_of_element_located((By.ID, 'kc-login')))

    # нажать на "Почта"
    selenium.find_element(By.ID, 't-btn-tab-ls').click()
    # ввод корректного e-mail
    selenium.find_element(By.ID, 'username').send_keys(correct_ls)
    # ввод корректного пароля
    selenium.find_element(By.ID, 'password').send_keys(correct_password)
    # нажимаем на кнопку "Войти"
    selenium.find_element(By.XPATH, '//button[@type="submit"]').click()
    time.sleep(5)

    assert selenium.find_element(By.TAG_NAME, 'h3').text == 'Учетные данные', print('Test failed')


# проверка, что введён верный номер телефона, но неверный пароль
def test_authorization_11(testing):
    selenium = testing
    # открытие сайта
    selenium.get('https://b2c.passport.rt.ru')

    element = WebDriverWait(selenium, 10).until(EC.visibility_of_element_located((By.ID, 'kc-login')))

    # нажать на "Телефон"
    selenium.find_element(By.ID, 't-btn-tab-phone').click()
    # ввод корректного номера телефона
    selenium.find_element(By.ID, 'username').send_keys(correct_phone_number)
    # ввод некорректного пароля
    selenium.find_element(By.ID, 'password').send_keys(incorrect_password)
    # нажимаем на кнопку "Войти"
    selenium.find_element(By.XPATH, '//button[@type="submit"]').click()
    time.sleep(5)

    assert selenium.find_element(By.ID, 'form-error-message').text == 'Неверный логин или пароль', \
        print('Test failed')


# проверка, что введена верная электронная почта, но неверный пароль
def test_authorization_12(testing):
    selenium = testing
    # открытие сайта
    selenium.get('https://b2c.passport.rt.ru')

    element = WebDriverWait(selenium, 10).until(EC.visibility_of_element_located((By.ID, 'kc-login')))

    # нажать на "Почта"
    selenium.find_element(By.ID, 't-btn-tab-mail').click()
    # ввод корректной электронной почты
    selenium.find_element(By.ID, 'username').send_keys(correct_email)
    # ввод некорректного пароля
    selenium.find_element(By.ID, 'password').send_keys(incorrect_password)
    # нажимаем на кнопку "Войти"
    selenium.find_element(By.XPATH, '//button[@type="submit"]').click()
    time.sleep(5)

    assert selenium.find_element(By.ID, 'form-error-message').text == 'Неверный логин или пароль', \
        print('Test failed')


# проверка, что введен верный логин, но неверный пароль
def test_authorization_13(testing):
    selenium = testing
    # открытие сайта
    selenium.get('https://b2c.passport.rt.ru')

    element = WebDriverWait(selenium, 10).until(EC.visibility_of_element_located((By.ID, 'kc-login')))

    # нажать на "Почта"
    selenium.find_element(By.ID, 't-btn-tab-login').click()
    # ввод корректной электронной почты
    selenium.find_element(By.ID, 'username').send_keys(correct_login)
    # ввод некорректного пароля
    selenium.find_element(By.ID, 'password').send_keys(incorrect_password)
    # нажимаем на кнопку "Войти"
    selenium.find_element(By.XPATH, '//button[@type="submit"]').click()
    time.sleep(5)

    assert selenium.find_element(By.ID, 'form-error-message').text == 'Неверный логин или пароль', \
        print('Test failed')


# проверка, что введен верный лицевой счёт, но неверный пароль
def test_authorization_14(testing):
    selenium = testing
    # открытие сайта
    selenium.get('https://b2c.passport.rt.ru')

    element = WebDriverWait(selenium, 10).until(EC.visibility_of_element_located((By.ID, 'kc-login')))

    # нажать на "Почта"
    selenium.find_element(By.ID, 't-btn-tab-ls').click()
    # ввод корректной электронной почты
    selenium.find_element(By.ID, 'username').send_keys(correct_ls)
    # ввод некорректного пароля
    selenium.find_element(By.ID, 'password').send_keys(incorrect_password)
    # нажимаем на кнопку "Войти"
    selenium.find_element(By.XPATH, '//button[@type="submit"]').click()
    time.sleep(5)

    assert selenium.find_element(By.ID, 'form-error-message').text == 'Неверный логин или пароль', \
        print('Test failed')


# проверка, что пользователь может перейти на страницу "Восстановление пароля"
def test_authorization_15(testing):
    selenium = testing
    # открытие сайта
    selenium.get('https://b2c.passport.rt.ru')

    element = WebDriverWait(selenium, 10).until(EC.visibility_of_element_located((By.ID, 'kc-login')))

    # нажимаем на кнопку "Забыл пароль"
    selenium.find_element(By.ID, 'forgot_password').click()

    assert selenium.find_element(By.TAG_NAME, 'h1').text == 'Восстановление пароля', print('Test failed')
    assert selenium.find_element(By.TAG_NAME, 'p').text == 'Введите данные и нажмите «Продолжить»', \
        print('Test failed')
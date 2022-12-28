Тестирование интерфейса авторизации на портале https://b2c.passport.rt.ru 

Для работы автотестов необходимы библиотеки Pytest и Selenium и webdriver Selenium. Также следует добавить корректные регданные конфиг.

Запустить тесты можно через терминал cmd:

python3 -m pytest -v --driver Chrome --driver-path chromedriver.exe test_authorization.py

или через Run в PyCharm

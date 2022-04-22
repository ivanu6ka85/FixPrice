# FixPrise
Тестовые сценарии проверяют кликабельность кнопок, равенство карточек товара и картинок к ним. 
Проверяется также присутствие элементов на странице.
Для запуска теста необходимо указать путь до файла chromedriver.exe. Для этого в PyCharm в левой колонке находим файл chromedriver.exe,
кликаем по нему правой клавишей мыши, выбираем Copy Path --> Absolute Path.
D:/SkillFactory/FixPrise_Final/chromedriver.exe. Дописываем путь до файла с тестами Tests\login.py.
python -m pytest -v --html=.\Reports\report.html --driver Chrome --driver-path - показываем с помощью каких инструментов
будет работать тест и в каком браузере. --html=.\Reports\report.html - формирует отчет в HTML. Полная команда для запуска теста получилась такая:
python -m pytest -v --html=.\Reports\report.html --driver Chrome --driver-path D:/SkillFactory/FixPrise_Final/chromedriver.exe Tests/login.py

# Сокращаем ссылки с помощью сервиса Bitly

### Как использовать скрипт

Запустить через командную строку файл скрипта

'''

python main.py [url]

'''

В результате работы программа автоматически определит тип ссылки (битли или нет)
Если это битли выведет статистику кликов
Если это любая другая ссылка выведет сокращенную сервисом битли ссылку

### Как установить

Python3 должен быть уже установлен.
Затем воспользуйтесь 'pip' (или 'pip3', есть конфликт с Python2) для установки зависимостей\

'''

pip install -r requirements.txt

'''

Рекомендуется использовать [virtualenv/venv](https://docs.python.org/3/library/venv.html) для изоляции проекта.

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
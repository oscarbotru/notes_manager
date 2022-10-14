# Менеджер заметок "ManNot"

## Общая техническая информация

### Требования

- python 3.6+

### Подготовка

1. `python -m venv env` - создание виртуального окружения
2. `source env/bin/activate` - активация виртуального окружения
3. `pip install -r requirements.txt` - установка зависимостей
4. `python manage.py createsuperuser` - создание админа
5. `python manage.py seeding` - начальное заполнение справочников

### Запуск

`python manage.py runserver`

## Дополнительно

### Пояснения

1. Использовал Bootstrap для визуала клиента, возможностей меньше, чем в ExtJS, но так для меня было быстрее
2. Хорошим вариантом, на мой взгляд, является сразу вынести отдельно приложение работы с пользователей и переопределить свою модель, чтобы потом ее было легче расширять и работать с ней
3. В качестве обработки ajax запросов реализовал работу с фильтрацией и списками. Сама по себе в datatable работа с ajax не очень подходит для этих задач, поэтому вытащил из старого проекта тот вариант, который подходил. Тут пришлось впихнуть все в один файл, вообще это все лучше унифицировать (DRY)
4. Не стал описывать получение переменных окружения, хотя пакет по привычке поставил, тут пока не для чего было (да, есть дебаг и доступные хосты, но смысла в этом не увидел, если бы были рассылки или интеграции, то да)
5. Тесты также не стал закладывать, хотя есть что потестировать, например те же права доступа
6. Проверкой на доступ обложил, но в силу того, что для идентификации используется uuid, не стал дополнять проверку на получение одиночных записей, хотя несколько раз порывался написать миксин для этого
7. В целом кое-где пренебрег вынесением общих блоков кода, которые повторяются, но делал это из-за того, что уже подзатянул со сроком сдачи
8. Не вынес sercet key из настроек также потому что не сделал перемененные окружения, то тем легче будет тестировать


### На развитие

Функционал, который я бы предложил реализовать в первую очередь для дальнейшего развития проекта

1. Добавить поле со сроком выполнения
2. Напоминания на почту о сроке выполнения через обычные крон задачи, в последствии можно перейти на очередь
3. Кастомизируемый список категорий для каждого пользователя
4. Настройки профиля пользователя как минимум для смены пароля
5. Верификация пользователя после регистрации
6. Восстановление пароля для пользователя

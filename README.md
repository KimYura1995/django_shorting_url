### Проверить работу можно по ссылке:
https://kim-yura-work.ru/

### Или можно запустить на локальной машине:
1. Установить Python 3.7.6
2. Установить модули из файла requirements.txt
3. Перейти в папку с проектом django_shorting_url
4. Применить миграции
    ``` python
    python manage.py migrate
    ```
5.  Запустить веб-сервер
    ``` python
    python manage.py runserver
    ```
6. Открыть браузер и перейти
    http://127.0.0.1:8000/
    
### Работа с API:
* Вы можете отправить GET запрос:
* https://kim-yura-work.ru/api/?original_url=<your_url>
* your_url - ссылка которую вы хотите укоротить
* В ответ вы получите JSON:
    ``` json
    {
    "original_url": "<your_url>",
    "redirect_url": "<shortened_url>"
    }
    ```

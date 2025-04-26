# Разработка FastAPI для интеграции с RetailCRM

## Регистрация в RetailCRM
1. Перейдите на сайт RetailCRM (https://www.retailcrm.ru/).
Зарегистрируйте тестовый аккаунт (обычно есть бесплатный тестовый период).
После регистрации войдите в систему.
2. В интерфейсе RetailCRM перейдите в "Настройки" → "Интеграция".
Нажмите "Добавить" для создания новой интеграции.
Сгенерируйте новый API ключ и сохраните его (он понадобится позже)


## Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/OlegShapovalov1990/RetailCRM_FastAPI_test
   
2. Активируйте виртуальное окружение в корне проекта:
    ```bash
   pip install virtualenv
    python -m venv .venv 
    .\.venv\Scripts\activate # для Windows
   
3. Установите poetry в вашем виртуальном окружении
    ```bash
   python -m pip install poetry
   
4. Установите зависимости
    ```bash
   python -m poetry install
   
5. Создайте файл .env с вашими учетными данными RetailCRM - RETAILCRM_API_URL, RETAILCRM_API_KEY


6. Запустите приложение в main.py или в терминале 
    ```bash
   uvicorn app.main:app --reload
   
## Docker
1. Установить Docker(если у вас Windows, установите Docker Desktop и WSL): https://docs.docker.com/engine/install/ubuntu/
2. Сборка и запуск контейнеров
    ```bash
   docker-compose up -d --build
   
## Тестирование API
1. После запуска приложения вы можете протестировать API с помощью Swagger UI:
http://localhost:8000/docs 
2. Добавление клиентов : POST http://localhost:8000/customers/
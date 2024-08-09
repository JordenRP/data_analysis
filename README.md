
# Data Analysis Project

## Описание
Этот проект предназначен для анализа экономических данных, связанных с заработными платами в России. В проекте используются Python и Docker для обеспечения повторяемости анализа и изолированного окружения.

## Структура проекта
- **data/**: Данные проекта
  - **raw/**: Исходные данные
  - **processed/**: Обработанные данные
  - **results/**: Результаты анализа
- **scripts/**: Скрипты анализа данных
- **Dockerfile**: Файл конфигурации Docker
- **requirements.txt**: Зависимости проекта
- **README.md**: Описание проекта
- **.gitignore**: Файл для исключения из контроля версий

## Установка и запуск
1. Склонируйте репозиторий:
    ```bash
    git clone https://github.com/yourusername/data-analysis-project.git
    ```
2. Соберите Docker-образ:docker build -t data-analysis-image .
    ```bash
    docker build -t data-analysis-image .
    ```
3. Запустите контейнер:
    ```bash
    docker run --rm --name data-analysis-container -v $(pwd)/data:/app/data data-analysis-image scripts/data_preparation.py
    docker run --rm --name data-analysis-container -v $(pwd)/data:/app/data data-analysis-image scripts/data_analysis.py
    ```

# Practica Project

Проект для практики Python с функционалом маркетплейса, корзины и скидок.  
Включает: 
- юнит-тесты для проверки функций расчета скидок
- UI-тесты для тестирования веб-страницы Wildberries
- генерацию документации для модуля маркетплейс с классами корзины и продукта
- статический анализ кода
- проверку покрытия кода тестами
- генерацию отчетов

---

## Установка зависимостей
В корне проекта выполните:

```bash
pip install pytest pytest-cov pytest-html selenium webdriver-manager chromedriver-autoinstaller Sphinx sphinx-autodoc-typehints pytest-metadata Jinja2 MarkupSafe docutils Pygments pylint
```

## Запуск UI-тестов 
в корне проекта

запуск ui-тестов
```bash
pytest ui_tests
```

запуск ui-тестов с генерацией html-отчета
```bash
pytest ui_tests/ --html=report.html --self-contained-html
```

## Запуск юнит-тестов 
в корне проекта

запуск юнит-тестов 
```bash
pytest unit_tests
```

запуск юнит-тестов с выводом отчета в консоль
```bash
pytest unit_tests/ --cov=app --cov-report=term-missing
```

запуск юнит-тестов с генерацией html-отчета
```bash
pytest unit_tests/ --cov=app --cov-report=term-missing --html=report.html --self-contained-html
```

## Запуск генерации документации 
в дирректории app

инициализация проекта документации
```bash
sphinx-quickstart
```

генерация документации 
```bash
.\make.bat html
``` 

анализ кода
```bash
pylint marketplace.py
```
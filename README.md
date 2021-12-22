

#### Команды для запуска из командной строки:

##### Показать меню:

python pizza.py menu

##### Сделать заказ (pepperoni, hawaiian или margherita, доступные размеры: L, XL), для доставки использовать флаг --delivery:

python pizza.py order pepperoni XL --delivery

#### Тесты:

python -m pytest pizza_tests.py

python -m pytest pizza_tests.py --cov . --cov-report html

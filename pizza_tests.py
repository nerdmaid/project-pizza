import pytest
import pizza
import fnmatch2
import random
from unittest.mock import patch
from click.testing import CliRunner

runner = CliRunner()


def test_str_output():
    assert pizza.Pepperoni('XL').__str__() == 'Pepperoni 🍕, размер XL'


def test_equal():
    assert pizza.Margherita('L') == \
           pizza.Pizza('Margherita 🧀', {'ingredients': ['tomato sauce', 'mozzarella', 'tomatoes']}, 'L')


def test_size_exception():
    with pytest.raises(ValueError):
        pizza.Hawaiian(size='M')


def test_menu():
    actual = runner.invoke(pizza.menu)
    assert actual.output == '-Margherita 🧀: tomato sauce, mozzarella, tomatoes\n' \
                            '-Pepperoni 🍕: tomato sauce, mozzarella, pepperoni\n' \
                            '-Hawaiian 🍍: tomato sauce, mozzarella, chicken, pineapples\n'


def test_order():
    actual = runner.invoke(pizza.order, ['pepperoni'])
    assert fnmatch2.fnmatch2(actual.output, 'Ваш заказ*аппетита!\n')


def test_log_pizza():
    my_pizza = pizza.Margherita('XL')
    with patch.object(random, 'randint') as rand:
        pizza.bake(my_pizza)
        rand.assert_called_once()

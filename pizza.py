import click
import random


class Pizza:
    def __init__(self, name, ingredients, size='L'):
        self.name = name
        self.size = size
        self.ingredients = ingredients

    def menu_position(self):
        """Показывает, как пицца будет
             отображаться в меню"""
        menu_position = ', '.join(self.ingredients.get('ingredients'))
        return f'-{self.name}: {menu_position}'

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if value not in ['L', 'XL']:
            raise ValueError('У нас только большие размеры')
        self.__size = value

    def dict(self):
        """Выводит рецепт пиццы в виде словаря"""
        print(f"{self.name}:{self.ingredients}")

    def __eq__(self, other):
        if isinstance(other, Pizza):
            if self.name == other.name and self.size == other.size:
                return True
        return False

    def __str__(self):
        return f'{self.name}, размер {self.size}'


class Margherita(Pizza):
    def __init__(self, size='L'):
        self.size = size
        self.name = 'Margherita 🧀'
        self.ingredients = {'ingredients': ['tomato sauce', 'mozzarella', 'tomatoes']}


class Pepperoni(Pizza):
    def __init__(self, size='L'):
        self.size = size
        self.name = 'Pepperoni 🍕'
        self.ingredients = {'ingredients': ['tomato sauce', 'mozzarella', 'pepperoni']}


class Hawaiian(Pizza):
    def __init__(self, size='L'):
        self.size = size
        self.name = 'Hawaiian 🍍'
        self.ingredients = {'ingredients': ['tomato sauce', 'mozzarella', 'chicken', 'pineapples']}


@click.group()
def cli():
    pass


def log(text):
    """Выводит рандомное время выполнения"""
    def decorator(function):
        def wrapper(*args, **kwargs):
            function(*args, **kwargs)
            time = random.randint(1, 200)
            print(text.format(str(time)))

        return wrapper

    return decorator


@log('👨🏻‍🍳 Приготовили за {} с!')
def bake(pizza: Pizza):
    """Готовит пиццу"""


@log('🛵 Доставили за {} с!')
def deliver(pizza: Pizza):
    """Доставляет пиццу"""


@log('🏠 Забрали за {}с!!')
def pickup(pizza: Pizza):
    """Забирает пиццу"""


@cli.command()
@click.option('--delivery', default=False, is_flag=True)
@click.argument('pizza', nargs=1)
@click.argument('size', default='L')
def order(pizza, size, delivery: bool):
    """Заказать пиццу (ее приготовят и, если нужно, доставят)"""
    if pizza == 'margherita':
        order_pizza = Margherita(size)
    elif pizza == 'pepperoni':
        order_pizza = Pepperoni(size)
    elif pizza == 'hawaiian':
        order_pizza = Hawaiian(size)
    else:
        click.echo('Пожалуйста, выберите из: margherita, pepperoni, hawaiian')
        return
    click.echo(f'Ваш заказ: {(order_pizza)}')
    bake(order_pizza)

    if delivery:
        deliver(order_pizza)
    else:
        pickup(order_pizza)

    click.echo('Приятного аппетита!')


@cli.command()
def menu():
    """Выводит меню"""
    click.echo(Margherita().menu_position())
    click.echo(Pepperoni().menu_position())
    click.echo(Hawaiian().menu_position())


if __name__ == '__main__':
    cli()

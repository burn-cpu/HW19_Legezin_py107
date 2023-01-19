# HW декоратор дебаг
def debug(func):

    def wrapper(*args):
        print(func.__name__)
        print(*args)
        return func(*args)

    return wrapper


@debug
def amount(k, b):
    return k + b


ex = amount(3, 5)
print(ex)

# Счетчик вызываемой фунцкции
def count(func):

    def wrapper(*args):
        wrapper.count += 1
        return func(*args)
    wrapper.count = 0
    return wrapper


@count
def amount():
    print(123)


amount()
amount()
print(amount.count)



class Tomato:
    states = {1 : 'Зеленые',
              2 : 'Желтые',
              3 : 'Красные'}

    def __init__(self, _index):
        self._index = _index
        self._state = 1

    def grow(self):
        if self._state < 3:
            self._state += 1


    def is_ripe(self):
        if self._state == 3:
            return f'Томат созрел {self._state}'


class TomatoBush:

    def __init__(self, amount):
        self.amount = amount
        self.tomates = [Tomato(i) for i in range(amount)]


    def grow_all(self):
        for i in self.tomates:
            if i == 3:
                pass
            else:
                return i.grow()



    def all_are_ripe(self):
        counter = 0
        for i in self.tomates:
            if i.is_ripe():
                counter += 1
        return counter == self.amount

    def give_away_all(self):
        self.tomates.clear()


class Gardener:

    def __init__(self, name, _plant):
        self.name = name
        self._plant = _plant

    def work(self):
        self._plant.grow_all()
        return f'{self.name}'


    def harvest(self):
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            return f'Плоды созрели'
        else:
            return f'Плоды еще не созрели'


    @staticmethod
    def knowledge_base():
        print()


Gardener.knowledge_base()
a = TomatoBush(7)
c = Gardener("Tom", a)
print(c.work())
print(c.harvest())
print(c.work())
print(c.harvest())


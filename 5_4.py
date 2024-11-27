class House:
    houses_history = []  # История построек

    def __new__(cls, *args, **kwargs):
        # Добавляем название здания в историю
        cls.houses_history.append(args[0])  # args[0] — название здания
        return super().__new__(cls)

    def __init__(self, name, floors):
        self.name = name
        self.floors = floors

    def __del__(self):
        # Сообщение при удалении объекта
        print(f"{self.name} снесён, но он останется в истории")


# Пример работы программы
h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)

h2 = House('ЖК Акация', 20)
print(House.houses_history)

h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)

# Пример удаления последнего объекта
del h1


''' Пояснения:

Метод __new__:

            При создании объекта добавляет название здания (первый аргумент args) в список houses_history, который является атрибутом класса.
            Возвращает созданный объект с помощью вызова super().__new__(cls).

Метод __init__:

            Инициализирует экземпляр, добавляя параметры объекта, такие как name и floors.

Метод __del__:

              Вызывается при удалении объекта. В данном случае он выводит сообщение о сносе здания.

Список houses_history:

                Хранит историю всех созданных зданий, даже после их удаления.'''
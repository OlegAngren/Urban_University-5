class House:
    def __init__(self, name, number_of_floors):
        # Инициализация объекта
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        # Логика перемещения на этаж
        if 1 <= new_floor <= self.number_of_floors:
            for floor in range(1, new_floor + 1):
                print(floor)
        else:
            print("Такого этажа не существует")


# Создаем объекты класса House
h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)

# Вызываем метод go_to с произвольным числом
h1.go_to(5)  # Выводит 1, 2, 3, 4, 5
h2.go_to(10)  # Выводит "Такого этажа не существует"
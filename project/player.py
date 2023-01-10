from project.core.validator import Validator


class Player:
    used_names = set()

    def __init__(self, name: str, age: int, stamina=100):
        self.name = name
        self.age = age
        self.stamina = stamina

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.if_string_is_empty(value, "Name not valid!")  # or if not Value
        if value in self.used_names:
            raise Exception(f"Name {value} is already used!")
        self.used_names.add(value)
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        Validator.if_value_is_negative(value, f"The player cannot be under {value} years old!")
        self.__age = value

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, value):
        Validator.value_is_in_range(value, 0, 100, "Stamina not valid!")
        self.__stamina = value

    @property
    def need_sustenance(self):
        return self.stamina < 100

    def __str__(self):
        return f"Player: {self.name}, {self.age}, {self.stamina}, {self.need_sustenance}"

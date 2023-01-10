class Validator:
    @staticmethod
    def if_string_is_empty(value, message):
        if value == "":
            raise ValueError(message)

    @staticmethod
    def if_value_is_negative(value, message):
        if value < 0:
            raise ValueError(message)

    @staticmethod
    def value_is_in_range(value, min_value, max_value, message):
        if value < min_value or value > max_value:
            raise ValueError(message)

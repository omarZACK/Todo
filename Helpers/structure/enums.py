from enum import Enum

class ChoiceEnum(Enum):
    @classmethod
    def choices(cls):
        return [(member.value, member.name.capitalize()) for member in cls]

    @classmethod
    def values(cls):
        return [member.value for member in cls]

    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)
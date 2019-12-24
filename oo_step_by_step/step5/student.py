from oo_step_by_step.step5.klass import Klass
from oo_step_by_step.step5.person import Person


class Student(Person):

    def __init__(self, id, name, age, klass) -> None:
        super().__init__(id, name, age)
        self.klass = klass

    def introduce(self):
        result = self.__basic_introduce()
        if self.klass.has_leader(self):
            result += " I am Leader of {self.klass}.".format(self=self)
        else:
            result += " I am at {self.klass}.".format(self=self)
        return result

    def __basic_introduce(self):
        result = super().introduce() + " I am a Student."
        return result

    def with_name(self, handler) -> str:
        return handler(self.name)

    def in_klass(self, klass: Klass) -> bool:
        return self.klass.eqauls(klass)

    def equals(self, other):
        return self.id == other.id

    def resign_to(self, klass):
        self.klass = klass

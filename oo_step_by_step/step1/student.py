from oo_step_by_step.step1.person import Person


class Student(Person):

    def __init__(self, name, age, klass) -> None:
        super().__init__(name, age)
        self.klass = klass

    def introduce(self):
        return super().introduce() + " I am a Student. I am at Class {self.klass}.".format(self=self)



from oo_step_by_step.step1.person import Person


class Teacher(Person):

    def __init__(self, name, age, klass) -> None:
        super().__init__(name, age)
        self.klass = klass

    def introduce(self):
        result =  super().introduce() + " I am a Teacher."
        if self.klass != None:
            result += " I teach {self.klass}.".format(self=self)
        else:
            result += " I teach No Class."
        return result


from oo_step_by_step.step3.person import Person
from oo_step_by_step.step3.student import Student


class Teacher(Person):

    def __init__(self, id, name, age, klass) -> None:
        super().__init__(id, name, age)
        self.klass = klass

    def introduce(self) -> str:
        result = self.__basic_introduce()
        if self.klass != None:
            result += " I teach {self.klass}.".format(self=self)
        else:
            result += " I teach No Class."
        return result

    def __basic_introduce(self):
        result = super().introduce() + " I am a Teacher."
        return result

    def introduceWith(self, student:Student) -> str:
        result = self.__basic_introduce()
        with_student_name = student.with_name(lambda name: name + ".")
        if(student.inKlass(self.klass)):
            result += " I teach " + with_student_name
        else:
            result += " I don't teach " + with_student_name

        return result



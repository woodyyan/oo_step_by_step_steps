from oo_step_by_step.step5.observer import Observer
from oo_step_by_step.step5.person import Person
from oo_step_by_step.step5.student import Student


class Teacher(Person, Observer):

    def __init__(self, id, name, age, klasses) -> None:
        super().__init__(id, name, age)
        self.klasses = klasses

    def update(self, student_info):
        print('I am %s. I know %s has joined Class %s.' % (self.name, student_info.name, student_info.klass_number))

    def introduce(self) -> str:
        result = self.__basic_introduce()
        if len(self.klasses) != 0:
            klasses_str = ",".join(map(lambda klass: str(klass.klass_number), self.klasses))
            result += " I teach Class {klasses}.".format(klasses=klasses_str)
        else:
            result += " I teach No Class."
        return result

    def __basic_introduce(self):
        result = super().introduce() + " I am a Teacher."
        return result

    def introduce_with(self, student: Student) -> str:
        result = self.__basic_introduce()
        with_student_name = student.with_name(lambda name: name + ".")
        if any(list(map(lambda klass: student.in_klass(klass), self.klasses))):
            result += " I teach " + with_student_name
        else:
            result += " I don't teach " + with_student_name

        return result

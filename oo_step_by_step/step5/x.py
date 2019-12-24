from oo_step_by_step.step5.klass import Klass
from oo_step_by_step.step5.observer import Observer, StudentInfo


class X(Observer):
    def __init__(self, klass: Klass):
        self.klass = klass

    def update(self, student_info: StudentInfo):
        if student_info.klass_number == self.klass.klass_number:
            if student_info.is_leader:
                print('I am the Machine. I know %s become Leader of Class %s.' % (
                    student_info.name, student_info.klass_number))
            else:
                print(
                    'I am the Machine. I know %s has joined Class %s.' % (student_info.name, student_info.klass_number))

# coding:utf-8
import unittest

from oo_step_by_step.step5.klass import Klass
from oo_step_by_step.step5.student import Student
from oo_step_by_step.step5.teacher import Teacher


class TestTeacher(unittest.TestCase):
    def test_teacher_say_student_joined_class(self):
        student = Student("1", "Tom", 18, Klass(1))
        klass = Klass(1)
        teacher = Teacher("1", "Jerry", 18, [Klass(2)])
        klass.attach(teacher)
        klass.append_member(student)
        klass.notify()


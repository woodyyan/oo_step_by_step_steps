# coding:utf-8
import io
import sys
import unittest

from oo_step_by_step.step5.klass import Klass
from oo_step_by_step.step5.student import Student
from oo_step_by_step.step5.teacher import Teacher
from oo_step_by_step.step5.x import X


class TestTeacher(unittest.TestCase):
    def test_teacher_say_student_joined_class(self):
        sys.stdout = io.StringIO()
        student = Student("1", "Tom", 18, Klass(1))
        klass = Klass(2)
        teacher = Teacher("1", "Jerry", 18, [Klass(2)])
        klass.register(teacher)
        klass.append_member(student)
        self.assertEqual(str(sys.stdout.getvalue()), 'I am Jerry. I know Tom has joined Class 2.\n')

    def test_teacher_say_student_became_leader(self):
        sys.stdout = io.StringIO()
        klass = Klass(1)
        student = Student("1", "Tom", 18, klass)
        teacher = Teacher("1", "Jerry", 18, [klass])
        klass.register(teacher)
        klass.assign_leader(student)
        self.assertEqual(str(sys.stdout.getvalue()), 'I am Jerry. I know Tom become Leader of Class 1.\n')

    def test_teacher_and_x_say_student_joined_class(self):
        sys.stdout = io.StringIO()
        student = Student("1", "Tom", 18, Klass(1))
        klass = Klass(2)
        teacher = Teacher("1", "Jerry", 18, [Klass(2)])
        x = X(klass)
        klass.register(teacher)
        klass.register(x)
        klass.append_member(student)
        self.assertEqual(str(sys.stdout.getvalue()),
                         'I am Jerry. I know Tom has joined Class 2.\nI am the Machine. I know Tom has joined Class 2.\n')

    def test_teacher_and_x_say_student_became_leader(self):
        sys.stdout = io.StringIO()
        klass = Klass(1)
        student = Student("1", "Tom", 18, klass)
        teacher = Teacher("1", "Jerry", 18, [klass])
        x = X(klass)
        klass.register(teacher)
        klass.register(x)
        klass.assign_leader(student)
        self.assertEqual(str(sys.stdout.getvalue()),
                         'I am Jerry. I know Tom become Leader of Class 1.\nI am the Machine. I know Tom become Leader of Class 1.\n')

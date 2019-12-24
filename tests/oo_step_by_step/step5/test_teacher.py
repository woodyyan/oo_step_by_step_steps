# coding:utf-8
import io
import sys
import unittest

from oo_step_by_step.step5.klass import Klass
from oo_step_by_step.step5.student import Student
from oo_step_by_step.step5.teacher import Teacher


def stub_stdout(testcase_inst):
    stderr = sys.stderr
    stdout = sys.stdout

    def cleanup():
        sys.stderr = stderr
        sys.stdout = stdout

    testcase_inst.addCleanup(cleanup)
    sys.stderr = io.StringIO()
    sys.stdout = io.StringIO()


class TestTeacher(unittest.TestCase):
    def test_teacher_say_student_joined_class(self):
        stub_stdout(self)
        student = Student("1", "Tom", 18, Klass(1))
        klass = Klass(2)
        teacher = Teacher("1", "Jerry", 18, [Klass(2)])
        klass.register(teacher)
        klass.append_member(student)
        self.assertEqual(str(sys.stdout.getvalue()), 'I am Jerry. I know Tom has joined Class 2.\n')

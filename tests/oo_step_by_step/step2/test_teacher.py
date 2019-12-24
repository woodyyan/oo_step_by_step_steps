# coding:utf-8
import unittest

from oo_step_by_step.step2.klass import Klass
from oo_step_by_step.step2.teacher import Teacher


class TestTeacher(unittest.TestCase):
    def test_basic_introduce(self):
        person = Teacher("Tom", 21, Klass(2))

        actual = person.introduce()

        self.assertEqual(actual, "My name is Tom. I am 21 years old. I am a Teacher. I teach Class 2.")

    def test_basic_introduce_with_no_klass(self):
        person = Teacher("Tom", 21, None)

        actual = person.introduce()

        self.assertEqual(actual, "My name is Tom. I am 21 years old. I am a Teacher. I teach No Class.")


if __name__ == '__main__':
    unittest.main()

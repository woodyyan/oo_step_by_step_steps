# coding:utf-8
import unittest

from oo_step_by_step.step1.student import Student


class TestStudent(unittest.TestCase):
    def test_basic_introduce(self):
        person = Student("Tom", 21, 2)

        actual = person.introduce()

        self.assertEqual(actual, "My name is Tom. I am 21 years old. I am a Student. I am at Class 2.")


if __name__ == '__main__':
    unittest.main()

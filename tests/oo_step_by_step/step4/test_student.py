# coding:utf-8
import unittest

from oo_step_by_step.step4.klass import Klass
from oo_step_by_step.step4.student import Student


class TestStudent(unittest.TestCase):
    def test_basic_introduce(self):
        person = Student("1","Tom", 21, Klass(2))

        actual = person.introduce()

        self.assertEqual(actual, "My name is Tom. I am 21 years old. I am a Student. I am at Class 2.")

    def test_leader_introduce_as_leader(self):
        klass = Klass(2)
        person = Student("1", "Tom", 21, klass)
        klass.assign_leader(person)

        actual = person.introduce()

        self.assertEqual(actual, "My name is Tom. I am 21 years old. I am a Student. I am Leader of Class 2.")

if __name__ == '__main__':
    unittest.main()

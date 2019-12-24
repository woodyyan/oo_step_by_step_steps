# coding:utf-8
import unittest

from oo_step_by_step.step4.klass import Klass
from oo_step_by_step.step4.student import Student


class TestKlass(unittest.TestCase):
    def test_append_member(self):
        klass = Klass(2)
        person = Student("1", "Tom", 21, Klass(1))
        klass.append_member(person)
        self.assertEqual(person.klass, klass)

    def test_assign_leader_that_not_in_this_klass(self):
        klass2 = Klass(2)
        klass1 = Klass(1)
        person = Student("1", "Tom", 21, klass1)
        klass2.assign_leader(person)

        actual = person.introduce()

        self.assertNotEqual(klass2.leader, person)
        self.assertNotEqual(klass2, person.klass)
        self.assertEqual(actual, "My name is Tom. I am 21 years old. I am a Student. I am at Class 1.")

if __name__ == '__main__':
    unittest.main()

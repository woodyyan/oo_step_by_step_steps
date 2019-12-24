# coding:utf-8
import unittest
from oo_step_by_step.step3.person import Person


class TestPerson(unittest.TestCase):
    def test_basic_introduce(self):
        person = Person("1","Tom", 21)

        actual = person.introduce()

        self.assertEqual(actual, "My name is Tom. I am 21 years old.")


if __name__ == '__main__':
    unittest.main()

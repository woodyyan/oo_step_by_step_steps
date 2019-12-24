# coding:utf-8
import unittest

from oo_step_by_step.step3.klass import Klass
from oo_step_by_step.step3.student import Student
from oo_step_by_step.step3.teacher import Teacher


class TestTeacher(unittest.TestCase):
    def test_basic_introduce(self):
        person = Teacher("1", "Tom", 21, Klass(2))

        actual = person.introduce()

        self.assertEqual(actual, "My name is Tom. I am 21 years old. I am a Teacher. I teach Class 2.")

    def test_basic_introduce_with_no_klass(self):
        person = Teacher("1", "Tom", 21, None)

        actual = person.introduce()

        self.assertEqual(actual, "My name is Tom. I am 21 years old. I am a Teacher. I teach No Class.")


    def test_introduce_with_given_student_that_I_am_teaching(self):
        teacherTom = Teacher("1", "Tom", 21, Klass(2))
        studentJerry = Student("1", "Jerry", 18, Klass(2))

        actual = teacherTom.introduceWith(studentJerry)

        self.assertEqual(actual, "My name is Tom. I am 21 years old. I am a Teacher. I teach Jerry.")

    def test_introduce_with_given_student_that_I_am_not_teaching(self):
        teacherTom = Teacher("1", "Tom", 21, Klass(2))
        studentJerry = Student("1", "Jerry", 18, Klass(3))

        actual = teacherTom.introduceWith(studentJerry)

        self.assertEqual(actual, "My name is Tom. I am 21 years old. I am a Teacher. I don't teach Jerry.")

if __name__ == '__main__':
    unittest.main()

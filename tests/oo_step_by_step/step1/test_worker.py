# coding:utf-8
import unittest

from oo_step_by_step.step1.worker import Worker


class TestWorker(unittest.TestCase):
    def test_basic_introduce(self):
        person = Worker("Tom", 21)

        actual = person.introduce()

        self.assertEqual(actual, "My name is Tom. I am 21 years old. I am a Worker. I have a job.")



if __name__ == '__main__':
    unittest.main()

import unittest
import sys
import os
import std


class TestRoot(unittest.TestCase):

    def test_root_program(self):
        sys.stdout = open('std_out_result', 'w')
        std.input("hello world")
        sys.stdout.close()
        self.assertEqual(in_stdout(), "hello world\n")

    def tearDown(self):
        os.remove('std_out_result')


class TestCase1(unittest.TestCase):

    def test_case_1(self):
        sys.stdout = open('std_out_result', 'w')
        std.input("hello23world", 1)
        sys.stdout.close()
        self.assertEqual(in_stdout(), "dnvk\n")

    def tearDown(self):
        os.remove('std_out_result')


class TestCase2(unittest.TestCase):

    def test_case_2(self):
        std.input("hello23world", 2)
        with open('file_11', 'r') as fh:
            output = fh.read()

        self.assertEqual(output, "dnvk")


class TestCase3(unittest.TestCase):

    def test_case_3(self):
        sys.stdout = open('std_out_result', 'w')
        std.input("hello23world", 3)
        sys.stdout.close()
        self.assertEqual(in_stdout(), "hoo\n")

    def tearDown(self):
        os.remove('std_out_result')


def in_stdout():
    return open('std_out_result', 'r').read()


def main():
    unittest.main()

if __name__ == '__main__':
    main()

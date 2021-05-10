import unittest
import main


class TestMain(unittest.TestCase):
    def setUp(self):  # sets up before start of test

        print('about to run a function')  # this is printed before each test

    def test_do_stuff(self):
        ''' HIIIIIIII'''  # to add comment
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15)  # test that result equals 15
        # self.assertEqual(result, 10)  # this worked on terminal and not console

    def test_do_stuff2(self):
        test_param = 'shkshks'
        result = main.do_stuff(test_param)  # this will give a value error cos of the param
        self.assertTrue(isinstance(result, ValueError))
        # to check that result is an instance of valueerror,
        # to check if assertion is true... it gives u ok for the two tests
        # self.assertIsInstance(result, ValueError) this can be used

    def test_do_stuff3(self):
        test_param = None
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'please enter a number')

    def test_do_stuff4(self):
        test_param = ''
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'please enter a number')

    def tearDown(self):  # at the end of test
        print('cleaning up')  # printed after each test


if __name__ == '__main__':
    print(unittest.main())
# print(TestMain())

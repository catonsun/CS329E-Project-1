import unittest
from app import returnSuccess, getFileName


class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual("success", returnSuccess())

    def test1(self):
        self.assertNotEqual("error", returnSuccess())

    def test3(self):
        self.assertEqual("", getFileName())

    def test4(self):
        self.assertEqual(getFileName()[-3:].lower(), "jpg")


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MyTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
    unittest.main()

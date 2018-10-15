import unittest
from app import returnSuccess, getFileName, setFileName, uploadAction


class MyTest(unittest.TestCase):
    def test1(self):
        self.assertEqual("success", returnSuccess())

    def test2(self):
        self.assertNotEqual("error", returnSuccess())

    def test3(self):
        self.assertNotEqual("", getFileName())

    def test4(self):
        self.assertEqual(getFileName()[-3:].lower(), "jpg")

    def test5(self):
        self.assertEqual("picture.jpg", setFileName("picture.jpg"))

    def test6(self):
        self.assertEqual("picture opened successfully", uploadAction('static/picture.jpg'))


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MyTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
    unittest.main()

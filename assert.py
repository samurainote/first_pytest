
# プログラムをテストすることは、「想定結果」と「実行結果」を比べること
import unittest

# テストクラス（テストケースメソッド）
class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")
    def test_not_upper(self):
        self.assertNotEqual("foo".upper(), "foo")
    def test_is_digit(self):
        self.assertTrue("123".isdigit())
    def test_is_not_digit(self):
        self.assertFalse("123ppap".isdigit())

import unittest


import unittest
import sys

sys.path.append("../src")
from dic import myDic

class TestBch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setUpClass')
        cls.path = '../datas/dics/0.txt'
    
    def test_find_list(self):
        d = myDic(self.path)
        word, flag = d.find('半老徐娘', 0)
        self.assertEqual(word, '半老徐娘')
        self.assertTrue(flag)
        word, flag = d.find('残花败柳', 1)
        self.assertEqual(word, '残花败柳')
        self.assertTrue(flag)
        word, flag = d.find('彷徨', 0)
        self.assertFalse(flag)
        word, flag = d.find('包含', 0)
        self.assertEqual(word, '包含')
        self.assertTrue(flag)
        word, flag = d.find('包含', 1)
        self.assertEqual(word, '包括')
        self.assertTrue(flag)

if __name__ == '__main__':
    unittest.main()
import unittest
import task


class TestCase(unittest.TestCase):

    def test1(self):
        self.assertTrue(True)

    def test_num_1(self):
        num = 12345
        s_to_num = task.conv_num('12345')
        self.assertEqual(s_to_num, num,
                         msg='{} is not {}'.format(s_to_num, num))

    def test_num_2(self):
        num = -123.45
        s_to_num = task.conv_num('-123.45')
        self.assertEqual(s_to_num, num,
                         msg='{} is not {}'.format(s_to_num, num))

    def test_num_3(self):
        num = 0.45
        s_to_num = task.conv_num('0.45')
        self.assertEqual(s_to_num, num,
                         msg='{} is not {}'.format(s_to_num, num))

    def test_num_4(self):
        num = 123.0
        s_to_num = task.conv_num('123.')
        self.assertEqual(s_to_num, num,
                         msg='{} is not {}'.format(s_to_num, num))

    def test_num_5(self):
        num = 2772
        s_to_num = task.conv_num('0xAD4')
        self.assertEqual(s_to_num, num,
                         msg='{} is not {}'.format(s_to_num, num))

    def test_num_6(self):
        self.assertIsNone(task.conv_num('0xAZ4'), msg='{} should be None'
                          .format(task.conv_num('0xAZ4')))

    def test_num_7(self):
        self.assertIsNone(task.conv_num(''), msg='{} should be None'
                          .format(task.conv_num('')))

    def test_num_8(self):
        self.assertIsNone(task.conv_num('12345A'), msg='{} should be None')

    def test_num_9(self):
        self.assertIsNone(task.conv_num('12.3.45'), msg='{} has more than'
                                                        'one decimal')

    def test_num_10(self):
        num = 0.0
        s_to_num = task.conv_num('0.0')
        self.assertEqual(s_to_num, num,
                         msg='{} is not {}'.format(s_to_num, num))

    def test_num_11(self):
        num = 0.
        s_to_num = task.conv_num('0.')
        self.assertEqual(s_to_num, num,
                         msg='{} is not {}'.format(s_to_num, num))


if __name__ == '__main__':
    unittest.main()

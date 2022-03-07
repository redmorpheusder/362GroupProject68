from task import my_datetime


class MyTestCase(unittest.TestCase):
    def test_datetime_1(self):
        date_return = "11-29-1973"
        self.assertEqual(my_datetime(123456789), date_return)

    def test_datetime_2(self):
        date_return = "01-01-1970"
        self.assertEqual(my_datetime(0), date_return)

    def test_datetime_3(self):
        date_return = "12-22-2282"
        self.assertEqual(my_datetime(9876543210), date_return)

    def test_datetime_4(self):
        date_return = "02-29-8360"
        self.assertEqual(my_datetime(201653971200), date_return)

    def test_datetime_5(self):
        date_return = "09-25-1986"
        self.assertEqual(my_datetime(527990400), date_return)

    def test_datetime_6(self):
        date_return = "10-31-2022"
        self.assertEqual(my_datetime(1667174400), date_return)

    def test_datetime_7(self):
        date_return = "10-30-1980"
        self.assertEqual(my_datetime(341712000), date_return)

    def test_datetime_8(self):
        date_return = "02-28-1972"
        self.assertEqual(my_datetime(68083200), date_return)

    def test_datetime_9(self):
        date_return = "07-30-1976"
        self.assertEqual(my_datetime(207532800), date_return)

    def test_datetime_10(self):
        date_return = "03-01-1976"
        self.assertEqual(my_datetime(194486400), date_return)

    def test_datetime_11(self):
        date_return = "09-01-1976"
        self.assertEqual(my_datetime(210384000), date_return)

    def test_datetime_12(self):
        date_return = "11-01-1976"
        self.assertEqual(my_datetime(215654400), date_return)

    def test_datetime_13(self):
        date_return = "01-01-2030"
        self.assertEqual(my_datetime(1893456000), date_return)

    def test_datetime_14(self):
        date_return = "01-01-2121"
        self.assertEqual(my_datetime(4765132800), date_return)

    def test_datetime_15(self):
        date_return = "01-01-1973"
        self.assertEqual(my_datetime(94694400), date_return)


if __name__ == '__main__':
    unittest.main()

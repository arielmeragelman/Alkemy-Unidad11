import sys
import datetime
import unittest
sys.path.append("..")
import functions.functions as f


class Test2(unittest.TestCase):

    def test_sumas(self):

        self.assertEqual(f.sumar(1, 2, 3, 4, 5), 15)
        self.assertEqual(f.sumar(-1, -2, -3, -4, -5), -15)
        self.assertEqual(f.sumar(1, 2, 3, -4, -5), -3)
        self.assertEqual(f.restar(0, 2,), -2)


def insert_header(data):
    data.write('\n')
    data.write('******************TESTING**************************')
    data.write('\n')
    now = datetime.datetime.now()
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    data.write(date_time)
    data.write('\n')
    return data


def main(out=sys.stderr, verbosity=2):
    loader = unittest.TestLoader()

    suite = loader.loadTestsFromModule(sys.modules[__name__])
    unittest.TextTestRunner(out, verbosity=verbosity).run(suite)


if __name__ == '__main__':
    with open('testing.txt', 'a') as data:
        data = insert_header(data)
        main(data)

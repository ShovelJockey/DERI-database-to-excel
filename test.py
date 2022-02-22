import unittest
import main


class DBDataImportTest(unittest.TestCase):
    def setUp(self):
        self.instance = main.DBDataImport()
        self.filename = 'LSOA, ward and LA DB.csv'

    def test_get_data_len(self):
        actual = self.instance.get_data(self.filename)
        expected = 34754
        actual = len(actual)
        assert(actual == expected)

    def test_get_data_retrieve(self):
        data_list = self.instance.get_data(self.filename)
        actual = data_list[1][6]
        expected = 'Middlesbrough'
        assert(actual == expected)


class DataMerge(unittest.TestCase):
    def setUp(self):
        self.instance = main.DataMerge()
        self.LA_data_mock = [
            ['1','E01012053','Middlesbrough 009A','E05009862','Linthorpe','E06000002','Middlesbrough'], 
            ['26252','E01010483','Wolverhampton 007B','E05001325','Bushbury South and Low Hill','E08000031','Wolverhampton'],
            ['26353','E01010199','Solihull 018A','E05001296','Shirley East','E08000029','Solihull']
        ]

    def test_list_to_dict_LA_data(self):
        self.instance.list_to_dict_LA_data(self.LA_data_mock)
        assert(len(self.instance.LA_dict) == 2)
        assert(self.instance.LA_dict['E01010199'][3] == 'Solihull')


unittest.main()
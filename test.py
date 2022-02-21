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

unittest.main()
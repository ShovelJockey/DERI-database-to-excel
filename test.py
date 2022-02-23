import unittest
from main import DBDataImport, DataMerge


class DBDataImportTest(unittest.TestCase):
    def setUp(self):
        self.instance = DBDataImport()
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


class DataMergeTest(unittest.TestCase):
    def setUp(self):
        self.instance = DataMerge()
        self.LA_data_mock = [
            ['1','E01012053','Middlesbrough 009A','E05009862','Linthorpe','E06000002','Middlesbrough'], 
            ['26252','E01010483','Wolverhampton 007B','E05001325','Bushbury South and Low Hill','E08000031','Wolverhampton'],
            ['26353','E01010199','Solihull 018A','E05001296','Shirley East','E08000029','Solihull']
        ]
        self.DERI_data_mock = [
            ['E01010483','91.88243802','560.5095541','68.126','0.346889952','0.235862069','0.168600155','0.21763471','0.630917874','0.303846154','0.513615734','0.205992509','37.89293478','20.40816327','5.891','0.00619195','0','0.022326064','0.015316719','0.070512821','0.118963486','0.134826526','0.021676301','8.512894673','1.343090446','5.619972543','3.150432907','0','1.697997131','1.709227745','8.863666376','5.04790512','9.004403544','7.425298387','1.497841118','3.805604824','7.913394538','4.405613493'],
            ['E01010199','97.37572016','343.9490446','64.431','0.43373494','0.377777778','0.181236674','0.277324633','0.528037383','0.293233083','0.436379163','0.173969072','36.77915129','0','1.363','0.005905512','0','0.044126416','0.012522361','0.04136253','0.037593985','0.051130777','0.006648936','0.408289465','2.073268379','1.403038427','2.066381124','0','3.219389156','3.916345135','1.280303995','5.101512425','3.433428828','1.070344612','1.379883168','3.486779169','1.949706032','2.27212279']
        ]

    def test_list_to_dict_LA_data(self):
        self.instance.list_to_dict_LA_data(self.LA_data_mock)
        assert(len(self.instance.LA_dict) == 2)
        assert(self.instance.LA_dict['E01010199'][3] == 'Solihull')

    def test_list_to_dict_DERI_data(self):
        self.instance.list_to_dict_DERI_data(self.DERI_data_mock)
        assert(self.instance.DERI_dict['E01010483'] == ['4.405613493'])

    def test_dict_merge(self):
        self.instance.list_to_dict_LA_data(self.LA_data_mock)
        self.instance.list_to_dict_DERI_data(self.DERI_data_mock)
        actual = self.instance.dict_merge()
        assert(len(actual) == 2)
        assert(actual['E01010483'][0] == 'Wolverhampton 007B')
        assert(actual['E01010199'][1] == 'E01010199')
        assert(actual['E01010199'][4] == '2.27212279')


unittest.main()
import csv


class DBDataImport:
    def get_data(self, filename):
        with open(filename, newline='') as csvfile:
            data = csv.reader(csvfile, delimiter=',')
            data_list = list(data)
        return data_list
        

class DataMerge:
    Target_LA = [
    'Bolton', 'Bury', 'Manchester', 'Oldham', 'Rochdale', 'Salford', 'Stockport', 'Tameside', 'Trafford', 'Wigan', 
    'Birmingham', 'Coventry', 'Dudley', 'Herefordshire', 'Sandwell', 'Shropshire', 'Solihull', 'Staffordshire', 'Stoke-on-Trent', 
    'Telford and Wrekin', 'Walsall', 'Warwickshire', 'Wolverhampton', 'Worcestershire', 'Newcastle', 'North Tyneside', 'Northumberland'
    ]

    LA_dict = {}
    DERI_dict = {}


    def list_to_dict_LA_data(self, list):
        for x in list:
            if x[6] in self.Target_LA:
                self.LA_dict[x[1]] = [x[2],x[1],x[4],x[6]]


    def list_to_dict_DERI_data(self, list):
        for x in list:
            self.DERI_dict[x[0]] = [x[37]]


    def dict_merge(self):
        combined_dict = {key: value + self.DERI_dict[key] for key, value in self.LA_dict.items()}
        return combined_dict


class XlWriter:
    pass


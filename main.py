import csv


class DBDataImport:
    '''returns local authority data from CSV file '''
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


class XlWriter:
    pass


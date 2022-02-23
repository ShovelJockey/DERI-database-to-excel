import csv
import xlsxwriter


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
    workbook = xlsxwriter.Workbook('DERI.xlsx')
    worksheet = workbook.add_worksheet()
        
    def write_Xl(self, combined_dict):
        row = 0
        for x in combined_dict.values():
            self.worksheet.write_row(row, 0, x)
            row += 1
        self.workbook.close()


if __name__ == '__main__':
    db = DBDataImport()
    dm = DataMerge()
    xl = XlWriter()

    LA_data = db.get_data('LSOA, ward and LA DB.csv')
    DERI_data = db.get_data('LSOA calculations and scores (district level)_v1.4.csv')

    dm.list_to_dict_LA_data(LA_data)
    dm.list_to_dict_DERI_data(DERI_data)
    combined_dict = dm.dict_merge()
    xl.write_Xl(combined_dict)
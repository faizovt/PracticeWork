import pandas as pd
import datetime

class ConvertData():
    """Class to convert data"""
    def __init__(self, date_begin=None, time_begin=None, time_end=None, chem_data=None, transformer=None):
        """ initiate our class """
        self.date_begin = date_begin
        self.time_begin = time_begin
        self.time_end = time_end
        self.chem_data = chem_data
        self.transformer = transformer

    def set_date_begin(self, date_begin):
        self.date_begin = date_begin
        self.date_begin = datetime.datetime.strptime(self.date_begin, '%d-%m-%Y')

    def set_time_begin(self, time_begin):
        self.time_begin = time_begin

    def set_time_end(self, time_end):
        self.time_end = time_end

    def set_chem_data(self, chem_data):
        self.chem_data = chem_data
        self.chem_data.fillna(value=-1, inplace=True)

    def set_transformer(self, transformer):
        self.transformer = transformer
        self.transformer.fillna(value=-1, inplace=True)

    def set_all(self, date_begin, time_begin, time_end, chem_data, transformer):
        self.date_begin = date_begin
        self.time_begin = time_begin
        self.time_end = time_end
        self.chem_data = chem_data
        self.transformer = transformer
        self.chem_data.fillna(value=-1, inplace=True)
        self.transformer.fillna(value=-1, inplace=True)

    def __convert(self):
        """ This method will convert your main data to javascript format """
        if self.chem_data.empty:
            return str("var chem_data = [];\n")
        else:
            heat_cust = str(('var heat_cust = ' + '"' + str(self.chem_data['HEATCUST'][0]) + '";\n'))
            start = str(('var start = ' + '"' + str(self.date_begin) + '";\n'))

            try:
                dtime_begin = datetime.datetime.strptime(self.date_begin + ' ' + self.time_begin, '%d-%m-%Y %H:%M')
            except Exception as e:
                print(e)
                dtime_begin = datetime.datetime.now()


            if self.time_end is None:
                dtime_end = datetime.datetime.now()
            else:

                dtime_end = datetime.datetime.strptime(self.date_begin + ' ' + self.time_end, '%d-%m-%Y %H:%M')

            delta_time = str(dtime_end - dtime_begin)
            now_time = str(datetime.datetime.now())

            array = []

            self.chem_data.reset_index()
            a = len(self.chem_data.index)

            for i in range(a):
                array.append(
                    '[' + str('"' + self.chem_data['DATETIME'][i]) + '"' + ', ' + str(self.chem_data['VALC'][i]) + ', ' +
                    str(self.chem_data['VALSI'][i]) + ', ' + str(self.chem_data['VALMN'][i]) + ', ' +
                    str(self.chem_data['VALP'][i]) + ', ' + str(self.chem_data['VALS'][i]) + ', ' +
                    str(self.chem_data['VALCU'][i]) + ', ' + str(self.chem_data['VALCR'][i]) + ', ' +
                    str(self.chem_data['VALMO'][i]) + ', ' + str(self.chem_data['VALNI'][i]) + ', ' +
                    str(self.chem_data['VALAS'][i]) + ', ' + str(self.chem_data['VALSN'][i]) + ', ' +
                    str(self.chem_data['VALN'][i]) + ', ' + str(self.chem_data['VALZN'][i]) + ', ' +
                    str(self.chem_data['TEMP'][i]) + ', ' + str(self.chem_data['VALO2_PPM'][i]) + ']')

            return str(heat_cust + start + 'var chem_data = [' + ', '.join(map(str, array)) + '];\n' +
                       'var delta_time = ' + '"' + delta_time[:delta_time.find(".")] + '";\n' + 'var now_time = "' +
                       now_time[:now_time.find(".")] + '";\n')

    def __convert_energy(self):
        """ This method will convert your energy data to javascript format """
        if self.transformer.empty:
            return "var transformer = [];"
        else:
            array = []
            a = len(self.transformer.index)
            for i in range(a):
                array.append('["' + str(self.transformer['STARTTIME'][i]) + '", ' +
                                 '"' + str(self.transformer['DURATION'][i]) + '", ' +
                                 str(self.transformer['MW'][i]) + ']')

            return 'var transformer = [' + ', '.join(map(str, array)) + '];\n'

    def printdata(self):
        """ This method will print formatted data on screen """
        return ConvertData.__convert(self) + ConvertData.__convert_energy(self)

    def writedata(self):
        """ This method will write formatter data to .TXT file """
        with open('config.dat') as config:
            for num, line in enumerate(config, 1):
                if 'path :' in line:
                    path = line[line.find(":")+1:].strip()
                    file = open(path, 'w')
                    file.write(ConvertData.__convert(self) + ConvertData.__convert_energy(self))
                    file.close
        config.close()

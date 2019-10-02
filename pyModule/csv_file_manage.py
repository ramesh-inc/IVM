import csv
from pathlib import Path

class csv_file_manage:
    def __init__(self):
        self.csv_file = ''
        self.csv_writer = ''
        self.csv_reader = ''

    def cseAvailability(self, filename):
        my_file = Path(filename + '.csv')
        if my_file.is_file():
            return True
        return False

    def openCsv(self, filename, mode):
        self.csv_file = open(filename + '.csv', mode=mode, newline='')

        if mode=='w' or mode=='a':
            self.csv_writer = csv.writer(self.csv_file)
        elif mode=='r':
            self.csv_reader = csv.reader(self.csv_file)

    def writeValues(self, values):
        valueArray = []
        for value in values:
            temp = ''
            if isinstance(value, list):
                for val in value:
                    temp = temp + ' ' + val
            else:
                temp = value

            valueArray.append(temp)

        self.csv_writer.writerow(valueArray)

    def writeHeaders(self, values):
        self.csv_writer.writerow(values)

    def closeCsv(self):
        self.csv_file.close()

    def getReaderObject(self):
        return self.csv_reader
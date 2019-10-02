import dill
import os

class file_manage:
    file = ''
    fileType = ''

    def __init__(self, fileType):
        self.fileType = '.' + fileType

    def openFile(self, filename, mode):
        self.file = open(filename + self.fileType, mode)

    def closeFile(self):
        self.file.close()

    def fileAvailability(self, filename):
        return os.path.isfile(filename + self.fileType)

    def writeValues(self, val):
        if self.fileType == '.arff':
            self.file.write(val + '\n')

        elif self.fileType == '.pkl':
            dill.dump(val, self.file)

    def readValues(self):
        if self.fileType == '.arff':
            return self.file

        elif self.fileType == '.pkl':
            return dill.load(self.file)

    def getFile(self):
        return self.file
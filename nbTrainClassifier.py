from __future__ import division
from collections import defaultdict
from dbModule import sq_cv_q_meta as cqmClass, sq_cv_meta as cmClass, sq_cv_q as cqClass
from pyModule import file_manage as fmClass, text_modification as tmClass

class TrainClassifier:
    def __init__(self):
        self.fileName = ""
        self.tempFileOb = ''
        self.tm = tmClass.text_modification()
        self.fmArff = fmClass.file_manage('arff')
        self.fmPkl = fmClass.file_manage('pkl')

        self.features = {}
        self.featureNameList = []
        self.featureCounts = defaultdict(lambda :1)
        self.featureVectors = []
        self.labelCounts = defaultdict(lambda :0)


    def DataTraning(self):
        for fv in self.featureVectors:
            self.labelCounts[fv[len(fv)-1]] += 1 #udpate count of the label
            for counter in range(0, len(fv)-1):
                self.featureCounts[(fv[len(fv)-1], self.featureNameList[counter], fv[counter])] += 1

        for label in self.labelCounts:
            for feature in self.featureNameList[:len(self.featureNameList)-1]:
                self.labelCounts[label] += len(self.features[feature])


    def GetValues(self):
        self.fmArff.openFile('nbDataset/' + self.fileName, 'r')
        data = self.fmArff.readValues()
        
        for line in data:
            if line[0] != '@':  #start of actual data
                self.featureVectors.append(line.strip().lower().split(','))
            else:   #feature definitions
                if line.strip().lower().find('@data') == -1 and (not line.lower().startswith('@relation')):
                    self.featureNameList.append(line.strip().split()[1])
                    self.features[self.featureNameList[len(self.featureNameList) - 1]] = line[line.find('{')+1: line.find('}')].strip().split(',')

        self.fmArff.closeFile()


    def SaveOnDill(self):
        self.fmPkl.openFile('nbPklFiles/' + self.fileName, 'wb')
        self.fmPkl.writeValues(self.featureCounts)
        self.fmPkl.closeFile()

        self.fmPkl.openFile('nbPklFiles/' + self.fileName + 'Label', 'wb')
        self.fmPkl.writeValues(self.labelCounts)
        self.fmPkl.closeFile()


    def setFile(self, filename):
        self.fileName = filename

    def createAttributeRaw(self, strArr):
        i = 1
        finalString = ''
        for val in strArr:
            val = self.tm.stringLowercase(val)
            if i == 1:
                finalString += '{'

            finalString += val

            if i == len(strArr):
                finalString += '}'
            else:
                finalString += ', '
            i += 1

        return finalString

    def setFileObject(self, obj):
        self.tempFileOb = obj

    def addElementDataSet(self, elements, pos, line):
        for element in elements[pos]:
            element = self.tm.stringLowercase(element)
            if len(elements) != pos + 1:
                self.addElementDataSet(elements, pos + 1, line + element + ',')
            else:
                self.tempFileOb.writeValues(line + element)

if __name__ == "__main__":
    cm = cmClass.sq_cv_meta()
    cqm = cqmClass.sq_cv_q_meta()
    cq = cqClass.sq_cv_q()

    fm = fmClass.file_manage('arff')
    tm = tmClass.text_modification()
    Train = TrainClassifier()

    types = cm.getMetaValue('predict_cat')

    for idx, type in enumerate(types):
        if not fm.fileAvailability('nbDataset/' + tm.stringUppercase(type)):
            fm.openFile('nbDataset/' + tm.stringUppercase(type), 'w')
            fm.writeValues('@RELATION ' + tm.stringUppercase(type))

            for val in cqm.getAll():
                if type == 'job' and val[0] == 'salary':
                    continue

                if val[0] != type:
                    fm.writeValues('@ATTRIBUTE ' + tm.stringLowercase(val[0]) + ' ' + Train.createAttributeRaw(tm.splitContent(val[1], ',')))

            finalAttr = cqm.getMetaValue(type)
            fm.writeValues('@ATTRIBUTE ' + type + ' ' + Train.createAttributeRaw(tm.splitContent(finalAttr, ',')))
            fm.writeValues('@DATA')

        else:
            fm.openFile('nbDataset/' + tm.stringUppercase(type), 'a')

        dataSet = cq.getDataForNbDataset()
        Train.setFileObject(fm)
        for data in dataSet:

            elements = []
            if type == 'job':
                elements.append(tm.splitContent(str(data[1]), ','))
                elements.append(tm.splitContent(str(data[2]), ','))
                elements.append(tm.splitContent(str(data[4]), ','))
                elements.append(tm.splitContent(str(data[5]), ','))
                elements.append(tm.splitContent(str(data[6]), ','))
                elements.append(tm.splitContent(str(data[7]), ','))
                elements.append(tm.splitContent(str(data[3]), ','))

            if type == 'salary':
                elements.append(tm.splitContent(str(data[1]), ','))
                elements.append(tm.splitContent(str(data[2]), ','))
                elements.append(tm.splitContent(str(data[3]), ','))
                elements.append(tm.splitContent(str(data[4]), ','))
                elements.append(tm.splitContent(str(data[5]), ','))
                elements.append(tm.splitContent(str(data[6]), ','))
                elements.append(tm.splitContent(str(data[7]), ','))
                elements.append(tm.splitContent(str(data[8]), ','))

            Train.addElementDataSet(elements, 0, '')

            if len(types) == idx + 1:
                cq.updateNbStatus(data[0])
            print(elements)

        fm.closeFile()

        Train = TrainClassifier()
        Train.setFile(tm.stringUppercase(type))
        Train.GetValues()
        Train.DataTraning()
        Train.SaveOnDill()
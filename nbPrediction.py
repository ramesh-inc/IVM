from __future__ import division
from collections import defaultdict
import math
from dbModule import sq_cv_q_meta as cqmClass, sq_cv_meta as cmClass, sq_cv_q as cqClass, sq_nb_prediction as nbpClass, sq_cv_q_predict as cqpClass
from pyModule import file_manage as fmClass, text_modification as tmClass
import predictionDT

class Prediction:

    def __init__(self):
        self.cm = cmClass.sq_cv_meta()
        self.cqm = cqmClass.sq_cv_q_meta()
        self.cq = cqClass.sq_cv_q()
        self.cqp = cqpClass.cv_q_predict()
        self.nbp = nbpClass.sq_nb_prediction()
        self.predicDT = predictionDT.predictionDT()

        self.tm = tmClass.text_modification()
        self.fm = fmClass.file_manage('arff')
        self.fmPkl = fmClass.file_manage('pkl')

        self.fileName = ""
        self.featureNameList = []
        self.features = {}
        self.featureCounts = defaultdict(lambda :1)
        self.featureVectors = []
        self.labelCounts = defaultdict(lambda :0)


    def Classify(self, featureVector):  # featureVector is a simple list like the ones that we use to train
        probabilityPerLabel = {}

        for label in self.labelCounts:
            logProb = 0
            for featureValue in featureVector:
                logProb += math.log(
                    self.featureCounts[(label, self.featureNameList[featureVector.index(featureValue)], featureValue)] /
                    self.labelCounts[label])
                probabilityPerLabel[label] = (self.labelCounts[label] / sum(self.labelCounts.values())) * math.exp(
                    logProb)

        maxkey = max(probabilityPerLabel, key=lambda classValue: probabilityPerLabel[classValue])

        totalVal = 0
        for x in probabilityPerLabel.values():
            totalVal += x

        return {'maxType': maxkey, 'maxPercentage': round(probabilityPerLabel[maxkey]/totalVal*100, 2)}

    def ReadOnDill(self):
        self.fmPkl.openFile('nbPklFiles/' + self.fileName, 'rb')
        self.featureCounts = self.fmPkl.readValues()
        self.fmPkl.closeFile()

        self.fmPkl.openFile('nbPklFiles/' + self.fileName + 'Label', 'rb')
        self.labelCounts = self.fmPkl.readValues()
        self.fmPkl.closeFile()

    def setFile(self, filename):
        self.fileName = filename

    def setFeatureNameList(self, categories):
        self.featureNameList = categories

    def addElementTempData(self, elements, pos, line):
        for element in elements[pos]:
            element = self.tm.stringLowercase(element)
            if len(elements) != pos + 1:
                self.addElementTempData(elements, pos + 1, line + element + ',')
            else:
                self.fm.writeValues(line + element + ",''")

    def makePredictionNb(self):
        types = self.cm.getMetaValue('predict_cat')
        attributes = self.cqm.getMetaKeys()

        for idx, type in enumerate(types):
            self.setFile(self.tm.stringUppercase(type))
            predictAttri = []

            if type == 'job':
                for attri in attributes:
                    if attri == 'job' or attri == 'salary':
                        continue
                    predictAttri.append(attri)
                predictAttri.append(attributes[2])

            if type == 'salary':
                for attri in attributes:
                    predictAttri.append(attri)

            dataSet = self.cqp.getDataForNbPrediction()

            for data in dataSet:
                self.fm.openFile('nbDataset/temp', 'w')
                elements = []

                if type == 'job':
                    elements.append(self.tm.splitContent(str(data[2]), ','))
                    elements.append(self.tm.splitContent(str(data[3]), ','))
                    elements.append(self.tm.splitContent(str(data[4]), ','))
                    elements.append(self.tm.splitContent(str(data[5]), ','))
                    elements.append(self.tm.splitContent(str(data[6]), ','))
                    elements.append(self.tm.splitContent(str(data[7]), ','))

                if type == 'salary':
                    elements.append(self.tm.splitContent(str(data[2]), ','))
                    elements.append(self.tm.splitContent(str(data[3]), ','))
                    elements.append(self.tm.splitContent(str(self.nbp.getPredictionExp(data[1])), ','))
                    elements.append(self.tm.splitContent(str(data[4]), ','))
                    elements.append(self.tm.splitContent(str(data[5]), ','))
                    elements.append(self.tm.splitContent(str(data[6]), ','))
                    elements.append(self.tm.splitContent(str(data[7]), ','))

                self.addElementTempData(elements, 0, '')
                self.fm.closeFile()

                self.fm.openFile('nbDataset/temp', 'r')
                tempData = self.fm.readValues()
                predictData = ''
                maxPrecentage = 0
                maxValue = ''

                for td in tempData:
                    predictData = self.tm.splitContent(td, ',')
                    predictData[len(predictData) - 1] = ''

                    self.setFeatureNameList(predictAttri)
                    self.ReadOnDill()
                    PredictResult = self.Classify(predictData)

                    print(PredictResult)

                    if PredictResult['maxPercentage'] >= maxPrecentage:
                        maxValue = PredictResult['maxType']
                        maxPrecentage = PredictResult['maxPercentage']

                print(maxValue)
                maxValue = self.tm.stringLowercase(maxValue)
                if self.nbp.getCountRowsPrediction(data[1]) < 1:
                    if type == 'job':
                        self.nbp.setPredictionExpValue(data[1], maxValue, maxPrecentage)
                    else:
                        self.nbp.setPredictionSalValue(data[1], maxValue, maxPrecentage)
                else:
                    if type == 'job':
                        self.nbp.updatePredictionExpValue(data[1], maxValue, maxPrecentage)
                    else:
                        self.nbp.updatePredictionSalValue(data[1], maxValue, maxPrecentage)

                if len(types) == idx + 1:
                    self.cqp.updateNbStatus(data[0])
                    self.predicDT.makePredictionDt(data[0])

if __name__ == "__main__":
    Predic = Prediction()
    Predic.makePredictionNb()


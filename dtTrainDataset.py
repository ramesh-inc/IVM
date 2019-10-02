from dbModule import sq_cv_q_meta as cqmClass, sq_cv_meta as cmClass, sq_cv_q as cqClass
from pyModule import text_modification as tmClass, csv_file_manage as cfmClass

class TrainDataset:
    def __init__(self):
        self.cqm = cqmClass.sq_cv_q_meta()
        self.tm = tmClass.text_modification()

    def convertToNumeric(self, str, key):
        keyValues = self.cqm.getMetaValue(key)
        keyValues = self.tm.splitContent(keyValues, ',')

        # Convert all meta keys into lowercase
        for idx, keyV in enumerate(keyValues):
            keyValues[idx] = self.tm.stringLowercase(keyV)

        val = 0
        for st in str:
            st = self.tm.stringLowercase(st)
            index = keyValues.index(st)
            val = val + index

        # If there are more than one values, then it multiplies by 10000 to get unique value
        if len(str) > 1:
            val = val * 10000

        return val

if __name__ == "__main__":
    cm = cmClass.sq_cv_meta()
    cq = cqClass.sq_cv_q()

    tm = tmClass.text_modification()
    cfm = cfmClass.csv_file_manage()
    td = TrainDataset()

    """
        Functions Related to Save data in CSV files predictionDT.py
    """
    types = cm.getMetaValue('predict_cat')

    for idx, type in enumerate(types):
        cfm.openCsv('predictionDTDataset/' + tm.stringUppercase(type), 'a')

        dataSet = cq.getDataForDtDataset()
        for data in dataSet:

            elements = []
            if type == 'job':
                elements.append(td.convertToNumeric(tm.splitContent(str(data[1]), ','), 'age'))
                elements.append(td.convertToNumeric(tm.splitContent(str(data[2]), ','), 'skills'))
                elements.append(td.convertToNumeric(tm.splitContent(str(data[4]), ','), 'experience_yrs'))
                elements.append(td.convertToNumeric(tm.splitContent(str(data[5]), ','), 'university'))
                elements.append(td.convertToNumeric(tm.splitContent(str(data[6]), ','), 'degree'))
                elements.append(td.convertToNumeric(tm.splitContent(str(data[7]), ','), 'specialization'))
                elements.append(td.convertToNumeric(tm.splitContent(str(data[3]), ','), 'job'))

            if type == 'salary':
                elements.append(td.convertToNumeric(tm.splitContent(str(data[1]), ','), 'age'))
                elements.append(td.convertToNumeric(tm.splitContent(str(data[2]), ','), 'skills'))
                elements.append(td.convertToNumeric(tm.splitContent(str(data[3]), ','), 'job'))
                elements.append(td.convertToNumeric(tm.splitContent(str(data[4]), ','), 'experience_yrs'))
                elements.append(td.convertToNumeric(tm.splitContent(str(data[5]), ','), 'university'))
                elements.append(td.convertToNumeric(tm.splitContent(str(data[6]), ','), 'degree'))
                elements.append(td.convertToNumeric(tm.splitContent(str(data[7]), ','), 'specialization'))
                elements.append(td.convertToNumeric(tm.splitContent(str(data[8]), ','), 'salary'))
            print(elements)
            cfm.writeHeaders(elements)

            if len(types) == idx + 1:
                cq.updateDtStatus(data[0])

        cfm.closeCsv()

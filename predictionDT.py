import pandas
from sklearn import model_selection
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from dbModule import sq_cv_q_meta as cqmClass, sq_cv_meta as cmClass, sq_cv_q as cqClass, sq_dt_prediction as dtpClass, sq_cv_q_predict as cqpClass
from pyModule import text_modification as tmClass, csv_file_manage as cfmClass
import vacancyMatching

class predictionDT:
	def __init__(self):
		self.cm = cmClass.sq_cv_meta()
		self.cq = cqClass.sq_cv_q()
		self.cqm = cqmClass.sq_cv_q_meta()
		self.cqp = cqpClass.cv_q_predict()
		self.dtp = dtpClass.sq_dt_prediction()

		self.cfm = cfmClass.csv_file_manage()
		self.tm = tmClass.text_modification()
		self.vacMatching = vacancyMatching.VacancyMatching()

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

	def getFinalValue(self, loc, key):
		keyValues = self.cqm.getMetaValue(key)
		keyValues = self.tm.splitContent(keyValues, ',')
		return keyValues[loc]

	def makePredictionDt(self, rowId):
		types = self.cm.getMetaValue('predict_cat')
		for idx, type in enumerate(types):
			filenameUrl = 'predictionDTDataset/' + self.tm.stringUppercase(type) + '.csv'

			names = ''
			if type == 'job':
				names = ['age', 'skills', 'experience_yrs', 'university', 'degree', 'specialization', 'job']

			if type == 'salary':
				names = ['age', 'skills', 'job', 'experience_yrs', 'university', 'degree', 'specialization', 'salary']

			dataset = pandas.read_csv(filenameUrl, names=names)
			array = dataset.values

			X = ''
			Y = ''
			validation_size = 0.30
			seed = 100
			if type == 'job':
				X = array[:, 0:6]
				Y = array[:, 6]

			if type == 'salary':
				X = array[:, 0:7]
				Y = array[:, 7]

			X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)

			# # Test options and evaluation metric (10-fold cross validation)
			seed = 100
			scoring = 'accuracy'

			models = []
			models.append(('DT', DecisionTreeClassifier()))

			# Make predictions on validation dataset
			LR = DecisionTreeClassifier()
			LR.fit(X_train, Y_train)

			dataSet = self.cqp.getDataForDtPrediction(rowId)

			for data in dataSet:
				tempArr = []
				if type == 'job':
					tempArr.append(self.convertToNumeric(self.tm.splitContent(str(data[2]), ','), 'age'))
					tempArr.append(self.convertToNumeric(self.tm.splitContent(str(data[3]), ','), 'skills'))
					tempArr.append(self.convertToNumeric(self.tm.splitContent(str(data[4]), ','), 'experience_yrs'))
					tempArr.append(self.convertToNumeric(self.tm.splitContent(str(data[5]), ','), 'university'))
					tempArr.append(self.convertToNumeric(self.tm.splitContent(str(data[6]), ','), 'degree'))
					tempArr.append(self.convertToNumeric(self.tm.splitContent(str(data[7]), ','), 'specialization'))

				if type == 'salary':
					tempArr.append(self.convertToNumeric(self.tm.splitContent(str(data[2]), ','), 'age'))
					tempArr.append(self.convertToNumeric(self.tm.splitContent(str(data[3]), ','), 'skills'))
					tempArr.append(self.convertToNumeric(self.tm.splitContent(str(self.dtp.getPredictionExp(data[1])), ','), 'job'))
					tempArr.append(self.convertToNumeric(self.tm.splitContent(str(data[4]), ','), 'experience_yrs'))
					tempArr.append(self.convertToNumeric(self.tm.splitContent(str(data[5]), ','), 'university'))
					tempArr.append(self.convertToNumeric(self.tm.splitContent(str(data[6]), ','), 'degree'))
					tempArr.append(self.convertToNumeric(self.tm.splitContent(str(data[7]), ','), 'specialization'))

				P = ([tempArr])  # assign values to p list
				predictions = LR.predict(P)  # do the prediction here

				if type == 'job':
					prediction = self.getFinalValue(predictions[0], 'job')
				if type == 'salary':
					prediction = self.getFinalValue(predictions[0], 'salary')

				y_pred = LR.predict(X_validation)
				value = round(accuracy_score(Y_validation, y_pred) * 100, 2)

				prediction = self.tm.stringLowercase(prediction)

				if self.dtp.getCountRowsPrediction(data[1]) < 1:
					if type == 'job':
						self.dtp.setPredictionExpValue(data[1], prediction, str(value))
					else:
						self.dtp.setPredictionSalValue(data[1], prediction, str(value))
				else:
					if type == 'job':
						self.dtp.updatePredictionExpValue(data[1], prediction, str(value))
					else:
						self.dtp.updatePredictionSalValue(data[1], prediction, str(value))

				if len(types) == idx + 1:
					self.cqp.updateDtStatus(rowId)
					self.vacMatching.matchingByUserId(data[1])


# if __name__ == "__main__":
#  	Predic = predictionDT()
#  	Predic.makePredictionDt(1)
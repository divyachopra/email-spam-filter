from sklearn.ensemble import RandomForestClassifier
from sklearn import svm
import numpy as np
from numpy import genfromtxt, savetxt
import sys
import random

def print_misclassification_error(a):
	dataset = genfromtxt(open('data.csv','r'), delimiter=',', dtype='f8')[0:]

	dataset = dataset[~np.isnan(dataset).any(axis=1)]

	np.random.shuffle(dataset)

	size = len(dataset)

	size_train = np.ceil(a/100.0*size)

	training = dataset[:size_train]
	test = dataset[size_train:]

	training_labels = [x[10] for x in training]
	training_data = [x[0:10] for x in training]

	test_labels = [x[10] for x in test]
	test_data = [x[0:10] for x in test]

	#RandomForest

	rf = RandomForestClassifier(n_estimators=100)
	rf.fit(training_data,training_labels)

	predict_rf = rf.predict(test_data)

	actual = np.array(test_labels)
	predicted_rf = np.array(predict_rf)

	error_rf = np.sum(actual!=predicted_rf)

	#SVM

	clf = svm.SVC()
	clf.fit(training_data,training_labels)

	predict_svm = clf.predict(test_data)
	predicted_svm = np.array(predict_svm)
	
	error_svm = np.sum(actual!=predicted_svm)
	
	misclassification_error_rf = error_rf/(len(test_data)*1.0)*100
	misclassification_error_svm = error_svm/(len(test_data)*1.0)*100
	print misclassification_error_rf, misclassification_error_svm


if __name__ == '__main__':
    print_misclassification_error(float(sys.argv[1]))















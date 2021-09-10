from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from pandas import read_csv

clf = GaussianNB()

classes = { 0: "Bad Risk", 1: "Good Risk" }

def load_model():
	df=read_csv('german_cs.csv');

	# Spliting Target Variable
	numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
	d ={"Bad Risk" : 0,"Good Risk" : 1}

	X = df.select_dtypes(include=numerics)
	X = X.drop(X.columns[0], axis=1)

	y= df["Cost Matrix(Risk)"].replace(d)



	X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2)
	clf.fit(X_train, y_train)

	acc = accuracy_score(y_test, clf.predict(X_test))
	print(f"Model trained with accuracy: {round(acc, 3)}")

def predict(query_data):
	x = list(query_data.dict().values())
	prediction = clf.predict([x])[0] 
	print(f"Model prediction: {classes[prediction]}")
	return classes[prediction]

# function to retrain the model as part of the feedback loop
def retrain(data):
    # pull out the relevant X and y from the FeedbackIn object
    X = [list(d.dict().values())[:-1] for d in data]
    y = [r_classes[d.flower_class] for d in data]

    # fit the classifier again based on the new data obtained
    clf.fit(X, y)



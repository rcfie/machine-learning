from sklearn.naive_bayes import GaussianNB

clf = GaussianNB()
clf.fit(features, labels)

print(clf.predict([[-0.8, -1]]))

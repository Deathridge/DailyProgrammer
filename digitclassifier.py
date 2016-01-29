import matplotlib.pyplot as plt

from sklearn import datasets,svm,metrics

digits = datasets.load_digits()

images = zip(digits.images)
labels = zip(digits.target)


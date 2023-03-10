# -*- coding: utf-8 -*-
"""Debowski_SVM_CLASSIFY_TUNING

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tvZedaHERB9yoKoFOQk8GAzBvgXaCFCX
"""

from sklearn import datasets
from sklearn.model_selection import train_test_split 
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report 
from sklearn.svm import SVC

digits = datasets.load_digits()

n_samples = len(digits.images)

X = digits.images.reshape((n_samples, -1))

y = digits.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.5, random_state=0)

tuned_parameters = [{'kernel': ['rbf'], 'gamma': [1e-3, 1e-4],
                     'C': [1, 10, 100, 1000]},
                    {'kernel': ['linear'], 'C': [1, 10, 100, 1000]}]

scores = ['precision', 'recall']

for score in scores:
    print("# Tuning hyper-parametrów dla kryterium: %s" % score)
    print()
    clf = GridSearchCV(
        SVC(), tuned_parameters, scoring='%s_macro' % score
    )

clf.fit(X_train, y_train)

print("Najlepsze rezultaty osiągnięto na zbiorze parametrów:")
print()
print(clf.best_params_)
print()
print("Wyniki uzyskane dla poszczególnych elementów siatki:")
print()

means = clf.cv_results_['mean_test_score']
stds = clf.cv_results_['std_test_score']

# Commented out IPython magic to ensure Python compatibility.
 for mean, std, params in zip(means, stds, clf.cv_results_['params']):
   print("%0.3f (+/-%0.03f) for %r"
#     % (mean, std * 2, params))
   print()

print("Szczegółowy raport z klasyfikacji:")
print()
print("The model is trained on the full development set.")
print("The scores are computed on the full evaluation set.")
print()
y_true, y_pred = y_test, clf.predict(X_test)
print(classification_report(y_true, y_pred))
print()

#ZADANIE 2

# Commented out IPython magic to ensure Python compatibility.
#TESTOWY 30%
from sklearn import datasets
from sklearn.model_selection import train_test_split 
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report 
from sklearn.svm import SVC

# Ładowanie zbioru o nazwie digits
digits = datasets.load_digits()

n_samples = len(digits.images)

X = digits.images.reshape((n_samples, -1))
y = digits.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=0)

tuned_parameters = [{'kernel': ['rbf'], 'gamma': [1e-3, 1e-4],
                     'C': [1, 10, 100, 1000]},
                    {'kernel': ['linear'], 'C': [1, 10, 100, 1000]}]

scores = ['precision', 'recall']

for score in scores:
   print("# Tuning hyper-parametrów dla kryterium: %s" % score)
   print()
   clf = GridSearchCV(
        SVC(), tuned_parameters, scoring='%s_macro' % score
   )

   clf.fit(X_train, y_train)

print("Najlepsze rezultaty osiągnięto na zbiorze parametrów:")
print()
print(clf.best_params_)
print()
print("Wyniki uzyskane dla poszczególnych elementów siatki:")
print()

means = clf.cv_results_['mean_test_score']
stds = clf.cv_results_['std_test_score']

for mean, std, params in zip(means, stds, clf.cv_results_['params']):
  print("%0.3f (+/-%0.03f) for %r"
#      % (mean, std * 2, params))
print()

print("Szczegółowy raport z klasyfikacji:")
print()
print("The model is trained on the full development set.")
print("The scores are computed on the full evaluation set.")
print()
y_true, y_pred = y_test, clf.predict(X_test)
print(classification_report(y_true, y_pred))
print()

# Commented out IPython magic to ensure Python compatibility.
#TESTOWY 20%
from sklearn import datasets
from sklearn.model_selection import train_test_split 
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report 
from sklearn.svm import SVC

# Ładowanie zbioru o nazwie digits
digits = datasets.load_digits()

n_samples = len(digits.images)

X = digits.images.reshape((n_samples, -1))
y = digits.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=0)

tuned_parameters = [{'kernel': ['rbf'], 'gamma': [1e-3, 1e-4],
                     'C': [1, 10, 100, 1000]},
                    {'kernel': ['linear'], 'C': [1, 10, 100, 1000]}]

scores = ['precision', 'recall']

for score in scores:
   print("# Tuning hyper-parametrów dla kryterium: %s" % score)
   print()
   clf = GridSearchCV(
        SVC(), tuned_parameters, scoring='%s_macro' % score
   )

   clf.fit(X_train, y_train)

print("Najlepsze rezultaty osiągnięto na zbiorze parametrów:")
print()
print(clf.best_params_)
print()
print("Wyniki uzyskane dla poszczególnych elementów siatki:")
print()

means = clf.cv_results_['mean_test_score']
stds = clf.cv_results_['std_test_score']

for mean, std, params in zip(means, stds, clf.cv_results_['params']):
  print("%0.3f (+/-%0.03f) for %r"
#      % (mean, std * 2, params))
print()

print("Szczegółowy raport z klasyfikacji:")
print()
print("The model is trained on the full development set.")
print("The scores are computed on the full evaluation set.")
print()
y_true, y_pred = y_test, clf.predict(X_test)
print(classification_report(y_true, y_pred))
print()

# Commented out IPython magic to ensure Python compatibility.
#TESTOWY 5%
from sklearn import datasets
from sklearn.model_selection import train_test_split 
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report 
from sklearn.svm import SVC

# Ładowanie zbioru o nazwie digits
digits = datasets.load_digits()

n_samples = len(digits.images)

X = digits.images.reshape((n_samples, -1))
y = digits.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.1, random_state=0)

tuned_parameters = [{'kernel': ['rbf'], 'gamma': [1e-3, 1e-4],
                     'C': [1, 10, 100, 1000]},
                    {'kernel': ['linear'], 'C': [1, 10, 100, 1000]}]

scores = ['precision', 'recall']

for score in scores:
   print("# Tuning hyper-parametrów dla kryterium: %s" % score)
   print()
   clf = GridSearchCV(
        SVC(), tuned_parameters, scoring='%s_macro' % score
   )

   clf.fit(X_train, y_train)

print("Najlepsze rezultaty osiągnięto na zbiorze parametrów:")
print()
print(clf.best_params_)
print()
print("Wyniki uzyskane dla poszczególnych elementów siatki:")
print()

means = clf.cv_results_['mean_test_score']
stds = clf.cv_results_['std_test_score']

for mean, std, params in zip(means, stds, clf.cv_results_['params']):
  print("%0.3f (+/-%0.03f) for %r"
#      % (mean, std * 2, params))
print()

print("Szczegółowy raport z klasyfikacji:")
print()
print("The model is trained on the full development set.")
print("The scores are computed on the full evaluation set.")
print()
y_true, y_pred = y_test, clf.predict(X_test)
print(classification_report(y_true, y_pred))
print()


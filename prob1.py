# -*- coding: utf-8 -*-
"""prob1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Jmcw98TzOY26iO7Md8_RrBkch9PgB90Z
"""

from sklearn.neural_network import MLPClassifier

x=[[0.,0.],[0.,1.],[1.,0.],[1.,1.]]
y=[0,1,1,0]

clf=MLPClassifier(activation='relu',solver='lbfgs',learning_rate='adaptive',hidden_layer_sizes=(2),max_iter=500, early_stopping=True, random_state=6)

clf.fit(x,y)

print(clf.coefs_[0])

print(clf.coefs_[1])

print(clf.intercepts_[0])

print(clf.intercepts_[1])

print(clf.predict(x))


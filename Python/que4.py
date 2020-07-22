import numpy as np

X = np.random.normal(0, 1, size=(20, 20))
y = np.random.randint(2, size=20)

var1 = np.linalg.inv(np.dot(X.T, X))
var2 = np.dot(var1, X.T)
theta = np.dot(var2, y)

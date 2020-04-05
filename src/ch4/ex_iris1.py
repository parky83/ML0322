# import pandas as pd
# from sklearn.datasets import load_iris

# data=load_iris()

# X=pd.DataFrame(data.data, columns=data.feature_names)
# y=pd.DataFrame(data.target, columns=[]])

from sklearn.metrics import confusion_matrix
y_true=[2,0,2,2,0,1]
y_pred=[0,0,2,2,0,2]

result=confusion_matrix(y_true, y_pred)

print(result)

y_true=[1,0,1,1,0,1]
y_pred=[0,0,1,1,0,1]

result=confusion_matrix(y_true, y_pred)

print(result)

# result=condition
from sklearn.metrics import classification_report

y_true=[0,0,0,1,1,0,0]
y_pred=[0,0,0,0,1,1,1]

report=classification_report(y_true, y_pred, target_names=['class0', 'class1'])

print(report)



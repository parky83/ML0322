import matplotlib.pyplot as plt
import pandas as pd

import glob, os.path, re, json
# print('cwd: '+ os.getcwd())
os.chdir('./pyml-master/day3')


tbl = pd.read_csv("bmi.csv", index_col=2)

# 그래?�� 그리�? ?��?��
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

# ?���? ?���? ?��?�� - �??��?�� ?��?��블을 ?��?��?�� ?��?���? 칠하�?
def scatter(lbl, color):
    b = tbl.loc[lbl]
    ax.scatter(b["weight"],b["height"], c=color, label=lbl)
scatter("fat",    "red")
scatter("normal", "yellow")
scatter("thin",   "purple")
ax.legend() 
plt.savefig("bmi-test.png")
plt.show()
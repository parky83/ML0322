from matplotlib import pyplot as plt
from sklearn.datasets import make_blobs
from sklearn import svm, metrics
X, y = make_blobs(n_samples=50, centers=2, cluster_std=0.5, random_state=4)
print(X)
print(y)
y = 2 * y - 1
print(y)

# 입력을 학습 전용 데이터와 테스트 전용 데이터로 분류하기 --- (※1)
x_df = pd.DataFrame(X)
x_df.loc[:,2]=pd.DataFrame(y)

x_data = x_df.loc[:, 0:1]  # 데이터
x_label = x_df.loc[:, 2]   # 레이블
# 데이터 학습과 예측하기 --- (※2)
clf = svm.SVC(kernel='linear', gamma=2)
clf = svm.SVC()
clf.fit(x_data, x_label)
pre = clf.predict(x_data)
# 정답률 구하기 --- (※3)
ac_score = metrics.accuracy_score(x_label, pre)
print("정답률 =", ac_score)

print(clf.get_params())


plt.clf()
plt.scatter(X[y == -1, 0], X[y == -1, 1], marker='o', label="-1 class")
plt.scatter(X[y == +1, 0], X[y == +1, 1], marker='x', label="+1 class")
plt.plot(clf)
plt.xlabel("x1")
plt.ylabel("x2")
plt.legend()
plt.title("leaning data")
plt.show()

from sklearn import svm
# XOR의 계산 결과 데이터 --- (※1)
xor_data = [
    #P, Q, result
    # [1, 1, 1],
    # [0, 0, 1],
    # [0, 1, 0],
    # [1, 0, 0],
    # [0, 1, 0],
    # [0, 1, 0],
    # [1, 1, 1],
    # [1, 0, 0],
    # [1, 1, 1],
    # [0, 0, 1]
    [2, 1, 2],
    [0, 2, 0],
    [3, 2, 6],
    [1, 8, 8],
    [3, 5, 15],
    [5, 7, 35],
    [5, 3, 15],
    [2, 5, 10],
    [7, 8, 56],
    [3, 34, 102]
]
# 학습을 위해 데이터와 레이블 분리하기 --- (※2)
data = []
label = []
for row in xor_data:
    p = row[0]
    q = row[1]
    r = row[2]
    data.append([p, q])
    label.append(r)
# 데이터 학습시키기 --- (※3)
clf = svm.SVC()
clf.fit(data[0:5], label[0:5])
# 데이터 예측하기 --- (※4)
pre = clf.predict(data)
print(" 예측결과:", pre)
# 결과 확인하기 --- (※5)
ok = 0
total = 0
for idx, answer in enumerate(label):
    p = pre[idx]
    if p == answer:
        ok += 1
    total += 1
    print("예측결과:",  p, "정답:", answer)
print("정답률:", ok, "/", total, "=", ok/total)

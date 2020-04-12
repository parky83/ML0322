from sklearn.model_selection import train_test_split
import tensorflow as tf
import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.callbacks import EarlyStopping


import os
os.getcwd()


# ---------------------------------------------------
# 데이터을 로딩
df = pd.read_csv("./pyml-master/day4/thoracic_surgery.csv")
data_set = df.values  # 실제 데이터만 array 형태로 읽어온다
data_set

# ---------------------------------------------------
# 데이터를 학습데이터, 테스트데이터로 분리

train, test = train_test_split(data_set, test_size=0.2)  # 20%를 테스트 데이터로 사용
test

# 속성과 라벨(클래스) 분리하기
X_train = train[:, 0:16]  # 0,1,2,3,...,15,16
y_train = train[:, 16]
# X_train
X_test = test[:, 0:16]  # 0,1,2,3,...,15,16
y_test = test[:, 16]
# Y_train.shape  # 1차원 array
# X_train.shape

model = Sequential()
model.add(Dense(512, input_shape=(2,)))
model.add(Activation('relu'))
model.add(Dropout(0.1))
model.add(Dense(512))
model.add(Activation('relu'))
model.add(Dropout(0.1))
model.add(Dense(3))
model.add(Activation('softmax'))
# 모델 구축하기 --- (※4)
model.compile(
    loss='categorical_crossentropy',
    optimizer="rmsprop",
    metrics=['accuracy'])
# 데이터 훈련하기 --- (※5)
hist = model.fit(
    X_train, y_train,
)
# 테스트 데이터로 평가하기 --- (※6)
score = model.evaluate(X_test, y_test)
print('loss=', score[0])
print('accuracy=', score[1])

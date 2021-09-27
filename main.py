from keras.layers.merge import add
from tensorflow.keras.layers import Dense
from tensorflow.keras import Sequential
import numpy as np
import random as r

model = Sequential()
model.add(Dense(10, activation='relu', input_shape=(1,)))
model.add(Dense(8, activation='relu',))
model.add(Dense(4, activation='relu'))
model.add(Dense(10, activation='sigmoid'))

model.compile()
print(model.summary())

x = np.array(['5+5'])
y= np.array(['10'])

for i in range(50000):
    temp1 = r.randrange(0, 50001)
    temp2 = r.randrange(0, 50001)
    total = temp1 + temp2
    xtemp = np.array([str(temp1) + '+' + str(temp2)])
    ytemp = np.array([str(total)])
    x = np.vstack([x, xtemp])
    y = np.vstack([y, ytemp])
print(x)
print(y)

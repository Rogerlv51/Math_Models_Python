from tensorflow import keras
from tensorflow.keras.datasets import mnist
from tensorflow.python.keras.utils import np_utils
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,Activation
from tensorflow.keras.optimizers import RMSprop

# 数据导入
(x_train,y_train),(x_test,y_test) = mnist.load_data()
print(x_train.shape,y_train.shape)
print(x_test.shape,y_test.shape)


# 数据预处理
x_train = x_train.reshape(x_train.shape[0],-1)  / 255.0
x_test = x_test.reshape(x_test.shape[0],-1) / 255.0
y_train = np_utils.to_categorical(y_train,num_classes=10)
y_test = np_utils.to_categorical(y_test,num_classes=10)


# 直接使用keras.Sequential()搭建全连接网络模型
model = Sequential()
model.add(Dense(128, input_shape=(784,)))
model.add(Activation('relu'))
model.add(Dense(10))
model.add(Activation('softmax'))


#lr为学习率，epsilon防止出现0，rho/decay分别对应公式中的beta_1和beta_2
rmsprop = RMSprop(lr=0.001,rho=0.9,epsilon=1e-08,decay=0.00001) 
model.compile(optimizer=rmsprop,loss='categorical_crossentropy',metrics=['accuracy'])
print("---------------training--------------")
model.fit(x_train,y_train,epochs=10,batch_size=32)
print('\n')
print("--------------testing----------------")
loss,accuracy = model.evaluate(x_test,y_test)
print('loss:',loss)
print('accuracy:',accuracy)
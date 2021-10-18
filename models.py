from tensorflow.keras.layers import  Input,Conv2D,BatchNormalization,Activation,Subtract,LeakyReLU,Add,Average,Lambda,MaxPool2D,Dropout,UpSampling2D,Concatenate,Multiply,GlobalAveragePooling2D,Dense,ZeroPadding2D,AveragePooling2D
from tensorflow.keras.layers import concatenate,Flatten,Layer,ReLU, MaxPooling2D,concatenate, ConvLSTM2D
from tensorflow.keras.models import Model, load_model
from tensorflow.keras.optimizers import Adam

inputs = Input(shape=(224,224,3))
fe = Conv2D(256,kernel_size = (8,8),strides = (4,4))(inputs)
fe = BatchNormalization()(fe)
fe = ReLU()(fe)
fe = MaxPooling2D(pool_size = (3,3),strides = (2,2))(fe)

fe = Conv2D(64,kernel_size = (3,3), padding='same')(fe)
fe = BatchNormalization()(fe)
fe = ReLU()(fe)
fe = MaxPooling2D(pool_size = (3,3),strides = (2,2))(fe)

fe = Conv2D(64,kernel_size = (3,3), padding='same')(fe)
fe = BatchNormalization()(fe)
fe = ReLU()(fe)
fe = MaxPooling2D(pool_size = (2,2),strides = (2,2))(fe)

fe = Conv2D(32,kernel_size = (4,4), padding='same')(fe)
fe = BatchNormalization()(fe)
fe = ReLU()(fe)
fe = MaxPooling2D(pool_size = (2,2),strides = (2,2))(fe)

fe = Conv2D(128,kernel_size = (3,3), padding='same')(fe)
fe = BatchNormalization()(fe)
fe = ReLU()(fe) 
fe = MaxPooling2D(pool_size = (2,2),strides = (2,2))(fe)



flat = Flatten()(fe)

dense_1 = Dense(128,activation = 'elu')(flat)
dense_2 = Dense(128,activation = 'elu')(dense_1)
prediction = Dense(3,activation = 'softmax')(dense_2) 


in3_pred = Model(inputs = inputs,outputs = [prediction])
print(in3_pred.summary())

in3_pred.compile(loss='categorical_crossentropy', optimizer=Adam(learning_rate=1e-4), metrics=['accuracy','mse'])

history = in3_pred.fit(train_data, train_labels, batch_size = 16, epochs = 30,validation_split=0.1)

in3_pred.evaluate(test_data,test_labels)


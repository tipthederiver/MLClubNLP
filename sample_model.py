from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.layers import LSTM
from keras.optimizers import RMSprop
from keras.callbacks import LambdaCallback, ModelCheckpoint
import random
import sys
import io

model = Sequential()
model.add(LSTM(256, input_shape=(MAX_LEN,DIC_LEN)))
model.add(Dense(2))
model.add(Activation('softmax'))

optimizer = RMSprop(lr=0.01)
model.compile(loss='categorical_crossentropy', optimizer=optimizer)

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# define the checkpoint
filepath = "Wordweights.hdf5"
checkpoint = ModelCheckpoint(filepath, 
                             monitor='loss', 
                             verbose=1, 
                             save_best_only=True, 
                             mode='min')

model.fit(x_train, pd.get_dummies(y_train),
          batch_size=256,
          epochs=10,
          verbose=1,
          callbacks=[checkpoint])

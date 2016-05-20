

keras.optimizers.Adagrad()
keras.objectives.categorical_crossentropy()
metrics=['accuracy']


model = Sequential()
model.add(Dense(32, input_dim=100)
model.add(Dense(10, activation='softmax'))
model.compile(optimizer='adagrad', loss='categorical_crossentropy', metrics=['accuracy'])





# Momentum, Dropout, regularization
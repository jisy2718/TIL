[toc]



# practice 1

## [1] MLP

```python
# 1. 데이터 가져오기
import tensorflow as tf
fashion_mnist = tf.keras.datasets.fashion_mnist

(x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()

x_train, x_valid , y_train, y_valid = model_selection.train_test_split(x_train, y_train, test_size = 0.2)

# 2. 데이터 시각화
import matplotlib.pyplot as plt
plt.figure()
plt.imshow(x_train[0])
plt.colorbar()
plt.grid(False)
plt.show()


# 3. 모델 구성하기
x_train.shape # (48000,28,28)

# 3-1 모델
model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28,28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10, activation='softmax'),
])

# 3-2 loss, optimizer
# CategoricalCrossentropy : input이 one-hot 인 경우 이용
loss_fn = tf.keras.losses.SparseCategoricalCrossentropy()  # label이 int 형태인 경우 이용
optim_fn = tf.keras.optimizers.Adam()

# 3-3 compile
model.compile(optimizer=optim_fn,
              loss=loss_fn,
              metrics=['accuracy']) # metrics=['mae', 'acc'] 여러개 가능

model.summary()


# 4. training
hist = model.fit(x_train, y_train, epochs=10, validation_data=(x_valid, y_valid))
hist.history


# 5. training 결과 확인

acc = hist.history['accuracy']
val_acc = hist.history['val_accuracy']
loss = hist.history['loss']
val_loss = hist.history['val_loss']


# 6. 평가와 예측
model.evaluate(x_test, y_test, verbose=2)
predictions = model.predict(x_test)


```


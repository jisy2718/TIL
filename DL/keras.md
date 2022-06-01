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



## [2] Tensorflow에 필요한 추가 기능

### (1) Callback 사용

+ callback을 사용하기 위해서는 리스트 형태로 callback 함수들을 저장한 뒤, fit()으로 전달해주면 된다. `tf.keras.callbacks.Callback` 라이브러리에 있는 built-in callback 함수들을 잘 활용한다.
  - ModelCheckpoint : 주기적으로 모델을 저장한다.
  - LearningRateScheduler: Epoch에 따라서 Learning rate를 조정한다.
    - epoch 증가하면서 줄이는 것이 보편적
  - EarlyStopping : validation metrics가 향상되지 않을 때 학습을 멈춘다.
  - TensorBoard : 시각화하기위해서 모델 log들을 주기적으로 작성해서 텐서보드로 보여준다.
  - CSVLogger : loss, metrics data의 stream들을 CSV 파일로 넘긴다.



+ 코드

  ```python
  callbacks = [
      tf.keras.callbacks.TensorBoard(log_dir = './logs'),
      tf.keras.callbacks.EarlyStopping(monitor='loss', patience=3), #loss를 관찰하다 training을 중간에 그만두게 할 수 있다.
      tf.keras.callbacks.ModelCheckpoint(filepath=checkpoint_prefix, save_weights_only = True),
      tf.keras.callbacks.LearningRateScheduler(decay),
      PrintLR()
  ]
  
  model.fit(x_train, y_train, epochs=2, callbacks=callbacks)
  ```

  

  



### (2) 전체 모델 저장 및 불러오기



```python
#Tensorflow SavedModel 형식으로 모델을 저장하는 방법 -> 2가지 API 존재

path = 'saved_model/'
model.save(path) #1번째 API  => 주로 이용
tf.keras.models.save_model(model, path) #2번째 API 


os.listdir('saved_model')
>>> ['assets', 'keras_metadata.pb', 'saved_model.pb', 'variables']
#saved_model.pb에는 모델 아키텍처 및 훈련 구성(옵티마이저, loss & matric)이 저장된다.
#가중치의 경우 variables 폴더에 저장된다.
#Assets 폴더에는 Graph 생성에 필요한 정보들이 저장되어 있다.

#Saved model을 로드하고 Evaluate
loaded_model = tf.keras.models.load_model(path)
eval_loss, eval_acc = loaded_model.evaluate(x_test, y_test)

print('loss : {}, accuracy : {}'.format(eval_loss, eval_acc))
```







### (3) Regularization 방법

+ Keras의 regularizers API를 이용하면 과적합을 막을 수 있다. 각 Layer를 생성할 때 regularizer argument를 넣어주면 사용가능하다. 이와 별개로 Dropout layer를 추가하여 과적합을 막는 방식도 가능하다.

+ 코드

  ```python
  #L1 regularization : LASSO
  #L2 regularization : Ridge
  #Dropout
  #Elastic Regularization
  #https://www.tensorflow.org/api_docs/python/tf/keras/regularizers
      
  from tensorflow.keras.regularizers import l2
  
  inputs = tf.keras.Input(shape=(784,))
  dense = tf.keras.layers.Dense(64, activation="relu")
  x = dense(inputs)
  
  #Regularizer를 적용하고 싶다면 아래와 같이 Layer 생성시 regularizer를 넣어주자.
  #Dense layer의 경우 kernel_regularizer, bias_regularizer, activity_regularizer 등을 사용가능하다.
  #상세 내용은 Documentation을 참고하라. https://www.tensorflow.org/api_docs/python/tf/keras/layers/Dense
  layer = tf.keras.layers.Dense(64, kernel_regularizer=l2(0.01), bias_regularizer=l2(0.01))
  x = layer(x)
  
  # Dropout layer를 추가하여 Overfitting을 방지할 수도 있다.
  dropout = tf.keras.layers.Dropout(0.3)
  x = dropout(x)
  outputs = tf.keras.layers.Dense(10, activation='softmax')(x)
  
  ```

  





## [3] Data

+ pytorch 는 dataloader가 있지만 tf는 중구난방
+ 이용가능한 API
  + Keras data API
  + Keras preprocess API
  + Tensorflow data API



### (1) Keras data API

+ 데이터 종류

  - boston_housing module: Boston housing price regression dataset.

  - cifar10 module: CIFAR10 small images classification dataset.

  - cifar100 module: CIFAR100 small images classification dataset.

  - fashion_mnist module: Fashion-MNIST dataset.

  - imdb module: IMDB sentiment classification dataset.

  - mnist module: MNIST handwritten digits dataset.

  - reuters module: Reuters topic classification dataset.



+ 코드

  ```PYTHON
  fashion_mnist = tf.keras.datasets.cifar10
  
  #Load data
  (x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()
  
  #Split train| set into train/valid set
  from sklearn import model_selection
  x_train, x_valid, y_train, y_valid = model_selection.train_test_split(x_train, y_train,test_size=0.2)
  ```

  

+ agumentation

  ```python
  data_augmentation = tf.keras.Sequential([
      ###### 아래 빈칸. 실습하면서 완성 #####
      tf.keras.layers.experimental.preprocessing.Rescaling(1.0/255.0),
      tf.keras.layers.experimental.preprocessing.RandomFilp('horizontal_and_vertical'),
      tf.keras.layers.experimental.preprocessing.RandomRotation(0.2)
  
  
      ###### 빈칸 끝 #####
  ])
  ```

  



### (2) Keras preprocess API

+ ImageDataGenerator
+ 





### (3) Tensorflow data API

+ 세부적인 데이터 가공이 가능함
+ `tf.data.Datasets` 모듈을 이용
  + `tf.data.Dataset`을 이용할 때에는 Dataset.map()을 활용하여 데이터 가공을 수행할 수 있다. 아래에서 데이터를 1/255로 나누어주는 작업을 수행해 보자.





### (4) File로부터 Tensorflow Dataset 만들기

+ 적당한 data다운로드 받고 경로 저장

  ```python
  import pathlib
  flowers_root  = tf.keras.utils.get_file(
      "flower_photos",
      "https://storage.googleapis.com/download.tensorflow.org/example_images/flower_photos.tgz",
      untar=True)
  
  # The path of data folder
  flowers_root = pathlib.Path(flowers_root) 
  ```

  

+ 파일로부터 Dataset을 만들기 위해서 폴더 구조는 아래와 같이 구성되어 있어야 한다. 즉, 각 클래스별 폴더 아래에 이미지가 모여 있는 형태가 되어야 한다.

  main_directory/
  ...class_a/
  ......a_image_1.jpg
  ......a_image_2.jpg
  ...class_b/
  ......b_image_1.jpg
  ......b_image_2.jpg

  위와 같이 폴더 구조를 구성한 후 `keras.preprocessing.image_dataset_from_directory` method를 이용하면 아래와 같이 tf.data.Dataset 클래스로 구성해 준다. 

```python
train_ds = tf.keras.preprocessing.image_dataset_from_directory(
  flowers_root,
  validation_split=0.2,
  subset="training",
  seed=123, # For shuffling, shuffle is defaulted to True
  image_size=(180, 180)
)

val_ds = tf.keras.preprocessing.image_dataset_from_directory(
  flowers_root,
  validation_split=0.2,
  subset="validation",
  seed=123,
  image_size=(180, 180)
)
```


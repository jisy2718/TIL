[toc]



## 목차

+ [tensor&layer&역전파]()
+ [model]()
  + 생성(Sequential, Functional, Subclassing), 내부접근, complie(optimizer, loss, metrics) , 학습 및 평가 예측, 저장 및 복원, callbacks

+ [과소/과대적합

  + 방지법,

+ 실습

  + [MINIST]()

  + [Fashion MNIST]()

    





## 이수안컴퓨터연구소

### [1. 딥러닝 한번에 끝내기](이수안)

+ 코드는 ipynb에 있으므로, 개념과 함수위주

#### [1] tensor

+ tensor 생성
  + `tf.constant()`
+ 데이터 타입 설정
  + `tf.constant( [int, float, string] 중1, dtype=[float16, int8] 등 존재)`
+ 데이터 타입 변환
  + `tf.cast(data, tf.dtype)`

+ tensor 연산
  + tf는 같은 dtype 아니면, 연산 불가
    + `print(tf.constant(2)+tf.constant(2.2))` : 불가
    + `print(tf.cast(tf.constant(2),tf.float32)+tf.constant(2.2))` : 형변환 해줘야



#### [2] layer

+ `Dense, Activation, Flatten, Input`



##### Dense

+ `Dense(units, activation, name, kernel_initializer)`



##### Activation





##### Flatten



##### Input

+ `Input(shape, dtype`)



#### [3] model 생성방법

##### Sequential







##### Functional API

+ `layers.Concatenate`
+ 다중 input, 다중 output





##### Subclassing

+ 권장되는 방법은 아님

+ `fit(), evaluate(), predeict()`
+ `save(), load()`
+ `call()`





#### [4] model 내부 접근

##### layer 접근

+ `model.layers`
+ `model.get_layer('layer name')`

##### weight

+ `weights, biases = layer.get_weights()`





#### [5] model compile

##### loss function

+ `sparse_categorical_crossentropy`: 클래스가 배타적 방식으로 구분, 즉 (0, 1, 2, ..., 9)와 같은 방식으로 구분되어 있을 때 사용
+ `categorical_cross_entropy`: 클래스가 원-핫 인코딩 방식으로 되어 있을 때 사용
+ `binary_crossentropy`: 이진 분류를 수행할 때 사용
+ `mae, mse`

+ 교차 엔트로피 오차(Cross Entropy Error, CEE)
  - 이진 분류(Binary Classification), 다중 클래스 분류(Multi Class Classification)
  - 소프트맥스(softmax)와 원-핫 인코딩(ont-hot encoding) 사이의 출력 간 거리를 비교
  - 정답인 클래스에 대해서만 오차를 계산
  - 정답을 맞추면 오차가 0, 틀리면 그 차이가 클수록 오차가 무한히 커짐
  - y=log(x)
    - x가 1에 가까울수록 0에 가까워짐
    - x가 0에 가까울수록 y값은 무한히 커짐
+ 교차 엔트로피 오차 식: $ \qquad \qquad E = - \frac{1}{N}\sum_{n} \sum_{i} y_i\ log\tilde{y}_i $ 
  - $y_i$ : 학습 데이터의 i 번째 정답 (원-핫 인코딩, one-hot encoding)
  - $\tilde{y}_i$ : 학습 데이터의 입력으로 추정한 i 번째 출력
  - $N$ : 전체 데이터의 개수
  - $i$ : 데이터 하나당 클래스 개수





##### optimizer

+ Keras에서 여러 옵티마이저 제공
  - `keras.optimizer.SGD()`: 기본적인 확률적 경사 하강법
  - `keras.optimizer.Adam()`: 자주 사용되는 옵티마이저
  - Keras에서 사용되는 옵티마이저 종류: https://keras.io/ko/optimizers/
  
+ 보통 옵티마이저의 튜닝을 위해 따로 객체를 생성하여 컴파일

  

###### 안장점(Saddle Point)

- 기울기가 0이지만 극값이 되지 않음
- 경사하강법은 안장점에서 벗어나지 못함



##### 지표(Metrics)

- 모니터링할 지표로 모델 학습에 사용되지 않음
- `mae`나 `accuracy` 등 loss에서 사용되는 모든 것 사용가능
- Keras에서 사용되는 지표 종류: https://keras.io/ko/metrics/





#### [6] model 학습 및 평가, 예측

+ `fit()`
+ `evalueate()`
+ `predict()`



#### [7] backpropagation

- 오차역전파 알고리즘
  - 학습 데이터로 정방향(forward) 연산을 통해 손실함수 값(loss)을 구함
  - 각 layer별로 역전파학습을 위해 중간값을 저장
  - 손실함수를 학습 파라미터(가중치, 편향)로 미분하여 마지막 layer로부터 앞으로 하나씩 연쇄법칙을 이용하여 미분
  - 각 layer를 통과할 때마다 저장된 값을 이용
  - 오류(error)를 전달하면서 학습 파라미터를 조금씩 갱신
- 오차역전파 학습의 특징
  - 손실함수를 통한 평가를 한 번만 하고, 연쇄법칙을 이용한 미분을 활용하기 때문에 학습 소요시간이 매우 단축
  - 미분을 위한 중간값을 모두 저장하기 때문에 메모리를 많이 사용
- [잘설명된블로그](https://bskyvision.com/718)
  - weight를 output과 가까운 곳부터 update 하는데, $d(cost)/dw$ 를 계산하기 위해서, chain rule을 사용
  - 그래서 output과 가까운 w를 update 시킴(우선 update될 값만 가지고 있다가, 모든 weight가 update값 가지게 되면 갱신) 



#### [8] model 저장과 복원

- `save()`
- `load_model()`
- Sequencial API, 함수형 API에서는 모델의 저장 및 로드가 가능하지만 서브클래싱 방식으로는 할 수 없음
- 서브클래싱 방식은 `save_weights()`와 `load_weights()`를 이용해 모델의 파라미터만 저장 및 로드
- JSON 형식
  - `model.to_json()` (저장)
  - `tf.keras.models.model_from_json(file_path)` (복원)
- YAML로 직렬화
  - `model.to_yaml()` (저장)
  - `tf.keras.models.model_from_yaml(file_path)` (복원)





#### [9] callbacks

- `fit()` 함수의 callbacks 매개변수를 사용하여 케라스가 훈련의 시작이나 끝에 호출할 객체 리스트를 지정할 수 있음
- 여러 개 사용 가능
- ModelCheckpoint
  - `tf.keras.callbacks.ModelCheckpoint`
  - 정기적으로 모델의 체크포인트를 저장하고, 문제가 발생할 때 복구하는데 사용
- EarlyStopping
  - `tf.keras.callbacks.EarlyStopping`
  - 검증 성능이 한동안 개선되지 않을 경우 학습을 중단할 때 사용
- LearningRateSchduler
  - `tf.keras.callbacks.LearningRateSchduler`
  - 최적화를 하는 동안 학습률(learning_rate)를 동적으로 변경할 때 사용
- TensorBoard
  - `tf.keras.callbacks.TensorBoard`
  - 모델의 경과를 모니터링할 때 사용





#### [10] 과소/과대적합

+ 과소적합 (Underfitting)

  - 학습 데이터를 충분히 학습하지 않아 성능이 매우 안 좋은 경우

  - 모델이 지나치게 단순한 경우

  - 해결 방안

    - 충분한 학습 데이터 수집

    - 보다 더 복잡한 모델 사용

    - 에폭수(epochs)를 늘려 충분히 학습

      

+ 과대적합 (Overfitting)

  - 모델이 학습 데이터에 지나치게 맞추어진 상태

  - 새로운 데이터에서는 성능 저하

  - 데이터에는 잡음이나 오류가 포함

  - 학습 데이터가 매우 적을 경우

  - 모델이 지나치게 복잡한 경우

  - 학습 횟수가 매우 많을 경우

  - 해결방안

    - 다양한 학습 데이터 수집 및 학습

    - 모델 단순화: 파라미터가 적은 모델을 선택하거나, 학습 데이터의 특성 수를 줄임

    - 정규화(Regularization)을 통한 규칙 단순화

    - 적정한 하이퍼 파라미터 찾기

      

##### 과대적합(overfitting)과 과소적합(underfitting) 방지 방법

- 모델의 크기 축소
- 가중치 초기화(Weight Initializer)
- 옵티마이저(Optimizer)
- 배치 정규화(Batch Normalization)
- 규제화(Regularization)
- 드롭아웃(Dropout)





##### 옵티마이저

+ SGD

  + `optimizer = SGD(learning_rate=0.001, momentum=0.9, nesterov=True)`

    

+ AdaGrad(Adaptive Gradient)

  - 가장 가파른 경사를 따라 빠르게 하강하는 방법
  - 학습률을 변화시키며 진행하며 적응적 학습률이라고도 부름
  - 경사가 급할 때는 빠르게 변화, 완만할 때는 느리게 변화
  - 간단한 문제에서는 좋을 수는 있지만 딥러닝(Deep Learning)에서는 자주 쓰이지 않음
  - 학습률이 너무 감소되어 전역최소값(global minimum)에 도달하기 전에 학습이 빨리 종료될 수 있기 때문
  - `optimizer = Adagrad(learning_rate=0.001)`

  

+ RMSProp (Root Mean Square Propagation)
  - AdaGrad를 보완하기 위한 방법으로 등장
  - 합 대신 지수의 평균값을 활용
  - 학습이 안되기 시작하면 학습률이 커져서 잘 되게하고, 학습률이 너무 크면 학습률을 다시 줄임
  - `optimizer = RMSprop(learning_rate=0.001, rho=0.9)`



+ Adam (Adaptive Moment Estimation)
  - 모멘텀 최적화와 RMSProp의 아이디어를 합친 것
  - 지난 그래디언트의 지수 감소 평균을 따르고(Momentum), 지난 그레디언트 제곱의 지수 감소된 평균(RMSProp)을 따름
  - 가장 많이 사용되는 최적화 방법
  - `optimizer = Adam(learning_rate=0.001, beta_1=0.9, beta_2=0.999)`





###### Momentum

- 운동량을 의미, 관성과 관련
- 공이 그릇의 경사면을 따라서 내려가는 듯한 모습
- 이전의 속도를 유지하려는 성향
- 경사하강을 좀 더 유지하려는 성격을 지님
- 단순히 SGD만 사용하는 것보다 적게 방향이 변함
- Momentum 수식





##### 가중치초기화전략

+ 선형활성화함수
  + Xavier 이용
+ 비선형활성화함수
  + He 이용



##### 배치정규화

+ Dense 이후, activation 이전에 넣어줌
+ data의 분포 자체를 정규화시켜서, 학습이 더 원활하게 일어나게 해줌
  + 가중치의 활성화 값이 적당히 퍼질 수 있게 끔 강제



##### 규제화

+ L2 , L1, L1_L2
+ 드랍아웃





#### [11] 하이퍼파라미터

+ 학습률(learning_rate), 학습횟수(epochs), 미니배치크기, 검증데이터
+ 

#### [12] Fashion MNIST 실습





## 코드

+ `history`

  + ```python
    history.history.keys()
    ```

  + 

+ `model.fit()`

+ `plot_model(model, show_shapes=True)`

+ `plt.add_subplot()` : [블로그 참조](https://pyvisuall.tistory.com/68)





+ np 소수점

  + ```python
    np.set_printoptions(precision=3)  # 소수점 3째자리
    ```

    





### confusion matrix

+ plot & report

```python
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns
sns.set(style='white')

# 1. heatmap
plt.figure(figsize=(8,8))
cm = confusion_matrix(np.argmax(y_test, axis=1), np.argmax(pred_ys, axis=1))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Predicted label')
plt.ylabel('True label')
plt.show()

# 2. report
print(classification_report(np.argmax(y_test,axis=-1), np.argmax(pred_ys, axis=-1)))
```


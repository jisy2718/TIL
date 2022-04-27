[toc]

[교재](https://wikidocs.net/21687)

# NLP

[딥러닝을 이용한 자연어 처리 입문](https://wikidocs.net/book/2155) 내용 요약

# 2. 텍스트 전처리

+ 토큰화 (tokenization)
+ 정제 (cleaning)
+ 정규화 (Normalization)

## [1] 토큰화

+ 주어진 코퍼스(텍스트 집합으로 된 언어리소스)에서 토큰이라 불리는 단위로 나누는 작업을 **토큰화**
  + 보통 의미있는 단위로 토큰화 진행



### (1) 단어 토큰화

+ 토큰의 기준을 단어로 하는 경우



### (2) 단어 토큰화에서 고려 사항

**구두점이나 특수 문자를 단순 제외해서는 안됨**

+ 예

  + . 의 경우 문장의 끝을 알려주기도 하므로 무조건 제거 x

  + $ 는 가격을 나타낼 수 있고, /는 22/12/31 과 같이 날짜를 나타낼 수도 있음

  + 123,111,111 과 같이 숫자 단위에 , 있을 수 있음

    

**줄임말과 단어 내에 띄어쓰기가 있는 경우**

+ 아래와 같은 예들도 하나의 토큰으로 인식가능해야 함

+ 예
  + I'm
  + New York
  + rock n roll



### (3) 문장토큰화

+ 토큰의 단위가 문장인 경우로 **문장분류**라고도 불림
+ 문장 단위 구분은 **?, !, .** 과 같은 것으로 할 수 있다고 생각할 수 있지만 **.** 의 경우 문장의 끝이 아니더라도 출현 가능
  + 예
    + Ph.D.
    + nlp@gmail.com



#### (a) KSS 한국어 패키지

```python
import kss

text = '딥 러닝 자연어 처리가 재미있기는 합니다. 그런데 문제는 영어보다 한국어로 할 때 너무 어렵습니다. 이제 해보면 알걸요?'
print('한국어 문장 토큰화 :',kss.split_sentences(text))
```





### (4) 영어와 한국어 차이

#### (a) 영어

+ New York, Rock n Roll과 같은 합성어나, he's 와 같은 줄임말에 대한 예외처리만 잘하면, 띄어쓰기(whitespace)를 기준으로 하는 토큰화를 수행해도 단어 토큰화가 잘 작동함

  + 거의 대부분의 경우에서 단어 단위로 띄어쓰기가 이루어지기 때문

    

####  (b) 한국어

+ 교착어 (조사, 어미등을 붙여서 말을 만드는 언어) 이므로, 띄어쓰기 단위(어절 단위) 로의 토큰화는 NLP에서 지양됨



##### 교착어 특성

+ 한국어의 경우 '그가, 그에게, 그를, 그와, 그는' 과 같이 '그'와 함께 여러 조사가 띄어쓰기 없이 사용됨
  + 대부분의 경우 NLP에서 조사를 분리해 줘야함



+ 형태소(morpheme)
  + 형태소란 뜻을 가진 가장 작은 말의 단위
  + **자립형태소**
    + 그 자체로 단어가됨
    + 체언(명사,대명사,수사), 수식언(관형사, 부사), 감탄사
  + **의존형태소**
    + 다른 형태소와 결합하여 사용되는 형태소
    + 접사, 어미, 조사, 어간



### (5) 품사 태깅 (Part-of_speech tagging)

#### (a) 영어

+ NLTK

  ```PYTHON
  from nltk.tokenize import word_tokenize
  from nltk.tag import pos_tag
  
  text = "I am actively looking for Ph.D. students. and you are a Ph.D. student."
  tokenized_sentence = word_tokenize(text)
  
  print('단어 토큰화 :',tokenized_sentence)
  print('품사 태깅 :',pos_tag(tokenized_sentence))
  
  >>>
  단어 토큰화 : ['I', 'am', 'actively', 'looking', 'for', 'Ph.D.', 'students', '.', 'and', 'you', 'are', 'a', 'Ph.D.', 'student', '.']
      
  품사 태깅 : [('I', 'PRP'), ('am', 'VBP'), ('actively', 'RB'), ('looking', 'VBG'), ('for', 'IN'), ('Ph.D.', 'NNP'), ('students', 'NNS'), ('.', '.'), ('and', 'CC'), ('you', 'PRP'), ('are', 'VBP'), ('a', 'DT'), ('Ph.D.', 'NNP'), ('student', 'NN'), ('.', '.')]
  ```

  





#### (b) 한국어

+ KONLPY

  + morphs : 형태소 추출
  + pos : 품사 태깅(Part-of-speech tagging)
  + nouns : 명사 추출

  ```PYTHON
  from konlpy.tag import Okt
  from konlpy.tag import Kkma
  
  okt = Okt()
  kkma = Kkma()
  
  print('OKT 형태소 분석 :',okt.morphs("열심히 코딩한 당신, 연휴에는 여행을 가봐요"))
  print('OKT 품사 태깅 :',okt.pos("열심히 코딩한 당신, 연휴에는 여행을 가봐요"))
  print('OKT 명사 추출 :',okt.nouns("열심히 코딩한 당신, 연휴에는 여행을 가봐요")) 
  
  >>>
  OKT 형태소 분석 : ['열심히', '코딩', '한', '당신', ',', '연휴', '에는', '여행', '을', '가봐요']
      
  OKT 품사 태깅 : [('열심히', 'Adverb'), ('코딩', 'Noun'), ('한', 'Josa'), ('당신', 'Noun'), (',', 'Punctuation'), ('연휴', 'Noun'), ('에는', 'Josa'), ('여행', 'Noun'), ('을', 'Josa'), ('가봐요', 'Verb')]
      
  OKT 명사 추출 : ['코딩', '당신', '연휴', '여행']
  ```

  











## [2] 정제(Cleaning) & 정규화(Normlaization)

### (1) 목적

+ 정제 
  + 갖고 있는 코퍼스로부터 노이즈 데이터 제거
  + 토큰화 전/후 모두 이용
+ 정규화 
  + 표현 방법이 다른 단어들을 통합시켜서 같은 단어로 만듦
  + 코퍼스의 복잡성을 줄이기가 목적



### (2) 방법

#### (a) 규칙에 기반한 표기가 다른 단어들의 통합

+ 예시
  + us & usa 는 같게 취급
  + uh-huh 와 uhhuh 같게 취급

#### (b) 대, 소문자 통합

#### (c) 불필요한 단어 제거

+ 등장 빈도가 적은 단어 제거

  + 전체 데이터에서 조금만 등장하는 단어는 제외

+ 길이가 짧은 단어 제거

  + 영어권 언어는 길이가 짧은 단어는 대부분 불용어여서, 효과적
  + 한국어에서는 한 글자만으로도 의미가 있는 경우 많아서, 효과적이지 않은 경우 있음

  ```PYTHON
  # 길이가 1~2인 단어 정규표현식으로 삭제
  
  import re
  text = "I was wondering if anyone out there could enlighten me on this car."
  
  # 길이가 1~2인 단어들을 정규 표현식을 이용하여 삭제
  shortword = re.compile(r'\W*\b\w{1,2}\b')
  print(shortword.sub('', text))
  
  >>> was wondering anyone out there could enlighten this car.
  ```

  

#### (d) 정규 표현식

+ 코퍼스 내에서 계속해서 등장하는 글자들(HTML 태그, 기사의 게재시간 등)을 규칙에 기반하여, 한 번에 제거하는 방식으로 유용

  





#### (e) 표제어 추출 (Lemmatization) & 어간추출 (stemming)

+ 여러 단어를 하나의 단어로 일반화 시킬 수 있다면 일반화 시켜서, 코퍼스 내의 단어 개수 줄이겠다는 것

  + 정규화 기법 중, 코퍼스에 있는 단어의 개수를 줄이는 기법

+ Bow (Bag of Words) 표현을 사용하는 NLP에서 주로 사용

+ 어간 추출이 표제어 추출보다 보통 빠름

  

##### 어간

+ 단어의 의미를 담고 있는 핵심 부분

##### 접사

+ 단어에 추가적인 의미를 주는 부분



#### (f) 표제어 추출

+ 표제어
  + 기본 사전형 단어로 그 단어의 뿌리
  + 예
    + be : is, am , are 의 뿌리



##### nltk.stem.WordNetLemmatizer

+ 단어의 품사를 알려줘야 정확하게 표제어를 추출 가능

```python
from nltk.stem import WordNetLemmatizer

# 1. 품사를 알려주지 않는 경우
lemmatizer = WordNetLemmatizer()

words = ['policy', 'doing', 'organization', 'have', 'going', 'love', 'lives', 'fly', 'dies', 'watched', 'has', 'starting']

print('표제어 추출 전 :',words)
print('표제어 추출 후 :',[lemmatizer.lemmatize(word) for word in words])

>>>
표제어 추출 전 : ['policy', 'doing', 'organization', 'have', 'going', 'love', 'lives', 'fly', 'dies', 'watched', 'has', 'starting']
표제어 추출 후 : ['policy', 'doing', 'organization', 'have', 'going', 'love', 'life', 'fly', 'dy', 'watched', 'ha', 'starting']
    
    
    
# 2. 품사를 알려주는 경우
lemmatizer.lemmatize('dies', 'v')
>>> 'die'
lemmatizer.lemmatize('watched', 'v')
>>> 'watch'
lemmatizer.lemmatize('has', 'v')
>>> 'have'
```



#### (g) 어간추출(Stemming)

##### nltk.stem.PorterStemmer

+ 어간 추출 알고리즘
  + 포터 알고리즘(영어에서 준수한 선택)
    + ALIZE → AL
      ANCE → 제거
      ICAL → IC
    + formalize → formal
      allowance → allow
      electricical → electric
  + 랭커스터 스태머 알고리즘

```python
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

stemmer = PorterStemmer()

sentence = "This was not the map we found in Billy Bones's chest, but an accurate copy, complete in all things--names and heights and soundings--with the single exception of the red crosses and the written notes."
tokenized_sentence = word_tokenize(sentence)

print('어간 추출 전 :', tokenized_sentence)
print('어간 추출 후 :',[stemmer.stem(word) for word in tokenized_sentence])

>>>

어간 추출 전 : ['This', 'was', 'not', 'the', 'map', 'we', 'found', 'in', 'Billy', 'Bones', "'s", 'chest', ',', 'but', 'an', 'accurate', 'copy', ',', 'complete', 'in', 'all', 'things', '--', 'names', 'and', 'heights', 'and', 'soundings', '--', 'with', 'the', 'single', 'exception', 'of', 'the', 'red', 'crosses', 'and', 'the', 'written', 'notes', '.']
    
어간 추출 후 : ['thi', 'wa', 'not', 'the', 'map', 'we', 'found', 'in', 'billi', 'bone', "'s", 'chest', ',', 'but', 'an', 'accur', 'copi', ',', 'complet', 'in', 'all', 'thing', '--', 'name', 'and', 'height', 'and', 'sound', '--', 'with', 'the', 'singl', 'except', 'of', 'the', 'red', 'cross', 'and', 'the', 'written', 'note', '.']
```



#### (h) 한국어 어간 추출

##### 한국어 구조

| 언                     | 품사               |
| ---------------------- | ------------------ |
| 체언                   | 명사, 대명사, 수사 |
| 수식언                 | 관형사, 부사       |
| 관계언                 | 조사               |
| 독립언                 | 감탄사             |
| **용언** (어간 + 어미) | **동사, 형용사**   |



##### 규칙 & 불규칙 경우

+ 구체적 규칙은 [나무위키참조](https://namu.wiki/w/한국어/불규칙%20활용)

+ 규칙적인 경우
  + 어간이 어미를 취할 때, 어간의 모습이 변하지 않는 경우는 어간(stem)을 분리해주면 됨
+ 불규칙적인 경우
  + 어간이 어미를 취할 때, 어간의 모습이 변하는 경우, 복잡한 규칙 필요





## [1] re

+ dfd

  ```python
  import re 
  
  train = train.dropna(how = 'any')
  train['data'] = train['data'].str.replace("[^ㄱ-ㅎㅏ-ㅣ가-힣 ]"," ")
  test['data'] = test['data'].str.replace("[^ㄱ-ㅎㅏ-ㅣ가-힣 ]"," ")
  ```

  







# 3. 언어모델

## [1] 언어 모델이란?

### (1) 정의

+ 언어모델은 **단어 시퀀스에 확률을 할당**하는 일을 하는 모델
  + 기본모델
    + 이전의 단어들로 다음 단어를 예측
  + BERT
    + 주어진 양쪽 단어들로부터 가운데 비어있는 단어 예측

### (2) 예시

+ 기계 번역
  $$
  P(나는 버스를 탔다) > P(나는 버스를 태운다
  $$

+ 오타 교정
  $$
  P(달려갔다) > P(잘려갔다)
  $$
  
+ 음성 인식
  $$
  P(나는 메롱을 먹는다) < P(나는 메론을 먹는다)
  $$
  

### (3) 확률 표현

+ 하나의 단어를 w, 단어 시퀀스를 W라고 한다면
  $$
  P(W) = P(w_1,w_2,\cdots, w_n)\\
  \\
  P(w_n|w_1,\cdots,w_{n-1})\\
  \\
  P(W) = P(w_1,w_2,\cdots, w_n) = \prod_{i=1}^nP(w_i|w_1,\cdots,w_{i-1})
  $$
  

## [2] 통계적 언어모델

### (1) count 기반

**조건부확률기반**
$$
P(\text{is }| \text{the man who}) = \frac{\text{ count(the man who is)}}{\text{count(the man who)}}
$$


### (2) n-gram





### (3) count 기반의 한계

**희소문제**

+ 충분한 데이터를 관측하지 못하여 언어를 정확히 모델링하지 못하는 문제를 **희소 문제(sparsity problem)**
  + cur sentence나 cur sentence next가 training set에 없으면, 확률이 정의되지 않거나, 확률이 0 됨

+ count 기반은 희소문제를 해결하지 못함
  + n-gram, 스무딩, 백오프와 같은 여러 기법들로도 근본해결 불가
  + 인공신경망 언어모델로 트렌드 넘어감







+ 





# ---------------------



+ find-tuning
  + 다른 작업에 대해서 파라미터 재조정을 위한 추가 훈련 과정을 **파인 튜닝(Fine-tuning)**이라고 합니다.
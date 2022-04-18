[toc]

# DB03 - ManyToMany

# INTRO

## 1. 1:N 모델의 한계

+ 1 : N 모델을 이용해서는 의사와 환자의 예약관계같은 다대다 관계를 모델링 할 수 없음

+ Table1 (1:N)

  | 환자 | 의사 |
  | ---- | ---- |
  | 1    | 1    |
  | 2    | 1    |
  | 3    | 1    |
  | 1    | 2    |
  | 2    | 2    |
  | 3    | 2    |
  |      |      |

  + 새로운 예약을 생성하려면 새로운 환자 객체를 생성해야 함

    + 1개의 1번 환자로, 의사 1, 2 모두를 참조할 수 없음
    + 예약 관계 외의 정보들 ( 진료시간, 진료과 ) 같은 것들 모델링하려면 중복되는 내용을 많이 포함하게 됨

    





# 중개 테이블

+ N : M 관계를, 중개 테이블을 이용해서 1 : N 과 1 : M 관계로 만들어냄
  + 즉 N : M 을 1:N, M:1 처럼 바꿔야함
  + **환자 >-< 의사  (N:M)**     ->    **환자 -< 중계테이블 >- 의사 (1 : N, M : 1)**

## 1. 직접생성 (ManyToManyField 이용 x)

+ 코드

  ```PYTHON
  from django.db import models
  
  
  class Doctor(models.Model):
      name = models.TextField()
  
      def __str__(self):
          return f'{self.pk}번 의사 {self.name}'
  
  class Patient(models.Model):
      name = models.TextField()
  
      def __str__(self):
          return f'{self.pk}번 환자 {self.name}'
  
  # 중개모델 작성
  class Reservation(models.Model):
      doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
      patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
  
      def __str__(self):
          return f'{self.doctor_id}번 의사의 {self.patient_id}번 환자'
  ```





## 2. ManyToManyField 이용

### [1] 생성법 / 메서드 / Argument / 저장

#### (1) 생성법

+ `models.py`의 `Doctor / Patient` class 둘 중 아무 곳에 `ManyToManyField` 넣어주면 됨
+ `ManyToManyField` 만 이용시, 중개테이블에서 N:M 관계만 표현할 수 있고, 부가정보(진료과목, 예약시간 등)는 넣을 수 없음
+ 부가정보 표현하려면, `through` 이용해서, 직접 중개테이블 만들어줘야



#### (2) 메서드 : add, remove

+ 객체 생성

  ```python
  doctor1 = Doctor.objects.create(name='justin')
  patient1 = Patient.objects.create(name='tony')
  patient2 = Patient.objects.create(name='harry')
  ```

+ 참조

  ```python
  patient1.doctors.add(doctor1)       
  patient1.doctors.all()
  patient2.doctors.remove(doctor1)
  ```

+ 역참조

  ```python
  doctor1.patient_set.add(patient2)
  doctor1.patient_set.all()
  doctor1.patient_set.remove(patient1)`
  ```


+ 중개테이블 만든 경우

  ```python
  reservation1 = Reservation(doctor=doctor1, patient=patient1, symptom='headache')
  patient2.doctors.add(doctor1, through_defaults={'symptom': 'flu'})
  ```

  



#### (3) Argument : related_name, through, symmetrical

+ `related_name` 

  + Doctor에서 Patient 역참조할 때, `patient_set` 으로 안하고, `realted_name` 이용하면 됨

  + `doctors = models.ManyToManyField(Doctor, related_name='patients')`

  + 역참조 (기존의 `patient_set` 은 사용 못함) 코드

    ```python
    doctor1.patients.add(patient2)
    doctor1.patients.all()
    doctor1.patients.remove(patient1)
    ```

    

+ `through`

  + 중개테이블을 직접만드는 경우활용
  + Many to Many 관계 표현뿐만아니라, 부가 정보를 넣는 경우에 사용

  

+ `symmetrical`
  + `True`인 경우 두 class에서 한 class 가 다른 한 class 참조하면, 반대반향도 참조하게 됨
    + 예 : A가 B 팔로우시, B도 A 팔로우하게 됨

​	

#### (4) 저장방법 2가지

+ `ManyToManyField` 이용하고, 중개테이블을 생성한 경우, 2가지 방법으로 N:M 관계 저장가능

```python
# 방법1
reservation1 = Reservation(doctor=doctor1, patient=patient1, symptom='headache')
patient2.doctors.add(doctor1, through_defaults={'symptom': 'flu'})

# 방법2
patient2.doctors.add(doctor1, through_defaults={'symptom': 'flu'})

# 위의 두 방법 모두, Reservation.objects.all() 하면, instance 저장되어 있음
```





### [2] 코드

#### (1) 중개테이블 모델링 안한 경우

+ ```python
  from django.db import models
  
  class Doctor(models.Model):
      name = models.TextField()
  
      def __str__(self):
          return f'{self.pk}번 의사 {self.name}'
  
  class Patient(models.Model):
      # ManyToManyField - related_name 작성
      doctors = models.ManyToManyField(Doctor, related_name='patients')
      name = models.TextField()
  
      def __str__(self):
          return f'{self.pk}번 환자 {self.name}'
  ```

  + 실제로 Doctor와 Patient에는 아무 Field도 만들어지지 않고, appname_patient_doctor 중개 테이블 생성됨

    

+ 인스턴스 코드

  ```python
  doctor1 = Doctor.objects.create(name='justin')
  patient1 = Patient.objects.create(name='tony')
  patient2 = Patient.objects.create(name='harry')
  
  patient1.doctors.add(doctor1)
  patient1.doctors.all()
  doctor1.patients.all()
  
  doctor1.patients.add(patient2)
  doctor1.patients.all()
  patient2.doctors.all()
  patient1.doctors.all()
  
  doctor1.patients.remove(patient1)
  doctor1.patients.all()
  patient1.doctors.all()
  
  patient2.doctors.remove(doctor1)
  patient2.doctors.all()
  doctor1.patients.all()
  ```

  



#### (2)중개테이블 모델링 한 경우

+ 추가적인 속성 (`symptom` , `reserved_at`) 활용가능

  ```python
  from django.db import models
  
  class Doctor(models.Model):
      name = models.TextField()
  
      def __str__(self):
          return f'{self.pk}번 의사 {self.name}'
  
  class Patient(models.Model):
      doctors = models.ManyToManyField(Doctor, related_name='patients',through='Reservation')
      name = models.TextField()
  
      def __str__(self):
          return f'{self.pk}번 환자 {self.name}'
  
  class Reservation(models.Model):
      doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
      patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
      symptom = models.TextField()
      reserved_at = models.DateTimeField(auto_now_add=True)
  
      def __str__(self):
          return f'{self.doctor.pk}번 의사의 {self.patient.pk}번 환자'
  ```

  

+ 인스턴스 코드

  ```python
  doctor1 = Doctor.objects.create(name='justin')
  patient1 = Patient.objects.create(name='tony')
  patient2 = Patient.objects.create(name='harry')
  
  reservation1 = Reservation(doctor=doctor1, patient=patient1, symptom='headache')
  reservation1.save()       # reservation이 object instance 이므로 저장해주어야 함
  doctor1.patients.all()
  patient1.doctors.all()
  
  patient2.doctors.add(doctor1, through_defaults={'symptom': 'flu'})
  doctor1.patients.all()
  patient2.doctors.all()
  
  doctor1.patients.remove(patient1)
  patient2.doctors.remove(doctor1)
  ```
  
  







# Like 구현

+ 서로 다른 모델 간의 N : M 관계
+ user와 article instance들
  +  한 user가 여러 article like 할 수 있고, 한 article도 여러 user로 부터 like 받을 수 있음 



## 1. ManyToManyField

+ Article class에 주로 많이 작성했으므로, User가 아닌 Article에 작성하기로



### [1] 코드

#### (1) articles/models.py

```python
# articles/models.py
from django.db import models
from django.conf import settings


class Article(models.Model):
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL)  # 생성

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content

```

+ 작성 후, migration 하기

  

#### (2) urls.py

```python
path('<int:article_pk>/likes/', views.likes, name='likes'),
```



#### (3) views.py

```python
@require_POST
def likes(request, article_pk):
    
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk = article_pk)

        # remove 좋아요 없애기 경우    
        # if request.user in article.like_users.all():
        if article.like_users.filter(pk=request.user.pk).exists():
            article.like_users.remove(request.user)
    
         # add 좋아요 경우
        else:
            article.like_users.add(request.user)
        
        return redirect('articles:index')
    return redirect('accounts:login')
    
```





#### (4) templates/articles/index.html

```django
...
<div>
  <form action="{% url 'articles:likes' article.pk %}" method='POST'>  # 역참조
    {% csrf_token %}
    {% if user in article.like_users.all %}         # 이미 좋아요 눌렀다면
      <input type='submit' value='좋아요 취소'>
    {% else %}
      <input type='submit' value='좋아요'>
    {% endif %}
</div>
...
```



























# follow 구현



## 1. profile 구현

### [1] accounts.urls.py

```python
path('<username>/', views.profile, name='profile'),  # 맨 위로가면, 아주 큰 문제가 생김. accounts/string 꼴 주소는 모두 이것에 걸림
```



### [2] accounts/views.py

```python

def profile(request, username):
    user = get_user_model()
    person = get_object_or_404(user, username=username)
    context = {
        'person':person,
    }
    
    return render(request, 'accounts/profile.html',context)
```



### [3] accounts/profile.html

```django
{% extends 'base.html' %}
{% block content %}
<h1>  {{ person.username }} 님의 profile </h1>
<hr>

{% comment %} 작성한 게시글 목록 {% endcomment %}
<h2> {{ person.username }} 이 작성한 게시글 </h2>
{% for article in person.article_set.all %}
<p> {{ article.title }} </p>
{% endfor %}

<hr>
{% comment %} 작성한 댓글 목록 {% endcomment %}
<h2> {{ person.username }} 작성한 댓글 목록 </h2>

{% for comment in person.comment_set.all %}
<p> {{ comment.content }} </p>
{% endfor %}

<hr>
{% comment %} 좋아요를 누른 게시글 목록 {% endcomment %}
<h2> {{ person.username }} 좋아요를 누른 게시글 목록 </h2>
{% for article in person.like_articles.all %}
<p> {{ article.title }} </p>
{% endfor %}


<a href="{% url 'articles:index' %}"> back </a>


{% endblock content %}
```













## 2. follow 구현

+ 같은 class를 참조하므로 `'self'` 넣어주기

+ `symmetrical` 은 `True` 라면 한쪽 관계 성립되면 양방향 다 성립되는 것

  + A가 B 팔로우하면, B도 A 팔로우

     

### [1] accounts/models.py

```python
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')  
 # follwoings는 현재 내가 FOLLOWING을 하고 있는 사람들 / sys : 내가 FOLLOW 한다고 상대가 나를 FOLLOW 하지 않음 / 역참조 : followers ( 다른 사람이 나를 찾을 때 )
```

+ 마이그레이션 하기

  

### [2] 생성된 중개테이블

| table name : accounts_user_followings |         |
| ------------------------------------- | ------- |
| id                                    | integer |
| from_user_id  (여기 user : 주체)      | bigint  |
| to_user_id                            | bigint  |





### [3] accounts/profile.html

```django
{% extends 'base.html' %}

{% block content %}
<h1>  {{ person.username }} 님의 profile </h1>


-----------여기부터 follow--------------------------------------------------
{% with  followers=person.followers.all following=person.followings.all  %}
<div>
{% comment %} 
 팔로워 : {{ person.followers.all|length }} / 팔로우 : {{ person.followings.all|length }}
  {% endcomment %}
 팔로워 : {{ followers|length }} / 팔로우 : {{followings|length }}
</div>
<div>
  {% if user != person %}
<form action="{% url 'accounts:follow' person.pk %}" method='POST'>
  {% csrf_token %}
{% comment %} 
  {% if request.user in person.followers.all %}
   {% endcomment %}
  {% if request.user in followers %}
   <input type='submit' value='언팔로우'>
   
  {% else %}
  <input type='submit' value='팔로우>'>
  {% endif %}

</form>
{% endif %}
</div>
{% endwith %}

----------------------------------------------아래는 profile-----------------
<hr>

{% comment %} 작성한 게시글 목록 {% endcomment %}
<h2> {{ person.username }} 이 작성한 게시글 </h2>
{% for article in person.article_set.all %}

<p> {{ article.title }} </p>

{% endfor %}

<hr>
{% comment %} 작성한 댓글 목록 {% endcomment %}
<h2> {{ person.username }} 작성한 댓글 목록 </h2>

{% for comment in person.comment_set.all %}
<p> {{ comment.content }} </p>
{% endfor %}

<hr>
{% comment %} 좋아요를 누른 게시글 목록 {% endcomment %}
<h2> {{ person.username }} 좋아요를 누른 게시글 목록 </h2>
{% for article in person.like_articles.all %}
<p> {{ article.title }} </p>
{% endfor %}


<a href="{% url 'articles:index' %}"> back </a>


{% endblock content %}

```



#### [4] accounts/views.py



```python
# like 와 동일한 구조
@require_POST
def follow(request, user_pk):
    if request.user.is_authenticated:
        you = get_object_or_404(get_user_model(), pk=user_pk) # 상대방
        me = request.user
    
        if me != you:
            if you.followers.filter(pk=me.pk).exists():
            # if me in you.followers.all():
                you.followers.remove(me)
            else:
                you.followers.add(me)
        return redirect('accounts:profile', you.username)
    return redirect('accounts:login')
```





## 3. 새로 나온 표현들

### [1] filter(pk=request.user.pk).exists():

#### (1) 코드

```python
# 아래 두개는 같은 것인데, exists() 가 더빠르게 동작

# if request.user in article.like_users.all():
if article.like_users.filter(pk=request.user.pk).exists():
```

#### (2) 사용하는 이유

+ 속도에 가장 영향을 미치는 것은 데이터 전송부분임
  + 데이터 많다면, 모든 것을 조회하면 오래걸림
  + `article.like_users.all()` 는 DB에서 데이터 가져온 것이고 
  + `filter(pk=request.user.pk).exists():` 는 filter 부분까지는 DB에서 하는 것?
+ 그래서 데이터가 많은 경우 filter 통해서 최소한의 데이터만을 DB에서 처리해서 가져오도록





### [2] get_object_or_404(User, username=username)

#### (1) 코드

```python
# accounts/views.py

def profile(request, username):
    user = get_user_model()
    person = get_object_or_404(user, username=username)
    context = {
        'person':person,
    }
    
    return render(request, 'accounts/profile.html',context)
```



### [3] with [문서](https://docs.djangoproject.com/en/4.0/ref/templates/builtins/#with)

#### (1) 코드

+ DB에서 expensive 하게 작동하는 method 결과 저장해서 사용

```django
{% with  followers=person.followers.all following=person.followings.all  %}
<div>
{% comment %} 
 팔로워 : {{ person.followers.all|length }} / 팔로우 : {{ person.followings.all|length }}
  {% endcomment %}
 팔로워 : {{ followers|length }} / 팔로우 : {{followings|length }}
</div>
<div>
  {% if user != person %}
<form action="{% url 'accounts:follow' person.pk %}" method='POST'>
  {% csrf_token %}
{% comment %} 
  {% if request.user in person.followers.all %}
   {% endcomment %}
  {% if request.user in followers %}
   <input type='submit' value='언팔로우'>
   
  {% else %}
  <input type='submit' value='팔로우>'>
  {% endif %}

</form>
{% endif %}
</div>
{% endwith %}
```















# 질문사항

+  bootstrap form 수정

  https://django-bootstrap-v5.readthedocs.io/en/latest/templatetags.html#bootstrap-field 참고

  

+  is_valid() 통과 못하면? else의 context에 담기는 것?

  ```python
  @require_http_methods(['GET', 'POST'])
  def signup(request):
      if request.user.is_authenticated:
          return redirect('articles:index')
  
      if request.method == 'POST':
          form = CustomUserCreationForm(request.POST)
          if form.is_valid():
              user = form.save()
              auth_login(request, user)
              return redirect('articles:index')
      else:
          form = CustomUserCreationForm()
      context = {
          'form': form,
      }
      return render(request, 'accounts/signup.html', context)
  ```

  + 답 : 기존의 작성 내용 + 에러메세지 + 에러난 부분은 지워서 내보내기



+ custom.Meta 의 필드가 왜 더 적은지?

 ```python
 class CustomUserCreationForm(UserCreationForm):
 
     class Meta(UserCreationForm.Meta):
         model = get_user_model()
         # fields = UserCreationForm.Meta.fields + ('email',)
         fields = '__all__'
 ```

---

생각

 https://github.com/django/django/blob/main/django/contrib/auth/forms.py

```python
class UserCreationForm(forms.ModelForm):
    """
    A form that creates a user, with no privileges, from the given username and
    password.
    """

    error_messages = {
        "password_mismatch": _("The two password fields didn’t match."),
    }
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    class Meta:
        model = User
        fields = ("username",)
        field_classes = {"username": UsernameField}
```

\__all__ 하면 User의 모든 field 나오는 이유가 

위의 Meta에서  model = User이므로,  UserCreationForm.Meta 하면 그냥 USER model 가져오는 것?이지않을까?





+ 필터

 팔로워 : {{ person.followers.all|length }} / 팔로우 : {{ request.user.followings.all|length }}

 

 

+ with

• https://docs.djangoproject.com/en/4.0/ref/templates/builtins/

`{% with  followers=person.followers.all following=person.followings.all  %}`

 

여기서 변수선언해서 쓸 수 있음 / 

- DB에서 expensive 하게 작동하는 method 결과 저장해서 사용?

 

`{% endwith %}`

 

+ 

·     `article.like_users.all()` 는 DB에서 데이터 가져온 것이고 

·    `filter(pk=request.user.pk).exists():` 는 filter 부분까지는 DB에서 하는 것?

 

 

+ ` person = get_object_or_404(get_user_model(), username=username)` (model=, keyword= 으로 받은 것들 get() 함수에 넘김)


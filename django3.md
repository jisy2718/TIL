# Form



+ Form 선언
  + models.py 와 유사



+ Form Fields
  + input의 유효성 검사를 처리
+ Widgets
  + 웹페이지에서 input element의 단순 raw한 렌더링 처리





+ Form fileds 와 widget을 이용해서 여러 filed 이용가능
+ [widgets 공식문서](https://docs.djangoproject.com/en/4.0/ref/forms/widgets/)
+ [장고 권장 작성 style](https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/coding-style/)



# Model form

1. 모델 필드 속성에 맞는 html element를 만들어 주고(model의 fields를 보고 tag, type 등 알아서 만들어줌)
2. 이를 통해 받은 데이터를 view 함수에서 유효성 검사를 할 수 있도록 함

--------

+ model form 

  + 실제 DB에 저장이 이루어지는 데이터를 받으려면 Model form 사용
  + db와 비슷한 구조

+ ModelForm class

  + Meta class
    + model, fields, exclude 

  ---------------

+ form 은 db와 관련이 없음

  + 데이터를 처리해야하지만, db에 저장하지는 않을 때 이용
  + 예를 들어 로그인 할 때는 form 이용

--------------------



## [1] form

### (1) create

```python
# 요청으로부터 데이터 받아서 
# Model 객체에 담아서
# DB API 활용해서 DB에 저장

# 1. form 이용
def create(request):
    form = ArticleForm(request, POST)

    # 유효성 검사
    if form.is_valid():  # 받은 데이터가 유효한 경우
        article = form.save()  # DB에 DATA 저장됨 & return 으로 save 된 객체 나옴
        return redirect('articles:detail', article.pk)
    else: # 유효하지 않은 input을 받은 경우
        return redirect('articles:new')
    
    
# 2. 아래는 form 을 안쓰는 경우의 코드    
def create(request):

    title = request.POST.get('title')
    content = request.POST.get('content')

    article = Article(title=title, content=content)

    article.save()

    return redirect('articles:index')
 
```





## [3] method

### (1) save()

```python
article = Article.objects.get(pk=1)
form = # 이 경우 수정
form.save()  
```













# error 해결

+ NoReverseMatch
  + 내가 요청한 주소(해당템플릿)의 url만 보면됨!
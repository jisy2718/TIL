# Bootstrap

## 1. class 관련

## [1] [progress](https://getbootstrap.com/docs/4.0/components/progress/)

+ 가로줄을 이용해서, 시작적으로 0 ~ 100 % 를 표현할 수 있음

+ 0414 practice에 이용

+ 코드

  ```html
  <div class="progress">
    <div class="progress-bar bg-danger" role="progressbar" style="width: {{ ratio_a }}%" aria-valuenow="{{ ratio_a }}" aria-valuemin="0" aria-valuemax="100"> {{ ratio_a }}</div>
    <div class="progress-bar bg-primary" role="progressbar" style="width: {{ ratio_b }}%" aria-valuenow="{{ ratio_b }}" aria-valuemin="0" aria-valuemax="100"> {{ ratio_b }}</div>
  </div>
  ```

  





## 2. if/else/for 등

### [1] if / else/ for

```html
{% for comment in either.comment_set.all %}
  {% if comment.pick == 'red'  %}
    <div class="alert alert-danger" role="alert">{{ comment.content }}</div>
  {% else %}
    <div class="alert alert-primary" role="alert">{{ comment.content }}</div>
  {% endif %}
  <hr>
{% endfor %}
```






























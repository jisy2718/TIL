from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model  # 이를 호출하면, 현재 project에서 사용하는 user class를 return해줌

# 그대로 상속 받아서 field 만 지정할 것
class CustomUserChangeForm(UserChangeForm):

    # password=None   # 회원정보 수정에서 비밀번호 링크 없애기 /UserChangForm 구조 확인해보고 이렇게 하면 됨

    class Meta:
        model = get_user_model()  # user
        fields = ('email', 'first_name', 'last_name')

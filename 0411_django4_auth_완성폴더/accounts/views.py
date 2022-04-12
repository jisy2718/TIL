from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm #UserChangeForm
from .forms import CustomUserChangeForm
from django.contrib.auth import update_session_auth_hash

# Create your views here.
@require_http_methods(['POST','GET'])
def login(request):
    data = request.GET.get('next')   # '/articles/create/' 로 login 후에 redirect가 되어야 함


    # 이미 로그인 된 사람의 접근 차단
    if request.user.is_authenticated:
        return redirect('articles:index')


    if request.method =="POST":
        form= AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'articles:index')   # 이렇게 표현하면, data 있으면 왼쪽으로, 없으면 오른쪽으로 감

    else:
        form = AuthenticationForm()
        
        
    context = {
        'form':form,
    }
    
    return render(request, 'accounts/login.html',context)


@require_POST
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)

    return redirect('articles:index')



# 회원가입 페이지(get)와 회원가입 진행부분(post)
@require_http_methods(['GET', 'POST'])
def signup(request):

    if request.user.is_authenticated:
        redirect('articles:index')

    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request,user)
            return redirect('articles:index')

    else:
        form = UserCreationForm()
    context = {
        'form':form,
    }
    return render(request,'accounts/signup.html',context)



# 회원탈퇴
@require_POST  # @login_required 와 같이 쓸 수 없음
def delete(request):
    # 현재 로그인한 유저만
    if request.user.is_authenticated:
        # 반드시 회원 탈퇴 후 로그아웃 호출
        request.user.delete()
        auth_logout(request)  # 이것하면, user 정보가 request에서 빠지므로, 위아래 순서 바뀌면 회원탈퇴 안됨
    
    return redirect('articles:index')



def update(request):
    if request.method=='POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')

    else:
        form=CustomUserChangeForm(instance=request.user)
    context = {
        'form':form,
    }    
    return render(request, 'accounts/update.html',context)



@login_required
@require_http_methods(['GET','POST'])
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user = form.save()  # 비밀번호 변경
            update_session_auth_hash(request, user) # 여기 user는 비번 바꾼 user
            return redirect('articles:index')

    else:
        pass
        form = PasswordChangeForm(request.user) 

    context = {
        'form':form,
    }
    return render(request, 'accounts/change_password.html', context)
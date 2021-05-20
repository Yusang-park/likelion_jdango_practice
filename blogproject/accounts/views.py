from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.


def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                username=request.POST['username'], password=request.POST['password1'],
            )
            # 유저 생성
            user.save()  # 저장해줌
            auth.login(request, user)  # 로그인 함
            return redirect('main:index')  # 메인으로 돌아감
    return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('main:index')
        else:
            message = '아이디 혹은 비밀번호가 틀렸어요'
            return render(request, 'login.html', {'message': message})
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('main:index')
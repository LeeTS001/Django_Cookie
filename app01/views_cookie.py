from django.shortcuts import render, HttpResponse, redirect

# Create your views here.


# 装饰器，用于根据cookie判断当前登录状态，确认跳转页面
def login_require(fn):
    def inner(request, *args, **kwargs):
        if not request.COOKIES.get('is_login') == 'OK':
            path = request.path_info
            print(path)
            return redirect('/API/login/?to={}'.format(path))
        ret = fn(request, *args, **kwargs)
        return ret
    return inner


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        passwd = request.POST.get('pwd')
        if username == 'lee' and passwd == '123456':
            path = request.GET.get('to')
            if path:
                ret = redirect(path)
            else:
                ret = redirect('/API/index/')
            ret.set_cookie('is_login', 'OK', max_age=300)    # 设置cookie，用于状态校验
            return ret
    return render(request, 'login.html')


def logout(request):
    ret = redirect('/API/login/')
    ret.delete_cookie('is_login')   # 注销时清除cookie
    return ret


@login_require
def home(request):
    # if not request.COOKIES.get('is_login') == 'OK':
    #     return redirect('/API/login/')
    return render(request, 'home.html')


@login_require
def index(request):
    return render(request, 'index.html')

# Create your views here.
import hashlib
import uuid
from random import randint

from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

# from app.sms import SMS
from app.models import User, Blog, Comment


# 前台
# 生成token
def make_token():
    uid = str(uuid.uuid4())
    md = hashlib.md5()
    md.update(uid.encode('utf-8'))

    return uid


# 密码加密
def make_pwd(pwd):
    password = str(pwd)
    mdd = hashlib.md5()
    mdd.update(password.encode('utf8'))
    return mdd.hexdigest()


# 注册
def register(request):
    if request.method == 'GET':
        return render(request, 'app/login.html')
    else:
        u_name = request.POST.get("username")
        u_phone = request.POST.get("phone")
        pwd = request.POST.get("password")
        place = request.POST.get("native_place")
        profession = request.POST.get("profession")
        email = request.POST.get("email")
        # sms = request.POST.get("sms")
        u_icon = request.FILES['icon']
        users = User.objects.filter(phone=u_phone)

        if users.exists():
            return HttpResponse("此手机号已被注册")

        user = User()
        user.icon = u_icon
        user.username = u_name
        user.phone = u_phone
        user.password = make_pwd(pwd)
        user.native_place = place
        user.profession = profession
        user.email = email
        user.token = make_token()
        user.save()
        red = redirect(reverse('app:dologin'))
        red.set_cookie('token', user.token)

        return red

    # 从session中取出yzm
    # yzm = request.session.get('yzm')
    # yzm = str(yzm)
    # code = request.GET.get('sms')
    # print(yzm,code)
    # if yzm == code:
    #     return render(request,'index.html')
    # return redirect(reverse("app:index"))


# 登录
def login(request):
    if request.method == 'GET':
        return render(request, 'app/login.html')
    else:
        phone = request.POST.get('phone')
        pwd = request.POST.get('password')
        users = User.objects.filter(phone=phone)
        if not users.exists():
            return render(request, "app/404.html")
        user = users.first()
        print(user)
        print(make_pwd(pwd))
        if user.password == make_pwd(pwd):
            response = HttpResponseRedirect(reverse('app:dologin'))
            response.set_cookie('token', user.token)

            return response

        else:
            return HttpResponse("账号或密码错误，请重新登录")


def dologin(request):
    token = request.COOKIES.get("token")
    if not token:
        return render(request, 'app/404.html')
    user = User.objects.get(token=token)
    url = '/static/upload/' + user.icon.url
    blog = user.blog_set.all()
    # comment = Comment.objects.filter(Q(u_comm_id=user.id) & Q(b_comm_id=blog))
    context = {'users': user,
               'blogs': blog,
               'url': url
               # 'comment':comment
               }
    return render(request, 'app/dologin.html', context=context)


# 发送验证码
# def send(request):
# phone = request.GET.get('phone')
# sms = SMS('明天是个好日子','SMS_151549083')
# num = randint(100000,999999)
# request.session['yzm'] = num
# request = SMS.send_sms(phone,num)
# return HttpResponse(request)

def index(request):
    token = request.COOKIES.get('token')
    user = User.objects.get(token=token)
    blogs = user.blog_set.all()

    return render(request, 'app/index.html', context={'blogs': blogs,'user':user})


def about(request):
    return render(request, 'app/about.html')


def new(request):
    token = request.COOKIES.get('token')
    user = User.objects.get(token=token)
    blogs = user.blog_set.all()
    return render(request, 'app/new.html', context={'blogs': blogs,'user':user})


def newlist(request):
    token = request.COOKIES.get('token')
    user = User.objects.get(token=token)
    blogs = user.blog_set.all()
    return render(request, 'app/newlist.html',context={'blogs':blogs,'user':user})


def share(request):
    return render(request, 'app/share.html')


# 后台
def adminindex(request):
    if request.method == 'GET':
        return render(request, 'admin/index.html')
    # else:
    #     phone = request.POST.get("phone")
    #     pwd = request.POST.get("password")
    #     users = User.objects.filter(phone=phone)
    #     if not users.exists():
    #         render(request,'app/404.html')
    #     user = users.first()
    #     if user.password == make_pwd(pwd):
    #         HttpResponseRedirect(reverse('a'))


def adminmain(request):
    # token = request.COOKIES.get("token")
    # if not token:
    #     return render(request, 'app/404.html')
    # user = User.objects.get(token=token)
    # blog = user.blog_set.all()
    # print(blog)
    # context = {'users': user,
    #            'blogs': blog
    #            }
    return render(request, 'admin/main.html')


def add_article(request):
    return render(request, 'admin/add-article.html')


def add_category(request):
    return render(request, 'admin/add-category.html')


def add_flink(request):
    return render(request, 'admin/add-flink.html')


def add_notice(request):
    return render(request, 'admin/add-notice.html')


def article(request):
    return render(request, 'admin/article.html')


def category(request):
    return render(request, 'admin/category.html')


def comment(request):
    return render(request, 'admin/comment.html')


def flink(request):
    return render(request, 'admin/flink.html')


def loginlog(request):
    return render(request, 'admin/loginlog.html')


def manage_user(request):
    return render(request, 'admin/manage-user.html')


def notice(request):
    return render(request, 'admin/notice.html')


def readset(request):
    return render(request, 'admin/readset.html')


def setting(request):
    return render(request, 'admin/setting.html')


def update_flink(request):
    return render(request, 'admin/update-flink.html')


def update_category(request):
    return render(request, 'admin/update-category.html')


def update_article(request):
    return render(request, 'admin/update-article.html')

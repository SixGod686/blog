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


def dologin(request):
    token = request.COOKIES.get("token")
    if not token:
        return render(request, 'app/404.html')
    user = User.objects.get(token=token)
    blog = user.blog_set.all()
    # comment = Comment.objects.filter(Q(u_comm_id=user.id) & Q(b_comm_id=blog))
    print(blog)
    context = {'users':user,
               'blogs':blog,
               # 'comment':comment
               }
    return render(request, 'app/index.html',context=context)

def about(request):
    return render(request, 'app/about.html')

def new(request):
    return render(request, 'app/new.html')

def newlist(request):
    return render(request, 'app/newlist.html')

def share(request):
    return render(request, 'app/share.html')

#密码加密
def make_pwd(pwd):
    password = pwd
    mdd = hashlib.md5()
    mdd.update(password.encode('utf-8'))
    return mdd.hexdigest()

# 登录
def login(request):
    if request.method == 'GET':
        return render(request, 'app/login.html')
    else:
        phone = request.POST.get('phone')
        pwd = request.POST.get('password')
        user = User.objects.filter(phone=phone)
        if not user.exists():
            return render(request, "app/404.html")
        user = user.first()
        print(user)
        if user.password == make_pwd(pwd):
            response = HttpResponseRedirect(reverse('app:index'))
            response.set_cookie('token',user.token)

            return response

        else:
            return HttpResponse("账号或密码错误，请重新登录")


# 发送验证码
# def send(request):
    # phone = request.GET.get('phone')
    # sms = SMS('明天是个好日子','SMS_151549083')
    # num = randint(100000,999999)
    # request.session['yzm'] = num
    # request = SMS.send_sms(phone,num)
    # return HttpResponse(request)

# 生成token
def make_token():
    uid = str(uuid.uuid4())
    md = hashlib.md5()
    md.update(uid.encode('utf-8'))

    return uid

# 注册
def register(request):
    if request.method == 'GET':
        return redirect(reverse('app:login'))
    else:
        u_name = request.POST.get("username")
        u_phone = request.POST.get("phone")
        pwd = request.POST.get("password")
        place = request.POST.get("native_place")
        profession = request.POST.get("profession")
        email = request.POST.get("email")
        # sms = request.POST.get("sms")
        users = User.objects.filter(phone=u_phone)
        if users.exists():
            return HttpResponse("此手机号已被注册")

        user = User()
        user.username = u_name
        user.phone = u_phone
        user.password = make_pwd(pwd)
        user.native_place = place
        user.profession = profession
        user.email = email
        user.token = make_token()
        user.save()
        red = redirect(reverse('app:index'))
        red.set_cookie('token',user.token)

        return red

    # 从session中取出yzm
    # yzm = request.session.get('yzm')
    # yzm = str(yzm)
    # code = request.GET.get('sms')
    # print(yzm,code)
    # if yzm == code:
    #     return render(request,'index.html')
    # return redirect(reverse("app:index"))


def adminindex(request):
    if request.method == 'GET':
        return render(request,'admin/index.html')
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
    return render(request,'admin/add-article.html')


def add_category(request):
    return render(request, 'admin/add-category.html')


def add_flink(request):
    return render(request,'admin/add-flink.html')


def add_notice(request):
    return render(request,'admin/add-notice.html')


def article(request):
    return render(request,'admin/article.html')


def category(request):
    return render(request,'admin/category.html')


def comment(request):
    return render(request,'admin/comment.html')


def flink(request):
    return render(request,'admin/flink.html')


def loginlog(request):
    return render(request,'admin/loginlog.html')


def manage_user(request):
    return render(request,'admin/manage-user.html')


def notice(request):
    return render(request,'admin/notice.html')


def readset(request):
    return render(request,'admin/readset.html')


def setting(request):
    return render(request,'admin/setting.html')


def update_flink(request):
    return render(request,'admin/update-flink.html')


def update_category(request):
    return render(request,'admin/update-category.html')


def update_article(request):
    return render(request,'admin/update-article.html')


def index(request):
    blogs = Blog.objects.all()
    context = {"blogs":blogs}
    return render(request,'app/index.html',context=context)
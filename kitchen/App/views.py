import hashlib

from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse

from App.models import User, Type, Good


def index(request):
    # def index(request):
    #     type = Type.objects.all()
    #     Sp = Good.objects.all()
    #     return render(request, 'index.html', context={
    #         'type': type,
    #         'sp': Sp,
    #     })
    # type = Type.objects.all()
    # sp = Good.objects.all()
    if request.method == 'GET':
        return render(request,'login.html')

    if 'uid' in request.session:

        username = request.session.get('username')

        return render(request, "index.html")

    # return render(request, "login.html")
    # def index1(request):
    #     type = Type.objects.all()
    #     Sp = Good.objects.all()
    #     username = request.session['username']
    #     return render(request, 'index.html', context={
    #         'type': type,
    #         'sp': Sp,
    #         'username': username})




def login(request):
    type = Type.objects.all()
    Sp = Good.objects.all()
    if request.method == 'GET':
        return render(request, 'login.html')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 对密码进行sha1签名
        password = hashlib.sha1(password.encode('utf8')).hexdigest()
        #查询数据库
        res = User.objects.filter(username=username,password=password).values('username','id')
        if len(res) > 0:
            request.session['uid'] = res[0]['id']
            request.session.set_expiry(0)
            request.session['username'] = username
            return render(request,'index.html',context={
                'username': username,
                'type': type,
                'sp': Sp,})
        else:
            return render(request, 'login.html')






def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('cpwd')
        email = request.POST.get('email')
        res = User.objects.filter(username=username)
        if len(res)>0:
            return HttpResponse("用户已经存在")
        elif password !=password2:
            return HttpResponse("两次密码输入不正确")
        else:
            password = hashlib.sha1(password.encode('utf8')).hexdigest()
            request.session['username'] = username
            request.session.set_expiry(0)
            # User.objects.create(username=username,password=password,email=email)
            set = User()
            set.username = username
            set.password = password
            set.email = email
            set.save()
            return render(request,'login.html')


def logout(request):
        request.session.flush()
        return render(request,'login.html')







#支付订单
#购物车结算--->提交订单
def placeorder(request):
    return render(request,'place_order.html')


#全部订单
#我的订单-->全部订单   #点击我的订单默认跳转到全部订单
def order(request):
    return render(request,'user_center_order.html')

#用户中心
#大标题用户中心
#标题我的订单-->个人信息
def info(request):
    username = request.session.get('username')
    print(username)
    set = User.objects.filter(username=username)
    print(set)
    city = set[0].city
    email = set[0].email
    phone = set[0].phone
    sex = set[0].sex
    age = set[0].age
    birthday = set[0].birthday
    # phone = set[0].phone
    return render(request,'user_center_info.html',context={
        'city':city,
        'email':email,
        'phone':phone,
        'sex':sex,
        'age':age,
        'birthday':birthday,
    })

#收货地址
#我的订单---->收货地址
def site(request):
    return render(request,'user_center_site.html')


#商品信息
#首页点击商品跳转商品首页
def detail(request,goodid):
    # username = request.POST.get('username')
    good = Good.objects.get(id=goodid)

    return render(request,'detail.html',context={
        'good':good,
    })


#我的购物车
def cart(request,goodsid):

    good = Good.objects.get(id=goodsid)

    return render(request,'cart.html',context={
        'good':good,
    })


# 查询
def check(request):
    if request.method == 'POST':
        ret = request.POST.get('check')
        print(ret)
        good = Good.objects.filter(name__contains=ret)
        # books = Book.objects.filter(Q(ISBN__icontains=q)| Q(bookname__icontains=q)).order_by('-year')
        # pic = good[0].pic
        # name = good[0].name
        # price = good[0].price
        let = good.exists()
        if let:
            return render(request, 'check.html', context={
                'good':good
                # 'name': name,
                # 'price':price,
                # 'pic':pic
            })
    return HttpResponse("请输入正确的商品")

    #     print(good)
    #     if len(good):
    #         return render(request, 'detail.html', context={
    #             'good': good,
    #         })
    # return render(request,'login.html')

#修改
def change(request):
    # if request.method == 'POST':
    #     username = request.session.get('username')
    #     password = request.POST.get('password')
    #     city = request.POST.get('city')
    #     password = request.POST.get('password')
    #     email = request.POST.get('email')
    #     phone = request.POST.get('phone')
    #     set = User.objects.filter(username=username)
    #     set.update(password=password,city=city,email=email,phone=phone,)
    #     print(set)
    #     return render(request,'xiugai.html')
    # return render(request,'user_center_info.html')
    return render(request,'change.html')


def xiugai(request):
    return render(request,'xiugai.html')
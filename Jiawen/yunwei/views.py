from django.shortcuts import render

# Create your views here.

from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect

#
# def home(request):
#     return HttpResponse('<h1>如果邪恶是华丽残酷的乐章</h1>')

def login(request):

    error_msg = ""
    if request.method == 'POST':
        user = request.POST.get('user',None)
        pwd = request.POST.get('pwd',None)
        print(user,pwd)
        if user == 'lishang' and pwd == '12345':
            return redirect('/home')
        else:
            error_msg = "用户名或密码错误"

    return render(request,'login.html',{'error_msg':error_msg})

USER_LIST = [
    {'username':'lishang','tel':'17853491576@163.com','gender':'男'},
    {'username':'xiangmei','tel':'17853491576@163.com','gender':'女'},
    {'username':'xiaomeng','tel':'17853491576@163.com','gender':'女'},
]

# for index in range(19):
#     temp = {'username':'lishang'+str(index),'tel':'17853491576@163.com','gender':'男'}
#     USER_LIST.append(temp)

def home(request):
    if request.method == "POST":
        user = request.POST.get('username')
        tel = request.POST.get('tel')
        gender = request.POST.get('gender')
        temp =     {'username':user,'tel':tel,'gender':gender}
        USER_LIST.append(temp)
    return render(request,'home.html',{'user_list':USER_LIST})
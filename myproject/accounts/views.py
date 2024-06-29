from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import SignUpForm
from .models import FishNumber
from .models import FishData
from .models import Information
from django.db.models import Count
import json

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('system')  # 管理员登录后跳转到系统界面
            else:
                return redirect('usersystem')  # 普通用户登录后跳转到用户系统界面
        else:
            messages.error(request, '用户名或密码错误！')
    return render(request, 'login.html')


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')  # 注册成功后重定向到登录页面
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # 处理注册成功后的逻辑
    else:
        form = SignUpForm()
    return render(request, 'registration/register.html', {'form': form})

def system_view(request):
    return render(request, 'system.html')

def usersystem_view(request):
    return render(request, 'usersystem.html')

def main_info_view(request):
    # 获取最新的一条 Information 数据记录
    latest_info = Information.objects.latest('id')
    # 将数据传递给模板
    return render(request, 'main_info.html', {'latest_info': latest_info})

#def underwater_system_view(request):
#    return render(request, 'underwater_system.html')

def data_center_view(request):
    return render(request, 'data_center.html')

def smart_center_view(request):
    return render(request, 'smart_center.html')

def admin_management_view(request):
    users = User.objects.all()  # 获取所有用户信息
    return render(request, 'admin_management.html', {'users': users})

'''
def underwater_system_view(request):
    # 获取最新的一条数据
    fishnumber = FishNumber.objects.latest('id')
    context = {
        'total': fishnumber.total if fishnumber else 0,
        'add': fishnumber.add if fishnumber else 0,
        'minus': fishnumber.minus if fishnumber else 0,
        'score': fishnumber.score if fishnumber else 0
    }
    return render(request, 'underwater_system.html', context)

def fish_data_view(request):
    # 获取所有的 FishData 数据
    fish_data = FishData.objects.all()

    # 统计每种鱼类的数量
    fish_counts = fish_data.values('kind').annotate(count=Count('kind'))

    # 将数据组织成前端需要的格式
    data = {
        'kinds': [fish['kind'] for fish in fish_counts],  # 获取所有不同的鱼类种类
        'attributes': ['weight', 'length', 'height', 'width'],  # 属性列表
        'fish_data': {fish['kind']: {'weight': [], 'length': [], 'height': [], 'width': []} for fish in fish_counts}
    }

    for fish in fish_data:
        data['fish_data'][fish.kind]['weight'].append(fish.weight)
        data['fish_data'][fish.kind]['length'].append(fish.length)
        data['fish_data'][fish.kind]['height'].append(fish.height)
        data['fish_data'][fish.kind]['width'].append(fish.width)

    return render(request, 'underwater_system.html', {'data': data})
'''

def underwater_system_view(request):
    fishnumber = FishNumber.objects.latest('id')
    fish_data = FishData.objects.all()
    fish_counts = fish_data.values('kind').annotate(count=Count('kind'))

    data = {
        'total': fishnumber.total if fishnumber else 0,
        'add': fishnumber.add if fishnumber else 0,
        'minus': fishnumber.minus if fishnumber else 0,
        'score': fishnumber.score if fishnumber else 0,
        'kinds': [fish['kind'] for fish in fish_counts],
        'attributes': ['weight', 'length', 'height', 'width'],
        'fish_data': {fish['kind']: {'weight': [], 'length': [], 'height': [], 'width': []} for fish in fish_counts}
    }

    for fish in fish_data:
        data['fish_data'][fish.kind]['weight'].append(fish.weight)
        data['fish_data'][fish.kind]['length'].append(fish.length)
        data['fish_data'][fish.kind]['height'].append(fish.height)
        data['fish_data'][fish.kind]['width'].append(fish.width)

    json_data = json.dumps(data)  # 将数据转换为 JSON 字符串

    return render(request, 'underwater_system.html', {'json_data': json_data})

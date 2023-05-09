from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.
def index(request):
    print("Hello django")
    # return HttpResponse('<h1>Hello django!</h1>')
    return render(request, "./index.html")


def gen_password(request):
    length = eval(request.GET.get("length"))
    input_length = request.GET.get("input-length")
    # 起始密碼
    password_char = "abcdefghijklmnopqrstuvwsyz"
    # 加上大寫字母
    if request.GET.get("uppercase") == "on":
        password_char += password_char.upper()
    # 加上數字'0'~'9'
    if request.GET.get("number") is not None:
        password_char += "0123456789"
    # 加上特殊符號
    if request.GET.get("special"):
        password_char += "@#$%^&*?"
    # 判斷長度
    if input_length != "":
        length = eval(input_length)
    # 產生密碼
    password = "".join([random.choice(password_char) for i in range(length)])

    # print(request.GET.get("uppercase"))
    print(length, password, password_char)
    return render(request, "./password.html", {"password": password})

# coding: utf-8


from django.http import HttpResponse


def index(request):
    return HttpResponse("<div style='margin-top:200px;text-align:center'><h1>Hello World</h1></div>")

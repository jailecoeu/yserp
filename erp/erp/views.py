#coding:utf-8
from django.template.response import TemplateResponse
from account.decorators import login_required

@login_required
def home(request):
    return TemplateResponse(request,'index.html')

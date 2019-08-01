from django.shortcuts import render
from django.http import HttpResponse
from jp001.models import indiaJob,indiaJob1,indiaJob2,indiaJob3

# Create your views here.

def wish(request):
    s='<h1>Hi this is test<h1>'
    return HttpResponse(s)



def job1(request):
    return render(request,'jp001/index.html')

def job2(request):
    emp_list=indiaJob.objects.order_by('empname')
    my_dict={'emp_list':emp_list}
    return render(request,'jp001/delhijobs.html',context=my_dict)

def job3(request):
    emp_list=indiaJob1.objects.order_by('empname')
    my_dict={'emp_list':emp_list}
    return render(request,'jp001/ggnjobs.html',context=my_dict)

def job4(request):
    emp_list=indiaJob2.objects.order_by('empname')
    my_dict={'emp_list':emp_list}
    return render(request,'jp001/gazjobs.html',context=my_dict)

def job5(request):
    emp_list=indiaJob3.objects.order_by('empname')
    my_dict={'emp_list':emp_list}
    return render(request,'jp001/noidajobs.html',context=my_dict)

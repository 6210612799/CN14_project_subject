from django.urls import reverse
from audioop import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from rest_framework import status
from database.models import Person, Subject , Student ,Skill
import requests
HOST = "https://restapi.engr.tu.ac.th"

def homepage(request):
    return render(request,"subjectenroller/homepage.html")

def login_view(request):
    try:
        if request.session['user_id']:
            return HttpResponseRedirect(reverse("subjectenroller:login"))
    except:
        if request.method == "POST":
            username = request.POST["username"]
            password = request.POST["password"]
            data = {
                'username': username,
                'password': password
            }
            response = requests.post(
                HOST+'/api/v1/authentication/', data=data)
            if response.status_code == status.HTTP_200_OK:
                request.session['user_id'] = username
                request.session['name'] = response.json()['name']
                # print(request.session['user_id'])
                # print("render policy page")
                request.session['login_status'] = username
                request.session.modified = True
                # return render(request, "web/policy.html")
                return render(request,"subjectenroller/homepage.html")
            else:
                return render(request, "subjectenroller/login.html")
        return render(request, "subjectenroller/login.html")
    
def logout_view(request):
    del request.session['user_id']
    del request.session['name']
    return HttpResponseRedirect(reverse("login_view"))


def enroll(request):
    data = Subject.objects.all()
    # print(request.session['user_id'])
    # subject = Subject.objects.get(courses_id=S_id)
    # student = Student.objects.get(student_user=request.user)
    # student.student_temp.add(subject)
    # student.save()
    # subject.save()
    return render(request,"subjectenroller/test_enroll.html", {'data': data})


def detail(request):
    data = Subject.objects.all()
    return render(request,"subjectenroller/subject_detail.html", {'data': data})

def login(request):
    data = Subject.objects.all()
    return render(request,"subjectenroller/login.html", {'data': data})

def skill_tree(request):
    skills = Skill.objects.all()
    context = {'skills': skills}
    return render(request, 'subjectenroller/skill_tree.html', context)
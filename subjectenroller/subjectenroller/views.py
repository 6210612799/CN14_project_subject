from audioop import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from rest_framework import status
import requests
HOST = "https://restapi.engr.tu.ac.th"

def index(request):
    return render(request,"index.html")

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
                # print(request.session['user_id'])
                # print("render policy page")
                request.session['login_status'] = username
                request.session.modified = True
                # return render(request, "web/policy.html")
                return render(request,"subjectenroller/test_login.html")
            else:
                return render(request, "subjectenroller/login.html")
        return render(request, "subjectenroller/login.html")
    
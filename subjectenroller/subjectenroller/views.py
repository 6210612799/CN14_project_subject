from django.urls import reverse
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from audioop import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from rest_framework import status
from database.models import Person, Subject , Student ,Skill
from django.contrib import messages
import requests
HOST = "https://restapi.engr.tu.ac.th"

def homepage(request):
    return render(request,"subjectenroller/homepage.html")

def test(request):
    user_id = request.session.get('user_id')
    subject = Subject.objects.all()
    student = Student.objects.get(user_id=user_id)
    skills = Skill.objects.all()
    context = {
        'subject': subject,
        'student': student,
        'skills': skills,
    }
    return render(request,"subjectenroller/test_login.html",context)

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
                # Check if a Student object with the user_id already exists
                try:
                    student = Student.objects.get(user_id=username)
                except Student.DoesNotExist:
                    # Create a new Student object with student_id
                    student_id = str(username)  # Generating a student_id using username
                    student = Student(user_id=student_id)
                    student.save()
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


def enroll_page(request):
    subject = Subject.objects.all()
    print(request.session['user_id'])
    # print(request.session['user_id'])
    # subject = Subject.objects.get(courses_id=S_id)
    # student = Student.objects.get(student_user=request.user)
    # student.student_temp.add(subject)
    # student.save()
    # subject.save()
    subject = Subject.objects.all()
    skills = Skill.objects.all()
    context = {'skills': skills , 'subject': subject,}
    return render(request,"subjectenroller/test_enroll.html", context)


def detail(request):
    data = Subject.objects.all()
    return render(request,"subjectenroller/subject_detail.html", {'data': data})

def login(request):
    data = Subject.objects.all()
    return render(request,"subjectenroller/login.html", {'data': data})

def skill_tree(request):
    subject = Subject.objects.all()
    skills = Skill.objects.all()
    context = {'skills': skills , 'subject': subject}
    return render(request,"subjectenroller/test_enroll.html", context)


def enroll(request, S_id):
    if request.method == 'GET':
        user_id = request.session.get('user_id')
        if user_id:
            student = get_object_or_404(Student, user_id=user_id)
            subject = get_object_or_404(Subject, S_id=S_id)
            student.enrolled_subjects.add(subject)
            student.save()
            messages.success(request, 'Subject enrolled successfully!')
        else:
            messages.error(request, 'Please log in to enroll in a subject.')
    return redirect("subjectenroller/test_enroll.html", subject_id=S_id)

def un_enroll(request, S_id):
    if request.method == 'GET':
        user_id = request.session.get('user_id')
        if user_id:
            student = get_object_or_404(Student, user_id=user_id)
            subject = get_object_or_404(Subject, S_id=S_id)
            if subject in student.enrolled_subjects.all():
                student.enrolled_subjects.remove(subject)
                student.save()
                messages.success(request, 'Subject un-enrolled successfully!')
            else:
                messages.error(request, 'You have not enrolled in this subject.')
        else:
            messages.error(request, 'Please log in to un-enroll from a subject.')
    return redirect("test_enroll", S_id=S_id)


def test_enroll(request, S_id):
    user_id = request.session.get('user_id')
    subject = get_object_or_404(Subject, S_id=S_id)
    student = Student.objects.get(user_id=user_id)
    skills = Skill.objects.all()
    context = {
        'subject': subject,
        'student': student,
        'skills': skills,
    }
    return render(request, 'subjectenroller/test_enroll.html', context)
 

# def enroll_page(request):
#     user_id = request.session.get('user_id')
#     if user_id:
#         data = Subject.objects.all()
#         student = get_object_or_404(Student, user_id=user_id)
#         subjects = student.enrolled_subjects.all()
#         return render(request, "subjectenroller/test_enroll.html", {'data': data})
#     else:
#         messages.error(request, 'Please log in to view your enrolled subjects.')
#         return redirect("subjectenroller/login.html")



# def enroll(request, S_id):
#     user_id = request.session.get('user_id')
#     if user_id:
#         student = get_object_or_404(Student, user_id=user_id)
#         subject = get_object_or_404(Subject, id=S_id)
#         student.enrolled_subjects.add(subject)
#         messages.success(request, 'Subject enrolled successfully!')
#     else:
#         messages.error(request, 'Please log in to enroll in a subject.')
#     return redirect("subjectenroller/test_enroll.html")

# def test_enroll(request, S_id):
#     # Get the user_id from the session
#     user_id = request.session.get('user_id')
#     skills = Skill.objects.all()
#     context = {
#          'subject': subject,
#          'student': student,
#          'skills': skills,
#     }
#     # Get the Subject object from the database
#     subject = Subject.objects.get(S_id=S_id)

#     # Check if the user has already enrolled in the subject
#     try:
#         student = Student.objects.get(student_id=user_id, student_subject=subject)
#         messages.warning(request, f"You've already enrolled in {subject.S_name}.")
#         return redirect('subject_list')
#     except Student.DoesNotExist:
#         pass

#     # Create a new Student object and save it to the database
#     student = Student(student_id=user_id, student_subject=subject)
#     student.save()

#     # Get all the subjects that the user has enrolled in
#     enrolled_subjects = Student.objects.filter(student_id=user_id)

#     # Render the enrollment success message and the list of enrolled subjects
#     messages.success(request, f"You've successfully enrolled in {subject.S_name}.")
#     return render(request, 'enrolled_subjects.html', {'context': context})
    context = {'skills': skills}
    return render(request, 'subjectenroller/skill_tree.html', context)

def one_termone(request):
    skills = Skill.objects.all()
    context = {'skills': skills}
    return render(request, 'subjectenroller/one_termone.html', context)

def one_termtwo(request):
    skills = Skill.objects.all()
    context = {'skills': skills}
    return render(request, 'subjectenroller/one_termtwo.html', context)

def two_termone(request):
    skills = Skill.objects.all()
    context = {'skills': skills}
    return render(request, 'subjectenroller/two_termone.html', context)

def two_termtwo(request):
    skills = Skill.objects.all()
    context = {'skills': skills}
    return render(request, 'subjectenroller/two_termtwo.html', context)

def three_termone(request):
    skills = Skill.objects.all()
    context = {'skills': skills}
    return render(request, 'subjectenroller/three_termone.html', context)

def three_termtwo(request):
    skills = Skill.objects.all()
    context = {'skills': skills}
    return render(request, 'subjectenroller/three_termtwo.html', context)

def four_termone(request):
    skills = Skill.objects.all()
    context = {'skills': skills}
    return render(request, 'subjectenroller/four_termone.html', context)

def four_termtwo(request):
    skills = Skill.objects.all()
    context = {'skills': skills}
    return render(request, 'subjectenroller/four_termtwo.html', context)

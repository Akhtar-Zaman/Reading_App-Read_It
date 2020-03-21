from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .forms import StudentRegistrationForm,Teachers_Signing_Form
from django.core.files.storage import FileSystemStorage

from .models import pdf_file
from .forms import uploadpdf  

import cv2, time

# This Function works for saving the student information into database

def studentform(request):
     if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()           
            return redirect('homepage')
     else:
        form = StudentRegistrationForm()
        return render(request, 'studentform.html', {'form':form})

# This Function works for saving the Teacher information into database
def teacher_form(request):
     if request.method == 'POST':
        form = Teachers_Signing_Form(request.POST)
        if form.is_valid():
            form.save()           
            return redirect('homepage')
     else:
        form = Teachers_Signing_Form()
        return render(request, 'teacher_signing_form.html', {'form':form})


# This function works for student Login
def student_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)        
        if user:
             login(request, user)
          #    print('akhtar')
             return redirect("mainpage")
          
        else:
          #    print('zaman')
             return render(request, "home.html")
            
    else:   
         return render(request, "login.html")

# This function works for Teachers Login
def teacher_login_form(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)        
        if user:
             login(request, user)
             print('akhtar')
             return redirect("pdf_upload_page")
          
        else:
             print('zaman')
             return render(request, "home.html")
            
    else:   
         return render(request, "login.html")

# when teacher loged in then he will upload pdf file using this method
def pdf_up(request):
    if request.method == 'POST':
        form = uploadpdf(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("pdf_upload_page")
    else:
        form = uploadpdf()
    return render(request, 'fileupload.html', {'forms':form})

# when student logged in then he see their reading matarials
def pdf_view(request):
    pdf = pdf_file.objects.all()
    return render(request, 'mainpage.html', {'pdf':pdf } )


# When student readin their documen then after 5 second this function capture an image
def image_capture(request):   
     
    video = cv2.VideoCapture(0)
    framerate = video.get(5)
    a = 0
    while True:
        a = a+1
        check, frame = video.read()
    

        print(check)
        print(frame)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imwrite('pic{:>05}.jpg'.format(a), gray)
        time.sleep(5)
        key = cv2.waitKey(1)
     
        if key == ord('q'):
            break

    video.release()



def success(request):
   return render(request,'home.html')

class test(TemplateView):
    template_name= "mainpage.html"

class fileupload(TemplateView):
    template_name= "fileupload.html"
  


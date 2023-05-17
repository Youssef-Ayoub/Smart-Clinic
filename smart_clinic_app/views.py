import matplotlib.pyplot as plt
import keras.utils as image
from keras.models import load_model
import numpy as np
from django.shortcuts import render, redirect
from django.conf import settings
import base64
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.shortcuts import render
from PIL import Image
from django.http import HttpResponse
from django.http import request
from django.http.request import validate_host
from django.shortcuts import redirect, render
from . import forms, models
from django.urls import reverse_lazy
from .forms import Userform, Userforma
from django.contrib import messages
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.models import auth, User, Group
from django.contrib.auth.decorators import login_required, user_passes_test
from datetime import datetime, timedelta, date

from django.http import HttpResponseRedirect

from django.shortcuts import render
from PIL import Image

import tensorflow as tf
from django.shortcuts import render
from django.http import JsonResponse


# returns a compiled model
# identical to the previous one
model = load_model(
    'E:\paid project\smart_clinic\project\Last_project_my_model.h5')

# Create your views here.


def is_Patient(user):
    return user.groups.filter(name='PATIENT').exists()


def Resigter_Patient(request):
    if request.method == 'POST':
        fn = request.POST['First name']
        ln = request.POST['Last name']
        username = request.POST['Username']
        email = request.POST['Email']
        password = request.POST['Password']
        confirmpassword = request.POST['Confirm Password']
        if password == confirmpassword:
            if User.objects.filter(username=username).exists():
                messages.success(request, "username is Already Exist")
                return render(request, 'FrontEndPages/SignUpAsDoctor.html')
            elif User.objects.filter(email=email).exists():
                messages.success(request, "Email is Already used")
                return render(request, 'FrontEndPages/SignUpAsDoctor.html')
            else:
                user = User.objects.create_user(
                    first_name=fn, last_name=ln, username=username, email=email, password=password)
                user.save()
                PATIENT_group = Group.objects.get_or_create(name='PATIENT')
                PATIENT_group[0].user_set.add(user)
                messages.success(request, "Register Successfully")
                return render(request, 'FrontEndPages/loginasdoctor.html')
        else:
            messages.success(request, "password not matching..")
            return render(request, 'FrontEndPages/SignUpAsDoctor.html')
    else:
        return render(request, 'FrontEndPages/SignUpAsDoctor.html')


def login_Patient(request):
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            if is_Patient(user):
                auth.login(request, user)
                return messages.success(request, "Successfull Login")
            else:
                messages.success(
                    request, "You are a Doctor You can't login with this page ")

        else:
            messages.success(request, "Invalid User")
            return render(request, 'FrontEndPages/')
    else:
        return render(request, 'FrontEndPages/')

# ----------------------------------------------------------------------------------------------------------------------------


def is_Doctor(user):
    return user.groups.filter(name='DOCTOR').exists()


def Resigter_Doctor(request):
    if request.method == 'POST':
        username = password = email = ''
        username = request.POST.get('Username')
        password = request.POST.get('Password')
        email = request.POST.get('Email')

        if User.objects.filter(username=username).exists():
            messages.success(request, "Username is already Taken")
            return render(request, 'Register2.html')
        else:
            user = User.objects.create_user(
                username=username, password=password, email=email)
            user.save()
            DOCTOR_group = Group.objects.get_or_create(name='DOCTOR')
            DOCTOR_group[0].user_set.add(user)
            messages.success(request, "Register Successfully")
            return render(request, 'register.html')
    else:
        return render(request, 'register2.html')


def login_Doctor(request):
    if request.method == 'POST':

        username = password = ''
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            if is_Doctor(user):
                auth.login(request, user)
                messages.success(request, "succeesfully logged in")
                return render(request, 'about.html')
            else:
                messages.success(
                    request, "You are a Patient You can't login with this page ")
                return render(request, 'register.html')
        else:
            messages.success(request, "Invalid User")
            return render(request, 'register.html')
    else:
        messages.success(request, "you have logined in successfully")
        return render(request, 'register.html')


def about(request):
    return render(request, 'about.html')


def appointment(request):
    return render(request, 'appointment.html')


def blog(request):
    return render(request, 'blog.html')


def contact(request):
    return render(request, 'contact.html')


def detail(request):
    return render(request, 'detail.html')


def index(request):
    return render(request, 'index.html')


def service(request):
    return render(request, 'service.html')


def testimonial(request):
    return render(request, 'testimonial.html')


def treatment(request):
    return render(request, 'treatment.html')


def whatare(request):
    return render(request, 'what are.html')


def whatis(request):
    return render(request, 'what is.html')


#############################################


def camera_view(request):
    return render(request, 'camera.html')


def save_picture(request):
    picture_data = request.POST.get('picture_data')
    picture_data = picture_data.replace("data:image/png;base64,", "")
    picture_data = base64.b64decode(picture_data)

    with open(settings.MEDIA_ROOT + 'picture.png', 'wb') as f:
        f.write(picture_data)

    img1 = image.load_img("E:\paid project\smart_clinic\project\picture.png",
                          target_size=(150, 150), color_mode="grayscale")

    x = image.img_to_array(img1)
    x = np.expand_dims(x, axis=0)
    value = model.predict(x)

    value_dict = value.flatten()

    dic = {
        'value': int(value_dict[0])
    }

    return render(request, "camera.html", dic)

###################################################

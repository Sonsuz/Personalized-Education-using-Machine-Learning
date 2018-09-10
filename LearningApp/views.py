from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_object_or_404, redirect
from .forms import (
    EditProfileForm, UserForm, UserProfileForm,
)
from .models import (
    UserProfile, Course, Discussion
)
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from datetime import datetime

# Edit Profile -----
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.urls import reverse


def index(request):

    if not request.user.is_authenticated:
        return render(request, 'login.html')
    else:
        return render(request, 'index.html')

def v_courses(request):
    courses = Course.objects.all()
    context = {
        'courses': courses,
    }
    return render(request, 'course/courses.html', context)

def course_detail(request, course_id):
    coursed = Course.objects.get(pk = course_id)
    context = {
        'coursed': coursed,
    }
    return render(request, 'course/course_detail.html', context)

def v_discussion(request):
    discs = Discussion.objects.all()
    context = {
        'discs': discs,
    }
    return render(request, 'discussion/discussions.html', context)

def discussion_detail(request, discussion_id):
    disc = Discussion.objects.get(pk = discussion_id)
    context = {
        'disc': disc,
    }
    return render(request, 'discussion/discussion_detail.html', context)


def register(request):
    form = UserForm(request.POST or None)
    form2 = UserProfileForm(request.POST or None, request.FILES or None)

    if form.is_valid() and form2.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        userprofile = form2.save(commit=False)
        userprofile.user = form.save(commit=False)

        userprofile.save()
        user = authenticate(username=username, password=password)

    context = {
        "form": form,
        "form2": form2
    }
    return render(request, 'register.html', context)

def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return redirect('/LearningApp')


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/LearningApp/')
            else:
                return render(request, 'login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'login.html', {'error_message': 'Invalid login'})
    return render(request, 'login.html')

def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'profile/profile.html', args)

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect(reverse('LearningApp:view_profile'))
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'profile/edit_profile.html', args)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/LearningApp/edit')
        else:
            return redirect('/LearningApp/change-password')

    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'profile/change_password.html', args)

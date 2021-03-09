from django.shortcuts import render
from basic_app.forms import UserForm,UserProfileInfoForm

#LOGIN
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,'basic_app/index.html')

@login_required
def special(request):
    return HttpResponse ("you are logged in ,nice!")

@login_required    
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):

    registered = False

    if request.method == "POST":
        User_Form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if User_Form.is_valid() and profile_form.is_valid():
            
            user = User_Form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            registered = True
        
        else:
            print(User_Form.errors,profile_form.errors)
    else:
        User_Form = UserForm()
        profile_form = UserProfileInfoForm()

    return render (request,'basic_app/registration.html',
                           { 'User_Form': User_Form,
                             'profile_form':profile_form,
                              'registered':registered})




def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))


            else:
                return HttpResponse("ACCOUNT NOT FOUND")
        else:
            print("someone tried to login and failed")
            print("username:{} and password{}".format(username,password))
            return HttpResponse("invalid login details")
    else:
        return render(request,'basic_app/login.html',{})
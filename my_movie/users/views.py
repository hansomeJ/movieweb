from django.shortcuts import render,redirect,reverse


from django.contrib.auth import authenticate,login as mylogin,logout as mylogout

from django.http import HttpResponse


from .forms import UserLoginForm,SignUpForm



# Create your views here.

def login(request):
    if request.method == 'POST':
        next = request.POST.get('next','/')
        form = UserLoginForm(request=request,data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                mylogin(request,user)
                # return redirect(next)
                print(next)
                return HttpResponse('登陆成功！')
        else:
            print(form.errors)
            return render(request, 'registration/login.html', {'form': form})
    else:
        next = request.GET.get('next','/')
        form = UserLoginForm()
    return render(request,'registration/login.html',{'form':form,'next':next})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        # print(form.errors,'+++++++++++')
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            print(username)
            raw_password1=form.cleaned_data.get('password1')
            user = authenticate(username=username,password=raw_password1)
            return redirect(reverse('users:login'))
        else:
            print(form.errors)
    else:
        form = SignUpForm()
        # print(form)
    return render(request,'registration/signup.html',{'form':form})



def logout(request):
    pass

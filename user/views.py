from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import RegestrationForm, LoginForm, EditForm
# from .models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_GET
class UserRegestration(View):
    def setup(self, request, *args, **kwargs):
        super().setup(request,*args, **kwargs)

        request.title = "Ro'yxatdan o'tish"
    def get(self, request):
        form = RegestrationForm()

        return render(request, "user/regestration.html", {
            "form":form
        })
    def post(self, request):

        form = RegestrationForm(data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()
            messages.success(request, "Siz muvofaqiyatli ro'yxardan o'tdingiz.")
            return redirect('main:index')

            # data = form.cleaned_data
            # print(data)
            # del data['confirm']
            # user = User(**data)
            # user.set_password(data['password'])
            # user.save()

        return render(request, 'user/regestration.html',{
            "form":form,
        })


def user_login(request):
    request.title = "Tizimga kirish"
    form = LoginForm()
    if request.POST:
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data["username"], password=form.cleaned_data["password"])

            if user is not None:
                login(request, user)
                user_name = str(user.username).capitalize()
                messages.success(request, "Xush kelibsiz!! {}".format(user_name))
                return redirect("main:index")

            form.add_error("password", "Username va/yoki parolda xatolik!")

    return render(request, "user/login.html", {
        "form": form,
    })

@login_required
def user_logout(request):
    logout(request)
    return redirect("main:index")

@require_GET
@login_required
def user_info(request):
    request.title = "Foydalanuvchi malumotlari"
    return render(request, "user/edit.html", {
        "form": EditForm(instance=request.user)
    })

@require_POST
@login_required
def user_info_post(request):
    form = EditForm(data=request.POST, instance=request.user)
    if form.is_valid():
        form.save()
        messages.success(request, "Malumotlaringiz muvofaqiyatli saqlandi!")
        return redirect("user:info")

    return render(request, "user/edit.html", {
        "form": form
    })
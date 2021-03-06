from django.shortcuts import render, redirect
from django.views import View
from users.models import User


class LoginView(View):
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        try:
            user = User.objects.get(username=username)
            if password == user.password:
                print("password is correct")
            else:
                print("password if not correct")
            print("user is", user)
            request.session['loggedin'] = True
            return render(request, "index.html", context={"loggedin": True})
        except:
            print("user do not exit")
            return redirect("/")


class Logout(View):
    def get(self, request):
        request.session["loggedin"] = False
        return render(request, "index.html", context={"loggedin": False})

    def post(self, request):
        pass

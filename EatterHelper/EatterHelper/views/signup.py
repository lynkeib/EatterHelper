from django.shortcuts import render, redirect
from django.views import View
from users.models import User


class Signup(View):
    def get(self, request):
        return render(request, "register.html")

    def post(self, request):
        user = User()
        user.username = request.POST.get("username")
        user.password = request.POST.get("password")
        user.save()
        return redirect("/")

from django.shortcuts import render, redirect
from django.views import View


class Signup(View):
    def get(self, request):
        return render(request, "register.html")

    def post(self):
        pass
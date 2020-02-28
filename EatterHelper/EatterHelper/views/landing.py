from django.shortcuts import render, redirect
from django.views import View


class LandingView(View):
    def get(self, request):
        request.session["landing"] = True
        print('request from landing', request.session.keys())
        return render(request, "Landing.html")

    def post(self):
        pass

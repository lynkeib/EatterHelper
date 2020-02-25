from django.shortcuts import render, redirect
from django.views import View


class LandingView(View):
    def get(self, request):
        return render(request, "Landing.html")

    def post(self):
        pass

from django.shortcuts import render

def home(request):
    context={}
    return render(request, "hello/home.html/stress_input.html/results.html/about_us.html/history.html/profile.html",context)

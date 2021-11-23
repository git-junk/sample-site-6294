from django.shortcuts import render

def index(request):
  return render(request, "sample_site_app/index.html")

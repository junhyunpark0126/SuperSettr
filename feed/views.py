from django.shortcuts import render
from .models import Post

def home(request):
    context = {
        "posts": Post.objects.all()  #posts in string "" is what is accessible by templates (ex. home.html)
    }
    return render(request, "feed/home.html", context)

def about(request):
    return render(request, "feed/about.html", {"title": "About"}) #not making context variable here since we can just directly pass in our arguements
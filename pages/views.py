from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "pages/search.html")


def loved(request):
    return render(request, 'pages/loved.html')


def bookmarks(request):
    return render(request, 'pages/bookmarks.html')
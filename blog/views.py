from django.shortcuts import render

# Create your views here.
# This is a change I made on GitHub

def post_list(request):
    return render(request, 'blog/post_list.html', {})

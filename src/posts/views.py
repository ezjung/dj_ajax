from django.shortcuts import render
from .models import Post

# Create your views here.

def post_list_and_create(request):
    qs = Post.objects.all()
    context = {
        'qs': qs
    }
    return render(request, 'posts/main.html', context)

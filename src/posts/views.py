from django.shortcuts import render
from .models import Post
from django.http import JsonResponse

# Create your views here.

def post_list_and_create(request):
    qs = Post.objects.all()
    context = {
        'qs': qs
    }
    return render(request, 'posts/main.html', context)


def hello_view(request):
    return JsonResponse({'text': 'hello World'})
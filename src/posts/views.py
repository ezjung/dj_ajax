from django.shortcuts import render
from .models import Post
from django.http import JsonResponse
# from django.core import serializers

# Create your views here.

def post_list_and_create(request):
    qs = Post.objects.all()
    context = {
        'qs': qs
    }
    return render(request, 'posts/main.html', context)

def load_post_data_view(request):
    qs = Post.objects.all()
    # querySet needs to be translated to json format
    # data = serializers.serialize('json', qs)
    data = []
    for obj in qs:
        item = {
            'id': obj.id,
            'title': obj.title,
            'body': obj.body,
            'author': obj.author.user.username,
        }
        data.append(item)

    context = {'data': data}
    return JsonResponse(context)


def hello_view(request):
    return JsonResponse({'text': 'hello fucking World'})
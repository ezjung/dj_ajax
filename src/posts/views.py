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

def load_post_data_view(request, num_posts):
    # num_posts = kwargs.get('num_posts')
    visible = 3
    upper = num_posts
    lower = upper - visible
    size = Post.objects.all().count()

    qs = Post.objects.all()
    # querySet needs to be translated to json format
    # data = serializers.serialize('json', qs)
    data = []
    for obj in qs:
        item = {
            'id': obj.id,
            'title': obj.title,
            'body': obj.body,
            'liked': True if request.user in obj.liked.all() else False,
            'count': obj.like_count,
            'author': obj.author.user.username,
        }
        data.append(item)

    context = {
        'data': data[lower:upper],
        'size': size,
        }
    return JsonResponse(context)

def like_unlike_post(request):
    if request.is_ajax():
        pk = request.POST.get('pk')
        obj = Post.objects.get(pk=pk)
        if request.user in obj.liked.all():
            liked = False
            obj.liked.remove(request.user)
        else:
            liked = True
            obj.liked.add(request.user)

        data = {
            'liked': liked,
            'count': obj.like_count
        }

        return JsonResponse(data)

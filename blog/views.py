from django.shortcuts import render
from django.shortcuts import render, get_object_or_404

def post_list(request):
    Post.objects.get(pk=pk)
    return render(request, 'blog/post_list.html', {'post': post})
pass

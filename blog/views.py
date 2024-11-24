from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone



# Vista para listar los posts
def post_list(request):
    # Filtrar los posts que tienen una fecha de publicación pasada y ordenarlos
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    # Pasar los posts al contexto de la plantilla
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

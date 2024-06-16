from django.shortcuts import render, redirect
from .models import BlogPost
from .forms import BlogPostForm

def blog_list(request):
    posts = BlogPost.objects.all().order_by('-publication_date')
    return render(request, 'main/blog_list.html', {'posts': posts})

def blog_create(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else:
        form = BlogPostForm()
    return render(request, 'main/blog_create.html', {'form': form})
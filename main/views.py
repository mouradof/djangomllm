from django.shortcuts import render, redirect
from .models import BlogPost
from .forms import BlogPostForm  # Ensure this import
from django.utils.translation import gettext as _
from django.utils import translation

def blog_list(request):
    current_language = translation.get_language()
    print(f"Current language: {current_language}")  # Debug output
    posts = BlogPost.objects.all().order_by('-publication_date')
    context = {
        'posts': posts,
        'title': _("Blog Posts"),
        'create_post': _("Create a new post"),
    }
    return render(request, 'main/blog_list.html', context)

def blog_create(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else:
        form = BlogPostForm()
    context = {
        'form': form,
        'title': _("Create Blog Post"),
        'save': _("Save"),
        'back_to_list': _("Back to list"),
    }
    return render(request, 'main/blog_create.html', context)

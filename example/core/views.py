
from django.shortcuts import render, get_object_or_404
from django.template.defaultfilters import slugify
from .models import Post, Tag
from .forms import PostForm

# Create your views here.


def home_view(request):
    posts = Post.objects.order_by('-published')
    # Show most common tags
    form = PostForm(request.POST)
    if form.is_valid():
        newpost = form.save(commit=False)
        newpost.slug = slugify(newpost.title)
        newpost.save()
        # Without this next line the tags won't be saved.
        form.save_m2m()
    context = {
        'posts': posts,
        'form': form,
    }
    return render(request, 'home.html', context)


def detail_view(request, slug):
    post = get_object_or_404(Post, slug=slug)
    context = {
        'post': post,
    }
    return render(request, 'detail.html', context)


def tagged(request, slug):
    tag = Tag.objects.filter(slug=slug).values_list('tag', flat=True)
    posts = Post.objects.filter(tags__name__in=tag)

    return render(request, 'home.html', {'posts': posts, 'tag': tag, 'slug': slug})

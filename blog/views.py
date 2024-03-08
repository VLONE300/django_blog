from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from taggit.models import Tag
from blog.models import Post
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from blog.forms import PostForm


def post_list(request):
    posts = Post.objects.order_by('id')
    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'post_list.html', {'posts': posts,
                                              'page': page})


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'post_detail.html', {'post': post})


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            form.save_m2m()
            return redirect('post_list')
        else:
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})


def posts_by_tag(request, tag_slug):
    tag = Tag.objects.get(slug=tag_slug)
    posts = Post.objects.filter(tagged_items__tag_id__in=[tag.id])
    return render(request, 'post_by_tag.html', {'posts': posts, 'tag': tag})


class AuthorView(View):
    def get(self, request, author_id):
        posts = Post.objects.filter(author_id=author_id)
        author = get_object_or_404(User, id=author_id)
        return render(request, 'post_by_author.html', {'posts': posts, 'author': author})


class EditPostView(View):
    def get(self, request, pk):
        posts = Post.objects.get(pk=pk)
        form = PostForm(request.POST or None, instance=posts)
        return render(request, 'edit_news.html', {'posts': posts, 'form': form})

    def post(self, request, pk):
        post = Post.objects.get(pk=pk, author=request.user)
        post.title = request.POST["title"]
        post.text = request.POST["text"]
        post.save()
        return redirect('post_list')

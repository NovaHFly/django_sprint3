from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import render

from blog.models import BlogPost, Category


def index(request: HttpRequest) -> HttpResponse:
    """Show project main page.

    Args:
        request (HttpRequest): Request received from the user.
    """
    posts = BlogPost.objects.filter(is_published=True)
    template = 'blog/index.html'
    context = {'post_list': reversed(posts)}
    return render(request, template, context)


def post_detail(request: HttpRequest, id: int) -> HttpResponse:  # noqa: A002
    """Show post content.

    Args:
        request (HttpRequest): Request received from the user.
        id (int): Post id.
    """
    template = 'blog/detail.html'

    try:
        required_post = BlogPost.objects.get(pk=id)
    except BlogPost.DoesNotExist:
        raise Http404(f'Post with id {id} does not exist!')

    context = {'post': required_post}
    return render(request, template, context)


def category_posts(request: HttpRequest, category_slug: str) -> HttpResponse:
    """Show list of posts in a category.

    Args:
        request (HttpRequest): Request received from the user.
        category_slug (str): Category name.
    """
    template = 'blog/category.html'
    category = Category.objects.get(slug=category_slug)
    posts = reversed(category.posts.all())
    context = {'category': category.title, 'post_list': posts}
    return render(request, template, context)

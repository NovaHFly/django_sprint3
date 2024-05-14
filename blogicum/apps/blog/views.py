from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render

from blog.models import BlogPost, Category


def index(request: HttpRequest) -> HttpResponse:
    """Show project main page.

    Args:
        request (HttpRequest): Request received from the user.
    """
    posts = BlogPost.objects.filter(is_published=True).select_related(
        'category'
    )
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

    required_post = get_object_or_404(
        BlogPost.objects.all(),
        pk=id
    )

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
    posts = category.posts.all()
    context = {'category': category.title, 'post_list': reversed(posts)}
    return render(request, template, context)

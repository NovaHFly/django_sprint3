from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.utils import timezone

import blog.models


def index(request: HttpRequest) -> HttpResponse:
    """Show project main page.

    Args:
        request (HttpRequest): Request received from the user.
    """
    template = 'blog/index.html'

    posts = (
        blog.models.Post.objects.select_related(
            'category',
            'location',
            'author',
        )
        .filter(
            is_published=True,
            category__is_published=True,
            pub_date__lte=timezone.now()
        )
    )[:5]
    context = {'post_list': posts}
    return render(request, template, context)


def post_detail(request: HttpRequest, id: int) -> HttpResponse:  # noqa: A002
    """Show post content.

    Args:
        request (HttpRequest): Request received from the user.
        id (int): Post id.
    """
    template = 'blog/detail.html'
    required_post = get_object_or_404(
        blog.models.Post.objects.select_related(
            'category',
            'location',
            'author',
        ).filter(
            is_published=True,
            category__is_published=True,
            pub_date__lte=timezone.now()
        ),
        pk=id,
    )

    context = {'post': required_post}
    return render(request, template, context)


def category_posts(request: HttpRequest, category_slug: str) -> HttpResponse:
    """Show list of posts in a category.

    Args:
        request (HttpRequest): Request received from the user.
        category_slug (str): Category identifier.
    """
    template = 'blog/category.html'
    category = get_object_or_404(
        blog.models.Category.objects.filter(is_published=True),
        slug=category_slug,
    )
    posts = (
        category.posts.select_related(
            'location',
            'author',
        )
        .filter(is_published=True, pub_date__lte=timezone.now())
    )
    context = {'category': category.title, 'post_list': posts}
    return render(request, template, context)

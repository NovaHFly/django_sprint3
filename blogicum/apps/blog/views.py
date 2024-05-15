from datetime import datetime

from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render

import blog.models


def index(request: HttpRequest) -> HttpResponse:
    """Show project main page.

    Args:
        request (HttpRequest): Request received from the user.
    """
    template = 'blog/index.html'
    # - Cache all foreign keys (as all are needed)
    # - Exclude all posts which are either:
    #   1. Not published
    #   2. From a not published category
    #   3. Published at a date and time later than now
    # - Order resulting posts by publication date descending
    # - Get 5 latest posts
    posts = (
        blog.models.Post.objects.select_related(
            'category',
            'location',
            'author',
        )
        .filter(
            is_published=True,
            category__is_published=True,
            pub_date__lte=datetime.now(),
        )
        .order_by('-pub_date')
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
    # - Cache all foreign keys (as all are needed)
    # - Exclude all posts which are either:
    #   1. Not published
    #   2. From a not published category
    #   3. Published at a date and time later than now
    # - Get post which id is equal to [id]
    # - If no post found, return error 404
    required_post = get_object_or_404(
        blog.models.Post.objects.select_related(
            'category',
            'location',
            'author',
        ).filter(
            is_published=True,
            category__is_published=True,
            pub_date__lte=datetime.now(),
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
    # Get category object.
    # If category is not published or
    #   no match found for category_slug
    #   return error 404
    category = get_object_or_404(
        blog.models.Category.objects.filter(is_published=True),
        slug=category_slug,
    )
    # Get all posts from this category, exclude those which are:
    # 1. Not published
    # 2. Published at a date and time later than now
    # Order them by publication date descending
    posts = (
        category.posts.select_related(
            'location',
            'author',
        )
        .filter(is_published=True, pub_date__lte=datetime.now())
        .order_by('-pub_date')
    )
    context = {'category': category.title, 'post_list': posts}
    return render(request, template, context)

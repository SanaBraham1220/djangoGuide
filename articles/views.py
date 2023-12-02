from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Article

"""
@login_required replaces if request.user.is_authenticated testing
"""
@login_required
def article_create_view(request):
    context = {}
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        new_article_object = Article.objects.create(title=title, content=content)
        context["object"] = new_article_object
        context["created"] = True

    return render(request, "articles/create.html", context=context)


# To be tested
def article_search_view(request):
    object = None
    try:
        query = int(request.GET.get("q"))
    except:
        query = None
    print(query)
    if query is not None:
        object = Article.objects.get(id=query)
    context = {"object": object}
    print(context)

    return render(request, "articles/search.html", context=context)


# To be tested
def article_detail_view(request, id=None):
    object = None
    if id is not None:
        object = Article.objects.get(id=id)
    context = {"object": object}

    return render(request, "articles/detail.html", context=context)

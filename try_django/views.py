from articles.models import Article
from django.shortcuts import render

def home_view(request):
    
    article_queryset = Article.objects.all()
    context = {
        "objects_list" : article_queryset
    }

    return render(request,'home-view.html',context)
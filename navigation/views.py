from django.shortcuts import render
from .models import Category
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET"])
def index(request):
    # 获取所有分类及对应的链接（按权重排序）
    categories = Category.objects.prefetch_related('link_set').all()
    return render(request, 'nav/index.html', {'categories': categories})




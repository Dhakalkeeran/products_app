from django.shortcuts import render
from .models import Category, Tag, Product


def search(request):
    query = request.GET.get('query')
    category = request.GET.get('category')
    tag = request.GET.get('tag')

    products = Product.objects.all()

    if query:
        products = products.filter(description__icontains=query)
    if category:
        products = products.filter(category__name=category)
    if tag:
        products = products.filter(tags__name=tag)

    categories = Category.objects.all()
    tags = Tag.objects.all()
    
    return render(request, "products/search.html",  {
        'products': products,
        'categories': categories,
        'tags': tags,
    })
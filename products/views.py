from django.shortcuts import render
from .models import Category, Tag, Product


def search(request):
    # get request parameters
    query = request.GET.get('query')
    category = request.GET.get('category')
    tag = request.GET.get('tag')

    # get all products in database
    products = Product.objects.all()

    # filter products based on the parameters
    if query:
        products = products.filter(description__icontains=query)
    if category:
        products = products.filter(category__name=category)
    if tag:
        products = products.filter(tags__name=tag)

    # get all categories and tags
    categories = Category.objects.all()
    tags = Tag.objects.all()
    
    # render search page and pass data as context
    return render(request, "products/search.html",  {
        'products': products,
        'categories': categories,
        'tags': tags,
    })
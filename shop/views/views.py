from django.shortcuts import render
from ..models.models import *
from django.db.models import Case , When , BooleanField

def home(req):
    context = {}
    categories = Category.objects.all().prefetch_related('products')
    context['categories'] = categories
    products = {}
    if(req.user.is_authenticated):
        user = req.user
        for category in categories:
            products[category.title] = category.products.all().annotate(
                isWishlisted = Case(
                    When(wishlist__user=user , then=True),
                    default=False,
                    output_field=BooleanField()
                )
            )[:10]
    else:
        for category in categories:
            products[category.title] = category.products.all()[:10]

    context['products'] = products
    return render(req, 'pages/home.html',context=context)


from .models.cart_models import Cart
from .models.models import Category

def cart_context_processor(req):
    user = req.user
    context = {}
    if(user.is_authenticated):
        cart , _ = Cart.objects.get_or_create(user=user)
        total_qty = cart.total_quantity()
        context['total_qty'] = total_qty
    else:
        context['total_qty'] = 0
    return context


def category_context_processor(req):
    context= {}
    categories = Category.objects.all().prefetch_related('products')
    context['categories'] = categories
    return context
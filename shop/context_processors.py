from .models.cart_models import Cart

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
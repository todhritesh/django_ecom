def is_logged_in(user):
    return not user.is_authenticated

from .models.cart_models import Cart

def has_items_in_cart(user):
    return Cart.objects.filter(user=user).count() > 0
from django.views import View
from django.views.generic import TemplateView
from django.shortcuts import render , redirect , reverse
from ..models.order_models import *
from ..models.cart_models import *
from django.db.models import ExpressionWrapper , F , FloatField , Sum
from ..forms import AddressForm
from django.contrib import messages

class AddressView(TemplateView):
    template_name = 'pages/order_details.html'
    def get(self , req):
        user = req.user
        context = {}
        address_form = AddressForm()
        context['address_form'] = address_form
        addresses = Address.objects.filter(user=user)
        context['addresses'] = addresses
        return render(req, self.template_name , context=context)

    def post(self , req):
        address = req.POST.get('address',None)
        address_form = AddressForm(req.POST)
        if(address is not None):
            return redirect('order_details_process',addr=address)
        elif(address_form.is_valid()):
            addr = address_form.save(commit=False)
            addr.user = req.user
            addr.save()
            return redirect('order_details_address')
        else:
            messages.error(req, "Please select valid address")
            return redirect(req.META.get('HTTP_REFERER'))
        return redirect('order_details_address')

class OrderProcessView(TemplateView):
    template_name = 'pages/order_process.html'
    def get(self , req , addr):
        user = req.user
        context = {}
        address = Address.objects.filter(pk=addr)
        if(not address.exists()):
            return redirect(req.META.get('HTTP_REFERER'))
        
        cart , _ = Cart.objects.get_or_create(user=user)
        cart_items = CartItem.objects.filter(cart=cart).annotate(total_price=ExpressionWrapper(F('product__price') * F('qty'), output_field=FloatField()))
        cart_amount = cart_items.aggregate(Sum('total_price'))['total_price__sum']
        context['cart_amount'] = round(cart_amount or 0,2)
        context['cart_items'] = cart_items
        address = address.first()
        context['addr'] = address
        return render(req, self.template_name , context=context)

    def post(self , req , addr):
        mode_of_payment = req.POST.get('payment',None)
        if(mode_of_payment is None):
            messages.error(req, "Please select valid payment mode")
            return redirect(req.META.get('HTTP_REFERER'))
        user = req.user
        address = Address.objects.get(id=addr)
        cart = Cart.objects.get(user=user)
        cart_items = CartItem.objects.filter(cart=cart)
        order = Order()
        order.address = address
        order.total_amount = cart.calculate_total_amount()
        order.user = user
        order.save()
        for item in cart_items:
            order_item = OrderItem()
            order_item.order = order
            order_item.product = item.product
            order_item.qty = item.qty
            order_item.price = item.product.price
            order_item.save()
        payment = Payment()
        payment.order = order
        payment.mode_of_payment = mode_of_payment
        payment.save()
        cart.delete()
        messages.success(req, "Order Placed Successfully")
        return redirect('home')


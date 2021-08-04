from django.shortcuts import redirect
from django.views import View

from store.models.customer import Customer
from store.models.orders import Order
from store.models.products import Product


class Checkout(View):
    def post(self, request):
        name = request.POST.get('name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))

        for product in products:
            print(cart.get(str(product.id)))
            order = Order(customer=Customer(id=customer),
                          product=product,
                          price=product.price,
                          address=address,
                          phone=phone,
                          quantity=cart.get(str(product.id)))
            order.save()
        request.session['cart'] = {}
        print(name, address, phone, customer, cart, products)
        return redirect('cart')

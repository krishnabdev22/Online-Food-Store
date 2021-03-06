from django.shortcuts import render, redirect
from django.views import View

from store.models.customer import Customer
from store.models.orders import Order
from store.models.products import Product


class OrderView(View):
    def get(self, request):
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer(customer)
        print(orders)
        orders = orders.reverse()
        return render(request, 'orders.html', {'orders' : orders})

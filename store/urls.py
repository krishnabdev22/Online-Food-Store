from django.urls import path

from .views import login, signup
from .views.cart import Cart
from .views.checkout import Checkout
from .views.feedback import feed
from .views.home import Index
from .views.login import logout
from .views.orders import OrderView
from .views.otp import otpVerify

urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('signup', signup.Signup.as_view(), name='signup'),
    path('login', login.Login.as_view(), name='login'),
    path('logout', logout, name='logout'),
    path('cart', Cart.as_view(), name='cart'),
    path('check-out', Checkout.as_view(), name='checkout'),
    path('orders', OrderView.as_view(), name='orders'),
    # path('feedback',Feedback.as_view(),name='feedback'),
    path('feed', feed, name='feed'),
    path('otpVerify/<str:email>', otpVerify, name='otpVerify_url'),
    # path('quantity',quantity,name='quantity'),

]

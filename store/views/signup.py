from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.views import View
from store.utils import send_sms
import random

from store.models.customer import Customer


class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')
        otp = random.randrange(100000, 999999)

        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email,
        }

        error_message = None

        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            phone=phone,
                            email=email,
                            password=password,
                            otp=otp)

        error_message = self.validateCustomer(customer)

        # Saving
        if not error_message:
            print(first_name, last_name, phone, email, password)

            customer.password = make_password(customer.password)

            customer.register()
            if phone:
                print("-----------------------------------------------------------------",  phone)
                send_sms(otp, phone)
                # request.session['pk'] = user.pk
                return redirect('otpVerify_url', email)
            #return redirect('homepage')
            #return redirect('login')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'signup.html', data)

    def validateCustomer(self, customer):
        error_message = None

        if (not customer.first_name):
            error_message = "First Name Required"
        elif len(customer.first_name) < 3:
            error_message = "First Name Must have " \
                            "Atleast 3 Character"
        if (not customer.phone):
            error_message = "Enter Your Phone Number"
        elif len(customer.phone) != 10:
            error_message = "Phone Number Not Valid"

        if (not customer.password):
            error_message = "Enter Your Password"
        elif len(customer.password) < 4:
            error_message = "Password atleast Need 4 character/numbers"

        elif customer.isExists():
            error_message = "Email Already Exists"

        return error_message

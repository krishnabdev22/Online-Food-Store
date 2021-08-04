from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect
from django.views import View

from store.models.customer import Customer


class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        print("-----------------------", customer.phone)
        error_message = None
        if customer.otp_verified:
            if customer:
                flag = check_password(password, customer.password)
                if flag:
                    request.session['customer'] = customer.id
                    request.session['email'] = email
                    return redirect('homepage')
                else:
                    error_message = "Invalid Email or Password"
            else:
                error_message = "Invalid Email or Password"
        else:
            print("hello my dereeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
            error_message = "Not verified"
        print(email, password)
        return render(request, 'login.html', {'error': error_message})


def logout(request):
    request.session.clear()
    return redirect('login')

from django.shortcuts import render

# Create your views here.
def payment(request):
    return render(request, 'pyments/payment.html')
def add_account(request):
    return render(request, 'pyments/add_account.html')
def payment_status(request):
    return render(request, 'pyments/payment_status.html')

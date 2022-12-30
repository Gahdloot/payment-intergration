from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest, HttpResponse
from django.conf import settings
from django.contrib import messages
from . import forms
from .models import Payment


# Create your views here.

def initiate_payment(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        payment_form = forms.PaymentForm(request.POST)
        if payment_form.is_valid():
            payment = payment_form.save()
            return render(request, 'make_payments.html',
                          {'payments': payment, 'paystack_public_key': settings.PAYSTACK_PUBLIC_KEY})
    else:
        payment_form = forms.PaymentForm()
    return render(request, 'initiate_payments.html', {'payment_form': payment_form})


def verify_payment(request: HttpRequest, ref: str) -> HttpResponse:
    payments = get_object_or_404(Payment, ref=ref)
    verified = payments.verify_payment()
    if verified:
        messages.success(request, 'verification Successful')
    else:
        messages.error(request, 'Verification failed')
    return redirect('initiate-payment')


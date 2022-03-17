from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    """Checkout view"""
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51KeIuBFRia4cbWFL5kaT7M9YdjyLuADOOmtWqxNUOJoQEM1da3eYDYtn5a2TA0hBwfYgL6umuWxB6fPa4quPDe6000s0yDmy2M',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)

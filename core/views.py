from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Product
from .forms import OrderForm

def home(request):
    products = Product.objects.all()
    form = OrderForm()
    context = {
        'products': products,
        'form': form,
    }
    return render(request, 'core/home.html', context)

def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ваш заказ успешно оформлен! Мы свяжемся с вами в ближайшее время.')
            return redirect('home')
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки в форме.')
    return redirect('home')
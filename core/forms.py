from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer_name', 'customer_email', 'customer_phone', 'product']
        widgets = {
            'customer_name': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border rounded-lg focus:ring-2 focus:ring-green-500 focus:border-transparent', 'placeholder': 'Ваше имя'}),
            'customer_email': forms.EmailInput(attrs={'class': 'w-full px-4 py-2 border rounded-lg focus:ring-2 focus:ring-green-500 focus:border-transparent', 'placeholder': 'Email'}),
            'customer_phone': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border rounded-lg focus:ring-2 focus:ring-green-500 focus:border-transparent', 'placeholder': 'Телефон'}),
            'product': forms.Select(attrs={'class': 'w-full px-4 py-2 border rounded-lg focus:ring-2 focus:ring-green-500 focus:border-transparent'}),
        }
        labels = {
            'customer_name': 'Имя',
            'customer_email': 'Email',
            'customer_phone': 'Телефон',
            'product': 'Выберите букет',
        }
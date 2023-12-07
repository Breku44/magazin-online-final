from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from .models import CPU, GPU
import json
import os

json_file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'products.json')

with open(json_file_path) as file:
    products_data = json.load(file)

products = []

for item in products_data:
    if 'cores' in item:
        product = CPU(
            id=item['id'],
            name=item['name'],
            price=item['price'],
            quantity=item['quantity'],
            cores=item.get('cores', 0),
            clock_speed=item.get('clock_speed', 0.0)
        )
    else:
        product = GPU(
            id=item['id'],
            name=item['name'],
            price=item['price'],
            quantity=item['quantity'],
            memory_size=item.get('memory_size', 0),
            gpu_speed=item.get('gpu_speed', 0.0)
        )
    products.append(product)

def blog(request):
    return render(request, 'mycartapp/blog.html')

def announcement1(request):
    return render(request, 'mycartapp/announcement1.html')

def announcement2(request):
    return render(request, 'mycartapp/announcement2.html')

def home(request):
    request.session['cart'] = {}
    request.session['total_price'] = 0
    request.session.save()
    return render(request, 'mycartapp/home.html')

def product_list(request):
    cart = request.session.get('cart', {})
    total_price = request.session.get('total_price', 0)
    return render(request, 'mycartapp/product_list.html', {'products': products, 'cart': cart, 'total_price': total_price})

def add_to_cart(request):
    if request.method == 'POST':
        input_product_id = request.POST.get('product_id')

        if input_product_id is not None:
            try:
                input_product_id = int(input_product_id)
                quantity = int(request.POST.get('quantity', 1))

                product = next((p for p in products if p.id == input_product_id), None)

                if not product:
                    messages.error(request, "Product does not exist.")
                    return redirect(reverse('product_list'))

                if product.quantity < quantity:
                    messages.error(request, f"Sorry, only {product.quantity} units of {product.name} are available.")
                else:
                    cart = request.session.get('cart', {})
                    str_product_id = str(input_product_id)

                    product.quantity -= quantity

                    if str_product_id in cart:
                        cart[str_product_id] += quantity
                    else:
                        cart[str_product_id] = quantity

                    total_price_by_id = {}

                    for product_id, cart_quantity in cart.items():
                        product = next((p for p in products if p.id == int(product_id)), None)
                        if product:
                            total_price_by_id[str(product_id)] = total_price_by_id.get(str(product_id), 0) + (
                                    product.price * cart_quantity)

                    total_price = sum(total_price_by_id.values())
                    request.session['cart'] = cart
                    request.session['total_price'] = total_price
                    request.session.save()

                    messages.success(request, f"{quantity} units of {product.name} added to the cart.")
            except ValueError:
                messages.error(request, "Invalid product_id or quantity.")
    return redirect(reverse('product_list'))

def payment_confirmation(request):
    cart = request.session.get('cart', {})
    total_price = request.session.get('total_price', 0)

    request.session['cart'] = {}
    request.session['total_price'] = 0
    request.session.save()

    return render(request, 'mycartapp/payment_confirmation.html', {'total_price': total_price})

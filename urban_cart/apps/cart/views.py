from django.shortcuts import render,redirect
from django.contrib import messages
from apps.admin1.models import Product

# Create your views here.
# def cart(request):
#     return render(request, 'cart/cart.html')
def cart(request):
    # Retrieve the cart from the session, or initialize an empty cart if it doesn't exist
    cart = request.session.get('cart', {})

    cart_items = []
    total_price = 0

    for product_id, quantity in cart.items():
        try:
            product = Product.objects.get(id=product_id)
            total_price += product.product_price * quantity
            cart_items.append({
                'product': product,
                'quantity': quantity,
                'subtotal': product.product_price * quantity
            })
        except Product.DoesNotExist:
            # If the product no longer exists, remove it from the cart
            continue

    if request.method == 'POST':
        # Handle removing an item from the cart
        product_id = request.POST.get('product_id')
        if product_id in cart:
            quantity = cart[product_id]  # Get the quantity to restore stock
            try:
                product = Product.objects.get(id=product_id)
                product.product_stock += quantity  # Increase stock
                product.save()  # Save the updated stock
            except Product.DoesNotExist:
                messages.error(request, "Product not found.")

            del cart[product_id]  # Remove the item from the cart
            request.session['cart'] = cart  # Update the session
            messages.success(request, 'Item removed from cart.')

        return redirect('my_cart')  # Reload the cart page

    context = {
        'cart_items': cart_items,
        'total_price': total_price
    }
    return render(request, 'cart/cart.html', context)

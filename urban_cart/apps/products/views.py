from django.shortcuts import render,redirect
from apps.admin1.models import Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages

# Create your views here.
from django.shortcuts import render, get_object_or_404


# def product_list(request):
#     products = Product.objects.all()
#     if request.method == 'POST':  # Handle input quantity
#         product_id = request.POST.get('product_id')  # Get the book ID from the form
#         product_stock = request.POST.get('product_stock')  # Quantity from the form

#         try:
#             product_stock = int(product_stock)  # Convert quantity to integer
#         except ValueError:
#             product_stock = 0

#         if product_stock > 0:
#             try:
#                 # Retrieve the specific book by its primary key (id)
#                 product = Product.objects.get(id=product_id)

#                 # Check if there's enough stock
#                 if product.product_stock < product_stock:
#                     error_message = "Not enough stock available."
#                     return render(request, 'user_list.html', {'product': product, 'error_message': error_message})

#                 # Calculate the total price
#                 total_price = product.product_price * product_stock

#                 # Deduct the quantity from the actual stock
#                 product.product_stock -= product_stock
#                 product.save()  # Save the updated quantity

#                 # Prepare context to display the selected book info
#                 context = {
#                     'product_name': product.product_name,
#                     'product_description': product.product_description,
#                     'product_image1': product.product_image1,
#                     'product_image2': product.product_image2,
#                     'product_image3': product.product_image3,
#                     'product_category': product.product_category,
#                     'product_stock': product_stock,
#                     'product_price': total_price,
#                 }

#                 return render(request, 'cart.html', context)  # Redirect to the cart page

#             except Product.DoesNotExist:
#                 error_message = "Book not found."
#                 return render(request, 'cart/cart.html', {'product': product, 'error_message': error_message})
#     return render(request, 'products/product_list.html',{'products':products})
# def product_list(request):
#     # Fetch all products to display in the product list
#     products = Product.objects.all()

#     if request.method == 'POST':  # Handle adding to cart with input quantity
#         product_id = request.POST.get('product_id')  # Get the product ID from the form
#         product_stock = request.POST.get('product_stock')  # Quantity from the form

#         try:
#             product_stock = int(product_stock)  # Convert quantity to an integer
#         except ValueError:
#             product_stock = 0  # Default to 0 if the input is invalid

#         if product_stock > 0:
#             try:
#                 # Retrieve the specific product by its primary key (id)
#                 product = Product.objects.get(id=product_id)

#                 # Check if there's enough stock available
#                 if product.product_stock < product_stock:
#                     error_message = "Not enough stock available."
#                     return render(
#                         request,
#                         'products/product_list.html',
#                         {'products': products, 'error_message': error_message}
#                     )

#                 # Calculate the total price
#                 total_price = product.product_price * product_stock

#                 # Deduct the quantity from the actual stock
#                 product.product_stock -= product_stock
#                 product.save()  # Save the updated stock

#                 # Prepare context to display the selected product details in the cart
#                 context = {
#                     'product_name': product.product_name,
#                     'product_description': product.product_description,
#                     'product_image1': product.product_image1,
#                     'product_image2': product.product_image2,
#                     'product_image3': product.product_image3,
#                     'product_category': product.product_category,
#                     'product_stock': product_stock,
#                     'product_price': total_price,
#                 }

#                 # Redirect to the cart page with the selected product details
#                 return render(request, 'cart/cart.html', context)

#             except Product.DoesNotExist:
#                 error_message = "Product not found."
#                 return render(
#                     request,
#                     'products/product_list.html',
#                     {'products': products, 'error_message': error_message}
#                 )

#     # Render the product list page with all products
#     return render(request, 'products/product_list.html', {'products': products})
def product_list(request):
    # Fetch all products
    products_list = Product.objects.all()

    # Pagination setup: 10 products per page
    paginator = Paginator(products_list, 9)
    page = request.GET.get('page')  # Get the current page number from the request
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page
        products = paginator.page(1)
    except EmptyPage:
        # If page is out of range, deliver the last page of results
        products = paginator.page(paginator.num_pages)

    if request.method == 'POST':  # Handle adding to cart with input quantity
        product_id = request.POST.get('product_id')  # Get the product ID from the form
        product_stock = request.POST.get('product_stock')  # Quantity from the form

        try:
            product_stock = int(product_stock)  # Convert quantity to an integer
        except ValueError:
            product_stock = 0  # Default to 0 if the input is invalid

        if product_stock > 0:
            try:
                # Retrieve the specific product by its primary key (id)
                product = Product.objects.get(id=product_id)

                # Check if there's enough stock available
                if product.product_stock < product_stock:
                    error_message = "Not enough stock available."
                    return render(
                        request,
                        'products/product_list.html',
                        {'products': products, 'error_message': error_message}
                    )

                # Calculate the total price
                total_price = product.product_price * product_stock

                # Deduct the quantity from the actual stock
                product.product_stock -= product_stock
                product.save()  # Save the updated stock

                # Prepare context to display the selected product details in the cart
                context = {
                    'product_name': product.product_name,
                    'product_description': product.product_description,
                    'product_image1': product.product_image1,
                    'product_image2': product.product_image2,
                    'product_image3': product.product_image3,
                    'product_category': product.product_category,
                    'product_stock': product_stock,
                    'product_price': total_price,
                }

                # Redirect to the cart page with the selected product details
                return render(request, 'cart/cart.html', context)

            except Product.DoesNotExist:
                error_message = "Product not found."
                return render(
                    request,
                    'products/product_list.html',
                    {'products': products, 'error_message': error_message}
                )

    # Render the product list page with paginated products
    return render(request, 'products/product_list.html', {'products': products})

def product_details(request):
   products = Product.objects.all()
   if request.method == 'POST':
        product_id = request.POST.get('product_id')  # Get the selected book's ID
        product = get_object_or_404(Product, id=product_id)  # Fetch book or 404 if not found

        products = {
            'product': product,  # Pass the entire book object to the template
        }

        return render(request, 'products/product_details.html', products)


   return render(request, 'products/product_details.html',{'products':products})
# def product_category(request,category):
#    products = Product.objects.filter(category=category)
#    return render(request, 'products/product_category.html',{'products': products, 'category': category})
def product_category(request, category):
    # Validate the category exists
    if not Product.objects.filter(category=category).exists():
        error_message = f"No products found in the '{category}' category."
        return render(request, 'products/product_category.html', {'error_message': error_message})

    # Fetch products for the given category
    products = Product.objects.filter(category=category)

    # Pagination setup
    paginator = Paginator(products, 10)  # Show 10 products per page
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    # Render the template
    return render(request, 'products/product_category.html', {
        'products': products,
        'category': category,
    })
def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    quantity = int(request.POST.get('quantity', 1))

    if product_id in cart:
        cart[product_id] += quantity  # Increment the quantity
    else:
        cart[product_id] = quantity  # Add the new product

    request.session['cart'] = cart  # Save cart to session
    messages.success(request, 'Product added to cart.')
    return redirect('product_list')  # Redirect to the product list or detail page





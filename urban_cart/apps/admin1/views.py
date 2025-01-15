from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from .models import Product,Slider
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    return render(request, 'admin1/admin_dashboard.html')
def add_item(request):
    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        product_category = request.POST.get('product_category')
        product_description = request.POST.get('product_description')
        product_price = float(request.POST.get('product_price', '0') or 0.0)
        product_stock = int(request.POST.get('product_stock', '0') or 0)
        # product_stock = request.POST.get('product_stock')  # Convert to int for calculations
        # product_price = request.POST.get('product_price')  # Convert to float if needed
        product_image1 = request.FILES.get('product_image1')  # Handling file upload correctly
        product_image2 = request.FILES.get('product_image2')  # Handling file upload correctly
        product_image3 = request.FILES.get('product_image3')  # Handling file upload correctly
        # product_stock= int(product_stock)
        # product_price= float(product_price)
        # Check if the product already exists
        product, created = Product.objects.get_or_create(
            product_name=product_name,
            defaults={
                'product_image1': product_image1,
                'product_image2': product_image2,
                'product_image3': product_image3,
                'product_category': product_category,
                'product_description': product_description,
                'product_stock': product_stock,
                'product_price': product_price
            }
        )

        if not created:
            # If Product exists, update its quantity
            product.product_stock += product_stock
            product.save()
        else:
            # If newly created, save it now
            product.save()

        return redirect('add_item')

    return render(request, 'admin1/add_item.html')



    #return render(request, 'admin1/add_item.html')
def delete_item(request):
     if request.method == 'POST':
        product_name = request.POST.get('product_name')

        # Find the book with the specified name
        product = Product.objects.filter(product_name=product_name)

        if product.exists():
            product.delete()  # Deletes the matching book(s)
            message = f"product '{product_name}' deleted successfully."
        else:
            message = f"product '{product_name}' not found."

        return render(request, 'admin1/delete_item.html', {'message': message})
     return render(request, 'admin1/delete_item.html')
     
    
# def update_item(request):
#       if request.method == 'POST':
#         search_name = request.POST.get('product_name')

#         # Try to find the book using search_name
#         product = get_object_or_404(Product, product_name=search_name)

#         # Update the book's attributes if found
#         if 'product_name' in request.POST:
#             product.product_name = request.POST.get('product_name', product.product_name)
#         if 'product_category' in request.POST:
#             product.product_category = request.POST.get('product_category', product.product_category)
#         if 'product_description' in request.POST:
#             product.product_description = request.POST.get('product_description', product.product_description)
#         if 'product_stock' in request.POST:
#             product.product_stock = int(request.POST.get('product_stock', product.product_stock))
#         if 'product_price' in request.POST:
#             product.product_price = float(request.POST.get('product_price', product.product_price))
#         if 'product_image1' in request.FILES:
#             product.product_image1 = request.FILES.get('product_image1', product.product_image1)
#         if 'product_image2' in request.FILES:
#             product.product_image2 = request.FILES.get('product_image2', product.product_image2)
#         if 'product_image3' in request.FILES:
#             product.product_image3 = request.FILES.get('product_image3', product.product_image3)

#         # Save the updated book
#         product.save()

#         return redirect('admin_dashboard')  # Redirect to the same page or another page
#       return render(request, 'admin1/update_item.html')
def update_item(request):
    if request.method == 'POST':
        search_name = request.POST.get('search_name')  # Separate search name for clarity
        product = get_object_or_404(Product, product_name=search_name)

        # Track if any changes were made
        changes_made = False

        # Update fields only if provided
        if 'product_name' in request.POST:
            product.product_name = request.POST['product_name']
            changes_made = True
        if 'product_category' in request.POST:
            product.product_category = request.POST['product_category']
            changes_made = True
        if 'product_description' in request.POST:
            product.product_description = request.POST['product_description']
            changes_made = True
        if 'product_stock' in request.POST:
            product.product_stock = int(request.POST.get('product_stock', '0') or 0)
            changes_made = True
        if 'product_price' in request.POST:
            product.product_price = float(request.POST.get('product_price', '0') or 0.0)
            changes_made = True
        if 'product_image1' in request.FILES:
            product.product_image1 = request.FILES['product_image1']
            changes_made = True
        if 'product_image2' in request.FILES:
            product.product_image2 = request.FILES['product_image2']
            changes_made = True
        if 'product_image3' in request.FILES:
            product.product_image3 = request.FILES['product_image3']
            changes_made = True

        # Save only if changes were made
        if changes_made:
            product.save()
            return redirect('admin_dashboard')
        else:
            message = "No changes were made to the product."
            return render(request, 'admin1/update_item.html', {'message': message})

    return render(request, 'admin1/update_item.html')
      

   
# def list_item(request):
#     product = Product.objects.all()
#     return render(request,'admin1/list_item.html',{'product':product})
def list_item(request):
    product_list = Product.objects.all()
    paginator = Paginator(product_list, 9)  # Show 10 products per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'admin1/list_item.html', {'page_obj': page_obj})

    #return render(request, 'admin1/list_item.html')
# def slide(request):
#     if request.method == 'POST':
#         add_head = request.POST.get('add_head')
#         add_sub_head = request.POST.get('add_sub_head')
#         add_text = request.POST.get('add_text')
#         add_price = request.POST.get('add_price')
#         add_image = request.FILES.get('add_image')
       

#         slider = Slider(
#             add_head=add_head,
#             add_sub_head=add_sub_head,
#             add_text=add_text,
#             add_price=add_price,
#             add_image=add_image,
            
#         )
#         slider.save()
#         # show in home app inner index page in 4 houre
#         response.set_cookie('add_head', add_head, max_age=14400)
#         response.set_cookie('add_sub_head', add_sub_head, max_age=14400)
#         response.set_cookie('add_text', add_text, max_age=14400)
#         response.set_cookie('add_price', add_price, max_age=14400)
#         response.set_cookie('add_image', add_image, max_age=14400)
#         return redirect('admin1/add_item.html')
        
#     return render(request, 'admin1/slide.html')

def slide(request):
    if request.method == 'POST':
        add_head = request.POST.get('add_head')
        add_sub_head = request.POST.get('add_sub_head')
        add_text = request.POST.get('add_text')
        add_price = request.POST.get('add_price')
        add_image = request.FILES.get('add_image')

        # Save the slider data in the database
        slider = Slider(
            add_head=add_head,
            add_sub_head=add_sub_head,
            add_text=add_text,
            add_price=add_price,
            add_image=add_image,
        )
        slider.save()

        # Create a response object
        response = redirect('admin1/add_item.html')

        # Set cookies to expire after 4 hours (14400 seconds)
        response.set_cookie('add_head', add_head, max_age=14400)
        response.set_cookie('add_sub_head', add_sub_head, max_age=14400)
        response.set_cookie('add_text', add_text, max_age=14400)
        response.set_cookie('add_price', add_price, max_age=14400)
        response.set_cookie('add_image', add_image.name if add_image else '', max_age=14400)

        return response

    return render(request, 'admin1/slide.html')

    
   
# def add_category(request):
#     return render(request, 'add_category.html')
# def delete_category(request):
#     return render(request, 'delete_category.html')
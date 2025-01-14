from django.shortcuts import render,redirect
from .models import Register,State,District,Account
from django.contrib import messages
from django.urls import reverse
from apps.admin1.models import Product
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
# Create your views here.
# def login(request):
#      if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         try:
#             # Try to retrieve the user by email
#             user = Register.objects.get(username=username)

#             # Check the password (adjust this if your passwords are hashed)
#             if user.password == password or check_password(password, user.password):
#                 messages.success(request, 'Login successful')

#                 # login=Login.create()

               

#         except Register.DoesNotExist:
#             messages.warning(request, 'Email does not exist')
#             return redirect('login')
#         return render(request, 'users/login.html')
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            # Retrieve the user by username (ensure username is unique or handle appropriately)
            user = Register.objects.get(username=username)

            # Check the password (assuming passwords are hashed using Django's password hashing)
            if check_password(password, user.password):
                # If the password matches, set a success message and proceed
                messages.success(request, 'Login successful')
                return redirect('index')  # Redirect to a homepage or dashboard after successful login
            else:
                # If the password does not match, show an error message
                messages.warning(request, 'Incorrect password')
                return redirect('login')  # Redirect back to login page

        except Register.DoesNotExist:
            # If the user does not exist, show a warning message
            messages.warning(request, 'Username does not exist')
            return redirect('login')  # Redirect back to login page

    return render(request, 'users/login.html')

   
# def register(request):
#      if request.method == 'POST':
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         person = Register(
#             username=username,
#             email=email,
#             password=make_password(password),
           
#         )
#         person.save()
#         return redirect('index')
#      return render(request, 'users/register.html')
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Validate input fields
        if not username or not email or not password:
            messages.warning(request, 'All fields are required.')
            return redirect('register')

        if len(password) < 6:
            messages.warning(request, 'Password must be at least 6 characters long.')
            return redirect('register')

        # Check if email or username already exists
        if Register.objects.filter(username=username).exists():
            messages.warning(request, 'Username already exists. Please choose another one.')
            return redirect('register')

        if Register.objects.filter(email=email).exists():
            messages.warning(request, 'Email is already registered.')
            return redirect('register')

        # Create and save the new user
        person = Register(
            username=username,
            email=email,
            password=make_password(password),
        )
        person.save()

        messages.success(request, 'Registration successful! Please log in.')
        return redirect('index')  # Redirect to login or index page after registration

    return render(request, 'users/register.html')

   
# def account(request):
#     states=State.objects.all()
#     districts=District.objects.all()
#     if request.method == 'POST':
#         firstName = request.POST.get('firstName')
#         lastName = request.POST.get('lastName')
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         phone = request.POST.get('phone')
#         address = request.POST.get('address')
#         address2 = request.POST.get('address2')
#         state = request.POST.get('state')
#         district = request.POST.get('district')
#         pin = request.POST.get('pin')
#         # checkbox its optional someone can choose to give or not and choose one and two  options
#         same_address = request.POST.get('same_address') #Shipping address is the same as my billing address
#         save_info = request.POST.get('save_info') #Save this information for next time
#         # if save_info is checked then save the information in session
#         if save_info:
#             request.session['firstName'] = firstName
#             request.session['lastName'] = lastName
#             request.session['username'] = username
#             request.session['email'] = email
#             request.session['phone'] = phone
#             request.session['address'] = address
#             request.session['address2'] = address2
#             request.session['state'] = state
#             request.session['district'] = district
#             request.session['pin'] = pin
#             request.session['same_address'] = same_address
#             request.session['save_info'] = save_info
#             # if same_address is checked then save the information in session
#             if same_address:
#                 request.session['shipping_address'] = address
#                 else:
#     request.session['shipping_address'] = address2
#     return render(request, 'users/account.html', {'states': states, 'districts': districts
#                                                   return render(request, 'users/account.html', {'states': states, 'districts': districts
                                                                                                
       


#     return render(request, 'users/account.html')
# def account(request):
#     # Fetch all states and districts to display in the form
#     states = State.objects.all()
#     districts = District.objects.all()

#     if request.method == 'POST':
#         firstName = request.POST.get('firstName')
#         lastName = request.POST.get('lastName')
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         phone = request.POST.get('phone')
#         address = request.POST.get('address')
#         address2 = request.POST.get('address2')
#         state = request.POST.get('state')
#         district = request.POST.get('district')
#         pin = request.POST.get('pin')

#         # Optional checkboxes
#         same_address = request.POST.get('same_address')  # Shipping address same as billing
#         save_info = request.POST.get('save_info')        # Save information for next time

#         shipping_address= Account(firstName=firstName,lastName=lastName,username=username,email=email,phone=phone,address=address,address2=address2,state=state,district=district,pin=pin)

#         # If "Save Info" is checked, save the details in the session
#         if save_info:
#             request.session['firstName'] = firstName
#             request.session['lastName'] = lastName
#             request.session['username'] = username
#             request.session['email'] = email
#             request.session['phone'] = phone
#             request.session['address'] = address
#             request.session['address2'] = address2
#             request.session['state'] = state
#             request.session['district'] = district
#             request.session['pin'] = pin
#             request.session['same_address'] = same_address
#             request.session['save_info'] = save_info

#             shipping_address.save()
            

#         # Handle the "Shipping address is the same as billing address" logic
#         if same_address:
#             request.session['shipping_address'] = address
#         else:
#             request.session['shipping_address'] = address2

#         # Return success or redirect to another page
#         return redirect('index')  # Replace with the actual success page

#     # Render the account page with state and district data
#     return render(request, 'users/account.html', {'states': states, 'districts': districts})



def account(request):
    states = State.objects.all()
    districts = District.objects.all()

    if request.method == 'POST':
        firstName = request.POST.get('firstName')
        lastName = request.POST.get('lastName')
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        address2 = request.POST.get('address2')
        state_id = request.POST.get('state')
        district_id = request.POST.get('district')
        pin = request.POST.get('pin')
        same_address = request.POST.get('same_address')
        save_info = request.POST.get('save_info')

        # Validate required fields
        if not all([firstName, lastName, username, email, phone, address, state_id, district_id, pin]):
            messages.error(request, "All fields are required.")
            return render(request, 'users/account.html', {'states': states, 'districts': districts})

        # Fetch state and district objects
        state = State.objects.get(id=state_id)
        district = District.objects.get(id=district_id)

        # Save account data
        account = Account(
            firstName=firstName,
            lastName=lastName,
            username=username,
            email=email,
            phone=phone,
            address=address,
            address2=address2,
            state=state,
            district=district,
            pin=pin,
        )
        account.save()

        # Save info to session if requested
        if save_info:
            request.session['account_data'] = {
                'firstName': firstName,
                'lastName': lastName,
                'username': username,
                'email': email,
                'phone': phone,
                'address': address,
                'address2': address2,
                'state': state.s_name,
                'district': district.d_name,
                'pin': pin,
                'same_address': same_address,
            }

        # Determine shipping address
        shipping_address = address if same_address else address2
        request.session['shipping_address'] = shipping_address

        messages.success(request, "Account details saved successfully!")
        return redirect('index')

    return render(request, 'users/account.html', {'states': states, 'districts': districts})


# def logout(request):
#     # Clear the session data
#     request.session.clear()
#     return render(request, 'users/logout.html')
def logout(request):
    # Clear the session data
    request.session.clear()
    # Add a success message to inform the user
    messages.success(request, 'You have been logged out successfully.')
    # Redirect to the login page or home page
    return redirect('login')  # Replace 'login' with the name of your login page's URL pattern

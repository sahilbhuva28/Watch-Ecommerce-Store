from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from ecomm_store.models import Product
from .models import *
from ecomm_store.views import *
from .forms import OrderForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from .forms import ProfileForm, UserForm, PasswordChangeForm

@login_required
def cart_detail(request):
    cart = Cart.objects.get(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    categories = Category.objects.all()
    

    subtotal = sum(item.product.price * item.quantity for item in cart_items)
    shipping_charge = 10 if subtotal > 0 else 0
    total = subtotal + shipping_charge

    return render(request, 'cart/cart_detail.html', {
        'cart_items': cart_items,
        'subtotal': subtotal,
        'shipping_charge': shipping_charge,
        'total': total,
        'categories': categories,
    })



@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, product_id=product_id)
    
    # Check if the product is in stock
    if product.stock <= 0:
        # Optionally, you can add a message here to notify the user the product is out of stock
        return redirect('product')  # Redirect to the product page or a different page
    
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    
    if not created:
        cart_item.quantity += 1
    cart_item.save()

    # Redirect back to the page that the user came from (product page)
    return redirect(request.META.get('HTTP_REFERER', 'product'))

@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    cart_item.delete()
    return redirect('cart_detail')

@login_required
def update_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id)
    
    if request.method == 'POST':
        # Get the new quantity from the form
        quantity = int(request.POST.get('quantity', item.quantity))
        
        # Ensure the quantity is within the allowed stock range
        if quantity > item.product.stock:
            quantity = item.product.stock  # Max allowed quantity is the available stock
        
        if quantity <= 0:
            quantity = 1  # Prevent quantity from being zero or negative
        
        item.quantity = quantity
        item.save()

    return redirect('cart_detail')



@login_required
def order_page(request):
    cart = Cart.objects.get(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    subtotal = sum(item.product.price * item.quantity for item in cart_items)
    shipping_charge = 10 if subtotal > 0 else 0
    total = subtotal + shipping_charge

    categories = Category.objects.all()

    # Fetch or create the user's profile
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.total_price = total
            order.save()

            # Save each cart item as an order item
            for item in cart_items:
                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    quantity=item.quantity,
                    price=item.product.price
                )

                # Decrease product stock
                item.product.stock -= item.quantity
                item.product.save()

            # Update the user's profile address
            profile.address = form.cleaned_data['address']
            profile.save()

            # Clear the cart after order placement
            cart_items.delete()

            return redirect('order_success', order_id=order.id)

    else:
        form = OrderForm(initial={
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'email': request.user.email,
            'address': profile.address,  # Auto-fill the address from profile
            'payment_method': 'cod',
            
        })

    return render(request, 'cart/order_page.html', {
        'form': form,
        'subtotal': subtotal,
        'shipping_charge': shipping_charge,
        'total': total,
        'categories': categories,
    })




@login_required
def order_success(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    order_items = OrderItem.objects.filter(order=order)
    categories = Category.objects.all()

    return render(request, 'cart/order_success.html', {
        'order': order,
        'order_items': order_items,
        'categories': categories,
    })


@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    categories = Category.objects.all()

    # Add a calculated total with shipping for each order
    for order in orders:
        order.total_with_shipping = order.total_price + 10

    return render(request, 'cart/order_history.html', {'orders': orders, 'categories': categories})


@login_required
def profile(request):
    user = request.user
    profile, created = Profile.objects.get_or_create(user=user)  # Fetch or create profile
    categories = Category.objects.all()
    
    return render(request, 'cart/profile.html', {
        'user': user,
        'profile': profile,
        'categories': categories,
    })

@login_required
def update_profile(request):
    user = request.user
    profile, created = Profile.objects.get_or_create(user=user)

    categories = Category.objects.all()
   

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        profile_form = ProfileForm(request.POST, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            updated_user = user_form.save(commit=False)
            updated_user.username = updated_user.email  # Sync username with email
            updated_user.save()
            
            profile_form.save()
            return redirect('profile')
    else:
        user_form = UserForm(instance=user)
        profile_form = ProfileForm(instance=profile)

    return render(request, 'cart/update_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form, 
        'categories': categories,
    })

@login_required
def change_password(request):

    categories = Category.objects.all()
    

    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)  # Important to keep the user logged in!
            return redirect('profile')  # Redirect to profile or any page you like
        else:
            print(form.errors)  # Log errors to the console for debugging
    else:
        form = PasswordChangeForm(user=request.user)

    return render(request, 'cart/change_password.html', {'form': form,'categories': categories})
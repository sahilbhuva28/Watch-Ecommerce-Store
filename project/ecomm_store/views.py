from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
from django.contrib.auth.decorators import login_required
from .models import *
from django.shortcuts import render, get_object_or_404
from cart.models import Cart, CartItem
from django.contrib import messages


def index(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    sliders = Slider.objects.all()  # Fetch slider images
    
    return render(request, 'index.html', {'categories': categories,'products': products,'sliders': sliders})


def product(request):
    categories = Category.objects.all()  # Get all categories
    products = Product.objects.all()  # Get all products initially

    # Get the user's cart and the items in it
    cart_items = []
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_items = [item.product for item in CartItem.objects.filter(cart=cart)]

    # Search functionality
    search_query = request.GET.get('search', '')
    if search_query:
        products = products.filter(name__icontains=search_query)  # Filter products by name

    return render(request, 'product.html', {
        'products': products,
        'categories': categories,  # Pass categories for the menu
        'search_query': search_query,  # Pass the search query to keep it in the search bar
        'cart_items': cart_items,  # Pass the cart items to the template
    })
    
    
def about_us(request):
    categories = Category.objects.all()
    return render(request,'about_us.html',{'categories': categories})


def contact_us(request):
    categories = Category.objects.all()
    return render(request,'contact_us.html',{'categories': categories})


def sign_up(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('sign_up')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered.")
            return redirect('sign_up')

        user = User.objects.create_user(
            username=email,
            email=email,
            password=password1,
            first_name=first_name,
            last_name=last_name
        )
        user.save()
        messages.success(request, "Account created successfully. You can now log in.")
        return redirect('login')

    return render(request, 'sign_up.html')



def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)

        if user is not None:
            auth_login(request, user)
            messages.success(request, "Login successful!")
            return redirect('index')
        else:
            messages.error(request, "Invalid email or password.")
            return redirect('login')

    return render(request, 'login.html')





@login_required
def logout_view(request):
    auth_logout(request)  
    request.session.flush()
    return redirect('index')



def category_product(request, category_id):
    category = Category.objects.get(category_id=category_id)
    products = Product.objects.filter(category__category_id=category_id)
    categories = Category.objects.all()

    # Get the user's cart and the items in it
    cart_items = []
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_items = [item.product for item in CartItem.objects.filter(cart=cart)]
    
    return render(request, 'category_product.html', {
        'category': category,
        'products': products,
        'categories': categories,
        'cart_items': cart_items,  # Pass the cart items to the template
    })

def product_detail(request, product_id):
    product = get_object_or_404(Product, product_id=product_id)
    categories = Category.objects.all()
    
    # Get the user's cart and the items in it
    cart_items = []
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_items = [item.product for item in CartItem.objects.filter(cart=cart)]

    return render(request, 'product_detail.html', {
        'product': product,
        'categories': categories,
        'cart_items': cart_items,
    })


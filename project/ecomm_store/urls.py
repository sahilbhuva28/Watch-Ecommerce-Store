from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('home/',views.index,name='index'),
    path('product/',views.product,name='product'),
    path('contact_us/',views.contact_us,name='contact_us'),
    path('about_us/',views.about_us,name='about_us'),
    path('sign_up/',views.sign_up,name='sign_up'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('category/<int:category_id>/', views.category_product, name='category_product'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
]

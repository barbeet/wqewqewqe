from django.contrib import admin
from django.urls import path,include
from users import views as users_view
from .views import *
from django.contrib.auth import views as auth_views

app_name = 'user'

urlpatterns = [ 
    path('register/', users_view.register, name='register'),
    path('profile/', users_view.profile, name='profile'),
    path('profile/basket/', users_view.basket, name='basket'),
    path('profile/confirmation_qr_code/', QrCodePageCheckerView.as_view(), name='confirmation_qr_code'),
    path('profile/curret_orders/', users_view.curret_orders, name='curret_orders'),
    path('profile/curret_history/', users_view.curret_history, name='curret_history'),
    path('profile/new_order/', users_view.new_order, name='new_order'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('login_go/', auth_views.LoginView.as_view(template_name='users/login_ready_register.html'), name='login_ready'),
    path('product/add/<id>/', users_view.basket_add, name='product_add'),
    path('profile/curret_orders/order_delete/', users_view.order_delete, name='order_delete'),
    path('profile/curret_orders/order_repite/', users_view.order_repite, name='order_repite'),
    path('profile/basket/delete/<id>/', users_view.basket_delete, name='service_delete'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),
    path('password-reset-done/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),
]
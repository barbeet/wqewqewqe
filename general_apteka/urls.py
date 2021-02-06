from django.urls import path,include
from .views import *
from .import views 

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('articles/', ArticlesView.as_view(), name='articles'),
    path('about_us/', AboutUsView.as_view(), name='about_us'),
    path('about_us/you_questions/', YouQuestions.as_view(), name='you_questions'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('search_active_substances/', SearchActiveSubstancesPageView.as_view(), name='active_substances'),
    path('product/<product_id>/', views.ProductPageView, name='product_more_info'),
    path('products/', ProductPageAllView.as_view(), name='products'),
    path('discount/', ProductsWithDiscountsView.as_view(), name='products_with_discounts'),
    path('products/filter/<filter>', FilterProductView.as_view(), name='filter'),
    path('qrcodesearch/', QrCodePageCheckerView.as_view(), name='decode'),
    path('selling_prescription_goods/', SellingPrescriptionGoodsView.as_view(), name='selling_prescription_goods'),
    path('test/', TestView.as_view(), name='test'),
    path('ajax/', views.ajax, name='ajax'),
    path('ajax/filter', views.ajax_filter, name='ajax-filter'),
    path('basket_ajax/', views.basket_ajax, name='basket_ajax'),
    path('send_back_call/', views.send_back_call, name='send_back_call'),
]

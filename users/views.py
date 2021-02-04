from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, UserUpdateForm,ProfileUpdateForm, CreateNewOrderForm, Check, UploadFileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from general_apteka.models import Product, BasketProduct, PharmacieAddress, ProductCatalog, ProductCategory
from django.http import HttpResponseRedirect
from .models import Profile, CreateNewOrder, QrCodeSave, PriceDelivery
import datetime
import timeit
from django.http import JsonResponse
from django.views.generic import TemplateView, ListView, View
from .qr_decoder import *
import ast
import time


def get_list_display(request):
    list_display = ('fio_klient', 'adres')
    if request.user.is_superuser:
        return True
    return False


def register(request):
    message = []

    try:
        if request.method == "POST":
            form_user = UserRegistrationForm(request.POST)
            check = Check(request.POST)

            if form_user.is_valid() and check.is_valid():
                form_user.save()
                basket_dow(form_user.cleaned_data.get('username'), request.COOKIES['csrftoken'])
                return redirect('http://aptekaopeka.ru/accounts/login_go/')

        else:
            form_user = UserRegistrationForm()
            check = Check(request.POST)

        return render(request, 'users/register.html', {
            'form_user': form_user,
            'check':check,
            'categorys': ProductCategory.objects.all(),
            'catalogs': ProductCatalog.objects.all(),
            })

    except :

        return render(request, 'eror.html') 


@login_required
def profile(request):
    try:   
        object_inform = objects_inform(request)
        if request.method == "POST":
            form1 = UserUpdateForm(request.POST, instance=request.user)
            form = ProfileUpdateForm(request.POST, instance=request.user.profile)

            if form.is_valid() and form1.is_valid():
                form.save()
                form1.save()

                return redirect('http://aptekaopeka.ru/accounts/profile/')

        else:
            form1 = UserUpdateForm(request.POST, instance=request.user)
            form =  ProfileUpdateForm(request.POST, instance=request.user.profile)

        return render(request, 'users/profile.html', {
            'form': form,
            'is_superuser': get_list_display(request),
            'basket':object_inform['count'],
            'categorys': ProductCategory.objects.all(),
            'catalogs': ProductCatalog.objects.all(),
            })    

    except:

        return render(request, 'eror.html') 



def basket(request):
    user = user_is_anonymous(request)
    message = ''
    object_inform = objects_inform(request)
    try:
        object_inform = objects_inform(request)

        if len(object_inform['objects']) == 0:
            message = 'Ваша корзина пуста'

        return render(request, 'users/profile_basket.html', {
            'objects':object_inform['objects'],
            'count':object_inform['count'],
            'summ':object_inform['summ'],
            'message':message,
            'is_superuser': get_list_display(request),
            'basket':object_inform['count'],
            'categorys': ProductCategory.objects.all(),
            'catalogs': ProductCatalog.objects.all(),
            })

    except:
        return render(request, 'eror.html')


def curret_orders(request):
    object_inform = objects_inform(request)
    message1 = ''
    message2 = ''
    order_in_the_process = CreateNewOrder.objects.all().filter(user = request.user).order_by('-date_add_order').filter(status = 'status_1')
    order_in_the_pending = CreateNewOrder.objects.all().filter(user = request.user).order_by('-date_add_order').filter(status = 'status_2')
    if len(order_in_the_pending) == 0:
        message1 = 'Заказов не найдено'
    if len(order_in_the_process) == 0:
        message2 = 'Заказов не найдено'
    return render(request, 'users/current_orders.html', {
        'order_in_the_process':order_in_the_process,
        'order_in_the_pending':order_in_the_pending,
        'message1':message1,
        'message2':message2,
        'is_superuser': get_list_display(request),
        'categorys': ProductCategory.objects.all(),
        'catalogs': ProductCatalog.objects.all(),
        'basket':object_inform['count']
        })


def curret_history(request, message = ''):
    object_inform = objects_inform(request)
    current_history = CreateNewOrder.objects.all().filter(user = request.user).order_by('-date_add_order').filter(status = 'status_3')
    if len(current_history) == 0:
        message = 'Заказов не найдено'
    return render(request, 'users/current_history.html', {
            'order_in_the_history':current_history,
            'message':message,
            'is_superuser': get_list_display(request),
            'basket':object_inform['count'],
            'categorys': ProductCategory.objects.all(),
            'catalogs': ProductCatalog.objects.all(),
         })



@login_required
def new_order(request, recipe = False):
    delivery = PriceDelivery.objects.all()
    object_inform = objects_inform(request)
    products_recipe_confirmed = []
    products_recipe_notconfirmed = []
    basket  = BasketProduct.objects.all().filter(login = request.user)
    for object in basket:
        remove_basket = BasketProduct.objects.get(id = object.id)
        object_id_inform = Product.objects.get(id = object.product_id)
        
        if object_id_inform.recipe:
            try:
                qr_recipe = QrCodeSave.objects.get(user = request.user, id_product = object_id_inform.id, status = 'status_2', count = remove_basket.count)
                products_recipe_confirmed.append({'product_id':object_id_inform.id, 'product_name':object_id_inform.name, 'product_count':remove_basket.count})
            except:
                products_recipe_notconfirmed.append({'product_id':object_id_inform.id, 'product_name':object_id_inform.name, 'product_count':remove_basket.count})
                recipe = True
                delivery = PriceDelivery.objects.filter(id = 1)

    profile = Profile.objects.get(username = request.user)
    all_pharmacieaddress = PharmacieAddress.objects.all()
    inform = objects_inform(request)

    if len(basket)!= 0:

        if request.method == "POST":

            form = CreateNewOrderForm(request.POST)

            if form.is_valid():
                new_order = CreateNewOrder()
                address = PharmacieAddress.objects.all()
                new_order.user = request.user
                all_in_basket = ' '
                summ = 0
                fio = Profile.objects.get(username = request.user)
    
                new_order.fio = str(fio.username)
                new_order.method_of_obtaining = form.cleaned_data.get('method_of_obtaining')
                delivery_price = PriceDelivery.objects.get(name = new_order.method_of_obtaining)

                new_order.payment_method = form.cleaned_data.get('payment_method')
                new_order.contact = form.cleaned_data.get('contact')
                new_order.address = form.cleaned_data.get('address')
                new_order.status = 'status_1'
            
                if len(address.filter(address = new_order.address)) == 0:
                    return render(request, 'users/new_order.html', {
                    'form': form,
                    'all_pharmacieaddress':all_pharmacieaddress,
                    'inform':inform,
                    'profile':profile,
                    'delivery':delivery,
                    'recipe': recipe,
                    'products_recipe_confirmed':products_recipe_confirmed,
                    'products_recipe_notconfirmed':products_recipe_notconfirmed,
                    'is_superuser': get_list_display(request),
                    'categorys': ProductCategory.objects.all(),
                    'catalogs': ProductCatalog.objects.all(),
                    'basket':object_inform['count']
                    })
                else:
                    all_in_basket_dict = {}
                    for object in basket:
                        remove_basket = BasketProduct.objects.get(id = object.id)
                        object_id_inform = Product.objects.get(id = object.product_id)
                        product_price_inform = product_price(object_id_inform, remove_basket)
                        summ += product_price_inform['count_summ_product']
                        remove_basket.delete()
                        all_in_basket += 'ID:'+str(object.product_id) + ', ' + str(object_id_inform.name) +  ', количество - ' + str(object.count) + ', ' + str(product_price_inform['count_summ_product']) + '₽\n'
                        all_in_basket_dict[object.product_id] = {'count': str(object.count)}
                        try:
                            qr_edit = QrCodeSave.objects.get(id_product = object.product_id, user = request.user, count = object.count, status = 'status_2')
                            qr_edit.status = 'status_4'
                            qr_edit.save()
                        except:
                            pass


                new_order.all_product_id_and_count = all_in_basket
                new_order.all_product_id_and_count_dict = all_in_basket_dict
                new_order.sum_all = summ + int(delivery_price.add_price)

                if new_order.payment_method == 'online':
                    pass

                else:
                    new_order.save()

                    return redirect('http://aptekaopeka.ru/accounts/profile/curret_orders/')

            return render(request, 'users/new_order.html', {
                'form': form,
                'all_pharmacieaddress':all_pharmacieaddress,
                'inform':inform,
                'profile':profile,
                'recipe': recipe,
                'delivery':delivery,
                'products_recipe_confirmed':products_recipe_confirmed,
                'products_recipe_notconfirmed':products_recipe_notconfirmed,
                'is_superuser': get_list_display(request),
                'basket':object_inform['count'],
                'categorys': ProductCategory.objects.all(),
                'catalogs': ProductCatalog.objects.all(),
                })

        else:
            form =  CreateNewOrderForm(request.POST)

            return render(request, 'users/new_order.html', {
            'form': form,
            'all_pharmacieaddress':all_pharmacieaddress,
            'inform':inform,
            'profile':profile,
            'recipe': recipe,
            'delivery':delivery,
            'products_recipe_confirmed':products_recipe_confirmed,
            'products_recipe_notconfirmed':products_recipe_notconfirmed,
            'is_superuser': get_list_display(request),
            'categorys': ProductCategory.objects.all(),
            'catalogs': ProductCatalog.objects.all(),
            'basket':object_inform['count']
            })

    else:
         return redirect('http://aptekaopeka.ru/accounts/profile/basket')   



def basket_add(request,id_product):

        user = user_is_anonymous(request)
        product_add_to_user = BasketProduct()
        person = Product.objects.get(id=id_product)
        check = BasketProduct.objects.all().filter(login = user).filter(product_id = id_product)

        if len(check) != 0:

            if int(check[0].product_id) == int(id_product):
                check2 = BasketProduct.objects.get(id = check[0].id)
                check2.count +=1
                check2.save()
                
                object_inform = objects_inform(request)

                if person.discount != None:
                    pruduct_count_sum = check2.count * person.discount

                else:
                    pruduct_count_sum = check2.count * person.price

                objs = {'id_product':id_product, 'seconds':check2.count, 'summ':111,'count':1111,'summ_product':pruduct_count_sum, 'delete': 'NENADO'}
                
                return objs
 
            else:
                return add(product_add_to_user, id_product, user)
                    
        else:
            return add(product_add_to_user, id_product, user)




def add(check2, id_product, user):
    check2.product_id = id_product
    check2.count = 1
    check2.login = user
    check2.date = datetime.datetime.now()
    check2.save()  

    objs = {'id_product':id_product, 'seconds':check2.count, 'summ':111,'count':1111,'summ_product': 10, 'delete': 'nenado'}
    return objs

def basket_delete(request,id_product, delete=False):
        user = user_is_anonymous(request)       
        basket = BasketProduct.objects.filter(product_id = id_product).filter(login = user)
        edit = BasketProduct.objects.get(id = basket[0].id)
        product = Product.objects.get(id = edit.product_id)
        hai = 'NENADO'

        if edit.count<=1 or delete:
            edit.delete()
            hai = id_product
            count = 0

        else:
            edit.count -=1
            edit.save()
            count = edit.count

        if product.discount != None:
            pruduct_count_sum = edit.count * product.discount

        else:
            pruduct_count_sum = edit.count * product.price

        objs = {'id_product':id_product, 'seconds':count, 'summ':111,'count':1111,'delete':hai,'summ_product': pruduct_count_sum}
        return objs

def objects_inform(request, count = 0, summ = 0):
        objects = []
        user = user_is_anonymous(request)
        objects_user = BasketProduct.objects.all().filter(login = user)

        for object_user in objects_user:
            object_id = Product.objects.get(id = object_user.product_id)
            product_price_inform = product_price(object_id, object_user)
            summ += product_price_inform['count_summ_product']
            count += object_user.count

            objects.append({
                'id_user':object_user.id,
                'id_product': object_id.id,
                'name_product': str(object_id),
                'product_count': product_price_inform['count_product'],
                'product_price':product_price_inform['price_product'],
                'product_thumb': str(object_id.thumb),
                'pruduct_count_sum': product_price_inform['count_summ_product'],
                'product_discount': product_price_inform['discount_product'],
                })
   
        obj = {'summ':summ, 'count': count, 'objects':objects}
        return obj


def user_is_anonymous(request):
    try:
        if str(request.user) != 'AnonymousUser':
            return request.user

        else:
            return request.COOKIES['csrftoken']
    except:
        pass
            
def basket_dow(user, user_hash):
    objects_in_basket = BasketProduct.objects.all().filter(login = user_hash)

    for object in objects_in_basket:
        edit = BasketProduct.objects.get(id = object.id)
        edit.login = user
        edit.save()


def product_price(object, object_user):
    price = 0
    if object.discount != None:
        price = object.discount 
        pruduct_count_sum = object_user.count * object.discount

    else:
        price = object.price
        pruduct_count_sum = object_user.count * object.price

    return {'price_product':object.price,'discount_product':object.discount, 'count_product': object_user.count, 'count_summ_product': pruduct_count_sum, }


class QrCodePageCheckerView(ListView):
    def order_qr_user(self, request):
        order = QrCodeSave.objects.filter(user = request.user)
        order_in_wait = order.filter(status = "status_1")
        order_in_sucess = order.filter(status = "status_2")
        order_in_notsucess = order.filter(status = "status_3")
        if len(order_in_wait) == 0: order_in_wait = None;
        if len(order_in_sucess) == 0: order_in_sucess = None;
        if len(order_in_notsucess) == 0: order_in_notsucess = None;

        return {'order_in_wait':order_in_wait, 'order_in_sucess':order_in_sucess, 'order_in_notsucess':order_in_notsucess}

    def products_recipe_need(self,request):
        sds = [] 
        basket  = BasketProduct.objects.all().filter(login = request.user)
        for object in basket:
            remove_basket = BasketProduct.objects.get(id = object.id)
            object_id_inform = Product.objects.get(id = object.product_id)
            product_inform = product_price(object_id_inform, object)
            if object_id_inform.recipe:
                    sds.append({
                        'name_product': object_id_inform.name,
                        'id_product': object_id_inform.id, 
                        'id_in_basket': object.id, 
                        'product_thumb':object_id_inform.thumb,
                        'product_count':object.count, 
                        'product_count': product_inform['count_product'], 
                        'product_price':product_inform['price_product'],
                        'pruduct_count_sum': product_inform['count_summ_product'],
                        'product_discount': product_inform['discount_product'],
                        'is_superuser': get_list_display(request),
                        'categorys': ProductCategory.objects.all(),
                        'catalogs': ProductCatalog.objects.all(),
                        })

        if len(sds) ==0: sds = None
        return sds

    def get(self, request):
        object_inform = objects_inform(request)
        order_qr_user = self.order_qr_user(request)
        form = UploadFileForm(request.POST, request.FILES)
        return render(request, 'users/confirmation_qr_code.html', {
            'form': form,
            'objects': self.products_recipe_need(request),
            'order_in_wait': order_qr_user['order_in_wait'],
            'order_in_sucess': order_qr_user['order_in_sucess'],
            'order_in_notsucess': order_qr_user['order_in_notsucess'],
            'is_superuser': get_list_display(request),
            'basket':object_inform['count'],
            'categorys': ProductCategory.objects.all(),
            'catalogs': ProductCatalog.objects.all(),
            })

    def post(self, request):
        object_inform = objects_inform(request)
        order_qr_user = self.order_qr_user(request)
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data.get('image')
            id_product = form.cleaned_data.get('id_product')
            count = form.cleaned_data.get('count')
            qr = QrCodeSave()
            qr.status = 'status_1'
            qr.image = image
            qr.user = request.user
            qr.id_product = id_product
            qr.product_name = Product.objects.get(id = id_product)
            qr.count = count
            try:
                qr.qr_value = decoder(request.FILES['image'])
            except:
                qr.qr_value = "QR Code Ошибка в чтении"
            qr.save()

            return redirect('http://aptekaopeka.ru/accounts/profile/confirmation_qr_code/', message = 'hi')

        return render(request, 'users/confirmation_qr_code.html', {
            'form': form,
            'objects': self.products_recipe_need(request),
            'order_in_wait': order_qr_user['order_in_wait'],
            'order_in_sucess': order_qr_user['order_in_sucess'],
            'order_in_notsucess': order_qr_user['order_in_notsucess'],
            'is_superuser': get_list_display(request),
            'basket':object_inform['count'],
            'categorys': ProductCategory.objects.all(),
            'catalogs': ProductCatalog.objects.all(),
            })


def order_delete(request):
    delete = request.GET.get('delete')
    order = CreateNewOrder.objects.get(user = request.user, id = delete)
    product = ast.literal_eval(str(order.all_product_id_and_count_dict))
    for i in product.items():
        try:
            id, count = i
            qr = QrCodeSave.objects.get(id_product = id, count = count['count'], user = request.user)
            qr.status = 'status_2'
            qr.save()
        except:
            print('sd')

    order.delete()
    return JsonResponse({'delete':delete})


def order_repite(request):
    id = request.GET.get('id')
    object = CreateNewOrder.objects.get(id = id)
    object.pk = None
    object.status = 'status_1'
    object.save()
    print(object)
    return JsonResponse({'privet':"privet"})
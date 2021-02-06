from django.db.models import Q
from django.views.generic import TemplateView, ListView, View
from django.shortcuts import render, redirect
from .models import Product, Articles, ProductCatalog, BackCall, BasketProduct, Reviev, ProductDescription, ProductCategory, ScrollBarHome, ScrollBarDiscount
from .forms import RevievAddForm, QuestionForm
from django.http import JsonResponse
import datetime
import timeit, time
from users.views import basket_add, objects_inform, basket_delete,  user_is_anonymous
from rest_framework.response import Response
from rest_framework.views import APIView


class HomePageView(View):
    def get(self,request):
        scroll_bar_home = ScrollBarHome.objects.all()
        objects_list = Product.objects.all().order_by('sales')[:10]
        objects_discount_list = Product.objects.all().exclude(discount = None ).order_by('sales')[:10]
        object_inform = objects_inform(request)
        articles = Articles.objects.all().order_by('watches')[:5]

        return render(request, 'articles/home.html', {
            'objects_list':objects_list,
            'objects_discount_list' :objects_discount_list,
            'basket':object_inform['count'],
            'scroll_bar_home':scroll_bar_home,
            'categorys': ProductCategory.objects.all(),
            'catalogs': ProductCatalog.objects.all(),
            'articles': articles,

            })
class ArticlesView(View):
    def get(self,request):
        articles = Articles.objects.all().order_by('watches')[:5]
        return render(request, 'articles/home.html', {
            'articles':articles,
            'catalogs': ProductCatalog.objects.all(),
            })

class AboutUsView(View):
    def get(self,request):
        object_inform = objects_inform(request)

        return render(request, 'articles/about_us.html', {
            'basket':object_inform['count'],
            'catalogs': ProductCatalog.objects.all(),
            'categorys':ProductCategory.objects.all()
            })


class TestView(View):
    def get(self, request):
        object_inform = objects_inform(request)
        test = request.GET.get('button_text')
        id_product = request.GET.get('button_text')

        return render(request, 'articles/test.html', {
            'basket':object_inform['count'],
            'catalogs': ProductCatalog.objects.all(),
            'categorys':ProductCategory.objects.all(),

            })
        


class SearchResultsView(ListView):
    def get(self,request): 
        query = self.request.GET.get('q').split(':')
        object_inform = objects_inform(request)
        query.reverse()
        filter = ''
   
        if True:
            if len(query) !=1:
                filter = query[1].replace('Поиск ', '')
                if filter == 'Действующие вещества':
                    name_product = str(query[0].replace(' ', '')).replace('Поиск ', '')
                    search = name_product.replace(' ', '').split(',')
                    object_list = Product.objects.all()

                    for active_substance in search:
                        object_list = object_list.filter(active_substances = active_substance)

                else: 
                    name_product = str(query[0].replace(' ', '')).replace('Поиск ', '')
                    object_list = Product.objects.filter(Q(name__iregex=name_product) & Q(category=filter))

                return render(request, 'articles/search_results.html', {
                    'basket':object_inform['count'],
                    'object_list':object_list,
                    'filter': filter,
                    'name_product':name_product,
                    'categorys':ProductCategory.objects.all()
                    })


        object_inform = objects_inform(request)
        name_product = str(query[0].replace(' ', '')).replace('Поиск ', '')
        if filter == 'Все':object_list = Product.objects.filter(name__iregex=name_product); filter = 'Все'
        elif filter == '':object_list = Product.objects.filter(name__iregex=name_product); filter = 'Все'
        else:object_list = Product.objects.filter(Q(name__iregex=name_product) | Q(category=filter))

        return render(request, 'articles/search_results.html', {
            'basket':object_inform['count'],
            'object_list':object_list,
            'count_product': len(object_list),
            'filter': filter,
            'name_product':name_product,
            'basket':object_inform['count'],
            'catalogs': ProductCatalog.objects.all(),
            'categorys':ProductCategory.objects.all()
            })


class ProductPageAllView(View):
    def get(self,request):
        objects_list = Product.objects.all()
        object_inform = objects_inform(request)

        return render(request, 'articles/products.html', {
            'count_product': len(objects_list),
            'objects_list':objects_list,
            'basket':object_inform['count'],
            'catalogs': ProductCatalog.objects.all(),
            'categorys':ProductCategory.objects.all()
            })


def ProductPageView(request,product_id, message = ''):
    if request.method == "POST":
        form = RevievAddForm(request.POST)

        if form.is_valid():
            add_reviev = Reviev()
            add_reviev.id_product = product_id
            add_reviev.login = request.user
            add_reviev.heading_reviev = form.cleaned_data.get('heading_reviev')
            add_reviev.text_reviev = form.cleaned_data.get('text_reviev')
            add_reviev.save()

            return redirect('http://aptekaopeka.ru/product/' + str(product_id) + '/')

    else:
        form = RevievAddForm(request.POST)

    revievs = Reviev.objects.all().filter(id_product = product_id).filter(published = True)
    product = Product.objects.get(id = product_id)
    product_discriptions = ProductDescription.objects.filter(course = product_id)
    product.watches += 1
    product.save()

    objects_list = Product.objects.exclude(id = product.id)

    for active_substance in product.active_substances.replace(' ', '').split(','):
        objects_list = objects_list.filter(Q(active_substances__iregex = active_substance))

    if not len(objects_list):
        message = "<h3>Аналогов не найдено</h3>"
        
    object_inform = objects_inform(request)

    return render(request, 'articles/product_page.html', {
            'form':form,
            'product':product,
            'basket':object_inform['count'],
            'objects_list':objects_list,
            'revievs':revievs,
            'message':message,
            'product_discriptions':product_discriptions,
            'catalogs': ProductCatalog.objects.all(),
            'categorys':ProductCategory.objects.all()
            })


class FilterProductView(View):
    def get(self,request,filter):
        category_name = ProductCategory.objects.get(category = filter)
        objects_list = Product.objects.all().filter(category = category_name.id)
        object_inform = objects_inform(request)

        return render(request, 'articles/products_page_filter.html', {
            'objects_list':objects_list,
            'filter':category_name,
            'basket':object_inform['count'],
            'catalogs': ProductCatalog.objects.all(),
            'categorys':ProductCategory.objects.all(),
            'count_product': len(objects_list),
            })


class QrCodePageCheckerView(ListView):
    def get(self, request):
        form = UploadFileForm()
        categorys = category_product()
        object_inform = objects_inform(request)

        return render(request, 'articles/page_result.html', {
            'form': form,
            'basket':object_inform['count'],
            'catalogs': ProductCatalog.objects.all(),
            'categorys':categorys
            })


    def post(self, request):
        object_inform = objects_inform(request)
        form = UploadFileForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()   

            return redirect('/')

        return render(request, 'articles/page_result.html', {
            'form': form,
            'categorys':categorys,
            'basket':object_inform['count'],
            'catalogs': ProductCatalog.objects.all(),
            })


def ajax(request):
        if request.is_ajax():
            status = ''
            id_product = request.GET.get('button_text')
            user = user_is_anonymous(request)

            basket = BasketProduct.objects.all().filter(login = user)
            basket = len(basket)

            Product.objects.all()
            a = id_product.split(':')
            if a[0] == '-' or a[0] == '-all':
                if a[0]== '-all':
                    object_product = basket_delete(request, a[1],True)
                else:
                    object_product = basket_delete(request, a[1])
                status = 'удалён из козины'

            elif a[0] == '+':
                status = 'добавлен в козину'
                object_product = basket_add(request, a[1])

            message = 'Добавленно в корзину'
            object_inform = objects_inform(request) 
            objs = {'count_product_in_basket': object_inform['count'],'message':message,'id_product': a[1], 'seconds':object_product['seconds'], 'summ':object_inform['summ'], 'summ_product':object_product['summ_product'], 'delete': object_product['delete'], 'status_object':status}
            return JsonResponse(objs)


def ajax_filter(request):
    if request.is_ajax():
        filter = request.GET.get('button_filter')
        search = request.GET.get('search')
        category = request.GET.get('category')
        in_stock = request.GET.get('in_stock')
        with_discount  = request.GET.get('with_discount')
        prescription_only = request.GET.get('prescription_only')
        list_error = ['checkbox1','checkbox2','checkbox3']

        if category == 'Действующие вещества':
            search = search.replace(' ', '').split()
            products = Product.objects.all()

            for active_substance in search:
                products = products.filter(active_substances__iregex = active_substance)     

        else:
            if search != None:
                products = Product.objects.filter(Q(name__iregex=search))

            else:
                products = Product.objects.all()

        for error in list_error:
                if filter == error:
                    filter = False
                    break

        if filter:
            filter = filter.split('oreder_by_')
            filter = filter[1].split('_')

            if filter[1] == '+':
                filter[1] = ''

            products = products.order_by(filter[1] + filter[0])

        if in_stock == 'true':
            products = products.exclude(quantity = 0 )

        if with_discount == 'true':
            products = products.exclude(discount = None )

        if prescription_only == 'true':
            products = products.exclude(recipe = True )

        if category != None:
            if category == 'Действующие вещества':
                pass
            else:
                category_id = ProductCategory.objects.get(category = category)
                products = products.filter(category = category_id.id)

        objs = {}
        i=0   
        for product in products:
            i+=1
            objs[i] = {"id": product.id, "name": product.name, "price": product.price,'discount': product.discount, "company": product.company, 'image': str(product.thumb), 'recipe': product.recipe}

        return JsonResponse(objs)


class SearchActiveSubstancesPageView(View):
    def get(self,request):
        object_inform = objects_inform(request)

        return render(request, 'articles/active_substances.html', {
            'basket':object_inform['count'],
            'categorys':ProductCategory.objects.all(),
            'catalogs': ProductCatalog.objects.all(),
            })


class SellingPrescriptionGoodsView(View):
    def get(self,request):
        object_inform = objects_inform(request)
        return render(request, 'articles/selling_prescription_goods.html', {
            'categorys':ProductCategory.objects.all(),
            'basket':object_inform['count'],
            'catalogs': ProductCatalog.objects.all(),
            })

 
class ProductsWithDiscountsView(View):
    def get(self,request):
        scroll_bar_discount = ScrollBarDiscount.objects.all()
        object_inform = objects_inform(request)
        return render(request, 'articles/products_with_discounts.html', {
            'basket':object_inform['count'],
            'scroll_bar_discount':scroll_bar_discount,
            'categorys': category_product(),
            'objects_list':  Product.objects.all().exclude(discount = None ),
            'catalogs': ProductCatalog.objects.all(),
            })

class ContactsView(View):
    def get(self, request):
        form = QuestionForm(request.POST)
        object_inform = objects_inform(request)
        return render(request, 'articles/contacts_page.html',{
            'basket':object_inform['count'],
            'categorys': category_product(),
            'form':form,
            'catalogs': ProductCatalog.objects.all(),
            })
        
    def post(self, request):
        object_inform = objects_inform(request)
        form = QuestionForm(request.POST)

        if form.is_valid():
            form.save()   

            return redirect('/about_us/you_questions/')

        object_inform = objects_inform(request)
        return render(request, 'articles/contacts_page.html',{
            'basket':object_inform['count'],
            'categorys': category_product(),
            'form':form,
            'catalogs': ProductCatalog.objects.all(),
            })

class YouQuestions(View):
    def get(self, request):
        object_inform = objects_inform(request)
        return render(request, 'articles/you_questions.html',{
            'basket':object_inform['count'],
            'categorys': category_product(),
            'catalogs': ProductCatalog.objects.all(),
            })

def category_product():
    return ProductCategory.objects.all()


def basket_ajax(request):
    if request.is_ajax():
        time.sleep(0.2)
        objects = objects_inform(request)
        if objects['summ'] == 0 and objects['count'] ==0:
            return JsonResponse({'message':'Ваша корзина пуста'})
        return JsonResponse(objects)


def send_back_call(request):
    if request.is_ajax():
        fio = request.GET.get('fio')
        phone = request.GET.get('phone')
        comment = request.GET.get('comment')
        object = BackCall()
        print(fio)
        object.fio = fio
        object.phone = phone
        object.comment = comment
        object.save()
        return JsonResponse({ "ky":'ky'})
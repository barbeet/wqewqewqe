from django.contrib import admin
from .models import Product,BackCall, BasketProduct,ProductCatalog, PharmacieAddress, Reviev, ProductDescription, ProductCategory, Question, ScrollBarHome, ScrollBarDiscount, Articles
#from django_summernote.admin import SummernoteModelAdmin, SummernoteModelAdminMixin


class InLineLesson(admin.TabularInline):
    model = ProductDescription
    extra = 1
    max_num = 100

class ProductAdmin(admin.ModelAdmin):
	inlines = [InLineLesson]
	summernote_fields = '__all__'
	list_display = ("id","name","price","category","count","date_added")
	list_filter = ("date_added","category")

class QuestionAdmin(admin.ModelAdmin):
	list_display = ("id","name","email","text")
	list_filter = ("date_added",)

class PharmacieAddressAdmin(admin.ModelAdmin):	
    list_display = ("id","city","address")

#class ProductDescriptionInline(SummernoteModelAdminMixin, admin.StackedInline):
#    model = ProductDescription
#    extra = 1
#    max_num = 100
#    summernote_fields = ('text', )

#class ProductAdmin(SummernoteModelAdmin):
#    list_display = ("id","name","price","category","count","date_added")
#    list_filter = ("date_added","category")
#    summernote_fields = '__all__'
#    inlines = (ProductDescriptionInline, )

admin.site.register(BackCall)
admin.site.register(ProductCatalog)
admin.site.register(ProductCategory)
admin.site.register(Articles)
admin.site.register(ScrollBarHome)
admin.site.register(ScrollBarDiscount)
admin.site.register(Question,QuestionAdmin)
admin.site.register(ProductDescription)
admin.site.register(Product, ProductAdmin)
admin.site.register(BasketProduct)
admin.site.register(Reviev)
admin.site.register(PharmacieAddress, PharmacieAddressAdmin)
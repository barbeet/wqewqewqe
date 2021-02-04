from django.contrib import admin
from .models import Profile, CreateNewOrder, QrCodeSave, PriceDelivery


class CreateNewOrderAdmin(admin.ModelAdmin):
	search_fields = ('id',)
	list_display = ("id","user","all_product_id_and_count","method_of_obtaining","payment_method","contact","status","sum_all","date_add_order")
	list_filter = ("status","date_add_order","method_of_obtaining","payment_method")
	readonly_fields = ("user","fio", "address" ,"all_product_id_and_count","method_of_obtaining","payment_method","contact","sum_all","date_add_order")


class QrCodeSaveAdmin(admin.ModelAdmin):
	list_display = ("user","status","id_product","product_name","count","date")
	list_filter = ("status","date")
	readonly_fields = ("image","user","qr_value","id_product","product_name","count","date")


class ProfileAdmin(admin.ModelAdmin):
	list_display = ("id",)

admin.site.register(QrCodeSave , QrCodeSaveAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(PriceDelivery)
admin.site.register(CreateNewOrder, CreateNewOrderAdmin)

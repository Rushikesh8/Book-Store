from django.contrib import admin
from store.models import Category
from store.models import Product
from store.models import Order
from store.models import OrderItem
from store.models import Review


admin.site.register(Category)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','stock','available','created','updated']
    list_editable = ['price','stock','available']
    prepopulated_fields = {'slug':('name',)}
    list_per_item = 20

admin.site.register(Product, ProductAdmin)

class OrderItemAdmin(admin.TabularInline):
    model = OrderItem
    fieldsets = [
    ('Product',{'fields':['product'],}),
    ('Quantity',{'fields':['quantity'],}),
    ('Price',{'fields':['price'],}),
    ]
    readonly_fields = ['product','quantity','price']
    can_delete = False
    max_num =0  

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','billingName','emailAddress','created']
    list_display_links = ('id','billingName')
    search_fields = ['id','billingName','emailAddress']
    readonly_fields = ['id','token','total','emailAddress','created',
    'billingName','billingAddress1','billingCity','billingPincode','billingCountry',
    'shippingName','shippingAddress1','shippingCity','shippingPincode','shippingCountry']

    fieldsets = [
        ('ORDER INFORMATION',{'fields':['id','token','total','created']}),
        ('BILLING INFORMATION',{'fields': ['billingName','billingAddress1','billingCity','billingPincode','billingCountry','emailAddress']}),
        ('SHIPPING INFORMATION',{'fields':['shippingName','shippingAddress1','shippingCity','shippingPincode','shippingCountry']}),
    ]

    inlines=[OrderItemAdmin,]

    def has_delete_permission(self,request,obj=None):
        return False

    def has_add_permission(self,request):
        return False    

admin.site.register(Review)
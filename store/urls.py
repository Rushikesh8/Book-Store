from django.urls import path
from store.views import home
from store.views import product_detail
from store.views import cart_detail
from store.views import add_cart
from store.views import cart_remove
from store.views import cart_product_delete
from store.views import thanks_page
from store.views import signupView
from store.views import loginView
from store.views import logoutView
from store.views import orderHistory
from store.views import viewOrder
from store.views import search
from store.views import contact
from store.views import about

urlpatterns = [
    path('', home, name='home'),
    path('category/<slug:category_slug>',home,name='products_by_category'),
    path('category/<slug:category_slug>/<slug:product_slug>', product_detail, name='product_page'),
    path('cart/add/<int:product_id>',add_cart,name='add_cart'),
    path('cart/remove/<int:product_id>',cart_remove,name='cart_remove'),
    path('cart', cart_detail, name='cart_detail'),
    path('cart/product_delete/<int:product_id>',cart_product_delete,name='cart_product_delete'),
    path('thankyou/<int:order_id>',thanks_page, name='thanks_page'),
    path('account/create/',signupView,name='signup'),
    path('account/login/',loginView,name='login'),
    path('account/logout/',logoutView,name='logout'),
    path('order_history/',orderHistory,name='order_history'),
    path('order/<int:order_id>/',viewOrder,name='order_details'),
    path('search/',search,name='search'),
    path('contact/',contact,name='contact'),
    path('about/',about,name='about'),
]
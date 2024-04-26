from django.urls import path
from .views import *

urlpatterns = [

    path('', homepage, name='homepage'),
    path('logout',logout_user,name = "logout"),
    path('login',login_user,name = 'login'),
    path('menu',menu_page,name = 'menu_page'),
    path('signup',signup_page,name = 'signup'),
    path('restaurant',restaurant,name = "restaurant"),
    path('restaurant-menu/<int:id>',restaurant_menu,name = "restaurant_menu"),
    path('userprofile',user_profile,name = "userprofile"),
    path('cart',cart,name = "cart"),
    path('additemtocart/<int:fooditem_id>',add_item_to_cart,name ='add_cart_item'),
    path('removeitemfromcart/<int:fooditem_id>',remove_item_from_cart,name ="remove_cart_item"),
    path('deleteitemfromcart/<int:fooditem_id>',delete_item_from_cart,name = "delete_cart_item"),
    path('ordersuccessful',ordersuccessful,name = "ordersuccessful"),
    path('aboutus',aboutus,name ="aboutus"),
    path('checkout',checkout,name = 'checkout'),
    path('contactus',contactus,name="contactus"),
    path('cuisines',cuisines,name="cuisines"),
    path('aboutus',aboutus,name="aboutus"),

]
# another work login andsign up okok
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
    path('userprofile',user_profile,name = "userprofile")
]

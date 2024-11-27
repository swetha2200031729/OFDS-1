from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('cuisinemanagement',views.cuisinemanagement,name='cuisinemanagement'),
    path('fooditemmanagement',views.fooditemmanagement,name='fooditemmanagement'),
    path('userphonemanagement',views.userphonemanagement,name='userphonemanagement'),
    path('restaurantmanagement',views.restaurantmanagement,name='restaurantmanagement'),
    path('deleterestaurant',views.deleterestaurant,name ="deleterestaurant"),
    path('updaterestaurant/<int:obj_id>/',views.updaterestaurant,name= 'updaterestaurant'),
    path('restaurantadd',views.restaurantadd,name='restaurantadd'),
]
# another work login andsign up okok
#ec2-13-60-23-131.eu-north-1.compute.amazonaws.com
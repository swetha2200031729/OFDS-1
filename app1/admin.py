from django.contrib import admin
from .models import *
#ps: admin username = swetha
#user: sai ps: Swevara@20041184
admin.site.register(FoodItem)
admin.site.register(Restaurant)
admin.site.register(Cuisine)
admin.site.register(UserPhone)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(OrderItem)

# Register your models here.

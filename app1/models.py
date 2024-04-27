from django.contrib.auth.models import User
from django.db import models
class FoodItem(models.Model):
    name = models.CharField(max_length=100,null = False,unique=True)
    description = models.TextField()
    price = models.FloatField()
    vegetarian = models.BooleanField()
    restaurant = models.ForeignKey(to = "Restaurant",on_delete=models.CASCADE,null = True)
    image = models.ImageField(null = True)
    def image_url(self):
        return self.image.url
    def __str__(self):
        return self.name
class Cuisine(models.Model):
    name = models.CharField(max_length=40,unique=True)
    def __str__(self):
        return self.name
class Restaurant(models.Model):
    name = models.CharField(max_length = 100,unique = True)
    address = models.TextField()
    image = models.ImageField(null = True)
    # cuisines = models.ManyToManyField(to = "Cuisine")
    location_url = models.URLField(null = True)
    @property
    def image_url(self):
        return self.image.url
    def __str__(self):
        return self.name

class UserPhone(models.Model):
    user = models.OneToOneField(to = User, on_delete= models.CASCADE)
    phone = models.CharField(max_length=15,unique=True)
    def __str__(self):
        return self.user.username

class CartItem(models.Model):
    fooditem = models.ForeignKey(to = "FoodItem",on_delete=models.CASCADE)
    quantity = models.IntegerField()
    user = models.ForeignKey(to = User ,on_delete=models.CASCADE)
    @property
    def subtotal(self):
        return self.quantity * self.fooditem.price   #if self is the only parameter then u can use it as property

    def __str__(self):
        return f"{self.user.username} {self.fooditem.name}"
    class Meta:
        unique_together = ("fooditem" ,"user")


#https://www.google.com/maps/embed/v1/place?q=place_id:ChIJv58o7br6NToROPPDiCZ-HTU&key=AIzaSyDYuTnqsw7E-uUMYCr4P9AJSnP353TxPLY
'''Model lo

Order

User
Order placed at (datetimefirld)
Name
Contact
Address

Orderitem
Fooditem
Quantity
Order (foreign key)

Subtotal(propertu method)
'''
class Order(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    order_placed_time = models.DateTimeField(blank = True,auto_now_add=True)
    delivary_name = models.CharField(max_length = 100)
    delivary_phone = models.CharField(max_length= 100)
    delivary_address = models.TextField()
    @property
    def get_order_items(self):
        orderitems = OrderItem.objects.filter(order=self)
        return orderitems
    def __str(self):
        return f"{self.user.username} {self.delivay_name}"

class OrderItem(models.Model):
    order = models.ForeignKey(to = "Order", on_delete=models.CASCADE)                      #OrderItem.order.user
    fooditem = models.ForeignKey(to="FoodItem", on_delete=models.CASCADE)
    quantity = models.IntegerField()

    @property
    def subtotal(self):
        return self.quantity * self.fooditem.price  # if self is the only parameter then u can use it as property

    def __str__(self):
        return f"{self.order.id} {self.fooditem.name} {self.order.user}"

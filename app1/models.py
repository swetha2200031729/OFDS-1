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
    cuisines = models.ManyToManyField(to = "Cuisine")
    location_url = models.URLField(null = True)
    def image_url(self):
        return self.image.url
    def __str__(self):
        return self.name


#https://www.google.com/maps/embed/v1/place?q=place_id:ChIJv58o7br6NToROPPDiCZ-HTU&key=AIzaSyDYuTnqsw7E-uUMYCr4P9AJSnP353TxPLY
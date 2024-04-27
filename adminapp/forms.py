from django import forms
from app1.models import *


class Restaurantdetailsform(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = '__all__'


class FoodItemform(forms.ModelForm):
    class Meta:
        model = FoodItem
        fields = '__all__'


class Cuisineform(forms.ModelForm):
    class Meta:
        model = Cuisine
        fields = '__all__'


class UserPhoneform(forms.ModelForm):
    class Meta:
        model = UserPhone
        fields = '__all__'
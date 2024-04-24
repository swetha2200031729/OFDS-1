from django.shortcuts import render, redirect
from django.contrib.auth import *
from .models import *
# Create your views here.
def homepage(request):
    return render(request,'home.html')
def restaurant(request):

    restaurant_name  = request.GET.get("search_text","")
    restaurants = Restaurant.objects.filter(name__icontains = restaurant_name)
    return render(request,"restaurant.html",context = {"restaurant_list":restaurants})

def restaurant_menu(request,id):
    restaurant = Restaurant.objects.get(id = id )
    food_items = FoodItem.objects.filter(restaurant = restaurant)
    search_fooditem = request.GET.get('search_food-item', "")
    vegetarian = request.GET.getlist('vegetarian')
    if len(vegetarian) == 1:
        if vegetarian[0] == "nonveg":
            food_items = food_items.filter(vegetarian=False)

        else:
            food_items = food_items.filter(vegetarian=True)
    food_items = food_items.filter(name__icontains=search_fooditem)
    return render(request,"menu.html",context = {"fooditems" : food_items , "location" : restaurant.location_url})

def menu_page(request):
    search_fooditem = request.GET.get('search_food-item',"")
    vegetarian =  request.GET.getlist('vegetarian')
    if len(vegetarian) == 1:
        if vegetarian[0] == "nonveg":
            fooditem = FoodItem.objects.filter(vegetarian = False)

        else:
            fooditem = FoodItem.objects.filter(vegetarian = True)
    else:
        fooditem = FoodItem.objects.all()
    fooditem = fooditem.filter(name__icontains = search_fooditem)
    itemlist = {"fooditems": fooditem}  # assign them to a dict

    return render(request,'menu.html',itemlist)
def login_user(request):
    if request.user.is_authenticated:
        return redirect("homepage")
    if request.method == "POST":
        username = request.POST.get('nm')
        password = request.POST.get('pwd')
        user = authenticate(request,username = username,password = password )
        if user is not None:
            login(request,user)
            return redirect('homepage')
        else:
            return redirect("login")

    return render(request,'login.html')
def logout_user(request):
    logout(request)
    return redirect("login")
def signup_page(request):
    return render(request,"signup.html")

def user_profile(request):
    return render(request,"userprofile.html")
from django.shortcuts import render, redirect
from django.contrib.auth import *
from .models import *
from django.core.mail import send_mail
from .forms import SubscribeForm
from django.contrib import messages

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
    if request.user.is_authenticated:
        return redirect("homepage")
    if request.method == "POST":
        username = request.POST['username']
        name = request.POST['name']
        password = request.POST['password']
        confirm_password = request.POST['confirmpassword']
        phone_number = request.POST['phone']
        email = request.POST['email']
        address = request.POST['address']


        if confirm_password != password:
            return redirect('signup')

        user = User.objects.create_user( username=username,first_name = name ,email = email, password=password)
        user.save()
        user_phone = UserPhone()
        user_phone.user = user
        user_phone.phone = phone_number
        try:
            user_phone.save()
        except:
            user.delete()
        return redirect('login')
    return render(request,"signup.html")

def user_profile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user_phone = UserPhone.objects.get(user = request.user)
    context = {'phone':user_phone.phone}
    return render(request,"userprofile.html",context)
def cart(request):
    if not request.user.is_authenticated:
        return redirect('login')
    cart_items = CartItem.objects.filter(user = request.user)
    #add of subtotal
    total_value = 0.0
    total_items = 0
    for cart_item in cart_items:
        total_value +=  cart_item.subtotal
        total_items += cart_item.quantity
    context = {"cart_items" : cart_items , "total_value" : total_value ,"total_items" : total_items}
    return render(request,"Cart.html",context)
def add_item_to_cart(request,fooditem_id):
    if not request.user.is_authenticated:
        return redirect('login')
    fooditem = FoodItem.objects.get(id = fooditem_id)# at anycost only one item if lessthan 0 or more its an error
    cart_item = CartItem.objects.filter(fooditem = fooditem,user = request.user).first() # u get a collection and firest value in it
    if cart_item is None:
        cart_item = CartItem()
        cart_item.user = request.user
        cart_item.fooditem = fooditem
        cart_item.quantity = 1
        cart_item.save()
    else:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart')
def remove_item_from_cart(request,fooditem_id):
    if not request.user.is_authenticated:
        return redirect('login')
    fooditem = FoodItem.objects.get(id = fooditem_id)
    cart_items = CartItem.objects.filter(fooditem= fooditem,user = request.user)#for my understanding
    cart_item =cart_items.first()
    if cart_item:
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()
    return redirect('cart')
# feature to be added remove item completly
def delete_item_from_cart(request,fooditem_id):
    if not request.user.is_authenticated:
        return redirect('login')
    fooditem = FoodItem.objects.get(id=fooditem_id)
    cart_items = CartItem.objects.filter(fooditem=fooditem, user=request.user)  # for my understanding
    cart_item = cart_items.first()
    cart_item.delete()
    return redirect('cart')

def ordersuccessful(request):
    return render(request,"ordersuccessful.html")
def aboutus(request):
    return render(request,"About.html")
def checkout(request):
    return render(request,"checkout.html")

def contactus(request):
    form = SubscribeForm()
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            subject = 'issues'
            prob = request.POST.get('problem')
            message = prob
            recipient = form.cleaned_data.get('email')
            send_mail(subject,
                      message, settings.EMAIL_HOST_USER, [recipient], fail_silently=False)
            messages.success(request, 'mail sent successfully')
            return redirect('contactus')
    return render(request, 'contactus.html', {'form': form})


def cuisines(request):
    return render(request,'cuisines.html')
def aboutus(request):
    return render(request,"aboutus.html")





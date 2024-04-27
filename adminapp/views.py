from django.shortcuts import render, get_object_or_404, redirect
from .forms import *
from app1.models import *


def home(request):
    return render(request,'adminappt/home.html')


def restaurantmanagement(request):
    restaurants = Restaurant.objects.all()
    return render(request,'adminappt/restaurantmanagement.html', {'restaurants':restaurants})


def fooditemmanagement(request):
    fooditems = FoodItem.objects.all()
    return render(request,'adminappt/fooditemmanagement.html', {'fooditems':fooditems})


def cuisinemanagement(request):
    Cuisines = Cuisine.objects.all()
    return render(request,'adminappt/cuisinemanagement.html',{'Cuisines':Cuisines})


def userphonemanagement(request):
    UserPhones = UserPhone.objects.all()
    return render(request,'adminappt/userphonemanagement.html', {'UserPhones':UserPhones})


def deleterestaurant(request):
    if request.method == 'POST':
        obj_id = request.POST.get('obj_id')
        obj = get_object_or_404(Restaurant, id=obj_id)
        obj.delete()
        return redirect('restaurantmanagement')  # Redirect to your list view after deletion
    return redirect('restaurantmanagement')


def updaterestaurant(request, obj_id):
    obj = get_object_or_404(Restaurant, id= obj_id)
    if request.method == 'POST':
        form = Restaurantdetailsform(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('restaurantmanagement')  # Redirect to your list view after updating
    else:
        form = Restaurantdetailsform(instance=obj)
    return render(request, 'adminappt/updaterestaurant.html', {'form':form})


def restaurantadd(request):
    if request.method == 'POST':
        form = Restaurantdetailsform(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('restaurantmanagement')
    else:
        form = Restaurantdetailsform()
    return render(request, 'adminappt/restaurantadd.html', {'form':form})



def deleteup(request,obj_id):
    if request.method == 'POST':
        obj_id = request.POST.get('obj_id')
        obj = get_object_or_404(Restaurant, id=obj_id)
        obj.delete()
        return redirect('restaurantmanagement')  # Redirect to your list view after deletion
    return redirect('restaurantmanagement')


def updateup(request, obj_id=id):
    obj = get_object_or_404(Restaurant, id= obj_id)
    if request.method == 'POST':
        form = Restaurantdetailsform(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('restaurantmanagement')  # Redirect to your list view after updating
    else:
        form = Restaurantdetailsform(instance=obj)
    return render(request, 'adminappt/restaurantmanagment.html', {'form':form})


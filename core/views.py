from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate, login
from .models import ShippingLabel


# Create your views here.
def index(request):
    if request.method != 'POST':
        return render(request, 'index.html')
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('home')
    else:
        try:
            user = User.objects.get(username=username)
            messages.info(request,"Username and password didn't match")
            return redirect('index')
        except Exception:
            messages.info(request,'User does not exists !!!')
            return redirect('index')


def register(request):
    if request.method != 'POST':
        return render(request, 'register.html')

    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')

    try:
        user = User.objects.get(username=username)
        messages.info(request,'User with this username already exists !!!')
        return redirect('register')
    except Exception:
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.info(request,'Account created successfully')
    return redirect('index')


def home(request):
    return render(request, 'home.html')


def generate_new_label(request):
    if request.method != 'POST':
        return render(request, 'generate_new_label.html')

    new_label = ShippingLabel(customer_name=request.POST['customer_name'], phone_number=int(request.POST['phone_number']), falt_house_no_building_name=request.POST['flat_house_no_building_name'], street_colony=request.POST['street_colony'], pincode=request.POST['pincode'], city=request.POST['city'], state=request.POST['state'], landmark=request.POST['landmark'])
    new_label.save()

    return redirect('history')


def edit_label(request, id):
    shipping_label = ShippingLabel.objects.get(id=id)
    if request.method != 'POST':
        return render(request, 'edit_label.html', context={'shipping_label':shipping_label})

    shipping_label.customer_name=request.POST['customer_name'] 
    shipping_label.phone_number=int(request.POST['phone_number'])
    shipping_label.falt_house_no_building_name=request.POST['flat_house_no_building_name']
    shipping_label.street_colony=request.POST['street_colony']
    shipping_label.pincode=request.POST['pincode']
    shipping_label.city=request.POST['city']
    shipping_label.state=request.POST['state']
    shipping_label.landmark=request.POST['landmark']
    shipping_label.save()

    return redirect('history')


def delete_label(request, id):
    shipping_label = ShippingLabel.objects.get(id=id)
    shipping_label.delete()
    return redirect('history')


def history(request):
    if request.method != 'POST':
        shipping_labels = ShippingLabel.objects.all().order_by('-updated_at')
        return render(request, 'history.html' , {'shipping_labels':shipping_labels})
    return redirect('history')

def print_label(request, id):
    shipping_label = ShippingLabel.objects.get(id=id)
    return render(request, 'print_template.html', {'shipping_label':shipping_label})


def logout(request):
    auth.logout(request)
    return redirect('/')
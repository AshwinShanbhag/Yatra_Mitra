from http.client import HTTPResponse
from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.core.serializers import serialize
from django.contrib import messages
from .models import RegisteredBusiness,Tour,Business,TourReviews,Profile
from haversine import haversine,Unit
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .forms import UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password

# Create your views here.

def home(request):
    context={'name':"Kishor"}
    return render(request,"base/home.html",context)

def map(request):
    id=request.GET.get('id',1)
    tour=Tour.objects.get(id=id)
    context={'tour':tour}
    return render(request,"base/map.html",context)

def getTour(request,id):
    tour=Tour.objects.get(id=id)
    data=serialize('json',[tour])
    return JsonResponse(data,safe=False)

def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST': 
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        if User.objects.filter(username=username).exists(): 
            messages.add_message(request, messages.INFO, 'Username already exists.')
            return render(request,"base/signup.html")

        elif User.objects.filter(email=email).exists():
            messages.add_message(request, messages.INFO, 'Email already exists.')
            return render(request,"base/signup.html")

        else :
            user = User.objects.create(email=email, username=username, password=make_password(password))
            user.save() 
            auth_login(request, user)    
            messages.add_message(request, messages.INFO, 'You have successfully signed up.')
            return redirect('/')
    else:
        return render(request,"base/signup.html")

def login(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST': 
        login_username=request.POST['usernamel']
        login_password=request.POST['passwordl']
        user = authenticate(request, username = login_username, password = login_password)
        if user is not None:
            auth_login(request, user)
            messages.add_message(request, messages.INFO, 'You have successfully logged in.')
            return redirect('/')
        else:
            messages.add_message(request, messages.INFO, 'Invalid username or password.')
            return render(request,"base/login.html")
    return render(request,"base/login.html")

def recommendations(request):
    if request.method=='POST':
        contents=Tour.objects.all()
        category1= request.POST['category'] #Retrieves the category entered by the user
        category=1  
        if(category1=='Adventure'):
            category=1
        elif(category1=='Trekking'):
            category=2
        elif(category1=='Hiking'):
            category=3
        tourData = Tour.objects.all().filter(category=category).order_by('-rating').values() #Filter by highest rating
        context={
            'tourData':tourData
        }
        return render(request,"base/recommendations.html",context)
    else:
       tourData=Tour.objects.all().order_by('-rating').values()
       context={'tourData':tourData}
       return render(request,"base/recommendations.html",context)

def aboutUs(request):
    context={}
    return render(request,"base/aboutUs.html",context)

def contact(request):
    context={}
    return render(request,"base/contact.html",context)

def tourDetails(request):
    context={}
    return render(request,"base/tourDetails.html",context)

def tourForm(request):
    context={}
    return render(request,"base/tourForm.html",context)

@login_required
def tourReview(request,id):
    tour=Tour.objects.get(id=id)
    if request.method=='POST':
        rating=request.POST.get('rating')
        review=request.POST.get('review')
        if(rating==None): rating=1
        rev=TourReviews(rating=float(rating),review=review,tour=tour)
        rev.save()
        messages.add_message(request, messages.SUCCESS, 'Your Review has been submitted successfully!')
    context={'tour':tour}
    return render(request,"base/tourReview.html",context)

def trip(request):
    context={}
    return render(request,"base/trip.html",context)

def trips(request):
    context={}
    return render(request,"base/trips.html",context)

@login_required
def userProfile(request):
    if request.method == 'POST':
        u_form =UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.add_message(request, messages.SUCCESS, 'Your account has been Updated')
        else:
            messages.add_message(request, messages.ERROR, 'Please correct the error below.')
        return redirect('userProfile')
    else:
        u_form =UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context={
        'u_form':u_form,
        'p_form':p_form
    }
    return render(request, "base/userProfile.html",context)
        
@login_required
def registerBusiness(request):
    if request.method=='POST':
        name=request.POST.get('name')
        address=request.POST.get('address')
        zipcode=request.POST.get('zipcode')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        category=request.POST.get('category')
        website=request.POST.get('website')
        description=request.POST.get('description')
        lat=request.POST.get('latitude')
        lng=request.POST.get('longitude')
        logo=request.FILES.get('logo')
        banner=request.FILES.get('banner')
        business=RegisteredBusiness(name=name,address=address,zipcode=zipcode,phone=phone,email=email,category=category,description=description,lat=lat,lng=lng,logo=logo,banner=banner,website=website)
        business.save()
        messages.add_message(request, messages.SUCCESS, 'Your Business has been registered successfully!')

    return render(request,"base/registerBusiness.html")

# view to get registered business details by id:
def getBusinessDetails(request,id):
    business=RegisteredBusiness.objects.get(id=id)
    return render(request,"base/businessDetails.html",{'business':business})

# method to get nearby restaurants,hotels and repair shops:
@csrf_exempt
def getNearby(request,cat):
    nearby=[]
    body=json.loads(request.body.decode('utf-8'))
    routeCoords=body['routeCoordinates']
    tourCoords=body['tourCoordinates']
    centerCoord=body['center']
    # Calculate radius of center:
    radius=haversine((centerCoord[0],centerCoord[1]),(tourCoords[0][0],tourCoords[0][1]))+50
    query=Business.objects.all().filter(category=cat)

    locFiltered=[loc for loc in query if haversine((loc.lat,loc.lng),(centerCoord[0],centerCoord[1]))<=radius]
    for item in locFiltered:
        for route in routeCoords:
            if haversine((item.lat,item.lng),(route["lat"],route["lng"]),unit=Unit.KILOMETERS)<=3:
                nearby.append(item)
                break
    data=serialize('json',nearby)
    return JsonResponse(data,safe=False)

# method to get recommendations:
@csrf_exempt
def getRecommendations(request,cat):
    body=json.loads(request.body.decode('utf-8'))
    tourCoords=body['tourCoordinates']
    centerCoord=body['center']
    # Calculate radius of center:
    radius=haversine((centerCoord[0],centerCoord[1]),(tourCoords[0][0],tourCoords[0][1]))+10
    query=Business.objects.all().filter(category=cat)

    reco=[loc for loc in query if haversine((loc.lat,loc.lng),(centerCoord[0],centerCoord[1]))<=radius]
    data=serialize('json',reco)
    return JsonResponse(data,safe=False)

# method to get registered business by id
def getBusiness(request,id):
    business=RegisteredBusiness.objects.get(id=id)
    data=serialize('json',[business])
    return JsonResponse(data,safe=False)
    
def logout(request):
    auth_logout(request)
    messages.info(request,'You logged out.')
    return redirect('/')
    


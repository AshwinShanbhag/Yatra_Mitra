from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Tour model:
class Tour(models.Model):
    category_choices=[('1','Hiking'),('2','Trekking'),('3','Adventure')]
    id=models.BigAutoField(primary_key=True)
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=500)
    website=models.CharField(max_length=50,default="www.google.com")
    category=models.CharField(max_length=1,choices=category_choices,default='1')
    rating=models.FloatField(default=5,validators=[MinValueValidator(1),MaxValueValidator(5)])
    # rating_count=
    avg_fare=models.FloatField(default=0)
    address=models.CharField(max_length=700)
    contact=models.CharField(max_length=10)
    hours_open=models.CharField(max_length=100)
    lat=models.DecimalField(max_digits=20,decimal_places=15)
    lng=models.DecimalField(max_digits=20,decimal_places=15)
    createadAt=models.DateTimeField(auto_now_add=True)
    updateAt=models.DateTimeField(auto_now=True)
    image=models.ImageField(upload_to='images/recommendation',null=True)

    def __str__(self):
        return self.name

# Restaurant model:
class Restaurant(models.Model):
    id=models.BigAutoField(primary_key=True)
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=500)
    rating=models.FloatField(default=5,validators=[MinValueValidator(1),MaxValueValidator(5)])
    lat=models.DecimalField(max_digits=20,decimal_places=15)
    lng=models.DecimalField(max_digits=20,decimal_places=15)
    createadAt=models.DateTimeField(auto_now_add=True)
    updateAt=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def __str__(self):
        return self.name

class Profile(models.Model):
    gender_choices=[('1','Male'),('2','Female'),('3','Dont want to specify')]
    id=models.BigAutoField(primary_key=True)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    username= models.CharField(max_length=255)
    email = models.EmailField(blank=True, default="")
    password = models.CharField(max_length=20)
    gender=models.CharField(max_length=1,choices=gender_choices,default='1')
    DOB=models.DateField(blank=True,default="2001-01-01")
    phone = models.CharField(max_length=10)
    country=models.CharField(max_length=200, default="")
    state=models.CharField(max_length=200, default="")
    profile=models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    def __str__(self):
        return self.firstname
        
# Reviews model:
class TourReviews(models.Model):
    id=models.BigAutoField(primary_key=True)
    tour=models.ForeignKey(Tour,on_delete=models.CASCADE)
    # user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    rating=models.IntegerField(default=5,validators=[MinValueValidator(1),MaxValueValidator(5)])
    review=models.CharField(max_length=500)
    createadAt=models.DateTimeField(auto_now_add=True)
    updateAt=models.DateTimeField(auto_now=True)


# Hotel model:
class Hotel(models.Model):
    id=models.BigAutoField(primary_key=True)
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=500)
    website=models.CharField(max_length=50,default="www.google.com")
    rating=models.FloatField(default=5,validators=[MinValueValidator(1),MaxValueValidator(5)])
    lat=models.DecimalField(max_digits=20,decimal_places=15)
    lng=models.DecimalField(max_digits=20,decimal_places=15)
    createadAt=models.DateTimeField(auto_now_add=True)
    updateAt=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
        
# Repair shop model:
class RepairShop(models.Model):
    id=models.BigAutoField(primary_key=True)
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=500)
    rating=models.FloatField(default=5,validators=[MinValueValidator(1),MaxValueValidator(5)])
    lat=models.DecimalField(max_digits=20,decimal_places=15)
    lng=models.DecimalField(max_digits=20,decimal_places=15)
    createadAt=models.DateTimeField(auto_now_add=True)
    updateAt=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# Transport model:
class Transport(models.Model):
    id=models.BigAutoField(primary_key=True)
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=500)
    rating=models.FloatField(default=5,validators=[MinValueValidator(1),MaxValueValidator(5)])
    lat=models.DecimalField(max_digits=20,decimal_places=15)
    lng=models.DecimalField(max_digits=20,decimal_places=15)
    createadAt=models.DateTimeField(auto_now_add=True)
    updateAt=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# Registered Business model:
class RegisteredBusiness(models.Model):
    category_choices=[('1','Restaurant'),('2','Hotel'),('3','Clinic'),('4','Hospital'),('5','Pharmacy'),('6','Repair Shop'),('7','Travel')]
    id=models.BigAutoField(primary_key=True)
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=700)
    description=models.CharField(max_length=500)
    zipcode=models.CharField(max_length=6)
    category=models.CharField(max_length=1,choices=category_choices,default='5')
    phone=models.CharField(max_length=10)
    email=models.EmailField(max_length=100)
    website=models.CharField(max_length=50,null=True)
    rating=models.FloatField(default=5,validators=[MinValueValidator(1),MaxValueValidator(5)],null=True)
    lat=models.DecimalField(max_digits=20,decimal_places=15)
    lng=models.DecimalField(max_digits=20,decimal_places=15)
    logo=models.ImageField(upload_to='images/regBiz',null=True)
    banner=models.ImageField(upload_to='images/regBiz',null=True)
    createadAt=models.DateTimeField(auto_now_add=True)
    updateAt=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def __str__(self):
        return self.name
        
# Repair shop model:
class RepairShop(models.Model):
    id=models.BigAutoField(primary_key=True)
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=500)
    rating=models.FloatField(default=5,validators=[MinValueValidator(1),MaxValueValidator(5)])
    lat=models.DecimalField(max_digits=20,decimal_places=15)
    lng=models.DecimalField(max_digits=20,decimal_places=15)

    def __str__(self):
        return self.name

# Transport model:
class Transport(models.Model):
    id=models.BigAutoField(primary_key=True)
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=500)
    rating=models.FloatField(default=5,validators=[MinValueValidator(1),MaxValueValidator(5)])
    lat=models.DecimalField(max_digits=20,decimal_places=15)
    lng=models.DecimalField(max_digits=20,decimal_places=15)

    def __str__(self):
        return self.name

class DummyLatLng(models.Model):
    lat=models.DecimalField(max_digits=20,decimal_places=15)
    lng=models.DecimalField(max_digits=20,decimal_places=15)

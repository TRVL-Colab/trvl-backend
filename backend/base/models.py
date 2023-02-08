from django.db import models
from django.contrib.auth.models import User
from django.db.models import CharField

# Create your models here.

class Trip(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    depature_date = models.DateField()
    arrival_date = models.DateField()
    depature_place = CharField(max_length=255)
    note = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    createAt = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    flag = models.ImageField(null=True, blank=True, default='/placeholder.png')
    postalCode = models.CharField(max_length=200, null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.name)

class State(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    city_picture = models.ImageField(null=True, blank=True, default='/placeholder.png')
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.name)

class City(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    city_picture = models.ImageField(null=True, blank=True, default='/placeholder.png')
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.name)

class Destination(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    destination_picture = models.ImageField(null=True, blank=True, default='/placeholder.png')
    description = models.TextField(null=True, blank=True)
    trip = models.ForeignKey(Trip, on_delete=models.SET_NULL, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)
    
    def __str__(self):
        return str(self.name)

class Document(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    document_number = models.CharField(max_length=100, blank=True)
    document_type = models.CharField(max_length=200, null=True, blank=True) # Passport Visa Vaccination Card
    place_of_issue = models.CharField(max_length=200, null=True, blank=True)
    date_of_issue = models.CharField(max_length=200, null=True, blank=True)
    date_of_expiration = models.DateField()
    soft_copy = models.CharField(max_length=200, null=True, blank=True)
    trip = models.ForeignKey(Trip, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.name)

class Photo(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    image = models.CharField(max_length=200, null=True, blank=True)
    caption = CharField(max_length=200, null=True, blank=True)
    trip = models.ForeignKey(Trip, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.name)

class Transportation(models.Model):
    mode = models.CharField(max_length=200, null=True, blank=True) # Transportation mode  : Flight Bus Train
    number = models.CharField(max_length=200, null=True, blank=True)
    company = CharField(max_length=200, null=True, blank=True)
    note = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    destination = models.ForeignKey(Destination, on_delete=models.SET_NULL, null=True)
    isPaid = models.BooleanField(default=False)
    paymentMethod = models.CharField(max_length=200, null=True, blank=True)
    paidAt = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.name)
    


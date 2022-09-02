from django.db import models


# Create your models here.


class UserType(models.Model):
    type = models.CharField(max_length=20)


class User(models.Model):
    user_type = models.ForeignKey(UserType, on_delete=models.CASCADE)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=30)
    actual_id = models.IntegerField()


class Photographer(models.Model):
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    age = models.IntegerField()
    country = models.CharField(max_length=20)
    sex = models.CharField(max_length=10)
    bio = models.CharField(max_length=300)
    photo = models.ImageField()


class Customer(models.Model):
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    age = models.IntegerField()
    country = models.CharField(max_length=20)
    sex = models.CharField(max_length=10)
    photo = models.ImageField()


class Portfolio(models.Model):
    photographer = models.ForeignKey(Photographer, on_delete=models.CASCADE)
    caption = models.CharField(max_length=50)
    photo = models.ImageField()


class Photography_Package(models.Model):
    photographer = models.ForeignKey(Photographer, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=400)
    fee = models.IntegerField()


class Order(models.Model):
    photographer = models.ForeignKey(Photographer, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateField()

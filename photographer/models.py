from django.db import models


# Create your models here.


class UserType(models.Model):
    type = models.CharField(max_length=20)

    def __str__(self):
        return self.type

class User(models.Model):
    user_type = models.ForeignKey(UserType, on_delete=models.CASCADE)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=30)
    actual_id = models.IntegerField()

    def __str__(self):
        return self.username

class Photographer(models.Model):
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    age = models.IntegerField()
    address = models.CharField(max_length=200, null=True)
    sex = models.CharField(max_length=10)
    bio = models.CharField(max_length=300)
    photo = models.ImageField(null=True)

    def __str__(self):
        return self.name + " | " + self.phone

class Customer(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=20, null=True)
    age = models.IntegerField()
    address = models.CharField(max_length=200, null=True)
    sex = models.CharField(max_length=10)

    def __str__(self):
        return self.name

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

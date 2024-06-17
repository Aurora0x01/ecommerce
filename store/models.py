from django.db import models
from django.contrib.auth.models import User
import enum

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=False, default='default@example.com')

    def __str__(self):
        return self.name

class Server(models.Model):
    class Region(enum.Enum):
        NA = "North America"
        EUW = "Europe West"
        EUNE = "Europe Nordic & East"
        KR = "Korea"
        BR = "Brazil"

    name = models.CharField(max_length=100)
    server_region = models.CharField(max_length=20, choices=[(tag.name, tag.value) for tag in Region])

    def __str__(self):
        return f"{self.name} - {self.get_server_region_display()}"
class Product(models.Model):
    class Game(models.TextChoices):
        VALORANT = "VALORANT", "Valorant"
        LOL = "LOL", "League of Legends"

    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    value = models.IntegerField()
    digital = models.BooleanField(default=False, null=True, blank=True)
    server = models.ForeignKey(Server, on_delete=models.CASCADE)
    game = models.CharField(max_length=20, choices=Game.choices)
    image = models.ImageField(upload_to='products/', null=True, blank=True)

    def __str__(self):
        return f"{self.get_game_display()} - {self.value} - {self.server.name}"

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except ValueError:
            url = ''
        return url

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for item in orderitems:
            if not item.product.digital:
                shipping = True
                break
        return shipping

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum(item.get_total for item in orderitems)
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum(item.quantity for item in orderitems)
        return total

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    state = models.CharField(max_length=200, null=False)
    zipcode = models.CharField(max_length=200, null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address

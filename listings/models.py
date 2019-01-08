from django.db import models
from datetime import datetime
from realtors.models import Realtor

class Listing(models.Model):
  realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
  title = models.CharField(max_length=200)
  address = models.CharField(max_length=200)
  location = models.CharField(max_length=100)
  state = models.CharField(max_length=100)
  zipcode = models.CharField(max_length=20)
  description = models.TextField(blank=True)
  price = models.IntegerField()
  payment_plan = models.CharField(max_length=200)
  water = models.CharField(max_length=100)
  roads = models.CharField(max_length=100)
  electricity = models.CharField(max_length=100)
  plot_type = models.CharField(max_length=100)
  lot_size = models.CharField(max_length=100)
  sqft = models.IntegerField()
  photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
  item_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  item_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  item_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  item_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  item_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  item_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  is_published = models.BooleanField(default=True)
  list_date = models.DateTimeField(default=datetime.now, blank=True)
  def __str__(self):
    return self.title


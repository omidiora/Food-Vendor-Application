from django.db import models
from django.urls import reverse


# Create your models here.
class  Vendor(models.Model):
  businessName=models.CharField(max_length=200)
  email=models.CharField(max_length=200)

  def __str__(self):
      return self.businessName


class Order(models.Model):
    order=models.ManyToManyField(Vendor , blank=True)
    customerId=models.CharField(max_length=200)
    vendorId=models.CharField(max_length=200)
    description=models.CharField(max_length=200)
    itemsOrdered=models.CharField(max_length=200)
    amountDue=models.CharField(max_length=200)
    amountOutstanding=models.CharField(max_length=200)
    orderStatus=models.BooleanField(default=False)
    menuId=models.CharField(max_length=200)
    dateAndTimeOfOrder=models.CharField(max_length=200)

    def __str__(self):
        return self.customerId


class Menu(models.Model):
    name=models.CharField(max_length=200)
    description=models.CharField(max_length=200)
    price=models.IntegerField()
    quantity=models.IntegerField()
    dateTimeCreated=models.DateTimeField(auto_now_add=True)
    VendorId=models.CharField(max_length=200)
    # isRecurring=models.ForeignKey(Order,on_delete=models.CASCADE,blank=True)
    FrequencyOfReoccurence=models.CharField(max_length=200,blank=True)

    def __str__(self):
        return self.name

    # def  get_absolute_url(self):
    #     return reverse('home', kwargs={'pk': self.pk})


class orderStatus(models.Model):
    name=models.CharField(max_length=200)
    
    



    
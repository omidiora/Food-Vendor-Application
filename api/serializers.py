from rest_framework import serializers
from Vendor.models import Menu



class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model=Menu
        fields=['id','price','description','quantity']

      
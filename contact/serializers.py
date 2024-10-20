from rest_framework import serializers  
from .models import *
  
class ContactFormSerializer(serializers.ModelSerializer):  
  class Meta:  
    model = ContactForm  
    fields = '__all__' 


class CompanyInfoSerializer(serializers.ModelSerializer):  
   class Meta:  
      model = CompanyInfo
      fields = '__all__' 
from django.contrib import admin
from ardapp.models import Contact
from ardapp.models import  Customer
from ardapp.models import User
from ardapp.models import Image
from ardapp.models import Logo 
from ardapp.models import Review

# Register your models here.
admin.site.register(Contact)
admin.site.register(Customer)
admin.site.register(User)
admin.site.register(Image)
admin.site.register(Logo)
admin.site.register(Review)



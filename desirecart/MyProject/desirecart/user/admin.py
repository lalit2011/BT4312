from django.contrib import admin

# Register your models here.
from . models import *

class productAdmin(admin.ModelAdmin):
    list_display = ('id','category','subcategory','name','price','disprice','color','size','description','date','ppic')
admin.site.register(product,productAdmin)

class contactinfoAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','mobno','msg')
admin.site.register(contactinfo,contactinfoAdmin)

class feedbackinfoAdmin(admin.ModelAdmin):
    list_display = ('id','name','img','state','msg')
admin.site.register(feedbackinfo,feedbackinfoAdmin)


class subcategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name','date')
admin.site.register(subcategory,subcategoryAdmin)

admin.site.register(addtocart)

admin.site.register(order)

class signupAdmin(admin.ModelAdmin):
    list_display = ('name','mobile','email','password','cpassword','userpic','address')
admin.site.register(signup,signupAdmin)
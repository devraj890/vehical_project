from django.contrib import admin 
from django.contrib.auth.models import User
from .models import Complaint,feedback
from django.contrib.admin import AdminSite
from django.contrib import admin

admin.site.site_header='VEHICAL THEFT'
admin.site.site_title='VEHICAL THEFT'
admin.site.index_title='VEHICAL THEFT'



class feedbackad(admin.ModelAdmin):
    list_display =('user','description')
JAZZMIN_SETTINGS={"site_title":" vehcal theft"
} 

admin.site.register(Complaint)
admin.site.register(feedback,feedbackad)

from django.contrib import admin
from myprofile.models import Contact

# Register your models here.
admin.site.site_header='MyProfile Admin'
admin.site.site_title='Admin'
admin.site.index_title='Welcome'
admin.site.register(Contact)
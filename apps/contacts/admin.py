from django.contrib import admin

from apps.contacts.models import Contact,Contact_detail
# Register your models here.
admin.site.register(Contact)
admin.site.register(Contact_detail)


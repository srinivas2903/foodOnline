from django.contrib import admin
from vendor.models import Vendor

class VendorAdmin(admin.ModelAdmin):
    list_display=('user','vendor_name','is_approved','created_at')
    list_display_lists=('user','vendor_name')

admin.site.register(Vendor,VendorAdmin)

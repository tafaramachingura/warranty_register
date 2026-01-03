# warranty_api/admin.py
from django.contrib import admin
from .models import Asset

class AssetAdmin(admin.ModelAdmin):
    list_display = ('asset_id','asset_name','registered_by', 'registrant', 'registration_date', 'status')
    search_fields = ('asset_name', 'serial_number', 'registrant')
    list_filter = ('status', 'registration_date', 'warranty_end')

admin.site.register(Asset, AssetAdmin)
class WarrantyAdminSite(admin.AdminSite):
    class Media:
        css={
            'all': ('css/custom_admin.css',)
        }
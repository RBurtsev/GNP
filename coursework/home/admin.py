from django.contrib import admin
from .models import Owners, NotOwners, Ads, Indicators

admin.site.register(Owners)
admin.site.register(NotOwners)
admin.site.register(Ads)
admin.site.register(Indicators)


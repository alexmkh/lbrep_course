from django.contrib import admin
from listings.models import Listing
from listings.models import Poi
from listings.models import Area
from .forms import PoisForm

# Register your models here.


class PoiAdmin(admin.ModelAdmin):
    form = PoisForm


admin.site.register(Listing)
admin.site.register(Poi, PoiAdmin)
admin.site.register(Area)

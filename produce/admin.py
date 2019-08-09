from django.contrib import admin

from .models import Produce, ApplyForm

# Register your models here.
class Produceadmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date')

class ApplyFormadmin(admin.ModelAdmin):
    list_display = ('title', 'upload_date')


admin.site.register(Produce, Produceadmin)
admin.site.register(ApplyForm, ApplyFormadmin)
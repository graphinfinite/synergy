from django.contrib import admin

# Register your models here.
from .models import Occupation
'''

'''
class OccupationAdmin(admin.ModelAdmin):
    list_display = ('name', 'company_name')


admin.site.register(Occupation, OccupationAdmin)

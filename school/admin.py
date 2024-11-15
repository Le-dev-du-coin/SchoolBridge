from django.contrib import admin
from school.models import University


@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    '''Admin View for University'''

    list_display = ("country_code", "country_name", "name", "website")
    #list_filter = ('country_name',)
    readonly_fields = ("country_code", "country_name")
    ordering = ("country_name",)
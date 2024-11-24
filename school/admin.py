from school.models import University, Programs
from django.contrib import admin


class ProgramInline(admin.TabularInline):
    
    model = Programs
    extra = 1

class UniversityAdmin(admin.ModelAdmin):
    '''Admin View for University'''

    list_display = ("country_name", "name", "website")
    list_filter = ('country_name',)
    inlines = [ProgramInline]
    readonly_fields = ("country_code", "country_name")
    ordering = ("country_name",)

admin.site.register(University, UniversityAdmin)
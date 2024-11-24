from .models import Student, Country_wishlist
from django.contrib import admin



class Country_WishlistInline(admin.TabularInline):
    '''Tabular Inline View for Country_Wishlist'''

    model = Country_wishlist
    max_num = 3
    extra = 3
    

class StudentAdmin(admin.ModelAdmin):
    '''Admin View for Student'''

    #list_display = ("user", "")
    inlines = [Country_WishlistInline]


admin.site.register(Student, StudentAdmin)

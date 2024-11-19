from django.contrib import admin
from core.models import User, OnetimePasscode


admin.site.register(User)

@admin.register(OnetimePasscode)
class OnetimePasscodeAdmin(admin.ModelAdmin):
    '''Admin View for OnetimePasscode'''

    list_display = ('user', 'code', 'created_at')
    readonly_fields = ('created_at',)

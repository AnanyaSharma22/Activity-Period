from django.contrib import admin, messages as flash_messages
from app.models import User, ActivityPeriod

# Register your models here.

class CustomUserAdmin(admin.ModelAdmin):
    """
    Custom Admin class for Custom user model
    """

    def __init__(self, *args, **kwargs):
        super(CustomUserAdmin, self).__init__(*args, **kwargs)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {
            'fields': ('name',)}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser',
                                      'is_app_user', 'is_active')}),
    )

    list_display = ['email', 'name', 'is_active']

    search_fields = ['email', 'name']
    
    def save_model(self, request, obj, form, change):
        obj.save()
        if not change:
            password = form.cleaned_data.get('password')
            obj.set_password(password)
            obj.save()
   
admin.site.register(User, CustomUserAdmin)
admin.site.register(ActivityPeriod)
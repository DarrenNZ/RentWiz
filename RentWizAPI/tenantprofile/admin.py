from django.contrib import admin
from .models import Tenant
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from tenantprofile.models import Tenant


# ------ Extension of the User model -------
# reference: https://docs.djangoproject.com/en/2.0/topics/auth/customizing/#extending-the-existing-user-model
# TenantInline class for the User model
# - ensures tenant details appear in the User model in the admin pane
class TenantInline(admin.StackedInline):
    model = Tenant
    can_delete = False
    verbose_name_plural = 'tenant'


# UserAdmin class to include the tenant profile details
class UserAdmin(BaseUserAdmin):
    inlines = (TenantInline,)


# Re-register UserAdmin in order to display tenant/landlord details in-line
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

from django.contrib import admin
from skeletonpages.models import UserProfile
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.contrib.auth.models import User

class UserProfileInline(admin.StackedInline):
  model = UserProfile
  can_delete = False
  verbose_name = "User Profile"
  verbose_name_plural = "Additional User Information"

class UserAdmin(AuthUserAdmin):
  inlines = (UserProfileInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

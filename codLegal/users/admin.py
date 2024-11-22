from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users import models


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        ("Auth info", {"fields": ("email", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name", )}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined", "dob")})
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "usable_password", "password1", "password2"),
            },
        ),
    )
    list_display = ("email", "first_name", "last_name", "is_staff")
    list_filter = ("is_staff", "is_superuser", "is_active", "groups")
    search_fields = ("first_name", "last_name", "email")
    ordering = ("pk",)




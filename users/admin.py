from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from users.models import User, Payments, Prices


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'first_name', 'last_name', 'is_staff']
    list_filter = ['is_staff', 'is_superuser', 'is_active', 'groups']
    search_fields = ['first_name', 'last_name', 'email']
    exclude = ['password']
    filter_horizontal = [
        'groups',
        'user_permissions',
    ]
    save_on_top = True
    fieldsets = (
        (
            _('Personal info'),
            {
                'fields': (
                    'first_name',
                    'last_name',
                    'email',
                    'avatar',
                    'phone',
                    'city',
                )
            }
        ),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                    'groups',
                    'user_permissions',
                ),
            },
        ),
        (
            _('Important dates'),
            {
                'fields': (
                    'last_login',
                    'date_joined',
                )
            }
        ),
    )


@admin.register(Payments)
class PaymentsAdmin(admin.ModelAdmin):
    pass


@admin.register(Prices)
class PricesAdmin(admin.ModelAdmin):
    pass
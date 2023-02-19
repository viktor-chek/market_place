from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.urls import reverse
from django.utils.safestring import mark_safe

from user.models import User


@admin.register(User)
class User(UserAdmin):
    """Админ панель пользователя"""
    list_display = (
        "username", "first_name", "last_name", "email", "link_company")
    search_fields = ("username", "email", "first_name", "last_name")
    readonly_fields = ("last_login", "date_joined")
    fieldsets = (
        (None, {"fields": ("username", "password", "company")}),
        ("Информация о пользователе",
         {"fields": ("first_name", "last_name", "email")}),
        ("Полномочия", {"fields": ("is_active", "is_staff", "is_superuser")}),
        ("Даты", {"fields": ("last_login", "date_joined")}),
    )

    def link_company(self, obj):
        """Ссылка на предприятие пользователя"""
        if obj.company:
            return mark_safe(u"<a href='{0}'>{1}</a>".format(
                reverse('admin:company_company_change',
                        args=(obj.company.id,)),
                obj.company
            ))

    link_company.short_description = 'Компания'

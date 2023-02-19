from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe

from company.models import Product
from company.models import Company


@admin.action(description='Очистить задолженность перед поставщиком')
def cleaning_debt(modeladmin, request, queryset):
    queryset.update(debt=0)


@admin.register(Product)
class Product(admin.ModelAdmin):
    """Админ панель продукта"""
    list_display = ('title', 'model', 'release_date',)
    list_per_page = 10


@admin.register(Company)
class Company(admin.ModelAdmin):
    """Админ панель компании"""
    list_display = (
        'title', 'type_of_company', 'country', 'city', 'link_supplier', 'debt',
    )
    list_per_page = 10
    list_filter = ('city', 'type_of_company',)
    actions = (cleaning_debt,)

    def link_supplier(self, obj):
        """Ссылка на поставщика"""
        if obj.supplier:
            return mark_safe(u"<a href='{0}'>{1}</a>".format(
                reverse('admin:company_company_change',
                        args=(obj.supplier.id,)),
                obj.supplier
            ))

    link_supplier.short_description = 'Поставщик'

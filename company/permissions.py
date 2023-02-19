from rest_framework import permissions


class EmployeesPermission(permissions.BasePermission):
    """Пермишн ограничивает доступ всем за исключением активного персонала"""
    def has_permission(self, request, view):
        return request.user.is_staff

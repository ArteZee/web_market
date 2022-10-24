from rest_framework import permissions

from order.models import OrderModel


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.is_superuser

class UserOwnerPermissions(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        return obj == request.user

class IsUserOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj: OrderModel):
        if obj.user == request.user:
            return True
        return obj.user == request.user.is_superuser
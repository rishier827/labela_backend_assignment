from rest_framework import permissions

class IsStaff(permissions.BasePermission):
    """
    Custom permission to only allow staff to edit or delete a product.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_staff
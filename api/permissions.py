from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminUserOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            (request.user and request.user.is_staff)
        )


class IsUserDataOrAdminUserOrReadOnly(IsAdminUserOrReadOnly):
    def has_object_permission(self, request, view, obj):
        return bool(
            request.method in SAFE_METHODS or
            (request.user and request.user.is_staff) or
            obj == request.user or
            (hasattr(obj, 'user') and obj.user == request.user)
        )

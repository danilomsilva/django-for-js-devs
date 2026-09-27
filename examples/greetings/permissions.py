from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsStaffOrReadOnly(BasePermission):
    """Anyone can read; only staff users can write. Object-level check is the
    same here as view-level since Greeting has no owner field — see
    docs/13-permissions.md for the object-level variant with `has_object_permission`.
    """

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff)

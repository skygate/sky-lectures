from rest_framework.permissions import SAFE_METHODS, IsAuthenticated


class IsAdminOrOwner(IsAuthenticated):
    message = "You must be the owner of this object."

    def has_object_permission(self, request, view, obj):
        return (
            request.method in SAFE_METHODS
            or request.user == obj.user
            or request.user.is_superuser
        )


class IsAdminOrReadOnly(IsAuthenticated):
    message = "You must be admin to delete this."

    def has_object_permission(self, request, view, obj):
        return request.method in SAFE_METHODS or request.user.is_superuser

from rest_framework.permissions import IsAuthenticated, SAFE_METHODS


class IsAdminOrOwner(IsAuthenticated):
    message = "You must be the owner of this object."

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return request.user == obj.user or request.user.is_superuser

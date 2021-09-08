from rest_framework.permissions import SAFE_METHODS, IsAuthenticated


class IsAdminOrOwner(IsAuthenticated):

    message = "You must be an admin or the owner of this resource"

    def has_object_permission(self, request, res):
        return (
            request.method in SAFE_METHODS
            or request.user == res.user
            or request.user.is_superuser
        )


class IsAdminOrReadOnly(IsAuthenticated):
    message = "You must be an admin or owner to do it"
    SAFE_METHODS = ("GET", "HEAD", "OPTIONS", "POST")

    def has_object_permission(self, request):
        return request.method in SAFE_METHODS or request.user.is_superuser
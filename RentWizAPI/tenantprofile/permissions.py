from rest_framework import permissions


# Custom permissions class
# - Extends Django's BasePermission class
# - Allows any user to POST to a view, user must be authenticated to GET
class IsPostOrIsAuthenticated(permissions.BasePermission):
    # Allow tenants to create profiles but not access list API GET endpoint until authenticated
    def has_permission(self, request, view):
        # Allow all POST requests
        if request.method == 'POST':
            return True

        return request.user and request.user.is_authenticated

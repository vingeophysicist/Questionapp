from rest_framework.permissions import IsAdminUser, SAFE_METHODS
from rest_framework import permissions





class IsAdminUserOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Allow all safe methods (GET, HEAD, OPTIONS) for all users
        if request.method in SAFE_METHODS:
            return True

        # Allow write (POST, PUT, PATCH, DELETE) operations for admin users
        return request.user and request.user.is_staff

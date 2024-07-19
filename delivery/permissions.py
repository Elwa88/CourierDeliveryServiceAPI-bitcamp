from rest_framework.permissions import BasePermission, SAFE_METHODS
from .models import CustomUser
from django.shortcuts import get_object_or_404

class ParcelPermissions(BasePermission):
    def has_object_permission(self, request, view, obj):
        user = get_object_or_404(CustomUser, pk = request.user.pk)
        if user.role == "admin":
            return True
        if request.method == "POST":
            return user.role == "customer"
        if request.method in SAFE_METHODS:
            return obj.sender == request.user
        if request.method == "PUT":
            if user.role == "courier" or obj.sender == request.user:
                return True
            
class ProofPermissions(BasePermission):
    def has_object_permission(self, request, view, obj):
        user = get_object_or_404(CustomUser, pk = request.user.pk)
        if user.role == "admin" or user.role == "courier":
            return True

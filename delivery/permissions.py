from rest_framework.permissions import BasePermission

class CustomerPermissions(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == "POST":
             return True
        if request.method in ["PUT","DELETE","GET","PATCH"]:
            return obj.sender == request.user
        
class CourierPermissions(BasePermission):
    def has_permission(self, request, view):
        if request.method  in ["PUT","PATCH","GET"]:
            return True
        
        
class AdminPermissions(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == "admin"
    
class ProofPermissions(BasePermission):
    def has_permission(self, request, view):
        if request.user.role == 'admin':
            return True
        elif request.method == "POST":
            return request.user.role == 'courier'

from rest_framework import permissions
from .models import CustomUser

class UserAccessPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        
        if request.method == 'POST' and view.action == 'create':
            return True
        
        if request.user.is_anonymous:
            return False
            
        if request.user.is_deleted:
            return False
        
        if request.method == 'GET' and view.action == 'list':
            return False
        
        if view.action == 'retrieve':
            try:
                user = CustomUser.objects.get(id=request.user.id)
                if(user):
                    return True
            except:
                return False
        
        if view.action in ['update', 'destroy', 'partial_update']:
            try:
                user = CustomUser.objects.get(id=request.user.id)
                if(user):
                    return True
            except:
                return False
            
        return False

class DeletedUserPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_deleted:
            return False
        return True

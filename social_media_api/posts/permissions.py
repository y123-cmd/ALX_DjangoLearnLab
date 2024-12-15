from rest_framework.permissions import BasePermission

# custom permission
class IsAuthor(BasePermission):
    def has_object_permission(self, request, view, obj):
        
        """
        Return True if permission is granted, False otherwise.

        :param request: The request object
        :param view: The view object
        :param obj: The object to check permission against
        :return: True if permission is granted, False otherwise
        """
        if request.method in ['PUT', 'DELETE', 'PATCH'] and view.action in ['update', 'partial update', 'delete']:
            if request.user == obj.author:
                return True
            else:
                return False
        return True    
             
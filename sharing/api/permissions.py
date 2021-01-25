from django.views import View
from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.request import Request

from sharing.models import ShareableFile


class IsShareableFileOwner(BasePermission):
    message = 'You have got to be the owner of file to perform this action.'

    def has_object_permission(self, request: Request, view: View, obj: ShareableFile) -> bool:
        return request.user.id == obj.user.id


class CanDownloadFile(IsShareableFileOwner):
    message = 'The file you are trying to find does not exist or you have not authenticated.'

    def has_object_permission(self, request: Request, view: View, obj: ShareableFile) -> bool:
        return \
            super(CanDownloadFile, self).has_object_permission(request, view, obj) or \
            obj.public

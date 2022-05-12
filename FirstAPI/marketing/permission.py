from django.http import Http404
from rest_framework import permissions

from hr.models import Employee


class ContractApprovalPermission(permissions.BasePermission):
    message = "Contract Approval add permission deny"

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.user.is_superuser:
                return True
            else:
                return False
#user
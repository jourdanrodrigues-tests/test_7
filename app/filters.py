from rest_framework.filters import BaseFilterBackend


class IsOrderOwner(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        return queryset.filter(customer=request.user)

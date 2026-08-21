from django.urls import path
from .views import (
    RehabCenterListView,
    RehabCenterDetailView,
    TreatmentTypeListView,
    AmenityListView,
    FilterOptionsView,
)

urlpatterns = [
    path('listings/', RehabCenterListView.as_view(), name='listing-list'),
    path('listings/<slug:slug>/', RehabCenterDetailView.as_view(), name='listing-detail'),
    path('treatments/', TreatmentTypeListView.as_view(), name='treatment-list'),
    path('amenities/', AmenityListView.as_view(), name='amenity-list'),
    path('filters/', FilterOptionsView.as_view(), name='filter-options'),
]
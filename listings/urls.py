from django.urls import path
from .views import (
    RehabCenterListView,
    RehabCenterDetailView,
    RehabCenterByIdView,
    TreatmentTypeListView,
    AmenityListView,
    FilterOptionsView,
)


urlpatterns = [
    path('listings/', RehabCenterListView.as_view(), name='listing-list'),
    path('listings/by-id/<int:pk>/', RehabCenterByIdView.as_view(), name='listing-by-id'),
    path('listings/<slug:slug>/', RehabCenterDetailView.as_view(), name='listing-detail'),
    path('treatments/', TreatmentTypeListView.as_view(), name='treatment-list'),
    path('amenities/', AmenityListView.as_view(), name='amenity-list'),
    path('filters/', FilterOptionsView.as_view(), name='filter-options'),
]
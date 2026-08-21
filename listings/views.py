from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Q
from .models import RehabCenter, TreatmentType, Amenity
from .serializers import (
    RehabCenterListSerializer,
    RehabCenterDetailSerializer,
    TreatmentTypeSerializer,
    AmenitySerializer,
)


class RehabCenterListView(generics.ListAPIView):
    serializer_class = RehabCenterListSerializer

    def get_queryset(self):
        queryset = RehabCenter.objects.all()

        # Search
        query = self.request.query_params.get('q')
        if query:
            queryset = queryset.filter(
                Q(name__icontains=query) |
                Q(short_description__icontains=query) |
                Q(city__icontains=query) |
                Q(address__icontains=query)
            )

        # Treatment filter — fixed: outside the if query block
        treatment = self.request.query_params.get('treatment')
        if treatment:
            queryset = queryset.filter(treatment_types__slug=treatment)

        gender = self.request.query_params.get('gender')
        if gender:
            queryset = queryset.filter(gender=gender)

        price = self.request.query_params.get('price')
        if price:
            queryset = queryset.filter(price_range=price)

        category = self.request.query_params.get('category')
        if category:
            queryset = queryset.filter(category=category)

        surrounding = self.request.query_params.get('surrounding')
        if surrounding:
            queryset = queryset.filter(surrounding=surrounding)

        insurance = self.request.query_params.get('insurance')
        if insurance == 'true':
            queryset = queryset.filter(insurance_accepted=True)

        featured = self.request.query_params.get('featured')
        if featured == 'true':
            queryset = queryset.filter(featured=True)

        return queryset.distinct()


class RehabCenterDetailView(generics.RetrieveAPIView):
    serializer_class = RehabCenterDetailSerializer
    queryset = RehabCenter.objects.all()
    lookup_field = 'slug'


class TreatmentTypeListView(generics.ListAPIView):
    serializer_class = TreatmentTypeSerializer
    queryset = TreatmentType.objects.all()


class AmenityListView(generics.ListAPIView):
    serializer_class = AmenitySerializer
    queryset = Amenity.objects.all()


class FilterOptionsView(APIView):
    """
    GET /api/filters/
    Returns all available filter options that have at least one listing.
    Frontend uses this to show/hide filters dynamically.
    """
    permission_classes = []

    def get(self, request):
        # Treatments that have at least one center
        treatments = list(
            TreatmentType.objects.filter(centers__isnull=False)
            .distinct()
            .values('id', 'name', 'slug', 'category')
        )

        # Cities
        cities = list(
            RehabCenter.objects.exclude(city='')
            .values_list('city', flat=True)
            .distinct()
            .order_by('city')
        )

        # Surroundings
        surroundings = list(
            RehabCenter.objects.exclude(surrounding='')
            .values_list('surrounding', flat=True)
            .distinct()
        )

        # Genders
        genders = list(
            RehabCenter.objects.exclude(gender='')
            .values_list('gender', flat=True)
            .distinct()
        )

        # Price ranges
        price_ranges = list(
            RehabCenter.objects.exclude(price_range='')
            .values_list('price_range', flat=True)
            .distinct()
        )

        # Categories
        categories = list(
            RehabCenter.objects.exclude(category='')
            .values_list('category', flat=True)
            .distinct()
        )

        # Languages — flatten JSONField list
        languages_qs = RehabCenter.objects.exclude(languages=[]).values_list('languages', flat=True)
        all_languages = list(set(
            lang for langs in languages_qs for lang in (langs or [])
        ))

        # Patient profiles — flatten JSONField list
        profiles_qs = RehabCenter.objects.exclude(patient_profiles=[]).values_list('patient_profiles', flat=True)
        all_profiles = list(set(
            p for profiles in profiles_qs for p in (profiles or [])
        ))

        return Response({
            'treatments': treatments,
            'cities': cities,
            'surroundings': surroundings,
            'genders': genders,
            'price_ranges': price_ranges,
            'categories': categories,
            'languages': all_languages,
            'patient_profiles': all_profiles,
        })
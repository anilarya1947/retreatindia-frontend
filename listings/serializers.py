from rest_framework import serializers
from .models import RehabCenter, TreatmentType, Amenity, RehabCenterPhoto, RehabCenterTeamMember, RehabCenterAboutSection


class TreatmentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TreatmentType
        fields = ['id', 'name', 'slug', 'category']


class AmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenity
        fields = ['id', 'name', 'slug']


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RehabCenterPhoto
        fields = ['id', 'image', 'alt', 'order']


class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = RehabCenterTeamMember
        fields = ['id', 'name', 'role', 'qualification', 'photo', 'order']


class AboutSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RehabCenterAboutSection
        fields = ['id', 'title', 'description', 'image', 'order']


class RehabCenterListSerializer(serializers.ModelSerializer):
    treatment_types = TreatmentTypeSerializer(many=True, read_only=True)
    photos = PhotoSerializer(many=True, read_only=True)
    price_range_display = serializers.CharField(source='get_price_range_display', read_only=True)

    class Meta:
        model = RehabCenter
        fields = [
            'id', 'name', 'slug', 'short_description',
            'city', 'address', 'phone', 'whatsapp',
            'gender', 'price_range', 'price_range_display','insurance_accepted',
            'featured', 'verified',
            'treatment_types', 'photos',
        ]


class RehabCenterDetailSerializer(serializers.ModelSerializer):
    treatment_types = TreatmentTypeSerializer(many=True, read_only=True)
    amenities = AmenitySerializer(many=True, read_only=True)
    photos = PhotoSerializer(many=True, read_only=True)
    team_members = TeamMemberSerializer(many=True, read_only=True)
    about_sections = AboutSectionSerializer(many=True, read_only=True)

    class Meta:
        model = RehabCenter
        fields = [
            'id', 'name', 'slug', 'short_description', 'description',
            'address', 'city', 'state', 'pincode',
            'google_maps_url', 'lat', 'lng',
            'phone', 'email', 'website', 'whatsapp',
            'gender', 'price_range', 'category', 'surrounding',
            'insurance_accepted', 'patient_profiles', 'languages',
            'featured', 'verified',
            # highlights
            'experience_years', 'min_program_duration', 'total_rooms', 'total_beds',
            # facilities
            'in_room_facilities', 'center_facilities', 'recreational_activities',
            'therapies', 'videos',
            # seo
            'seo_title', 'seo_description',
            # relations
            'treatment_types', 'amenities', 'photos', 'team_members', 'about_sections',
            'created_at', 'updated_at',
        ]
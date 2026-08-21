from django.contrib import admin
from .models import RehabCenter, TreatmentType, Amenity, RehabCenterPhoto, RehabCenterTeamMember, RehabCenterAboutSection


class PhotoInline(admin.TabularInline):
    model = RehabCenterPhoto
    extra = 1


class TeamMemberInline(admin.TabularInline):
    model = RehabCenterTeamMember
    extra = 1


class AboutSectionInline(admin.TabularInline):
    model = RehabCenterAboutSection
    extra = 1


@admin.register(RehabCenter)
class RehabCenterAdmin(admin.ModelAdmin):
    list_display = ['name', 'city', 'featured', 'verified', 'created_at']
    list_filter = ['featured', 'verified', 'gender', 'price_range', 'category']
    search_fields = ['name', 'city', 'address']
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ['featured', 'verified']
    inlines = [PhotoInline, TeamMemberInline, AboutSectionInline]

    fieldsets = (
        ('Basic Info', {
            'fields': ('name', 'slug', 'short_description', 'description')
        }),
        ('Location', {
            'fields': ('address', 'city', 'state', 'pincode', 'google_maps_url', 'lat', 'lng')
        }),
        ('Contact', {
            'fields': ('phone', 'email', 'website', 'whatsapp')
        }),
        ('Filters', {
            'fields': ('treatment_types', 'amenities', 'gender', 'price_range', 'category', 'surrounding', 'insurance_accepted', 'patient_profiles', 'languages')
        }),
        ('Center Highlights', {
            'fields': ('experience_years', 'min_program_duration', 'total_rooms', 'total_beds')
        }),
        ('Facilities', {
            'fields': ('in_room_facilities', 'center_facilities', 'recreational_activities', 'therapies'),
            'description': 'Enter as JSON lists e.g. ["Air Conditioning", "Smart TV"]'
        }),
        ('Videos', {
            'fields': ('videos',),
            'description': 'Enter as JSON list of video URLs'
        }),
        ('Status', {
            'fields': ('featured', 'verified')
        }),
        ('SEO', {
            'fields': ('seo_title', 'seo_description'),
            'classes': ('collapse',)
        }),
    )


@admin.register(TreatmentType)
class TreatmentTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'category']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
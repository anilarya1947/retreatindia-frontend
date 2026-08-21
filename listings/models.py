from django.db import models


class TreatmentType(models.Model):
    CATEGORY_CHOICES = [
        ('adults', 'Adults'),
        ('child', 'Child & Adolescents'),
        ('geriatric', 'Geriatric (Elderly)'),
        ('others', 'Others'),
    ]
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='adults')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['category', 'name']


class Amenity(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Amenities'


class RehabCenter(models.Model):

    GENDER_CHOICES = [
        ('men', 'Men'), ('women', 'Women'), ('both', 'Men and Women'),
    ]
    PRICE_CHOICES = [
        ('lt2', 'Less than 2 Lakhs'), ('2to3', '2-3 Lakhs'),
        ('3to4', '3-4 Lakhs'), ('4to5', '4-5 Lakhs'), ('gt5', '5+ Lakhs'),
    ]
    CATEGORY_CHOICES = [
        ('luxury-wellness', 'Luxury Wellness Retreat'),
        ('luxury-clinical', 'Luxury Clinical Rehab'),
        ('budget-clinical', 'Budget Clinical Rehab'),
    ]
    SURROUNDING_CHOICES = [
        ('mountains', 'Mountains'), ('beach', 'Beach'), ('farm', 'Farm/Garden'),
        ('forest', 'Forest'), ('city', 'City'), ('lake', 'Lake/Riverside'),
    ]
    LANGUAGE_CHOICES = [
        ('english', 'English'), ('hindi', 'Hindi'), ('tamil', 'Tamil'),
        ('malayalam', 'Malayalam'), ('gujarati', 'Gujarati'), ('bengali', 'Bengali'),
        ('marathi', 'Marathi'), ('telugu', 'Telugu'), ('kannada', 'Kannada'),
        ('odia', 'Odia'), ('punjabi', 'Punjabi'),
    ]
    PATIENT_PROFILE_CHOICES = [
        ('men', 'Men'), ('women', 'Women'), ('both', 'Men and Women'),
        ('professionals', 'Professionals'), ('adolescents', 'Adolescents'),
        ('young-adults', 'Young Adults'), ('midlife', 'Midlife Adults'),
        ('executives', 'Executives'), ('lgbtqia', 'LGBTQIA+'),
        ('boys', 'Boys'), ('girls', 'Girls'), ('couples', 'Couples'),
        ('older-adults', 'Older Adults'), ('pregnant', 'Pregnant Women'),
    ]

    # Basic
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    short_description = models.TextField(max_length=300, blank=True)
    description = models.TextField(blank=True)

    # Location
    address = models.TextField()
    city = models.CharField(max_length=100, default='New Delhi')
    state = models.CharField(max_length=100, default='Delhi')
    pincode = models.CharField(max_length=10, blank=True)
    google_maps_url = models.URLField(blank=True)
    lat = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    lng = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    # Contact
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    website = models.URLField(blank=True)
    whatsapp = models.CharField(max_length=20, blank=True)

    # Filters
    treatment_types = models.ManyToManyField(TreatmentType, blank=True, related_name='centers')
    amenities = models.ManyToManyField(Amenity, blank=True, related_name='centers')
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='both')
    price_range = models.CharField(max_length=10, choices=PRICE_CHOICES, blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, blank=True)
    surrounding = models.CharField(max_length=20, choices=SURROUNDING_CHOICES, blank=True)
    insurance_accepted = models.BooleanField(default=False)
    patient_profiles = models.JSONField(default=list, blank=True)
    languages = models.JSONField(default=list, blank=True)

    # ── NEW FIELDS ──

    # Center highlights
    experience_years = models.PositiveIntegerField(null=True, blank=True, help_text='e.g. 15')
    min_program_duration = models.CharField(max_length=50, blank=True, help_text='e.g. 14 Days')
    total_rooms = models.PositiveIntegerField(null=True, blank=True)
    total_beds = models.PositiveIntegerField(null=True, blank=True)

    # Facilities — stored as JSON lists
    in_room_facilities = models.JSONField(default=list, blank=True)
    center_facilities = models.JSONField(default=list, blank=True)
    recreational_activities = models.JSONField(default=list, blank=True)
    therapies = models.JSONField(default=list, blank=True)

    # Videos — list of YouTube/video URLs
    videos = models.JSONField(default=list, blank=True, help_text='List of video URLs or YouTube embed URLs')

    # Status
    featured = models.BooleanField(default=False)
    verified = models.BooleanField(default=False)

    # SEO
    seo_title = models.CharField(max_length=255, blank=True)
    seo_description = models.TextField(max_length=300, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-featured', '-created_at']

    def __str__(self):
        return self.name


class RehabCenterPhoto(models.Model):
    center = models.ForeignKey(RehabCenter, related_name='photos', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='centers/')
    alt = models.CharField(max_length=255, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"Photo for {self.center.name}"


class RehabCenterTeamMember(models.Model):
    """Doctors and care team members for a center"""
    center = models.ForeignKey(RehabCenter, related_name='team_members', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255, help_text='e.g. Sr. Psychiatrist & Co-Founder')
    qualification = models.CharField(max_length=255, blank=True, help_text='e.g. M.B.B.S, MD')
    photo = models.ImageField(upload_to='team/', null=True, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.name} — {self.center.name}"


class RehabCenterAboutSection(models.Model):
    """'More about Center' cards — 3 image + title + text blocks"""
    center = models.ForeignKey(RehabCenter, related_name='about_sections', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='about/', null=True, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.title} — {self.center.name}"
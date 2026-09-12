from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator


# ── Lookup tables ──

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


# ── Choices ──

CENTRE_TYPE_CHOICES = [
    ('luxury-wellness', 'Luxury Wellness Center'),
    ('clinical-rehab', 'Clinical Rehab'),
    ('wellness-clinical', 'Wellness Center & Clinical Rehab'),
]

PRICE_CHOICES = [
    ('lt2', 'Less than 2 Lakhs'),
    ('2to3', '2-3 Lakhs'),
    ('3to4', '3-4 Lakhs'),
    ('4to5', '4-5 Lakhs'),
    ('gt5', '5+ Lakhs'),
]

SURROUNDING_CHOICES = [
    ('mountains', 'Mountains'),
    ('beach', 'Beach'),
    ('farm', 'Farm/Garden'),
    ('forest', 'Forest'),
    ('city', 'City'),
    ('lake', 'Lake/Riverside'),
]

TREATMENT_CHOICES = [
    ('alcohol-addiction', 'Alcohol Addiction'),
    ('drug-addiction', 'Drug Addiction'),
    ('prescription-drug', 'Prescription Drug Dependency'),
    ('smoking-tobacco', 'Smoking/Tobacco Addiction'),
    ('depression', 'Depression'),
    ('anxiety-disorders', 'Anxiety Disorders'),
    ('bipolar-disorder', 'Bipolar Disorder'),
    ('ptsd', 'PTSD'),
    ('schizophrenia', 'Schizophrenia'),
    ('severe-stress', 'Severe Stress or Burnout'),
    ('ocd', 'OCD'),
    ('sex-addiction', 'Sex Addiction'),
    ('pornography-addiction', 'Pornography Addiction'),
    ('adhd', 'ADHD'),
    ('autism', 'Autism Spectrum Disorders'),
    ('behavioral-issues', 'Behavioral Issues'),
    ('learning-disabilities', 'Learning Disabilities'),
    ('teen-substance', 'Teen Substance Abuse'),
    ('dementia', "Dementia / Alzheimer's"),
    ('post-stroke', 'Post-Stroke Recovery'),
    ('mobility-loss', 'Mobility Loss'),
    ('chronic-illnesses', 'Chronic Illnesses'),
    ('internet-gaming', 'Internet & Gaming Addiction'),
    ('porn-addiction', 'Porn Addiction'),
    ('eating-disorders', 'Eating Disorders'),
    ('luxury-wellness-rehab', 'Luxury Wellness Rehab'),
    ('corporate-burnout', 'Corporate Burnout Programs'),
    ('suicidality', 'Suicidality/Self Harm'),
]

PATIENT_PROFILE_CHOICES = [
    ('men', 'Men'),
    ('women', 'Women'),
    ('children', 'Children'),
    ('teens', 'Teens & Adolescents'),
    ('old-age', 'Old Age People'),
    ('couples', 'Couples'),
    ('families', 'Families'),
    ('professionals', 'Working Professionals'),
    ('executives', 'Executives'),
    ('lgbtq', 'LGBTQ+ Individuals'),
    ('pregnant', 'Pregnant Women'),
]

MAIN_FACILITIES_CHOICES = [
    ('cell-phones', 'Allows Cell Phones'),
    ('private-rooms', 'Private Rooms'),
    ('shared-rooms', 'Shared Rooms'),
    ('pet-friendly', 'Pet Friendly'),
    ('swimming-pool', 'Swimming Pool'),
    ('wellness', 'Wellness'),
    ('fitness-center', 'Fitness Center'),
    ('outdoor-lounge', 'Outdoor Lounge'),
    ('nature-access', 'Access to Nature'),
    ('lawn-garden', 'Lawn/Garden'),
]

IN_ROOM_FACILITIES_CHOICES = [
    ('ac', 'Air Conditioning'),
    ('air-purifier', 'Air Purifier'),
    ('geyser', 'Geyser'),
    ('writing-desk', 'Writing Desk & Chair'),
    ('coffee-tea', 'Coffee/Tea Maker'),
    ('refrigerator', 'Refrigerator'),
    ('smart-tv', 'Smart TV'),
    ('reading-lamp', 'Reading Lamp'),
    ('bottled-water', 'Bottled Water'),
    ('bathrobes', 'Bathrobes'),
    ('shower', 'Shower'),
    ('toiletries', 'Complimentary Toiletries'),
    ('wake-up-call', 'Wake-up Call'),
]

CENTER_FACILITIES_CHOICES = [
    ('24-7-medical', '24/7 Medical Supervision'),
    ('psychiatrists', 'In-house Psychiatrists & Psychologists'),
    ('nursing-staff', 'Nursing Staff'),
    ('diagnostic-room', 'Diagnostic & Assessment Room'),
    ('therapy-room', 'Therapy Room'),
    ('family-counseling', 'Family Counseling Room'),
    ('group-therapy', 'Group Therapy Hall'),
    ('yoga-meditation', 'Yoga & Meditation Hall'),
    ('spa-massage', 'Spa & Massage'),
    ('landscaped-garden', 'Landscaped Garden'),
    ('sit-out-areas', 'Sit-out Areas'),
    ('kitchen', 'In-house Kitchen'),
    ('dining-hall', 'Dining Hall'),
    ('cctv', 'CCTV Surveillance'),
    ('controlled-entry', 'Controlled Entry/Exit Points'),
    ('24-security', '24-hour Security'),
    ('fire-safety', 'Fire Safety Systems'),
    ('reception', 'Reception & Waiting Lounge'),
    ('conference-room', 'Conference Room'),
    ('fax', 'Fax/Photocopying'),
    ('housekeeping', 'Daily Housekeeping'),
    ('laundry', 'Laundry & Ironing Service (Paid)'),
    ('dry-cleaning', 'Dry Cleaning (Paid)'),
    ('room-service', 'Room Service'),
    ('wifi', 'Free Internet/Wi-Fi'),
    ('video-call', 'Video Call Facilities'),
    ('wheelchair', 'Wheelchair Accessibility'),
    ('parking', 'Inhouse Parking'),
]

ACTIVITIES_CHOICES = [
    ('gym', 'Fitness Center/Gym'),
    ('badminton', 'Badminton'),
    ('table-tennis', 'Table Tennis'),
    ('swimming', 'Swimming Pool'),
    ('billiards', 'Billiards Table'),
    ('board-games', 'Board Games'),
    ('walking-track', 'Walking Track'),
    ('aerobics', 'Aerobics & Zumba'),
    ('art-therapy', 'Art Therapy'),
    ('craft', 'Craft Work'),
    ('music-therapy', 'Music Therapy'),
    ('gardening', 'Gardening & Farming Activities'),
    ('dance', 'Dance & Movement Therapy'),
    ('sound-healing', 'Sound Healing'),
    ('puzzles', 'Puzzle Solving / Brain Games'),
    ('talent-shows', 'Talent Shows'),
    ('celebration', 'Celebration Events'),
    ('movie-nights', 'Movie Nights'),
    ('documentaries', 'Documentary Screenings'),
    ('karaoke', 'Karaoke Sessions'),
]

LANGUAGE_CHOICES = [
    ('english', 'English'),
    ('hindi', 'Hindi'),
    ('tamil', 'Tamil'),
    ('malayalam', 'Malayalam'),
    ('gujarati', 'Gujarati'),
    ('bengali', 'Bengali'),
    ('marathi', 'Marathi'),
    ('telugu', 'Telugu'),
    ('kannada', 'Kannada'),
    ('odia', 'Odia'),
    ('punjabi', 'Punjabi'),
]


class RehabCenter(models.Model):

    # ── Basic Info ──
    name = models.CharField(max_length=255, verbose_name='Name of the Centre')
    slug = models.SlugField(unique=True)
    mobile = models.CharField(max_length=20, blank=True, default='', verbose_name='Mobile No')
    mobile_alternate = models.CharField(max_length=20, blank=True, verbose_name='Mobile No (Alternate)')
    email = models.EmailField(blank=True, verbose_name='E-mail ID')
    district = models.CharField(max_length=100, blank=True, default='', verbose_name='District Name')
    state = models.CharField(max_length=100, verbose_name='State Name')
    address = models.TextField(verbose_name='Complete Address')
    city = models.CharField(max_length=100, default='New Delhi')

    # ── Centre Type ──
    centre_type = models.CharField(max_length=50, default='general')  # pick an appropriate default

    # ── Certification ──
    certified_from = models.CharField(max_length=255, blank=True, verbose_name='Certified From (Optional)')

    # ── About ──
    about = models.TextField(
    verbose_name='About (300-600 words)',
    validators=[MinLengthValidator(300)],
    help_text='Minimum 300 words, Maximum 600 words',
    blank=True,
    default=''
    )
    short_description = models.TextField(max_length=300, blank=True)

    # ── Details ──
    experience_years = models.PositiveIntegerField(null=True, blank=True, verbose_name='Experience (Years)')
    program_duration_min = models.PositiveIntegerField(null=True, blank=True, verbose_name='Program Duration Min (days)')
    program_duration_max = models.PositiveIntegerField(null=True, blank=True, verbose_name='Program Duration Max (days)')
    occupancy = models.CharField(max_length=100, blank=True, verbose_name='Occupancy (e.g. 24 Beds)')

    # ── Contact (additional) ──
    website = models.URLField(blank=True)
    whatsapp = models.CharField(max_length=20, blank=True)

    # ── Location ──
    google_maps_url = models.URLField(blank=True)
    lat = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    lng = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    pincode = models.CharField(max_length=10, blank=True)

    # ── Multi-select fields stored as JSON lists ──
    languages = models.JSONField(default=list, blank=True, verbose_name='Languages')
    surroundings = models.JSONField(default=list, blank=True, verbose_name='Surroundings')
    treatments = models.JSONField(default=list, blank=True, verbose_name='Treatments')
    patient_profiles = models.JSONField(default=list, blank=True, verbose_name='Patient Profile')
    main_facilities = models.JSONField(default=list, blank=True, verbose_name='Main Facilities')
    in_room_facilities = models.JSONField(default=list, blank=True, verbose_name='In-Room Facilities')
    center_facilities = models.JSONField(default=list, blank=True, verbose_name='Center Facilities')
    activities = models.JSONField(default=list, blank=True, verbose_name='Activities')

    # ── Price ──
    price_range = models.CharField(max_length=10, choices=PRICE_CHOICES, blank=True, verbose_name='Price Per Month')

    # ── Relations ──
    treatment_types = models.ManyToManyField(TreatmentType, blank=True, related_name='centers')
    amenities = models.ManyToManyField(Amenity, blank=True, related_name='centers')

    # ── Facilities (legacy JSON fields) ──
    recreational_activities = models.JSONField(default=list, blank=True)
    therapies = models.JSONField(default=list, blank=True)
    videos = models.JSONField(default=list, blank=True)

   

    # ── SEO ──
    seo_title = models.CharField(max_length=255, blank=True)
    seo_description = models.TextField(max_length=300, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

    @property
    def description(self):
        return self.about

    @property
    def min_program_duration(self):
        if self.program_duration_min and self.program_duration_max:
            return f"{self.program_duration_min} to {self.program_duration_max} days"
        elif self.program_duration_min:
            return f"{self.program_duration_min} days"
        return ''

    @property
    def phone(self):
        return self.mobile

    @property
    def category(self):
        return self.centre_type

    @property
    def surrounding(self):
        return self.surroundings[0] if self.surroundings else ''

    @property
    def total_beds(self):
        if self.occupancy:
            import re
            match = re.search(r'\d+', self.occupancy)
            return int(match.group()) if match else None
        return None


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
    center = models.ForeignKey(RehabCenter, related_name='team_members', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    qualification = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(upload_to='team/', null=True, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.name} — {self.center.name}"


class RehabCenterAboutSection(models.Model):
    center = models.ForeignKey(RehabCenter, related_name='about_sections', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='about/', null=True, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.title} — {self.center.name}"
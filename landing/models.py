from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.api import APIField
from modelcluster.fields import ParentalKey


class FAQItem(models.Model):
    page = ParentalKey(
        'wagtailcore.Page',
        related_name='faqs',
        on_delete=models.CASCADE,
        null=True,
    )
    question = models.CharField(max_length=500)
    answer = RichTextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.question


class CityLandingPage(Page):
    # Hero
    hero_title = models.CharField(max_length=255)
    hero_subtitle = models.TextField(blank=True)
    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    # Filter defaults
    default_city = models.CharField(max_length=100, blank=True)

    # Content
    intro = RichTextField(blank=True)
    about = RichTextField(blank=True)

    # SEO
    seo_title_override = models.CharField(max_length=255, blank=True)
    seo_description = models.TextField(max_length=300, blank=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('hero_title'),
            FieldPanel('hero_subtitle'),
            FieldPanel('hero_image'),
        ], heading='Hero Section'),
        FieldPanel('default_city'),
        FieldPanel('intro'),
        FieldPanel('about'),
        InlinePanel('city_faqs', label='FAQs'),
    ]

    promote_panels = Page.promote_panels + [
        FieldPanel('seo_title_override'),
        FieldPanel('seo_description'),
    ]

    # ── Expose fields to Wagtail API ──
    api_fields = [
        APIField('hero_title'),
        APIField('hero_subtitle'),
        APIField('default_city'),
        APIField('intro'),
        APIField('about'),
        APIField('seo_title_override'),
        APIField('seo_description'),
        APIField('city_faqs'),
    ]

    class Meta:
        verbose_name = 'City Landing Page'

    def get_context(self, request):
        context = super().get_context(request)
        context['default_city'] = self.default_city
        context['faqs'] = self.city_faqs.all()
        return context


class CityFAQItem(models.Model):
    page = ParentalKey(
        CityLandingPage,
        related_name='city_faqs',
        on_delete=models.CASCADE
    )
    question = models.CharField(max_length=500)
    answer = RichTextField()
    order = models.PositiveIntegerField(default=0)

    panels = [
        FieldPanel('question'),
        FieldPanel('answer'),
        FieldPanel('order'),
    ]

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.question


class TreatmentLandingPage(Page):
    # Hero
    hero_title = models.CharField(max_length=255)
    hero_subtitle = models.TextField(blank=True)
    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    # Filter defaults
    default_treatment_slug = models.CharField(max_length=100, blank=True)

    # Content
    intro = RichTextField(blank=True)
    about = RichTextField(blank=True)

    # SEO
    seo_title_override = models.CharField(max_length=255, blank=True)
    seo_description = models.TextField(max_length=300, blank=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('hero_title'),
            FieldPanel('hero_subtitle'),
            FieldPanel('hero_image'),
        ], heading='Hero Section'),
        FieldPanel('default_treatment_slug'),
        FieldPanel('intro'),
        FieldPanel('about'),
        InlinePanel('treatment_faqs', label='FAQs'),
    ]

    promote_panels = Page.promote_panels + [
        FieldPanel('seo_title_override'),
        FieldPanel('seo_description'),
    ]

    # ── Expose fields to Wagtail API ──
    api_fields = [
        APIField('hero_title'),
        APIField('hero_subtitle'),
        APIField('default_treatment_slug'),
        APIField('intro'),
        APIField('about'),
        APIField('seo_title_override'),
        APIField('seo_description'),
        APIField('treatment_faqs'),
    ]

    class Meta:
        verbose_name = 'Treatment Landing Page'


class TreatmentFAQItem(models.Model):
    page = ParentalKey(
        TreatmentLandingPage,
        related_name='treatment_faqs',
        on_delete=models.CASCADE
    )
    question = models.CharField(max_length=500)
    answer = RichTextField()
    order = models.PositiveIntegerField(default=0)

    panels = [
        FieldPanel('question'),
        FieldPanel('answer'),
        FieldPanel('order'),
    ]

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.question
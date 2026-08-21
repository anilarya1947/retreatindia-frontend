from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.snippets.models import register_snippet
from wagtail.api import APIField
from wagtail.images.api.fields import ImageRenditionField
from taggit.managers import TaggableManager


@register_snippet
class BlogCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    panels = [
        FieldPanel('name'),
        FieldPanel('slug'),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Blog Categories'


class BlogIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
    ]

    subpage_types = ['blog.BlogDetailPage']

    api_fields = [
        APIField('intro'),
    ]


class BlogDetailPage(Page):
    intro = models.TextField(max_length=300, blank=True)
    body = RichTextField()
    featured_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    category = models.ForeignKey(
        BlogCategory,
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='posts'
    )
    tags = TaggableManager(blank=True)
    published_date = models.DateField(null=True, blank=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('published_date'),
            FieldPanel('category'),
            FieldPanel('tags'),
        ], heading='Post Info'),
        FieldPanel('featured_image'),
        FieldPanel('intro'),
        FieldPanel('body'),
    ]

    parent_page_types = ['blog.BlogIndexPage']

    api_fields = [
    APIField('intro'),
    APIField('body'),
    APIField('published_date'),
    APIField('featured_image', serializer=ImageRenditionField('fill-800x600')),
    APIField('category'),
    ]

    def __str__(self):
        return self.title


class FlexPage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]

    api_fields = [
        APIField('body'),
    ]
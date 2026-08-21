from wagtail.api.v2.views import PagesAPIViewSet
from wagtail.api.v2.router import WagtailAPIRouter
from wagtail.images.api.v2.views import ImagesAPIViewSet
from wagtail.documents.api.v2.views import DocumentsAPIViewSet

router = WagtailAPIRouter('wagtailapi')
router.register_endpoint('pages', PagesAPIViewSet)
router.register_endpoint('images', ImagesAPIViewSet)
router.register_endpoint('documents', DocumentsAPIViewSet)
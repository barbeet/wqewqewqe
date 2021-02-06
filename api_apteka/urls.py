from rest_framework import routers
from .api import ProductViewSet

router = routers.DefaultRouter()
router.register('product', ProductViewSet, 'product_api')

urlpatterns = router.urls
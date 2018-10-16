from rest_framework.routers import SimpleRouter

from app.views import OrderViewSet

router = SimpleRouter()
router.register('orders', OrderViewSet)

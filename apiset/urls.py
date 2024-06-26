from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
print (router.urls)
urlpatterns = [
    path('', include(router.urls)),
]

# urlpatterns = router.urls
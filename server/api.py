from rest_framework import routers
from api import views as api_views

router = routers.DefaultRouter()
router.register(r'hello', api_views.HelloView, basename='hello')

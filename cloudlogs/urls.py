from django.urls import include, path
from rest_framework import routers

from .views import LogsViewset

app_name = 'cloudlogs'
router = routers.SimpleRouter()

router.register(r'logs', LogsViewset, base_name="logs"),


urlpatterns = [
    path('', include(router.urls)),
]

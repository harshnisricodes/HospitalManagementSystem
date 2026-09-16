from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PatientViewSet , home

router = DefaultRouter()
router.register('patients', PatientViewSet)

urlpatterns = [
    path('', home, name='home'),
    path('', include(router.urls)),
]
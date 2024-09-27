from rest_framework.routers import DefaultRouter
from .views import AnswerView
from django.urls import path, include


router = DefaultRouter()
router.register(r'generator', AnswerView, basename='generator')

urlpatterns = [
    path('', include(router.urls)),
]
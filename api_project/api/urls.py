# api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

# Create a router and register the BookViewSet
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

# Define URL patterns
urlpatterns = [
    # Include the router URLs for BookViewSet (all CRUD operations)
    path('', include(router.urls)),  # This will include all routes registered with the router
]


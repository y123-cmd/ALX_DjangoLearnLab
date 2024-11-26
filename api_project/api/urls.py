from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views  # Import the token view
from .views import BookViewSet

# Create a router and register the BookViewSet
router = DefaultRouter()
router.register(r"books_all", BookViewSet, basename="book_all")

# Define URL patterns
urlpatterns = [
    # Include the router URLs for BookViewSet (all CRUD operations)
    path(
        "", include(router.urls)
    ),  # This will include all routes registered with the router
    # Add the token authentication endpoint
    path("api-token-auth/", views.obtain_auth_token, name="api_token_auth"),
]

from django.urls import path
from . import views

urlpatterns = [
    # ... other URL patterns ...

    # Add the URL for creating a new blog post
    path('', views.create_blog, name='create_blog'),
]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include('books.urls')),  # Include the URLs of the books app
    # Add other URL patterns as needed
]

from django.contrib import admin
from django.urls import include, path

admin.autodiscover()

urlpatterns = [
    path('', include('rest_framework.urls')),
    path('api/', include('blog.urls')),
    path('api/', include('accounts.urls')),
    path('admin/', admin.site.urls),
]

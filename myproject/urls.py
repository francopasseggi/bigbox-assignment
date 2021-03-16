import debug_toolbar
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('__debug__/', include(debug_toolbar.urls)),
    path('admin/', admin.site.urls),
    path('', include('bigbox.urls')),
    path('polls/', include('polls.urls')),
    path('quickstart/', include('quickstart.urls')),
    path('snippets/', include('snippets.urls')),
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
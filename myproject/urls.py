import debug_toolbar
from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt

from graphene_django.views import GraphQLView

urlpatterns = [
    path('graphql', csrf_exempt(GraphQLView.as_view(graphiql=True))),
    path('__debug__/', include(debug_toolbar.urls)),
    path('admin/', admin.site.urls),
    path('bigbox', include('bigbox.urls')),
    path('polls/', include('polls.urls')),
    path('quickstart/', include('quickstart.urls')),
    path('', include('snippets.urls')),
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
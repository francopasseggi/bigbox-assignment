from django.urls import path
from .views import BoxList, BoxDetail, ActivityList, ActivityDetail, search_form, home

urlpatterns = [
    path('', home, name='home')
    path('search/', search_form, name='box-search'),
    path('box/', BoxList.as_view(), name='box-list'),
    path('box/<int:pk>/', BoxDetail.as_view(), name='box-detail'),
    path('activity/<int:pk>/', ActivityDetail.as_view(), name='activity-detail'),
    path('box/<int:pk>/activity/', ActivityList.as_view(), name='box-activity'),
    path('box/<slug:slug>/', BoxDetail.as_view(), name='box-search-result')
]

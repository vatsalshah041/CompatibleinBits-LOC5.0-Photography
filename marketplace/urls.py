from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from rest_framework_simplejwt import views as jwt_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('albumlist/',views.AlbumListView.as_view(), name='albumlist'),
    path('albumdetail/<int:pk>/',views.AlbumDetailView.as_view(), name='albumdetail'),
    path('albumimages/<int:pk>/',views.MarketImageAlbumView.as_view(), name='domain')
]

urlpatterns = format_suffix_patterns(urlpatterns)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
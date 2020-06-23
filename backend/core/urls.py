from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from . import settings

api_urlpatterns = [
    path('api/', include('backend.booking.api.urls')),

]

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('backend.booking.urls')),

                  re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
                  re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),

              ] + api_urlpatterns

import debug_toolbar
from django.conf import settings
from django.contrib import admin
from django.urls import include, path

api_v1_urlpatterns = [
    path('api/v1/blog/', include('blog.api.v1.urls')),
]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    *api_v1_urlpatterns
]

if settings.TOOLBAR:
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls))
    ]

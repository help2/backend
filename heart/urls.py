from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^heart/', include("world.urls")),
    url(r'^account/', include('registration.backends.default.urls'))
]

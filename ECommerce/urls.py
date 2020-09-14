
from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'^api/v1/users/', include(('ECommerce.apps.user.urls', 'user'), namespace='user')),
    url(r'^api/v1/web/', include(('ECommerce.apps.web.urls', 'web'), namespace='web')),
]

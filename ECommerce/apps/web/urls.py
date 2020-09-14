from django.conf.urls import url
from ECommerce.apps.web.views import right

urlpatterns = [
    
    url(r'^rights/(?P<data_type>\w+)/$', view=right.right, name='right'),
]

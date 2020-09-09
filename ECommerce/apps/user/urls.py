from django.conf.urls import url
from ECommerce.apps.user.views import login

urlpatterns = [
    url(r'^login$', view=login, name='login'),
]

from django.conf.urls import url
from ECommerce.apps.user import views

urlpatterns = [
    url(r'^login/$', view=views.login, name='login'),
    url(r'^$', view=views.users, name='users'),
]

from django.conf.urls import url
from ECommerce.apps.user import views

urlpatterns = [
    url(r'^login/$', view=views.login, name='login'),
    url(r'^$', view=views.users, name='users'),
    url(r'^(?P<uid>\d+)/$', view=views.user, name='user'),
    url(r'^(?P<uid>\d+)/state/(?P<state>\d+)/$', view=views.user_state, name='user_state'),
    url(r'^(?P<uid>\d+)/role/$', view=views.user_role, name='user_role'),
]

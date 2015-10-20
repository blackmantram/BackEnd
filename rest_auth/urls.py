from django.conf.urls import patterns, url

from rest_auth.views import (
    LoginView, LogoutView, UserDetailsView, PasswordChangeView,
    PasswordResetView, PasswordResetConfirmView
)

urlpatterns = patterns(
    '',
    # URLs that do not require a session or valid token
    url(r'^password/reset', PasswordResetView.as_view(),
        name='rest_password_reset'),
    url(r'^confirm/password/reset', PasswordResetConfirmView.as_view()),
   # url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', 'django.contrib.auth.views.password_reset_confirm', name='password_reset_confirm'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', PasswordResetConfirmView.as_view(), name='password_reset_confirm'), 
    url(r'^login', LoginView.as_view(), name='rest_login'),
    # URLs that require a user to be logged in with a valid session / token.
    url(r'^logout', LogoutView.as_view(), name='rest_logout'),
    url(r'^user/$', UserDetailsView.as_view(), name='rest_user_details'),
    url(r'^password/change', PasswordChangeView.as_view(),
        name='rest_password_change'),
)

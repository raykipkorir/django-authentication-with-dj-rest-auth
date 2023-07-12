from django.contrib import admin
from django.urls import include, path

from users.views import GoogleLogin, callback

# auth url if you are using authorization code grant - Sign In with Google
# https://accounts.google.com/o/oauth2/v2/auth?redirect_uri=<CALLBACK_URL_YOU_SET_ON_GOOGLE>&prompt=consent&response_type=code&client_id=<YOUR CLIENT ID>&scope=openid%20email%20profile&access_type=offline

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("dj_rest_auth.urls")), # login, logout, password reset, password change, user, token refresh, token verify
    path("api/signup/", include("dj_rest_auth.registration.urls")), # sign up url - sign up users using email, username and password
    path("api/google/", GoogleLogin.as_view(), name="google_login"),  # our access token url - where we exchange code for token
    path("api/callback/", callback), # callback url - In authorization code grant, code is returned as query parameter to this url

    # to be revisited
    # path("password-reset/confirm/<uidb64>/<token>/",
    #    password_reset_confirm,
    #    name='password_reset_confirm'),
]

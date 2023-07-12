import requests
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    callback_url = settings.CALLBACK_URL
    client_class = OAuth2Client


# triggered when user gives consent to client to have access to resource server
@api_view(["GET"])
def callback(request):
    """Callback"""
    code = request.GET.get("code")

    # exchange code with authorization server for access token
    res = requests.post("http://localhost:8000/api/google/", data={"code": code}, timeout=30)
    return Response(res.json())


# to be revisited
@api_view(["GET", "POST"])
def password_reset_confirm(request, uidb64, token):
    # code
    return Response({"hello"})

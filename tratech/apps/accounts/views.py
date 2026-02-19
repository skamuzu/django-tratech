from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
from django.conf import settings
from dj_rest_auth.views import LoginView, LogoutView, UserDetailsView, PasswordResetView
from dj_rest_auth.registration.views import RegisterView
from djangorestframework_camel_case.parser import (
    CamelCaseFormParser,
    CamelCaseJSONParser,
    CamelCaseMultiPartParser,
)


class CamelCaseParserMixin:
    parser_classes = (
        CamelCaseJSONParser,
        CamelCaseFormParser,
        CamelCaseMultiPartParser,
    )


class CamelCaseLoginView(CamelCaseParserMixin, LoginView):
    pass


class CamelCaseLogoutView(CamelCaseParserMixin, LogoutView):
    pass


class CamelCaseUserDetailsView(CamelCaseParserMixin, UserDetailsView):
    pass


class CamelCasePasswordResetView(CamelCaseParserMixin, PasswordResetView):
    pass


class CamelCaseRegisterView(CamelCaseParserMixin, RegisterView):
    pass

class GoogleLogin(SocialLoginView): 
    adapter_class = GoogleOAuth2Adapter
    callback_url = "postmessage"
    client_class = OAuth2Client


class CamelCaseGoogleLogin(CamelCaseParserMixin, GoogleLogin):
    pass

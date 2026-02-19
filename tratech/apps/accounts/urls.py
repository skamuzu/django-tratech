from django.urls import path
from .views import (
     CamelCaseGoogleLogin,
     CamelCaseLoginView,
     CamelCaseLogoutView,
     CamelCasePasswordResetView,
     CamelCaseRegisterView,
     CamelCaseUserDetailsView,
)

urlpatterns = [
     path("auth/login/", CamelCaseLoginView.as_view(), name="rest_login"),
     path("auth/logout/", CamelCaseLogoutView.as_view(), name="rest_logout"),
     path("auth/user/", CamelCaseUserDetailsView.as_view(), name="rest_user_details"),
     path(
          "auth/password/reset/",
          CamelCasePasswordResetView.as_view(),
          name="rest_password_reset",
     ),
     path(
          "auth/registration/",
          CamelCaseRegisterView.as_view(),
          name="rest_register",
     ),
     path("auth/google/", CamelCaseGoogleLogin.as_view(), name="google_connect"),
]
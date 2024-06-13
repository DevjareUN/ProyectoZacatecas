from django.urls import path
from django.contrib.auth.views import LogoutView
from frontend import views

urlpatterns = [
        path("", views.index, name="landing"),
        path("login/", views.LoginView.as_view(), name="login"),
        path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
        path("home/", views.Home.as_view(), name="home"),
        path("lookup/", views.Lookup.as_view(), name="lookup"),
        path("capture/", views.Capture.as_view(), name="capture"),
        ]

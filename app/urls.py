from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_user, name="login"),  # login first
    path("home/", views.home, name="home"),
    path("logout/", views.logout_user, name="logout"),

    path("add/", views.add_employee, name="add"),
    path("edit/<int:id>/", views.edit_employee, name="edit"),
    path("delete/<int:id>/", views.delete_employee, name="delete"),
]

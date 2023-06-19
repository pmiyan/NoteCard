from django.urls import path
from . import views

urlpatterns = [
    path("hello", views.hello_world, name="hello-world"),
    path("<int:card_id>", views.detail, name="card-detail"),
    path("", views.home, name="cards-home"),
]
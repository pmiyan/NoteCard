from django.urls import path
from . import views
from .views import CardListView, CardDetailView

urlpatterns = [
    path("hello", views.hello_world, name="hello-world"),
    path("<int:card_id>", CardDetailView.as_view(), name="card-detail"),
    path("", CardListView.as_view(), name="cards-home"),
]
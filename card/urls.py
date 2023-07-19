from django.urls import path
from . import views
from .views import CardListView, CardDetailView, CardCreateView, CardUpdateView, CardDeleteView, TypeListView, TypeDetailView, TypeCreateView, TypeUpdateView, TypeDeleteView

urlpatterns = [
    path("hello", views.hello_world, name="hello-world"),
    path("cards/", CardListView.as_view(), name="cards-home"),
    path("cards/<int:pk>/", CardDetailView.as_view(), name="card-detail"),
    path("cards/new/", CardCreateView.as_view(), name="card-new"),
    path("cards/<int:pk>/update", CardUpdateView.as_view(), name="card-update"),
    path("cards/<int:pk>/delete", CardDeleteView.as_view(), name="card-delete"),

    path("", TypeListView.as_view(), name="cards-homeview"),
    path("<int:pk>/", TypeDetailView.as_view(), name="card-typedetail"),
    path("new/", TypeCreateView.as_view(), name="type-new"),
    path("<int:pk>/update/", TypeUpdateView.as_view(), name="type-update"),
    path("<int:pk>/delete/", TypeDeleteView.as_view(), name="type-delete"),
]
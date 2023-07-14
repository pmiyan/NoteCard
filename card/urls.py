from django.urls import path
from . import views
from .views import CardListView, CardDetailView, CardCreateView, CardUpdateView, CardDeleteView

urlpatterns = [
    path("hello", views.hello_world, name="hello-world"),
    path("", CardListView.as_view(), name="cards-home"),
    path("<int:pk>/", CardDetailView.as_view(), name="card-detail"),
    path("new/", CardCreateView.as_view(), name="card-new"),
    path("<int:pk>/update", CardUpdateView.as_view(), name="card-update"),
    path("<int:pk>/delete", CardDeleteView.as_view(), name="card-delete")
]
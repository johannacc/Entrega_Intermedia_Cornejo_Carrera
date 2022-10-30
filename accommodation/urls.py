from django.urls import path

from accommodation import views

app_name = "accommodation"
urlpatterns = [
    path("accommodations/", views.accommodations, name="accommodation-list"),
    path("accommodation/add", views.create_accommodation, name="accommodation-add"),
    path("accommodation/<int:pk>/detail/", views.AccommodationDetailView.as_view(), name="accommodation-detail"),
    path("accommodation/<int:pk>/update/", views.AccommodationUpdateView.as_view(), name="accommodation-update"),
    path("accommodation/<int:pk>/delete/", views.AccommodationDeleteView.as_view(), name="accommodation-delete"),
]


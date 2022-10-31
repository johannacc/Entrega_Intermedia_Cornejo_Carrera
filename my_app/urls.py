from django.urls import path

from my_app import views

app_name = "my_app"
urlpatterns = [
    path("destinos", views.destinos, name="destinos-list"),
    path("destino/add", views.create_destino, name="destino-add"),
    path("destino/<int:pk>/detail/", views.ViajeDetailView.as_view(), name="destino-detail"),
    path("destino/<int:pk>/update/", views.ViajeUpdateView.as_view(), name="destino-update"),
    path("destino/<int:pk>/delete/", views.ViajeDeleteView.as_view(), name="destino-delete"),

]

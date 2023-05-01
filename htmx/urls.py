from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("component/<component>", views.render_component, name="component"),
    path("pokemon", views.pokemon, name="pokemon"),
    path("pokemon/<str:name>", views.pokemon_page, name="pokemon-page"),
]

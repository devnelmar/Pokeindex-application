from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from pokeindexapi.users.api.views import UserViewSet
from pokeindexapi.apps.pokedex.api.views import PokemonViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("pokemon", PokemonViewSet, basename="pokemon")


app_name = "api"
urlpatterns = router.urls

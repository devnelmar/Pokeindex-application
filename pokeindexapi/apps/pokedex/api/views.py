# Django
from django.db.models import Q

# DRF
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAdminUser

# Ours
from pokeindexapi.apps.pokedex.models import Pokemon
from pokeindexapi.apps.pokedex.api.serializers import PokemonSerializer


class PokemonViewSet(viewsets.ModelViewSet):
    serializer_class = PokemonSerializer
    permission_classes_by_action = {'list': [AllowAny]}

    def get_queryset(self):
        queryset = Pokemon.objects.all()
        search = self.request.GET.get("search")
        if search:
            queryset = queryset.filter(Q(name__icontains=search))
        return queryset

    def get_permissions(self):
        try:
            # return permission_classes depending on `action`
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            # action is not set return default permission_classes
            return [permission() for permission in self.permission_classes]

"""Pokemon Command."""

# Django
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Command for create an pokemon."""

    def add_arguments(self, parser):
        parser.add_argument("pokemon_id", nargs="+", type=int)

    def handle(self, *args, **options):
        """Handle command usage."""
        from pokeindexapi.apps.pokedex.utils.initialize_pokedex import (
            CreatePokemonUtils,
        )

        CreatePokemonUtils().create_pokemon_from_api(options["pokemon_id"][0])
        print('Pokemon has been created successfully')

# Django
from django.db import transaction


# Utils
from pokeindexapi.apps.pokedex.utils.poke_api import PokemonAPI

# Models
from pokeindexapi.apps.pokedex.models import Pokemon, PokemonStats


class CreatePokemonUtils:
    has_next_phase = True
    previous_phase = None

    def create_pokemon_from_api(self, pokemon_id):
        with transaction.atomic():
            poke_api = PokemonAPI()
            evolution_chain_data = poke_api.get_evolution_chain(pokemon_id)

            pokemon_data = evolution_chain_data["chain"]

            while self.has_next_phase:
                pokemon_name = pokemon_data["species"]["name"]
                pokemon_info = poke_api.get_pokemon(pokemon_name)

                pokemon = self._create_pokemon(
                    pokemon_info=pokemon_info,
                    pokemon_data=pokemon_data,
                    pre_phase=self.previous_phase,
                )
                self._create_pokemon_stats(pokemon, pokemon_info["stats"])

                if self.previous_phase:
                    self.previous_phase.post_phase = pokemon
                    self.previous_phase.save()

                self.previous_phase = pokemon

                if "evolves_to" in pokemon_data and pokemon_data["evolves_to"]:
                    self.has_next_phase = True
                    pokemon_data = pokemon_data["evolves_to"][0]
                else:
                    self.has_next_phase = False

    @staticmethod
    def _create_pokemon(
        pokemon_info: dict,
        pokemon_data: dict,
        pre_phase: Pokemon = None,
        post_phase: Pokemon = None,
    ):
        pokemon = Pokemon.objects.create(
            name=pokemon_info["name"],
            height=pokemon_info["height"],
            weight=pokemon_info["weight"],
            pokemon_api_id=pokemon_info["id"],
            is_baby=pokemon_data["is_baby"],
            species=pokemon_data["species"],
            pre_phase=pre_phase,
            post_phase=post_phase,
        )
        return pokemon

    @staticmethod
    def _create_pokemon_stats(pokemon: Pokemon, stats: list):
        for stat in stats:
            PokemonStats.objects.create(
                base_stat=stat["base_stat"],
                effort=stat["effort"],
                name=stat["stat"]["name"],
                url=stat["stat"]["url"],
                pokemon=pokemon,
            )

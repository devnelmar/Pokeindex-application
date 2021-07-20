from rest_framework import serializers

from pokeindexapi.apps.pokedex.models import Pokemon, PokemonStats


class PokemonStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PokemonStats
        fields = (
            "id",
            "name",
            "base_stat",
            "effort",
            "url",
        )


class PokemonPrePhaseSerializer(serializers.ModelSerializer):
    pokemon_stats = PokemonStatsSerializer(many=True)

    class Meta:
        model = Pokemon
        fields = (
            "id",
            "name",
            "weight",
            "pokemon_api_id",
            "is_baby",
            "species",
            "pokemon_stats",
        )


class PokemonPostPhaseSerializer(serializers.ModelSerializer):
    pokemon_stats = PokemonStatsSerializer(many=True)

    class Meta:
        model = Pokemon
        fields = (
            "id",
            "name",
            "weight",
            "pokemon_api_id",
            "is_baby",
            "species",
            "pokemon_stats",
        )


class PokemonSerializer(serializers.ModelSerializer):
    pokemon_stats = PokemonStatsSerializer(many=True)
    pre_phase = PokemonPrePhaseSerializer(many=False)
    post_phase = PokemonPostPhaseSerializer(many=False)

    class Meta:
        model = Pokemon
        fields = (
            "id",
            "name",
            "weight",
            "pokemon_api_id",
            "is_baby",
            "species",
            "pre_phase",
            "post_phase",
            "pokemon_stats",
        )

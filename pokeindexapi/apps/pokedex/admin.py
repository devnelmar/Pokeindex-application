from django.contrib import admin

from pokeindexapi.apps.pokedex.models import (
    Pokemon,
    PokemonStats,
)


class PokemonAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "height",
        "weight",
        "pokemon_api_id",
        "is_baby",
        "species",
        "pre_phase",
        "post_phase",
    )
    list_filter = ("name", "pokemon_api_id", "height", "weight")
    model = Pokemon


class PokemonStatsAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "base_stat",
        "effort",
        "url",
        "pokemon",
    )
    list_filter = ("name", "base_stat")
    model = PokemonStats


admin.site.register(Pokemon, PokemonAdmin)
admin.site.register(PokemonStats, PokemonStatsAdmin)

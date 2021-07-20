from django.db import models

from pokeindexapi.utils.models import BaseModel


class Pokemon(BaseModel):
    name = models.CharField(max_length=255)
    height = models.CharField(max_length=255)
    weight = models.CharField(max_length=255)
    pokemon_api_id = models.CharField(max_length=255)
    is_baby = models.BooleanField()
    species = models.JSONField()

    # Foreign keys
    pre_phase = models.ForeignKey(
        "self",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="pokemon_pre_phases",
    )
    post_phase = models.ForeignKey(
        "self",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="pokemon_post_phases",
    )


class PokemonStats(BaseModel):
    name = models.CharField(max_length=255)
    base_stat = models.CharField(max_length=255)
    effort = models.IntegerField()
    url = models.URLField()

    # Foreign keys
    pokemon = models.ForeignKey(
        Pokemon, on_delete=models.PROTECT, related_name="pokemon_stats"
    )

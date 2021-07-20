import json
import urllib.request
from urllib.request import Request, urlopen


class PokemonAPI:
    def __init__(self):
        self.url = "https://pokeapi.co/api/v2/"
        self.headers = {"User-Agent": "XYZ/3.0"}

    def get_evolution_chain(self, pokemon_id: int) -> dict:
        url = Request(
            f"{self.url}/evolution-chain/{pokemon_id}/",
            headers=self.headers,
        )
        return self.get_api_data(url)

    def get_pokemon(self, pokemon_name: str) -> dict:
        url = Request(f"{self.url}/pokemon/{pokemon_name}/", headers=self.headers)
        return self.get_api_data(url)

    @staticmethod
    def get_api_data(url):
        with urllib.request.urlopen(url) as response:
            return json.loads(response.read())

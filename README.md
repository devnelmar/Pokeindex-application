# Pokeindex application

This is a django application built using Python3, Postgres, Django Rest Framework, Docker and Docker-compose.

The proposal is having a command for create pokemons storaging info from a public API and endpoints that allow search pokemons and details from database.

# Setup

1. Clone the repository
 
2. Install docker and docker compose

# Basic Commands
Steps to run the complete all the environment locally.

`docker-compose -f local.yml build`

`docker-compose -f local.yml run --rm django python3 manage.py migrate`

`docker-compose -f local.yml up`

Now the app will be running on port 8000.

# Script

For run command to create a pokemon follow the next step:

***copy and paste the following command indicating the id of the pokemon you want to create

`docker-compose -f local.yml run --rm django python3 manage.py create_pokemon <pokemon_id>`

# API Endpoint
There is only one API endpoint that you can consume:

Get pokemon -> [GET] /api/pokemon/

You need to send the params search:

?search="Pikachu"

It will return a response like this 
```
[GET] /api/pokemon/

# response
{
        "id": "29f74374-73c0-4813-863e-eb9476e52c45",
        "name": "nidoqueen",
        "weight": "600",
        "pokemon_api_id": "31",
        "is_baby": false,
        "species": {
            "url": "https://pokeapi.co/api/v2/pokemon-species/31/",
            "name": "nidoqueen"
        },
        "pre_phase": {
            "id": "ccc27f80-5d33-442a-a205-ed6a410dcb42",
            "name": "nidorina",
            "weight": "200",
            "pokemon_api_id": "30",
            "is_baby": false,
            "species": {
                "url": "https://pokeapi.co/api/v2/pokemon-species/30/",
                "name": "nidorina"
            },
            "pokemon_stats": [
                {
                    "id": "a7a64eba-efd5-40a8-a621-d013be6cce33",
                    "name": "hp",
                    "base_stat": "70",
                    "effort": 2,
                    "url": "https://pokeapi.co/api/v2/stat/1/"
                },
                ...
            ]
        },
        "post_phase": null,
        "pokemon_stats": [
            {
                "id": "4633c257-48b8-4efb-8a6e-254965aaa439",
                "name": "hp",
                "base_stat": "90",
                "effort": 3,
                "url": "https://pokeapi.co/api/v2/stat/1/"
            },
            ...
        ]
    },

```

# Models

A litle explain about what contains models:

Class Pokemon():

Name: is the main name of the pokemon

Height: is the height of the pokemon as STR value

Weight: is the weight of the pokemon as STR value

Pokemon_api_id: is the id from PokeApi

Is_baby: boolean that represent if is young or not

Species: is a dict that containt relevant info from pokemon

Pre_phase: is the Pre evolution for the pokemon

Post_phase: is the next evolution for the pokemon 

Class PokemonStats():

Name: is the name of stat

Base_stats: is the stat value as STR value

Effort: is the number of effort for pokemon as INT value

Url: is the url of the pokemon stat

Pokemon: Is the pokemon who have this stats

# Admin

You can run command for create a superuser:
`docker-compose -f local.yml run --rm django python3 manage.py createsuperuser`

Whit the user that you has been created, you can access data from this url, once you has the server running: http://localhost:8000/admin/


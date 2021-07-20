# Pokeindex application

This is a django application built using Python3, Postgres, Django Rest Framework, Docker and Docker-compose.

The proposal is having a command for create pokemons storaging info from a public API and endpoints that allow search pokemons and details from database, 

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
                {
                    "id": "ec7adf77-d529-4363-ab7e-7c5fe9741fd7",
                    "name": "attack",
                    "base_stat": "62",
                    "effort": 0,
                    "url": "https://pokeapi.co/api/v2/stat/2/"
                },
                {
                    "id": "e75ea911-a5ac-48a6-ba4e-7023498925df",
                    "name": "defense",
                    "base_stat": "67",
                    "effort": 0,
                    "url": "https://pokeapi.co/api/v2/stat/3/"
                },
                {
                    "id": "28366696-69b8-4b95-b4fe-90a70e8206ab",
                    "name": "special-attack",
                    "base_stat": "55",
                    "effort": 0,
                    "url": "https://pokeapi.co/api/v2/stat/4/"
                },
                {
                    "id": "ff961f8c-92db-4a88-a624-6d91bd128420",
                    "name": "special-defense",
                    "base_stat": "55",
                    "effort": 0,
                    "url": "https://pokeapi.co/api/v2/stat/5/"
                },
                {
                    "id": "7e39e73d-01ea-4211-8658-fa8a02edfcc2",
                    "name": "speed",
                    "base_stat": "56",
                    "effort": 0,
                    "url": "https://pokeapi.co/api/v2/stat/6/"
                }
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
            {
                "id": "0297f9ee-c1c4-4ccf-a653-b712f398f766",
                "name": "attack",
                "base_stat": "92",
                "effort": 0,
                "url": "https://pokeapi.co/api/v2/stat/2/"
            },
            {
                "id": "c99fe138-bf1b-43f9-ab10-18b945571704",
                "name": "defense",
                "base_stat": "87",
                "effort": 0,
                "url": "https://pokeapi.co/api/v2/stat/3/"
            },
            {
                "id": "f040ec9e-9a51-411e-96ab-33b8ccaa7158",
                "name": "special-attack",
                "base_stat": "75",
                "effort": 0,
                "url": "https://pokeapi.co/api/v2/stat/4/"
            },
            {
                "id": "0e8c02bb-ca74-4533-8990-7570cb3b3587",
                "name": "special-defense",
                "base_stat": "85",
                "effort": 0,
                "url": "https://pokeapi.co/api/v2/stat/5/"
            },
            {
                "id": "edc41925-e8b9-486e-ac88-6f43c0ce4c6c",
                "name": "speed",
                "base_stat": "76",
                "effort": 0,
                "url": "https://pokeapi.co/api/v2/stat/6/"
            }
        ]
    },

```

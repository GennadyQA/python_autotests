import requests

URL = 'https://api.pokemonbattle.ru'
TOKEN = '34f30c1f483099693216ae6804e7f949'
HEADER = {"Content-Type" : "application/json",
          "trainer_token" : TOKEN}
pokemons_creat = {
    "name": "Charmander",
    "photo_id": 4
}




respons_creat = requests.post(url = f'{URL}/v2/pokemons', headers = HEADER, json = pokemons_creat)
print(respons_creat.json())

pokemons_id = respons_creat.json()['id']
pokemons_change = {
    "pokemon_id": pokemons_id,
    "name": "Wally",
    "photo_id": 2
}

respones_change = requests.put(url = f'{URL}/v2/pokemons', headers = HEADER, json = pokemons_change)
print(respones_change.json())

response_add = requests.post(url = f'{URL}/v2/trainers/add_pokeball', headers = HEADER, json = {'pokemon_id': pokemons_id })
print(response_add.json())
















'''pokemons_id = {
    "pokemon_id": "41779"
}

response_knockout = requests.post(url = f'{URL}/v2/pokemons/knockout', headers = HEADER, json = pokemons_id
)

print(response_knockout.json())'''

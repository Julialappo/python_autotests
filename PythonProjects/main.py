import requests 
URL = 'https://api.pokemonbattle.ru/v2'
token = '0c9636f1c08ca6f3cbdaccf5e7b2176f'
header = {'content-type': 'application/json', 'trainer_token': token } 
body_registration = {
    "trainer_token": token,
    "email": "login",
    "password": "password"
}
body_confirm = {
    "trainer_token": token
}

body_create = {
    "name": "Буль",
    "photo_id": 198
}
body_change = {
    "pokemon_id": "325644",
    "name": "Coбака",
    "photo_id": 11
}
body_add = {
    "pokemon_id": "325644"
}
'''responce = requests.post (url = f'{URL}/trainers/reg', headers = header, json = body_registration) 
print (responce.text)'''

'''responce_confirmation = requests.post (url = f'{URL}/trainers/confirm_email', headers = header, json = body_confirm)
print (responce_confirmation.text)'''

'''responce_create =  requests.post (url = f'{URL}/pokemons', headers= header, json = body_create)
print (responce_create.text)'''

'''responce_change=  requests.put (url = f'{URL}/pokemons', headers= header, json = body_change)
print (responce_change.text)'''


responce_add=  requests.post (url = f'{URL}/trainers/add_pokeball', headers= header, json = body_add)
print (responce_add.text)


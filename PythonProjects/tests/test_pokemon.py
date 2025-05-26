from multiprocessing import Value
import requests 
import pytest
URL = 'https://api.pokemonbattle.ru/v2'
token = '0c9636f1c08ca6f3cbdaccf5e7b2176f'
header = {'content-type': 'application/json', 'trainer_token': token } 
trainer_id = 38406

def test_status_code():
    Response = requests.get(url = f'{URL}/trainers',params={"trainer_id": trainer_id})
    assert Response.status_code == 200 

def test_part_of_response(): 
        response_get = requests.get(url = f'{URL}/trainers',params={"trainer_id": trainer_id})
        assert response_get.json()["data"][0] ["trainer_name"] == "yuliya" 


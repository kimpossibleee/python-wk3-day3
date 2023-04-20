import requests
from PIL import Image
'''
Exercise 1: Create a method that prints an image of your pokemon
STEPS:
1) I intially need to create a general endpoint
2) create a structure for the data that i will need to retrieve
3) create a class pokemon that will store pokemon data & methods
4) create a method that will print the image of the pokemon
5) create a method that evolves my pokemon
'''

api_endpoint = 'https://pokeapi.co/api/v2/pokemon/'

# poke_dict = {
#     name = data['name'],
#     image = data['sprites']['back_default']
#     identifier = data['id']
# }

class Pokemon():
    def __init__(self, name:str):
        self.name = name.lower()
        self.height = None
        self.sprite = None
        self.species_endpoint = None
        self.poke_api_call()

    def poke_api_call(self):
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{self.name}')
        if response.status_code == 200:
            data = response.json()
        else:
            return 'Error'

        self.sprite = data['sprites']['back_default']
        self.height = data['height']
        # ['sprites']['other']['home']['front_default']

    def print_pokemon(self):
        url = self.sprite
        img = Image.open(requests.get(url, stream=True).raw)

    def evolve(self):
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon-species/{self.name}')
        data = response.json()
        evolution_chain_url = data['evolution_chain']['url']
        response = requests.get(evolution_chain_url)
        data = response.json()
        evolution_chain = []
        #IN PROGRESS
        


charmander = Pokemon('charmander')
charmander.print_pokemon()
#I could not find a working alternative for Ipython, so I'm still working on researching how to show images. the current code for print_pokemon(self) was found on stackoverflow : https://stackoverflow.com/questions/7391945/how-do-i-read-image-data-from-a-url-in-python/40944159#40944159\

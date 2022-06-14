# This file MUST be configured in order for the code to run properly

# Make sure you put all your input images into an 'assets' folder. 
# Each layer (or category) of images must be put in a folder of its own.

# CONFIG is an array of objects where each object represents a layer
# THESE LAYERS MUST BE ORDERED.

# Each layer needs to specify the following
# 1. id: A number representing a particular layer
# 2. name: The name of the layer. Does not necessarily have to be the same as the directory name containing the layer images.
# 3. directory: The folder inside assets that contain traits for the particular layer
# 4. required: If the particular layer is required (True) or optional (False). The first layer must always be set to true.
# 5. rarity_weights: Denotes the rarity distribution of traits. It can take on three types of values.
#       - None: This makes all the traits defined in the layer equally rare (or common)
#       - "random": Assigns rarity weights at random. 
#       - array: An array of numbers where each number represents a weight. 
#                If required is True, this array must be equal to the number of images in the layer directory. The first number is  the weight of the first image (in alphabetical order) and so on...
#                If required is False, this array must be equal to one plus the number of images in the layer directory. The first number is the weight of having no image at all for this layer. The second number is the weight of the first image and so on...

# Be sure to check out the tutorial in the README for more details.                

CONFIG = [
    {
        'id': 1,
        'name': 'background',
        'directory': '00 Background',
        'required': True,
        'rarity_weights': None,
    },
    {
        'id': 2,
        'name': 'rare',
        'directory': '01 Rare',
        'required': False,
        'rarity_weights': None,
        'map': {
            'Beach.png' : 'Male-sitting-rare-kraken.png',
            'City.png' : 'Male-sitting-rare-cat.png',
            'Desert.png' : 'Male-sitting-rare-bikers.png', 
            'Easter Island.png' : 'Male-sitting-rare-lasers.png',
            'Jungle.png' : 'Male-sitting-rare-predator.png',
            'Mars.png' : 'Male-sitting-rare-nlo.png',
            'Mezoamerika.png' : 'Male-sitting-rare-mummy.png',
            'Mountain.png' : 'Male-sitting-rare-jeti.png',
            'Riverbank.png' : 'Male-sitting-rare-nessie.png',
         },
    },
    {
        'id': 3,
        'name': 'base',
        'directory': '02 Base',
        'required': True,
        'rarity_weights': None,
    },
    {
        'id': 4,
        'name': 'body',
        'directory': '03 Body',
        'required': True,
        'rarity_weights': None,
    },
    {
        'id': 5,
        'name': 'mouth',
        'directory': '04 Mouth',
        'required': True,
        'rarity_weights': None,
    },
    {
        'id': 6,
        'name': 'eyes',
        'directory': '05 Eyes',
        'required': True,
        'rarity_weights': None,
    },
    {
        'id': 7,
        'name': 'head',
        'directory': '06 Head',
        'required': True,
        'rarity_weights': None,
    },
    {
        'id': 8,
        'name': 'props',
        'directory': '07 Props',
        'required': True,
        'rarity_weights': None,
    }
]

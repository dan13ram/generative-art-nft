#!/usr/bin/env python
# coding: utf-8

# Import required libraries
import pandas as pd
import numpy as np
import time
import os
import shutil
import random
from progressbar import progressbar, ProgressBar

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)


# Import configuration file
from config import CONFIG


# Parse the configuration file and make sure it's valid
def parse_outputs():
    
    # Input traits must be placed in the assets folder. Change this value if you want to name it something else.
    output_path = 'output'

    outputs = sorted([output for output in os.listdir(output_path) if output[0] != '.'])

    print('Found', len(outputs), 'editions...');

    editions = {}
    total_images = 0

    # Loop through all paths in output
    for output in outputs:

        images_path = os.path.join(output_path, output, 'images')
        
        images = sorted([image for image in os.listdir(images_path) if image[0] != '.'])

        image_paths = [os.path.join(output_path, output, 'images', image) for image in images]

        metadata_path = os.path.join(output_path, output, 'metadata.csv')

        metadata = pd.read_csv(metadata_path)

        editions[output] = {
            'images': image_paths,
            'metadata': metadata
        }

        total_images = total_images + len(images)

    print('Total of', total_images, 'images...')
    print('Creating final edition...')
    print("Starting task...")
    print()

    final_images_path = os.path.join('final', 'images')
    if not os.path.exists(final_images_path):
        os.makedirs(final_images_path)

    zfill_count = 4

    image_num = 0
    pbar = ProgressBar(maxval=total_images).start()
    final_metadata = pd.DataFrame()
    while (image_num < total_images):
        output_num = random.randint(0, len(outputs) - 1)
        output = outputs[output_num]
        images = editions[output]['images']
        metadata = editions[output]['metadata']
        if (len(images) > 0):
           image_name = str(image_num).zfill(zfill_count) + '.png'
           num = random.randint(0, len(images) - 1)
           image = images.pop(num)
           new_image = os.path.join(final_images_path, image_name)
           shutil.copy(image, new_image)
           metadata.at[metadata.index[num],'Unnamed: 0'] = image_num
           row = metadata.iloc[num]
           final_metadata = final_metadata.append(row)
           image_num = image_num + 1
           editions[output]['images'] = images
           editions[output]['metadata'] = metadata.drop(metadata.index[num])
           pbar.update(image_num)
        else:
           outputs.pop(output_num)
    final_metadata = final_metadata.reset_index()
    final_metadata = final_metadata.drop('index', axis=1)
    final_metadata = final_metadata.drop('Unnamed: 0', axis=1)
    pbar.finish()
    return final_metadata


# Main function. Point of entry
def main():

    print("Parsing outputs...")
    rt = parse_outputs()

    print();
    print("Saving metadata...")
    rt.to_csv(os.path.join('final', 'metadata.csv'))

    print("Task complete!")


# Run the main function
main()

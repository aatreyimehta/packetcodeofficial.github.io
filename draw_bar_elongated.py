import os
import numpy as np
import random
import pandas as pd
import tensorflow as tf
from tqdm import tqdm

from bar_generator_elongated import generate_data, write_source_data, write_circle_target_data1, serialize_data
#from bar_generator import generate_data, write_source_data, write_circle_target_data, serialize_data
from utils import postprocessing, maskgen

NUM_SAMPLES = 1000
P_grid = 0.4

os.makedirs("./data/source", exist_ok=True)
#os.makedirs("./data/tactile", exist_ok=True)
os.makedirs("./data/tactile1", exist_ok=True)
#os.makedirs("./data/tactile1", exist_ok=True)


with tf.device('/device:GPU:0'):
    data, metadata, circle_data = generate_data(num_samples=NUM_SAMPLES)
    
    

    for i in tqdm(range(len(data)), desc='bar charts: '):

        #fig_size = random.choices([[512,512], [512,512], [512,512]], weights=[.5, .25, .25])[0]
        #fig_size = random.choices([[512,512], [512,512], [512,512]], weights=[.5, .25, .25])[0]
        fig_size = random.choices([[512,1024], [512,1024], [512,1024]], weights=[.5, .25, .25])[0]
        draw_grid = random.random() < P_grid
        tick_step = random.randint(10, 16)

        write_source_data(data[i], f"./data/source/s_{i+1001}.png", fig_size, draw_grid, tick_step)
        postprocessing(f"./data/source/s_{i+1001}.png")
        
        #write_circle_target_data(circle_data[i], f"./data/tactile/t_{i+1001}.png", fig_size, draw_grid, tick_step)
        #maskgen(f"./data/tactile/t_{i+1001}.png")
        
        #write_circle_target_data0(circle_data[i], f"./data/tactile/t_{i+5001}.png", fig_size1, draw_grid, tick_step)
        #maskgen(f"./data/tactile/t_{i+5001}.png")
        
        write_circle_target_data1(circle_data[i], f"./data/tactile1/t_{i+1001}.png", fig_size, draw_grid, tick_step)
        print(f"./data/tactile1/t_{i+1001}.png")
        
        #write_circle_target_data2(circle_data[i], f"./data/tactile1/t_{i+5001}.png", fig_size1, draw_grid, tick_step)
        #print(f"./data/tactile1/t_{i+5001}.png")
        
    # metadata_df = serialize_data(metadata, ["x", "y"])
    # metadata_df.to_csv("metadata.csv", index=False)

# !zip -qq -r ./bardata.zip ./data/ ./metadata.csv

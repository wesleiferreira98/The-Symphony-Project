import sys
import subprocess
from edge_sim_py import *
import networkx as nx
import msgpack
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import requests

# Download the dataset using Python requests
url = "https://raw.githubusercontent.com/EdgeSimPy/edgesimpy-tutorials/master/datasets/sample_dataset1.json"
response = requests.get(url)
with open("dataset.json", "wb") as f:
    f.write(response.content)

# Creating a Simulator object
simulator = Simulator()

# Loading the dataset from the local "dataset.json" file
simulator.initialize(input_file="dataset.json")

# Displaying some of the objects loaded from the dataset
for edge_server in EdgeServer.all():
    print(f"{edge_server}. CPU Capacity: {edge_server.cpu} cores")
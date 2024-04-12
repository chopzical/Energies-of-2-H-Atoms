import matplotlib.pyplot as plt
import os  

def get_valid_directory(prompt):
    
    while True:
        directory = input(prompt)
        if os.path.isdir(directory): 
            return directory
        else:
            print("Invalid directory. Please enter a valid path:")




import numpy as np
import matplotlib.pyplot as plt
import os
import time

#get output directory from the user to save the final plot as a PNG 
from pngdirectory import get_valid_directory 
directory = get_valid_directory("Enter the directory to save the plot: ")

# Create a unique filename to avoid overwriting
timestamp = time.strftime("%Y%m%d-%H%M%S")  
filename = f"energy plot_{timestamp}.png"  

# Save the plot to the specified directory with the chosen filename
full_path = os.path.join(directory, filename) 


#Variables
n = int(0)
x1 = 0.0
y1 = 0.0
z1 = 0.0
x2 = 0.0
y2 = 10.00
z2 = 0.0

xaxis = []


#write data to COM file
from writetoCOM import WriteToCom

for i in range (10):
    n = n+1
    xaxis.append(y2)
    WriteToCom(n,y2)
    y2 = y2 - 1
    if y2 == 1:
        break


#run gaussian 
from run import calculation
calculation()

#read log files 
from read import read_
returned_yaxis = read_()


#final lists
#print(returned_yaxis)
#print(xaxis)

#final energies as a Dict
E = dict(zip(xaxis, returned_yaxis))
print("Energies with the distance between two Hydrogen atoms: format -> {Distance(Ångström) : Energy(kJ/mol)}")
for key, value in E.items():
  print(f"{key}: {value}")  

#covert lists to arrays in order to plot
Y = np.array(returned_yaxis)
X = np.array(xaxis)

#plot and save it as a PNG to user given directory 
plt.plot(X, Y, marker='o', linestyle='-', color='b')
plt.xlabel('Distance between two H nuclei(Å)')
plt.ylabel('Potential Energy(kJ/mol)')
plt.title('Plot of Potential Energy of two H atoms vs Distance of their nuclei')
plt.grid(True)

plt.savefig(full_path)
print(f"Plot saved successfully to: {full_path}")


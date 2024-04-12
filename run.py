import subprocess
import re

def calculation() :
    k=0
    for i in range (10):
        k = k+1
        if k==10:
            break
        gauss_comm = "g16 " + "test_{0}".format(k) + ".com" 
        logs = subprocess.run(gauss_comm, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        #print(logs)

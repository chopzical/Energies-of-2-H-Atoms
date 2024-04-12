import re
import matplotlib.pyplot as np

def read_():
    multiplier = 2625.5
    yaxis = []
    m=0
    for i in range (10):
      m = m+1
      if m==10:
        break
      file = "test_{0}".format(m)+".log"
      logtext = " "
      with open(file , "r") as logtxt:
        logtext = logtxt.read() 

      
      out= re.findall(r' SCF Done:.*' , logtext)
      SCF = out[-1]
      patt = r"-?\d+\.\d+"
      value = re.findall(patt , SCF)
      valuestr = value[-1]
      
      yaxis.append(float(valuestr))
      multiplied_list = [item * multiplier for item in yaxis]
    
    return multiplied_list 


   
 
        
      
      
     
      
      
    
     	
    
    
    
    
      


      
    

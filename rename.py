# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os 
path=r"C:\Users\laksh\Music\animals10\raw_img\elefante" 
# Function to rename multiple files 
def main(): 
    i = 0
      
    for filename in os.listdir(path): 
        dst ="dog" + str(i) + ".jpg"
        src =path+ filename 
        dst =path+ dst 
          
        # rename() function will 
        # rename all the files 
        os.rename(src, dst) 
        i += 1
  
# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main() 
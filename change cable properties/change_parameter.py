# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 10:11:03 2019

@author: AV1
"""

import OrcFxAPI as ofx
import os


print("start")

# list all files in current directory
for file in os.listdir("."):
    # if files end with .dat use them
    if file.endswith(".dat"):
        # Print which model is being loaded
        print(f'Loading model {file}')
        # Load model
        model = ofx.Model(file)
        
        # get linetypes
        linetype_to_change = model["Test line type"]
        
        # change linetype parameters
        # Bend stiffness is referred to in Orcaflex as EIx
        linetype_to_change.EIx = 260.
        # Axial stiffness is referred to in Orcaflex as EA
        #linetype_to_change.??? = 1400
        
        # Mass is referred to in Orcaflex as ???
        #linetype_to_change.??? = 50
        
        # Save model
        model.SaveData(file)

print("end")
